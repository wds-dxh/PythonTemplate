#!/usr/bin/env python3
"""
日志记录器简单使用示例
"""
from src.utils.logger import get_logger


def main():
    """简单使用示例"""
    # 获取不同模块的日志记录器
    system_logger = get_logger("SYSTEM")
    api_logger = get_logger("API")
    db_logger = get_logger("DATABASE")

    # 记录不同级别的日志
    system_logger.info("系统启动")
    system_logger.debug("调试信息")

    api_logger.info("API服务启动")
    api_logger.warning("API请求频率过高")

    db_logger.info("数据库连接成功")
    db_logger.error("数据库查询失败")

    # 记录带有额外信息的日志
    api_logger.info("用户登录", extra={"user_id": 12345, "ip": "192.168.1.1"})


if __name__ == "__main__":
    main()
