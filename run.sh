#!/bin/bash
# 使用此方式规范导包流程，全部必须从项目根目录开始导入

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export PYTHONPATH="${PROJECT_ROOT}:${PYTHONPATH}"

# 检查是否提供了参数
if [ $# -eq 0 ]; then
    # echo "用法: $0 <python_script> [args...]"
    # echo "例如: $0 tests/client_example.py"
    # echo "     $0 main.py --port 8080"
    exit 1
fi

# 获取要执行的 Python 脚本路径（第一个参数）
PYTHON_SCRIPT="$1"
# 移除第一个参数，剩下的参数传递给 Python 脚本
shift

# 检查指定的 Python 脚本是否存在
if [ ! -f "${PROJECT_ROOT}/${PYTHON_SCRIPT}" ]; then
    echo "错误: Python 脚本 '${PROJECT_ROOT}/${PYTHON_SCRIPT}' 不存在。"
    exit 1
fi

# # 执行 Python 脚本，并传递剩余参数
# echo "执行 Python 脚本: ${PROJECT_ROOT}/${PYTHON_SCRIPT} $*"
uv run python "${PROJECT_ROOT}/${PYTHON_SCRIPT}" "$@"
