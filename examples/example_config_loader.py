#!/usr/bin/env python3
"""
配置加载器简单使用示例
"""

from src.utils.config_loader import get_config_loader


def main():
    """简单使用示例"""
    # 获取配置加载器
    loader = get_config_loader()

    # 验证配置
    loader.validate_config()

    # 获取日志配置
    log_config = loader.get_log_config()

    # 使用配置
    print(f"日志等级: {log_config.log_level}")
    print(f"日志目录: {log_config.log_dir}")
    print(f"日志文件: {log_config.log_file}")
    print(f"系统版本: {log_config.version}")


if __name__ == "__main__":
    main()
