# Quantitative UX Research Skill

> 基于《Quantitative User Experience Research: Informing Product Decisions by Understanding Users at Scale》(Chris Chapman & Kerry Rodden, Apress 2023) 构建的完整执行技能。

## 📖 简介

本 Skill 不仅是一个知识库，更是一个**具备直接执行能力**的量化用户体验研究工具包。涵盖从指标体系构建、调查设计、行为分析到实验设计的全链路能力，从教练到有经验执行者均可胜任。

## 🎯 7 大执行能力

| # | 执行能力 | Python 模块 | 核心类 | 说明 |
|---|---------|------------|--------|------|
| 1 | **HEART 框架与指标体系** | `heart.py` | `HEARTBuilder` | GSM 工作坊执行、Goals-Signals-Metrics 定义、指标体系报告 |
| 2 | **CSat 调查设计与分析** | `csat.py` | `CSatSurveyBuilder` / `CSatAnalyzer` | 问卷设计、Top-2-Box 分析、时间趋势、置信区间 |
| 3 | **日志序列路径分析** | `logs.py` | `LogsAnalyzer` | 会话化、序列频率、Markov 转移矩阵、Sunburst 数据 |
| 4 | **MaxDiff 功能优先级** | `maxdiff.py` | `MaxDiffDesigner` / `MaxDiffAnalyzer` | 调查设计验证、计数分析、标准化差异分数排序 |
| 5 | **A/B 测试设计与分析** | `abtest.py` | `ABTestPlanner` / `ABTestAnalyzer` | 样本量计算、转化率差异、置信区间、业务解读 |
| 6 | **研究规划与利益相关者诊断** | `research.py` | `ResearchPlanner` | 6 维请求诊断、方法推荐、研究计划生成 |
| 7 | **研究报告生成** | `research.py` | `ReportBuilder` | 标准报告结构、四大交付物原则、Markdown 输出 |

## 📁 项目结构

```
quant-ux-skill/
├── skills/quant-ux-research/
│   └── SKILL.md                 ← Skill 入口文件（执行能力 + 触发条件 + API 说明）
├── quantux/                     ← Python 执行包（纯标准库，无外部依赖）
│   ├── __init__.py   (130行)    统一入口类 QuantUXSkill
│   ├── config.py     (136行)    全局配置：HEART 维度、CSat/MaxDiff/AB 常量
│   ├── utils.py      (299行)    知识库搜索 + 统计工具（置信区间、样本量、T2B）
│   ├── templates.py  (170行)    工作坊 / 调查 / 报告模板 + 数据质量检查清单
│   ├── heart.py      (537行)    能力1: HEART 框架
│   ├── csat.py       (255行)    能力2: CSat 调查
│   ├── logs.py       (628行)    能力3: 日志序列
│   ├── maxdiff.py    (599行)    能力4: MaxDiff
│   ├── abtest.py     (240行)    能力5: A/B 测试
│   └── research.py   (731行)    能力6+7: 研究规划 & 报告
├── SKILL.md                     ← 原始知识库文档
├── pyproject.toml
├── requirements.txt
└── README.md
```

## 🚀 快速开始

### 作为 Skill 安装

将 `skills/quant-ux-research/` 目录复制到 `~/.aoneclaw/skills/` 下：

```bash
cp -r skills/quant-ux-research ~/.aoneclaw/skills/
```

### 作为 Python 包使用

```python
import sys
sys.path.insert(0, "/path/to/quant-ux-skill")
from quantux import QuantUXSkill

skill = QuantUXSkill("我的产品")
```

**无需安装任何外部依赖**，纯 Python 标准库实现。

## 💡 使用示例

### 能力1：HEART 框架

```python
from quantux import QuantUXSkill

skill = QuantUXSkill("飞猪旅行")
skill.heart_builder.add_goal("happiness", "提升用户对预订流程的满意度")
skill.heart_builder.add_signal("提升用户对预订流程的满意度", "预订后满意度评分", "success")
skill.heart_builder.add_metric("预订后满意度评分", "预订满意度T2B", "Top-2-Box比例", "survey", True)
print(skill.build_heart_framework())
```

### 能力2：CSat 分析

```python
skill.csat_analyzer.add_data_point("2024Q1", 500, {1:10, 2:20, 3:50, 4:180, 5:240})
skill.csat_analyzer.add_data_point("2024Q2", 480, {1:8, 2:18, 3:45, 4:190, 5:219})
print(skill.csat_analyzer.generate_report())
# 自动计算 Top-2-Box、置信区间、趋势分析
```

### 能力3：日志序列分析

```python
skill.logs_analyzer.add_event("user_001", "2024-01-01 10:00:00", "首页")
skill.logs_analyzer.add_event("user_001", "2024-01-01 10:02:00", "搜索")
skill.logs_analyzer.add_event("user_001", "2024-01-01 10:05:00", "详情页")
skill.logs_analyzer.add_event("user_001", "2024-01-01 10:08:00", "预订")
print(skill.analyze_logs())
# 自动会话化、序列频率统计、Markov 转移矩阵
```

### 能力4：MaxDiff 设计

```python
items = ["快速搜索", "价格对比", "评价可信", "退款便捷", "客服响应",
         "界面美观", "个性推荐", "行程规划", "优惠提醒", "地图导航"]
print(skill.design_maxdiff("功能优先级", items))
# 自动计算屏幕数、验证设计、输出调查文档
```

### 能力5：A/B 测试

```python
# 样本量计算
n = skill.calculate_ab_sample_size(baseline=0.35, mde=0.03)
print(f"每组需要 {n:,} 个样本")

# 结果分析
print(skill.analyze_ab_test("对照组", 5000, 1750, "实验组", 5000, 1900))
# 自动计算转化率差异、置信区间、p值、业务解读
```

### 能力6：利益相关者诊断

```python
print(skill.diagnose_request("验证我们的新设计方向是否正确"))
# 自动用 6 个维度诊断请求，给出建议
```

### 知识库搜索

```python
from quantux import search_knowledge
results = search_knowledge("置信区间")
```

## 🔑 核心理论基础

本 Skill 基于以下核心框架：

- **HEART 框架** — Happiness / Engagement / Adoption / Retention / Task Success
- **GSM 流程** — Goals → Signals → Metrics
- **T 型技能模型** — 编程 ∩ UX研究 ∩ 统计
- **以用户为中心五原则** — 用户视角、用户变量、认知方法、未满足需求、UX行动
- **四大交付物原则** — 简短聚焦、最少技术、保持无偏、可复现

## 📚 原书信息

- **书名**: Quantitative User Experience Research: Informing Product Decisions by Understanding Users at Scale
- **作者**: Chris Chapman & Kerry Rodden
- **出版**: Apress, 2023
- **内容**: 15 章 + 3 个附录，覆盖 Quant UXR 的完整知识体系

## 📜 许可

本 Skill 仅供内部学习和研究使用。
