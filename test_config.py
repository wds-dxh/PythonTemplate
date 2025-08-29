#!/usr/bin/env python3
"""
测试配置模型
"""
from src.utils.config_loader import get_config_loader
from pydantic import ValidationError

def test_config():
    """测试配置加载和验证"""
    try:
        loader = get_config_loader()
        config = loader.validate_config()
        
        print("✅ 配置验证成功!")
        print(f"日志等级: {config.log.log_level}")
        print(f"日志目录: {config.log.log_dir}")
        print(f"日志文件: {config.log.log_file}")
        print(f"版本: {config.log.version}")
        
        # 测试获取日志配置
        log_config = loader.get_log_config()
        print(f"日志轮转: {log_config.rotation}")
        print(f"日志保留: {log_config.retention}")
        
    except ValidationError as e:
        print("❌ 配置验证失败:")
        for error in e.errors():
            print(f"  - {error['loc']}: {error['msg']}")
    except Exception as e:
        print(f"❌ 错误: {e}")

if __name__ == "__main__":
    test_config()