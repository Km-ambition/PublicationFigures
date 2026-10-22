# MathModeling2026

数学建模项目工作区，用于保存数据、模型代码、实验笔记、论文材料和最终图表。

## 目录结构

```text
.
├── data/
│   ├── raw/          # 原始数据，只读保留
│   └── processed/    # 清洗、转换后的数据
├── docs/             # 题目分析、建模假设和论文材料
├── figures/          # 生成的图表
├── notebooks/        # 探索性分析 Notebook
├── reports/          # 最终报告及中间稿
├── src/
│   └── mathmodeling2026/  # 可复用的 Python 代码
├── tests/            # 自动化测试
└── .agents/skills/   # 项目级 Codex Skills
```

## 环境准备

需要 Python 3.10 或更高版本。

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Windows PowerShell 激活虚拟环境时使用：

```powershell
.venv\Scripts\Activate.ps1
```

## 常用命令

运行测试：

```bash
python -m pytest
```

在 Codex 中绘制论文图时，可以这样描述任务：

```text
请使用 scipilot-figure-skill 分析 data/raw/results.csv。
先剖析数据并推荐图型，确认后生成 PDF、SVG 和 300 DPI PNG，
将结果保存到 figures/。
```

## 工作约定

- 原始数据放入 `data/raw/`，原则上不直接修改。
- 清洗后的数据写入 `data/processed/`。
- 可复用逻辑放入 `src/mathmodeling2026/`，不要只保存在 Notebook 中。
- 最终图表从代码重新生成，避免手工修改导致结果不可复现。
- 大型或敏感数据不要直接提交到 Git；应记录获取方式和字段说明。
