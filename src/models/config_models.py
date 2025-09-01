"""
配置文件的Pydantic数据模型
"""
from pathlib import Path

from pydantic import BaseModel, Field, field_validator


class LogConfig(BaseModel):
    """日志配置模型"""
    log_format: str = Field(
        ...,
        description="控制台输出格式",
        min_length=1
    )
    log_format_file: str = Field(
        ...,
        description="日志文件输出格式",
        min_length=1
    )
    version: str = Field(
        default="0.1",
        description="系统版本"
    )
    log_level: str = Field(
        default="INFO",
        description="日志等级"
    )
    log_dir: str = Field(
        default="./tmp/log",
        description="日志路径"
    )
    log_file: str = Field(
        default="server.log",
        description="日志文件名"
    )
    rotation: str = Field(
        default="100 MB",
        description="日志轮转大小"
    )
    retention: str = Field(
        default="30 days",
        description="日志保留时间"
    )
    compression: str = Field(
        default="gz",
        description="日志压缩格式"
    )

    @field_validator('log_level')
    def validate_log_level(cls, v):
        """验证日志等级"""
        valid_levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
        if v.upper() not in valid_levels:
            raise ValueError(f'日志等级必须是以下之一: {valid_levels}')
        return v.upper()

    @field_validator('log_dir')
    def validate_log_dir(cls, v):
        """验证日志目录路径"""
        try:
            Path(v).resolve()
            return v
        except Exception as e:
            raise ValueError(f'无效的日志目录路径: {v}') from e

    @field_validator('compression')
    def validate_compression(cls, v):
        """验证压缩格式"""
        valid_formats = ['gz', 'bz2', 'xz', 'zip']
        if v.lower() not in valid_formats:
            raise ValueError(f'压缩格式必须是以下之一: {valid_formats}')
        return v.lower()


class Config(BaseModel):
    """完整配置模型"""
    log: LogConfig = Field(..., description="日志配置")

    class Config:
        # 允许额外字段
        extra = "allow"
