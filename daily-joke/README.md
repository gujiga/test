# Daily Joke

一个简单的每日笑话生成器，帮助您在繁忙的工作中放松心情。

## 功能特点

- 每日自动获取新笑话
- 支持多种笑话类型
- 简单易用的API接口

## 安装

使用pip安装：

```bash
pip install -e .
```

或者使用conda：

```bash
conda env create -f environment.yml
conda activate daily-joke
```

## 使用方法

### 命令行使用

```bash
daily-joke
```

### 作为库使用

```python
from dailyjoke import get_random_joke

# 获取随机笑话
joke = get_random_joke()
print(joke)
```

## 开发

### 运行测试

```bash
pytest
```

### 项目结构

```
daily-joke/
 ├── dailyjoke/       # 主源码目录
 │   ├── __init__.py  # 包初始化文件
 │   ├── main.py      # 主入口文件
 │   └── utils.py     # 工具函数
 ├── tests/           # 测试目录
 │   └── test_utils.py # 工具函数测试
 ├── .gitignore       # Git忽略文件
 ├── README.md        # 项目说明
 ├── requirements.txt # Python依赖
 ├── setup.py         # 安装配置
 ├── pyproject.toml   # 项目元数据
 └── environment.yml  # Conda环境配置
```

## 贡献

欢迎提交Issue和Pull Request！

## 许可证

MIT License