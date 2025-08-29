# Python 项目模板

一个标准化的 Python 项目开发模板，集成了配置管理、日志系统和 Pydantic 数据验证。

## 特性

- 🔧 **配置管理**: 基于 YAML 的配置文件，使用 Pydantic 进行数据验证
- 📝 **日志系统**: 集成 Loguru，支持控制台和文件输出，自动轮转和压缩
- 🏗️ **标准结构**: 清晰的项目目录结构，便于维护和扩展
- ✅ **类型安全**: 使用 Pydantic 模型确保配置数据的类型安全
- 🔄 **单例模式**: 日志管理器采用单例模式，确保全局唯一实例

## 项目结构

```
├── config/                 # 配置文件
│   └── config.yaml        # 主配置文件
├── examples/              # 使用示例
│   ├── example_config_loader.py
│   └── example_logger.py
├── src/                   # 源代码
│   ├── core/             # 核心功能模块
│   ├── models/           # 数据模型
│   │   ├── __init__.py
│   │   └── config_models.py  # 配置数据模型
│   ├── modules/          # 业务模块
│   └── utils/            # 工具类
│       ├── config_loader.py  # 配置加载器
│       └── logger.py         # 日志管理器
├── tmp/                   # 临时文件
│   └── log/              # 日志文件
├── main.py               # 程序入口
├── pyproject.toml        # 项目配置
└── README.md
```

## 快速开始

### 环境要求

- Python >= 3.12
- uv (推荐) 或 pip

### 安装依赖

使用 uv (推荐):
```bash
uv sync
```

或使用 pip:
```bash
pip install -r requirements.txt
```

### 运行项目

```bash
python main.py
```

## 核心组件

### 1. 配置管理

配置系统使用 Pydantic 进行数据验证，确保配置的正确性。

```python
from src.utils.config_loader import get_config_loader

# 获取配置加载器
loader = get_config_loader()

# 验证并加载配置
config = loader.validate_config()

# 获取日志配置
log_config = loader.get_log_config()
```

### 2. 日志系统

基于 Loguru 的日志系统，支持多种输出格式和自动轮转。

```python
from src.utils.logger import get_logger

# 获取日志记录器
logger = get_logger("MODULE_NAME")

# 记录日志
logger.info("这是一条信息日志")
logger.error("这是一条错误日志")
```

### 3. 配置文件

`config/config.yaml` 包含所有系统配置：

```yaml
log:
  log_level: DEBUG
  log_dir: ./tmp/log
  log_file: "server.log"
  rotation: "10 MB"
  retention: "30 days"
  compression: "gz"
  version: "0.1"
```

## 使用示例

查看 `examples/` 目录下的示例文件：

- `example_config_loader.py`: 配置加载器使用示例
- `example_logger.py`: 日志系统使用示例

## 依赖包

- **loguru**: 强大的日志库
- **pydantic**: 数据验证和设置管理
- **pyyaml**: YAML 文件解析

## 开发指南

### 添加新模块

1. 在 `src/modules/` 下创建新的业务模块
2. 在 `src/core/` 下添加核心功能
3. 在 `src/utils/` 下添加工具函数

### 添加新配置

1. 在 `src/models/config_models.py` 中定义新的配置模型
2. 在 `config/config.yaml` 中添加对应配置
3. 更新配置加载器以支持新配置

### 日志使用规范

- 使用有意义的模块标签: `get_logger("API")`, `get_logger("DATABASE")`
- 合理使用日志级别: DEBUG < INFO < WARNING < ERROR < CRITICAL
- 记录关键操作和错误信息


## 作者

wds @ (wdsnpshy@163.com)