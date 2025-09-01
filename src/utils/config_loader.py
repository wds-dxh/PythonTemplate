'''
Author: wds-a5000 wdsnpshy@163.com
Date: 2025-08-15 11:31:57
Description: 配置加载器 使用Pydantic进行数据验证
'''
from pathlib import Path

import yaml
from pydantic import ValidationError

from ..models.config_models import Config, LogConfig


class ConfigLoader:
    def __init__(self, config_path):
        self.config_path = Path(config_path)
        self.config_model: Config = None

    def validate_config(self) -> Config:
        """使用Pydantic验证配置文件"""
        try:
            with open(self.config_path, encoding='utf-8') as file:
                config_data = yaml.safe_load(file)

            # 使用Pydantic模型验证配置
            self.config_model = Config(**config_data)
            return self.config_model

        except FileNotFoundError as e:
            raise FileNotFoundError(f"配置文件未找到: {self.config_path}") from e
        except yaml.YAMLError as e:
            raise ValueError(f"配置文件格式错误: {e}") from e
        except ValidationError as e:
            raise ValueError(f"配置验证失败: {e}") from e

    def get_log_config(self) -> LogConfig:
        """获取日志配置"""
        if self.config_model is None:
            self.validate_config()

        return self.config_model.log

    def get_config(self) -> Config:
        """获取完整配置"""
        if self.config_model is None:
            self.validate_config()
        return self.config_model


# 返回全局唯一实例
instance = None


def get_config_loader() -> ConfigLoader:
    """获取配置加载器"""
    global instance
    if instance is None:
        base_path = Path(__file__).parent.parent.parent
        config_path = base_path / "config" / "config.yaml"
        instance = ConfigLoader(config_path)
    return instance
