# DemoOne

这是一个使用 Trae IDE 开始的演示项目。

## 项目概述

本项目旨在提供一个简单的起点，帮助您熟悉 Trae IDE 和基本的软件开发流程。我们选择 Python 作为初始编程语言，因为它易于学习且应用广泛。

## 第一个项目建议：文件统计工具

我们建议的第一个项目是一个**文件统计工具**，它可以：

- 扫描指定目录及其子目录
- 统计文件数量、类型分布
- 计算文件总大小
- 输出简洁的统计报告

这个项目涵盖了以下核心概念：
- 文件系统操作
- 命令行参数解析
- 数据统计与格式化输出
- 模块化代码组织

## 项目结构

```
DemoOne/
├── src/
│   └── file_stats.py    # 主程序
├── tests/
│   └── test_file_stats.py # 单元测试
├── requirements.txt      # Python 依赖
├── .gitignore           # Git 忽略文件
└── README.md            # 项目说明
```

## 快速开始

### 前提条件
- Python 3.8 或更高版本
- Git（可选，用于版本控制）

### 安装步骤

1. 克隆项目（如果使用 Git）：
   ```bash
   git clone <项目地址>
   cd DemoOne
   ```

2. 创建虚拟环境（推荐）：
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

### 使用说明

文件统计工具支持两种使用模式：

#### 1. 命令行参数模式
```bash
python src/file_stats.py /path/to/directory
```

#### 2. 交互式输入模式
```bash
python src/file_stats.py
```
运行后会提示输入目录路径，可以直接回车使用当前目录：
```
文件统计工具
==============================
请输入要扫描的目录路径 (默认: '.'，直接回车使用默认): 
```

#### 示例输出
两种模式都会产生相同的统计报告：
```
扫描目录: /path/to/directory
文件总数: 42
文件类型分布:
  .py: 15 个
  .txt: 10 个
  .md: 5 个
  其他: 12 个
总大小: 4.2 MB
```

## 开发指南

### 添加新功能
1. 在 `src/` 目录下创建新的模块
2. 编写相应的单元测试
3. 更新 `requirements.txt`（如需新依赖）
4. 更新本 README 的使用说明

### 运行测试
```bash
python -m pytest tests/
```

## 下一步计划

完成基础文件统计工具后，可以考虑以下扩展功能：

1. **可视化报表**：使用 matplotlib 生成图表
2. **历史记录**：保存每次扫描结果，支持对比分析
3. **过滤功能**：按文件类型、大小、修改时间筛选
4. **导出功能**：支持 CSV、JSON 格式导出

## 学习资源

- [Python 官方文档](https://docs.python.org/3/)
- [Trae IDE 使用指南](https://docs.trae.io)
- [Git 入门教程](https://git-scm.com/book/zh/v2)

## 许可证

本项目采用 MIT 许可证。详见 LICENSE 文件（待创建）。

---

**开始编码吧！** 打开 `src/file_stats.py` 并开始实现您的第一个功能。