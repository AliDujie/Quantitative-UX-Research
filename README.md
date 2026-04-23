# Quantitative UX Research Skill

基于《Quantitative User Experience Research》(Chapman & Rodden, 2023) 的完整量化用户体验研究工具包。

## 为什么使用

- **完整覆盖** — HEART 框架、CSat 调查、日志分析、MaxDiff、A/B 测试、研究规划
- **CEO 决策支持** — 内置业务影响评估、验证时间线、资源估算
- **零依赖** — 纯 Python 标准库实现

## 快速开始

```python
from quantux import QuantUXSkill

skill = QuantUXSkill("旅行平台")

# HEART 框架
heart = skill.build_heart_framework()

# CSat 调查设计
survey = skill.design_csat_survey("2024Q1 满意度")

# A/B 测试样本量
sample = skill.calculate_ab_sample_size(baseline_rate=0.15, mde=0.02)

# CEO 视角：完整研究报告 + 业务影响 + 资源估算
report = skill.generate_report("用户体验研究报告", include_ceo_analysis=True)
```

## 文件结构

```
Quantitative-UX-Research/
├── SKILL.md              # AI Agent 技能定义
├── quantux/              # Python 包（纯标准库）
│   ├── __init__.py       # QuantUXSkill 统一入口
│   ├── heart.py          # HEART 框架与 GSM 引擎
│   ├── csat.py           # CSat 调查设计与分析
│   ├── logs.py           # 日志序列分析
│   ├── maxdiff.py        # MaxDiff 优先级排序
│   ├── ab_test.py        # A/B 测试设计与分析
│   ├── research_plan.py  # 研究规划器
│   └── report.py         # 报告生成器
├── pyproject.toml
└── README.md
```

## 相关技能

- [Universal-Design-Methods](https://github.com/AliDujie/universal-design-methods) — 100 种设计研究方法
- [Web-Persona-Skill](https://github.com/AliDujie/web-persona-skill) — 人物角色创建与应用
- [Value-Proposition-Design](https://github.com/AliDujie/value-proposition-design) — 价值主张画布
- [Storytelling-with-Data](https://github.com/AliDujie/storytelling-with-data) — 数据叙事与可视化

## 依赖

Python >= 3.9，无外部依赖。

## 许可

MIT License
