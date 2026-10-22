# PublicationFigures

面向学术论文的可复现绘图仓库。用于管理原始数据、绘图代码、期刊样式、草稿和最终投稿图，避免只保留无法复现的手工图片。

## 目录结构

```text
.
├── data/
│   ├── raw/          # 原始数据，只读保留
│   └── processed/    # 清洗后的绘图数据
├── docs/             # 图表规划、图注和期刊要求
├── examples/         # 可直接运行的绘图示例
├── figures/
│   ├── drafts/       # 预览和迭代稿
│   └── final/        # 通过检查的投稿版本
├── notebooks/        # 探索性分析
├── src/
│   └── publication_figures/  # 公共样式和绘图工具
├── styles/           # 自定义期刊规范说明
├── tests/            # 样式和工具测试
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

生成示例图：

```bash
python examples/demo_figure.py
```

示例会在 `figures/drafts/` 中生成 PDF 和 300 DPI PNG。

## 在 Codex 中使用

可以直接这样描述任务：

```text
请使用 scipilot-figure-skill 分析 data/raw/results.csv。
这张图要论证的是：实验组相对对照组显著改善了目标指标。
请先剖析数据并推荐图型，确认后再绘制。
目标期刊为 Nature，使用单栏尺寸，输出 PDF、SVG 和 300 DPI PNG。
预览放入 figures/drafts/，检查通过的版本放入 figures/final/。
```

## 工作约定

- 原始数据放入 `data/raw/`，原则上不直接修改。
- 清洗后的数据写入 `data/processed/`。
- 可复用样式和绘图逻辑放入 `src/publication_figures/`。
- 每张正式图都应能从数据和代码重新生成，不依赖手工修改。
- 投稿图优先保存为 PDF/SVG 矢量格式，同时保留 300–600 DPI PNG/TIFF。
- 误差棒必须在图注中说明 SD、SEM 或置信区间，并记录样本量和统计方法。
- 大型或敏感数据不要直接提交到 Git；应记录获取方式和字段说明。
