import sys
from pathlib import Path

from loguru import logger

from .config_loader import get_config_loader


class LoggerManager:
    """日志管理器单例类"""

    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self._base_logger = None
            self._initialized = True

    def init_logger(self) -> logger:
        """
        初始化日志记录器,全局唯一实例
        从配置文件中读取日志配置并设置
        """
        if self._base_logger is not None:
            return self._base_logger

        try:
            # 获取配置加载器
            config_loader = get_config_loader()
            log_config = config_loader.get_log_config()

            # 移除默认处理器
            logger.remove()

            # 获取配置参数
            console_format = log_config.log_format
            file_format = log_config.log_format_file
            log_level = log_config.log_level
            log_dir = log_config.log_dir
            log_file = log_config.log_file
            rotation = log_config.rotation
            retention = log_config.retention
            compression = log_config.compression
            version = log_config.version

            # 确保日志目录存在
            log_dir_path = Path(log_dir)
            log_dir_path.mkdir(parents=True, exist_ok=True)

            # 完整的日志文件路径
            log_file_path = log_dir_path / log_file

            # 添加控制台输出处理器
            logger.add(
                sys.stdout,
                format=console_format,
                level=log_level,
                colorize=True,
                enqueue=True  # 多进程安全
            )

            # 添加文件输出处理器(带轮转)
            logger.add(
                str(log_file_path),
                format=file_format,
                level=log_level,
                rotation=rotation,
                retention=retention,
                compression=compression,
                enqueue=True,  # 多进程安全
                encoding="utf-8"
            )

            # 创建绑定了版本信息的基础logger
            self._base_logger = logger.bind(version=version)

            # 记录初始化成功信息
            self._base_logger.bind(tag="SYSTEM").info("日志系统初始化成功")
            self._base_logger.bind(tag="SYSTEM").info(f"控制台日志级别: {log_level}")
            self._base_logger.bind(tag="SYSTEM").info(
                f"文件日志路径: {log_file_path}")
            self._base_logger.bind(tag="SYSTEM").info(f"日志轮转设置: {rotation}")
            self._base_logger.bind(tag="SYSTEM").info(f"日志保留设置: {retention}")

            return self._base_logger

        except Exception as e:
            # 如果初始化失败,使用默认配置
            logger.remove()
            logger.add(sys.stdout, level="INFO")
            fallback_logger = logger.bind(version="1.0.0")
            error_message = f"日志系统初始化失败,使用默认配置: {e}"
            fallback_logger.bind(tag="ERROR").error(error_message)
            self._base_logger = fallback_logger
            return self._base_logger

    def get_logger(self, tag: str = "DEFAULT") -> logger:
        """
        获取带标签的日志记录器

        Args:
            tag: 模块标签,用于标识日志来源

        Returns:
            绑定了标签的logger实例
        """
        base_logger = self.init_logger()
        return base_logger.bind(tag=tag)

    def reset_logger(self):
        """重置日志记录器(主要用于测试)"""
        self._base_logger = None
        logger.remove()


# 全局函数 保持向后兼容
def get_logger(tag: str = "DEFAULT") -> logger:
    """
    获取带标签的日志记录器

    Args:
        tag: 模块标签,用于标识日志来源

    Returns:
        绑定了标签的logger实例
    """
    manager = LoggerManager()
    return manager.get_logger(tag)


def reset_logger():
    """重置日志记录器(主要用于测试)"""
    manager = LoggerManager()
    manager.reset_logger()
