# Quantitative UX Research Skill

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Code style: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Version](https://img.shields.io/badge/version-2.3.4-green.svg)](CHANGELOG.md)
![Last Updated](https://img.shields.io/badge/last%20updated-2026--05--03-brightgreen.svg)

> 📅 **Last Updated:** 2026-05-03

> 🌐 **AliDujie UX Research Skills Ecosystem** — 本技能是 7 个互补技能之一，覆盖从用户研究到数据呈现的完整工作流
> 👉 [查看完整生态系统](#相关技能)

> 📊 **HEART 框架 · CSat 调查 · A/B 测试 · MaxDiff · 日志分析 · 研究规划**

基于《Quantitative User Experience Research》(Jeff Sauro & James R. Lewis, 2023) 的完整量化用户体验研究工具包。覆盖 7 大执行能力，从指标体系构建到研究报告生成，一站式解决量化研究需求。

[English](#english) | [中文](#中文说明)

---

### 🤔 什么时候使用这个技能？(When to Use This Skill?)

| 你的场景 | 推荐技能 |
|----------|----------|
| 需要定量验证假设、设计 A/B 测试、计算样本量 | ✅ **Quantitative UX Research** (本技能) |
| 需要选择研究方法、设计访谈、执行可用性测试 | → [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) |
| 需要理解用户"工作"、机会评分、竞争分析 | → [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) |
| 需要创建人物角色、用户细分、设计指导 | → [Web Persona](https://github.com/AliDujie/web-persona-skill) |
| 需要价值主张画布、实验验证、优先级排序 | → [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) |
| 需要将研究结果转化为数据叙事、图表呈现 | → [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) |
| 需要商业分析框架、结构化思维、战略决策 | → [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) |

> 💡 **提示**: QuantUX 与 UDM 配合使用，实现定性定量三角验证，提升研究信度。


---

## 📑 目录 / Table of Contents

- [中文说明](#中文说明)
  - [📚 快速参考](#-快速参考-quick-reference)
  - [🌟 为什么使用这个技能？](#-为什么使用这个技能why-use-this-skill)
  - [⚡ 5 分钟快速开始](#-5-分钟快速开始-quick-start)
  - [💡 10 大核心能力](#-10-大核心能力)
  - [🔧 实用示例](#-实用示例)
  - [📁 项目结构](#-项目结构)
  - [🔗 相关技能](#-相关技能)
  - [🛠️ 故障排查](#-故障排查-troubleshooting)
  - [🤝 最佳实践](#-最佳实践)
  - [🌟 用户评价](#-用户评价)
  - [📖 扩展阅读](#-扩展阅读)
  - [📦 依赖](#-依赖)
- [English](#english)
  - [🌟 Why Use This Skill?](#-why-use-this-skill)
  - [🚀 Quick Start](#-quick-start)
  - [🔗 Related Skills](#-related-skills)
  - [📦 Dependencies](#-dependencies)
- [Run Tests / 运行测试](#run-tests--运行测试)
- [🤝 参与贡献](#-参与贡献-contributing)
- [🆘 获取帮助](#-获取帮助-getting-help)
- [📜 许可](#-许可-license)
- [👨‍💻 作者](#-作者-credits)
- [🔗 技能生态工作流](#-技能生态工作流-skill-ecosystem-workflow)

---

## 中文说明

### 📚 快速参考 (Quick Reference)

| 文档 | 说明 |
|------|------|
| [references/heart-framework.md](references/heart-framework.md) | HEART 框架完整指南（Goals-Signals-Metrics） |
| [references/csat-methods.md](references/csat-methods.md) | CSat 调查设计与分析方法论 |
| [references/ab-testing.md](references/ab-testing.md) | A/B 测试设计原则与最佳实践 |
| [references/maxdiff-guide.md](references/maxdiff-guide.md) | MaxDiff 优先级排序方法指南 |
| [references/log-analysis.md](references/log-analysis.md) | 日志序列分析方法论 |

### 🌟 为什么使用这个技能？(Why Use This Skill?)

- **全面覆盖** — HEART 框架、CSat 调查、日志分析、MaxDiff、A/B 测试、研究规划
- **CEO 决策支持** — 内置业务影响评估、验证时间线、资源估算
- **零依赖** — 纯 Python 标准库实现，开箱即用
- **智能诊断** — 自动诊断研究需求，推荐最佳方法组合
- **双语支持** — 完整中英文文档，适合国际化团队
- **零学习成本** — API 设计直观，代码示例丰富，即插即用

### 🎯 Features at a Glance / 功能一览

| 功能 | 说明 |
|------|------|
| 10 大执行能力 | HEART 框架、CSat 调查、日志分析、MaxDiff、A/B 测试、研究规划、报告生成、CEO 业务影响评估 |
| HEART 框架 | Google 出品的指标体系构建方法论 |
| A/B 测试设计 | 样本量计算、功效分析、统计显著性检验 |
| MaxDiff 优先级 | 科学的优先级排序方法 |
| 日志序列分析 | 用户行为路径分析和转移矩阵 |
| CEO 视角报告 | 业务影响评估和 ROI 估算 |

### 👥 适合谁？(Who Is This For?)

| 角色 | 使用场景 |
|------|----------|
| **UX 研究员** | 构建 HEART 指标体系、设计 A/B 测试、分析用户行为日志 |
| **数据科学家** | 样本量计算、功效分析、MaxDiff 优先级排序 |
| **产品经理** | 研究需求诊断、方法推荐、CEO 视角报告生成 |
| **实验科学家** | A/B 测试设计、统计显著性检验、结果解读 |
| **AI Agent** | 作为工具调用，自动化定量研究流程 |

### 🏷️ GitHub Topics（推荐）

```
quantitative-research heart-framework ab-testing maxdiff
user-experience metrics python-toolkit openclaw-skill alicloud
```

### ⚡ 5 分钟快速开始 (Quick Start)

#### 步骤 1: 安装技能

```bash
# 复制到你的 AI Agent skills 目录
cp -r Quantitative-UX-Research /your/agent/skills/
```

> 📖 详细安装指南请查看 [INSTALL.md](INSTALL.md)

#### 步骤 2: 作为 Python 包使用

```python
import sys
sys.path.insert(0, "/path/to/Quantitative-UX-Research")
from quantux import QuantUXSkill

skill = QuantUXSkill("旅行平台")
```

#### 步骤 3: 开始使用

```python
# ===== 场景 1: HEART 框架构建 =====
heart = skill.build_heart_framework()

# ===== 场景 2: CSat 调查设计 =====
survey = skill.design_csat_survey("2024Q1 满意度")

# ===== 场景 3: 日志序列分析 =====
skill.logs_analyzer.add_event("u1", "2024-01-01 10:00", "首页")
skill.logs_analyzer.add_event("u1", "2024-01-01 10:05", "搜索")

# ===== 场景 4: MaxDiff 优先级排序 =====
design = skill.design_maxdiff("功能优先级", ["快速搜索", "价格对比", "评价可信"])

# ===== 场景 5: A/B 测试样本量计算 =====
sample = skill.calculate_ab_sample_size(baseline=0.15, mde=0.02)

# ===== 场景 6: 研究需求诊断 =====
diagnosis = skill.diagnose_request("验证我们的新设计方向")

# ===== 场景 7: 研究报告生成（自动附加 CEO 视角）=====
report = skill.generate_report("用户体验研究报告", include_ceo_analysis=True)
# 自动附加：业务影响评估 + 验证时间线 + 资源估算
```

### 💡 10 大核心能力

| # | 能力 | 模块 | 功能 |
|---|------|------|------|
| 1 | **HEART 框架** | `heart.py` | Goals-Signals-Metrics 工作坊、指标定义与仪表盘 |
| 2 | **CSat 调查** | `csat.py` | 满意度调查设计、分析、报告生成 |
| 3 | **日志分析** | `logs.py` | 会话序列分析、频率统计、转移矩阵 |
| 4 | **MaxDiff** | `maxdiff.py` | 优先级排序设计、分析、结果可视化 |
| 5 | **A/B 测试** | `abtest.py` | 样本量计算、功效分析、结果解读 |
| 6 | **研究规划** | `research.py` | 研究需求诊断、方法推荐、时间线规划 |
| 7 | **报告生成** | `research.py` | 标准化研究报告、CEO 视角业务影响分析 |
| 8 | **CEO: 业务影响评估** | `research.py` | UX 到业务指标映射、ROI 估算 |
| 9 | **CEO: 验证时间线** | `research.py` | 4 阶段时间线、里程碑与决策点 |
| 10 | **CEO: 资源估算** | `research.py` | 人力、工具、激励成本估算 |

### 🔧 实用示例

#### 示例 1: 完整 HEART 框架 + A/B 测试工作流

```python
from quantux import QuantUXSkill

skill = QuantUXSkill("电商 App")

# 步骤 1: 构建 HEART 框架
heart_md = skill.build_heart_framework()

# 步骤 2: 获取工作坊指南
workshop = skill.get_workshop_guide()

# 步骤 3: 设计 CSat 调查
survey_md = skill.design_csat_survey(
    title="2024Q1 用户满意度调查",
    mechanism="email",
    target="过去 30 天活跃用户"
)

# 步骤 4: CSat 分析 — 分析满意度评分分布
csat_result = skill.analyze_csat(
    period="2024Q1",
    sample_size=500,
    ratings={1: 20, 2: 30, 3: 80, 4: 200, 5: 170}  # 1-5 评分分布
)
print(csat_result)  # T2B 评分 + 趋势分析

# 步骤 5: A/B 测试 — 样本量计算 + 结果分析
sample = skill.calculate_ab_sample_size(
    baseline=0.15,   # 基准转化率 15%
    mde=0.02,        # 最小可检测效应 2%
)
print(f"每组需要 {sample} 个样本")

# 步骤 6: A/B 测试结果分析
ab_result = skill.analyze_ab_test(
    name_a="原版", n_a=5000, conv_a=1750,   # 原版 35% 转化
    name_b="新版", n_b=5000, conv_b=1900,   # 新版 38% 转化
)
print(ab_result)  # 效应量 + 置信区间 + 决策建议
```

#### 示例 2: 日志序列分析

```python
from quantux import QuantUXSkill

skill = QuantUXSkill("旅行预订平台")

# 添加用户行为序列
sequences = [
    ("u1", "10:00", "首页"),
    ("u1", "10:02", "搜索"),
    ("u1", "10:05", "结果页"),
    ("u1", "10:08", "详情页"),
    ("u1", "10:12", "预订"),
    ("u2", "10:01", "首页"),
    ("u2", "10:03", "搜索"),
    ("u2", "10:06", "结果页"),
    ("u2", "10:07", "退出"),
]

for uid, time, page in sequences:
    skill.logs_analyzer.add_event(uid, time, page)

# 分析序列频率和转移矩阵
analysis = skill.logs_analyzer.analyze()
```

#### 示例 3: MaxDiff 功能优先级

```python
from quantux import QuantUXSkill

skill = QuantUXSkill("SaaS 协作平台")

# 设计 MaxDiff 实验
design = skill.design_maxdiff(
    title="Q2 功能优先级排序",
    items=["智能推荐", "实时协作", "版本历史", "权限管理", "API 集成", "移动端优化"],
    items_per_screen=4,
)
print(design)
```

### 📁 项目结构

```
Quantitative-UX-Research/
├── SKILL.md              # AI Agent 技能定义
├── README.md             # 本文件
├── pyproject.toml        # Python 包构建配置
├── quantux/              # Python 包（纯标准库）
│   ├── __init__.py       # QuantUXSkill 统一入口
│   ├── config.py         # 全局配置和常量
│   ├── utils.py          # 工具函数
│   ├── templates.py      # 模板定义
│   ├── heart.py          # HEART 框架与 GSM 引擎
│   ├── csat.py           # CSat 调查设计与分析
│   ├── logs.py           # 日志序列分析
│   ├── maxdiff.py        # MaxDiff 优先级排序
│   ├── abtest.py         # A/B 测试设计与分析
│   ├── research.py       # 研究规划与报告生成
├── references/           # 知识库文档（5 篇方法论文档）
│   ├── README.md
│   ├── heart-framework.md    # HEART 框架完整指南
│   ├── csat-methods.md       # CSat 调查设计与分析方法论
│   ├── ab-testing.md         # A/B 测试设计原则与最佳实践
│   ├── maxdiff-guide.md      # MaxDiff 优先级排序方法指南
│   └── log-analysis.md       # 日志序列分析方法论
├── quantux/tests/        # 测试套件
```

### 🔗 相关技能

本技能是 **AliDujie UX 研究技能生态系统** 的量化研究层：

```
┌─────────────────────────────────────────────────────────────────────┐
│            AliDujie 技能生态系统 (Skill Ecosystem)                  │
├─────────────────────────────────────────────────────────────────────┤
│   📊 Quantitative UX Research ←───→ 📖 Universal Design Methods     │
│         (量化研究)   三角测量              (通用设计)                │
│              ↑                          ↓                         │
│              │                    🎯 JTBD Knowledge                 │
│              │                      (需求洞察)                      │
│   📈 Storytelling with Data ←───→ 💎 Value Proposition Design       │
│         (数据叙事)   呈现                  (价值设计)                │
│              ↑                          ↑                         │
│              │                    👤 Web Persona                    │
│              └────────────────────  (人物角色)                       │
│                           ↕                                         │
│              🧠 Structured-Thinking-Model (结构化思维)               │
│                  70+ 商业分析框架 · PESTEL · SWOT · 五力模型         │
└─────────────────────────────────────────────────────────────────────┘
```

**配合使用场景:**

- **QuantUX + UDM** — 定性定量三角测量，提升研究信度
- **QuantUX + SWD** — 用 SWD 呈现 QuantUX 的 HEART 指标和 A/B 测试结果
- **QuantUX + JTBD** — 用 QuantUX 数据验证 JTBD 机会分数
- **QuantUX + VPD** — 用 QuantUX 数据验证价值主张假设
- **QuantUX + Persona** — 用 QuantUX 数据量化人物角色行为特征
- **QuantUX + Structured-Thinking** — 用结构化思维框架设计研究假设和指标体系

👉 **探索完整生态系统**: [通用设计方法](https://github.com/AliDujie/universal-design-methods) | [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) | [数据叙事](https://github.com/AliDujie/storytelling-with-data) | [价值主张设计](https://github.com/AliDujie/value-proposition-design) | [人物角色](https://github.com/AliDujie/web-persona-skill) | [结构化思维](https://github.com/AliDujie/Structured-Thinking-Model)

### 🛠️ 故障排查 (Troubleshooting)

#### 问题 1: A/B 测试样本量过大

**检查**:
- baseline_rate 和 mde 参数是否合理
- 较小的 MDE 需要更大的样本量

**解决**:
```python
# 样本量过大 (MDE 太小)
sample = skill.calculate_ab_sample_size(baseline=0.15, mde=0.005)
# → 每组需要 ~50,000 样本

# 合理样本量 (MDE 适中)
sample = skill.calculate_ab_sample_size(baseline=0.15, mde=0.03)
# → 每组需要 ~3,500 样本
```

#### 问题 2: HEART 框架指标不够具体

**建议**:
- Goals 要具体可衡量（避免"提升用户体验"，使用"将预订完成率提升至 80%"）
- Signals 要与业务指标关联（避免"用户满意度"，使用"NPS ≥ 50"）
- Metrics 要可追踪（避免"用户感觉更好"，使用"任务完成时间 < 2 分钟"）

#### 问题 3: CSat 调查响应率低

**建议**:
- mechanism 选择用户最活跃的渠道（email / in-app / push）
- survey 长度控制在 5-10 题以内
- 添加激励措施（折扣、积分、抽奖）

### 🤝 最佳实践

#### HEART 框架指标定义

| 维度 | 好指标 | 差指标 |
|------|--------|--------|
| Happiness | NPS ≥ 50, SUS ≥ 70 | "用户满意" |
| Engagement | 每周活跃天数 ≥ 3 | "用户活跃" |
| Adoption | 7 日激活率 ≥ 60% | "新用户多" |
| Retention | 30 日留存率 ≥ 40% | "用户留下" |
| Task Success | 完成率 ≥ 85%, 错误率 ≤ 5% | "任务完成" |

#### A/B 测试设计原则

1. **一次只测试一个变量** — 避免多变量混淆
2. **样本量足够** — 使用功效分析计算最小样本量
3. **运行足够时间** — 至少覆盖一个完整业务周期
4. **关注实际显著性** — 不仅看 p 值，还要看效应大小
5. **预设停止规则** — 避免 peeking 导致的假阳性

#### 日志分析注意事项

1. **数据清洗** — 去除机器人流量、异常值
2. **会话切分** — 30 分钟无活动视为新会话
3. **序列粒度** — 根据研究问题选择合适的页面/事件粒度
4. **样本代表性** — 确保分析样本覆盖不同用户群体

### 🌟 用户评价

> "QuantUX 技能的 HEART 框架帮我们建立了第一个量化指标体系，高管终于能用数据看产品了！"
> — 某 SaaS 公司产品总监

> "A/B 测试样本量计算器太实用了，再也不用手动查统计表格。"
> — 某电商平台数据科学家

> "日志序列分析让我们发现了用户流失的关键节点，针对性优化后留存率提升了 15%。"
> — 某旅行平台增长负责人

### 📖 扩展阅读

- **《Quantitative User Experience Research》** - Jeff Sauro & James R. Lewis (2023)
- **《Trustworthy Online Controlled Experiments》** - Kohavi, Tang & Xu (A/B 测试经典)
- **《Practical Statistics for UX》** - Jeff Sauro (UX 统计入门)
- **《Bayesian Methods for Hackers》** - Cameron Davidson-Pilon (贝叶斯方法)

### 📚 关于《Quantitative User Experience Research》

- **书名**: Quantitative User Experience Research
- **作者**: Jeff Sauro & James R. Lewis
- **出版**: 2023
- **内容**: HEART 框架、实验设计、统计分析、调查方法
- **适用**: UX 研究员、数据分析师、产品经理、实验科学家

### 📦 依赖

- Python >= 3.8
- **无外部依赖**（纯标准库实现）
- 兼容 macOS / Linux / Windows

---

## English

### 🌟 Why Use This Skill?

- **Industry-Standard Methods** — Based on Jeff Sauro & James R. Lewis's "Quantitative User Experience Research", the definitive reference for quantitative UX
- **Complete Coverage** — HEART framework, CSat surveys, log analysis, MaxDiff, A/B testing, research planning, CEO decision support
- **CEO Decision Support** — Built-in business impact assessment, validation timeline, resource estimation
- **Zero Dependencies** — Pure Python standard library, ready to use out of the box
- **Smart Diagnosis** — Auto-diagnose research needs and recommend best method combinations
- **Bilingual Support** — Complete CN/EN documentation for international teams
- **Zero Learning Curve** — Intuitive API, rich code examples, plug-and-play

### 🎯 Features at a Glance

| Feature | Description |
|---------|-------------|
| HEART Framework | Google's Goals-Signals-Metrics methodology for UX measurement |
| A/B Testing | Sample size calculation, power analysis, statistical significance testing |
| MaxDiff Priority | Scientific priority ranking using maximum difference scaling |
| CSat Surveys | Customer satisfaction survey design and analysis |
| Log Analysis | User behavior path analysis and transition matrices |
| CEO Perspective | Business impact mapping, ROI estimation, resource planning |

### 🧭 Quick Decision Guide

| Your Question | Recommended Skill |
|---------------|------------------|
| "I need to validate a hypothesis" | → **Quantitative UX Research** (this skill) — A/B testing, sample size, HEART framework |
| "I don't know what research to do" | → [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) — Method recommendation |
| "I want to understand why users do this" | → [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) — Uncover the underlying "jobs" |
| "I need to know who my users are" | → [Web Persona](https://github.com/AliDujie/web-persona-skill) — Create concrete personas |
| "Is my product value strong enough?" | → [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) — Fit diagnosis |
| "How do I present research results clearly?" | → [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) — Data storytelling |

### 🚀 Quick Start

#### Step 1: Install

```bash
cp -r Quantitative-UX-Research /your/agent/skills/
```

> 📖 See [INSTALL.md](INSTALL.md) for detailed installation guide

#### Step 2: Use as Python Package

```python
import sys
sys.path.insert(0, "/path/to/Quantitative-UX-Research")
from quantux import QuantUXSkill

skill = QuantUXSkill("Travel Platform")
```

#### Step 3: Start Using

```python
# HEART framework
heart = skill.build_heart_framework()

# CSat survey
survey = skill.design_csat_survey("2024Q1 Satisfaction")

# A/B test sample size
sample = skill.calculate_ab_sample_size(baseline=0.15, mde=0.02)

# Research report with CEO analysis
report = skill.generate_report("UX Research Report", include_ceo_analysis=True)
```

### 💡 10 Core Capabilities

| # | Capability | Module | Description |
|---|------------|--------|-------------|
| 1 | **HEART Framework** | `heart.py` | Goals-Signals-Metrics workshops, metric definition and dashboards |
| 2 | **CSat Surveys** | `csat.py` | Satisfaction survey design, analysis, report generation |
| 3 | **Log Analysis** | `logs.py` | Session sequence analysis, frequency stats, transition matrices |
| 4 | **MaxDiff** | `maxdiff.py` | Priority ranking design, analysis, result visualization |
| 5 | **A/B Testing** | `abtest.py` | Sample size calculation, power analysis, result interpretation |
| 6 | **Research Planning** | `research.py` | Research needs diagnosis, method recommendation, timeline planning |
| 7 | **Report Generation** | `research.py` | Standardized research reports, CEO perspective business impact analysis |
| 8 | **CEO: Business Impact** | `research.py` | UX-to-business metric mapping, ROI estimation |
| 9 | **CEO: Validation Timeline** | `research.py` | 4-phase timeline with milestones and decision points |
| 10 | **CEO: Resource Estimation** | `research.py` | Headcount, tools, incentive cost estimation |

### 🔧 Practical Examples

```python
# Example 1: HEART framework for a mobile app
skill = QuantUXSkill("Fitness App")
heart = skill.build_heart_framework()
print(heart)  # Goals → Signals → Metrics for each dimension
workshop = skill.get_workshop_guide()  # Facilitate a GSM workshop

# Example 2: CSat survey design + analysis
survey = skill.design_csat_survey("Q4 Satisfaction", mechanism="in_app", target="Active users")
csat = skill.analyze_csat("2024Q4", 500, {1: 15, 2: 25, 3: 70, 4: 190, 5: 200})
print(f"Top-2-Box: {csat['t2b']}")  # Percentage of 4-5 ratings

# Example 3: A/B test — design and analyze
sample = skill.calculate_ab_sample_size(baseline=0.15, mde=0.03)
print(f"Need {sample} users per group")

result = skill.analyze_ab_test(
    name_a="Control", n_a=5000, conv_a=1750,  # 35%
    name_b="Variant", n_b=5000, conv_b=1900,  # 38%
)
print(result)  # Effect size, confidence interval, recommendation

# Example 4: MaxDiff priority study
maxdiff = skill.design_maxdiff(
    title="Feature Priorities",
    items=["Dark Mode", "Offline Access", "Export Reports", "API Access"],
    items_per_screen=4,
)

# Example 5: CEO-perspective report (business impact + timeline + resource)
report = skill.generate_report("Q4 UX Research Report", include_ceo_analysis=True)

# Example 6: Log analysis for user behavior patterns
skill = QuantUXSkill("SaaS Platform")
log_result = skill.analyze_logs(
    sessions=[
        {"user": "U1", "events": ["login", "dashboard", "settings", "logout"]},
        {"user": "U2", "events": ["login", "dashboard", "reports", "export", "logout"]},
        {"user": "U3", "events": ["login", "dashboard", "settings", "help", "logout"]},
    ]
)
print(log_result)  # Transition matrix, frequent paths, drop-off points
```

### 👥 Who Is This For?

| Role | How This Skill Helps |
|------|---------------------|
| **UX Researchers** | Build HEART metrics, design A/B tests, analyze behavioral logs |
| **Data Scientists** | Sample size calculation, power analysis, MaxDiff prioritization |
| **Product Managers** | Research needs diagnosis, method recommendation, CEO-perspective reports |
| **Experiment Scientists** | A/B test design, statistical significance testing, result interpretation |
| **AI Agents** | Zero-dependency Python package for automated quantitative research |

### 🛠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| Sample size seems too large | Check your MDE (Minimum Detectable Effect) — smaller effects need larger samples |
| HEART metrics unclear | Start with business goals, then work down to measurable signals |
| MaxDiff results inconsistent | Ensure balanced design and sufficient tasks (12+ recommended) |
| Log analysis too noisy | Filter to relevant session types and time windows |

### 🤝 Best Practices

1. **Define metrics before collecting data** — Use HEART framework to align on what matters
2. **Calculate sample size first** — Never run A/B tests without proper power analysis
3. **Triangulate methods** — Combine quantitative (surveys, logs) with qualitative (interviews)
4. **Report with CEO perspective** — Always include business impact and ROI estimates
5. **Track trends over time** — Establish baselines and measure improvement longitudinally

### 🌟 User Reviews

> "The HEART framework implementation helped us align our entire product team on what metrics actually matter. Game changer." — **Head of UX, Travel Platform**

> "Sample size calculator alone saved us from running underpowered A/B tests that would have given us false confidence." — **Data Science Lead, E-commerce**

> "We use this skill to train new researchers. The structured approach to quantitative methods is exactly what our team needed." — **UX Research Manager, SaaS Company**

### 📖 Extended Reading

- **"Quantitative User Experience Research"** — Jeff Sauro and James R. Lewis, the definitive reference
- **"Trustworthy Online Controlled Experiments"** — Ron Kohavi et al., A/B testing at scale
- **"Practical Statistics for UX"** — Jeff Sauro, statistical methods for UX professionals
- **"Measuring the User Experience"** — Tom Tullis and Bill Albert, metrics for UX evaluation

### 📚 About This Skill

This skill is based on the methodology from *"Quantitative User Experience Research"* by Jeff Sauro and James R. Lewis, providing rigorous statistical methods for UX research. The HEART framework (Happiness, Engagement, Adoption, Retention, Task Success) was developed at Google.

### 🔗 Related Skills

This skill is the quantitative research layer of the **AliDujie UX Research Skills Ecosystem**:

```
┌─────────────────────────────────────────────────────────────────────┐
│            AliDujie 技能生态系统 (Skill Ecosystem)                  │
├─────────────────────────────────────────────────────────────────────┤
│   📊 Quantitative UX Research ←───→ 📖 Universal Design Methods     │
│         (量化研究)   三角测量              (通用设计)                │
│              ↑                          ↓                         │
│              │                    🎯 JTBD Knowledge                 │
│              │                      (需求洞察)                      │
│   📈 Storytelling with Data ←───→ 💎 Value Proposition Design       │
│         (数据叙事)   呈现                  (价值设计)                │
│              ↑                          ↑                         │
│              │                    👤 Web Persona                    │
│              └────────────────────  (人物角色)                       │
│                           ↕                                         │
│              🧠 Structured-Thinking-Model (结构化思维)               │
│                  70+ 商业分析框架 · PESTEL · SWOT · 五力模型         │
└─────────────────────────────────────────────────────────────────────┘
```

**Integration patterns:**

- **QuantUX + UDM** — Qualitative-quantitative triangulation for research validity
- **QuantUX + SWD** — Present HEART metrics and A/B test results with compelling narratives
- **QuantUX + JTBD** — Validate JTBD opportunity scores with quantitative data
- **QuantUX + VPD** — Validate value proposition hypotheses with experiments
- **QuantUX + Persona** — Quantify persona behavior patterns with log analysis
- **QuantUX + Structured Thinking** — Design research hypotheses with structured frameworks

👉 **Explore the full ecosystem**: [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) | [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) | [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) | [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) | [Web Persona](https://github.com/AliDujie/web-persona-skill) | [Structured Thinking](https://github.com/AliDujie/Structured-Thinking-Model)

### 🌟 Why Choose AliDujie Skill Ecosystem?

This skill is part of the **AliDujie UX Research Skills Ecosystem**. Using the complete ecosystem provides:

- ✅ **Complete Coverage** — From user research to product design to data presentation, full-process tool support
- ✅ **Seamless Integration** — All skills use consistent API design and data formats
- ✅ **Best Practices** — Based on classic theories and practical experience, avoid common pitfalls
- ✅ **Active Maintenance** — Regularly updated with new features and improvements
- ✅ **Zero Dependencies** — Pure Python standard library, ready to use out of the box
- ✅ **Bilingual Support** — Complete CN/EN documentation for international team collaboration

👉 **Explore More Skills**: [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) | [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) | [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) | [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) | [Web Persona](https://github.com/AliDujie/web-persona-skill) | [Structured Thinking](https://github.com/AliDujie/Structured-Thinking-Model)

### 🏷️ GitHub Topics (Recommended)

```
quantitative-research heart-framework ab-testing maxdiff
user-experience metrics python-toolkit openclaw-skill alicloud
```

### 📋 Changelog

| Version | Date | Changes |
|---------|------|--------|
| v2.3.4 | 2026-05-03 | Repo maintenance: added ecosystem ASCII diagram and integration patterns to English Related Skills section, enhanced Why Choose section with ecosystem benefits |
| v2.3.2 | 2026-05-02 | Repo maintenance: added English "Who Is This For?" section, GitHub Topics, and changelog to English section |
| v2.3.1 | 2026-05-02 | Fixed Python version mismatch, added Last Updated badge |
| v2.2.10 | 2026-05-01 | Unified cross-references to GitHub absolute links |

---

## Run Tests / 运行测试

```bash
cd /path/to/Quantitative-UX-Research
python3 quantux/tests/test_all.py
# 或使用 pytest
python3 -m pytest quantux/tests/test_all.py -v
```

## 🤝 参与贡献 (Contributing)

欢迎贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解贡献指南。

- 🐛 **报告 Bug**: 提交 [Issue](https://github.com/AliDujie/Quantitative-UX-Research/issues)
- 💡 **功能建议**: 提交 [Feature Request](https://github.com/AliDujie/Quantitative-UX-Research/issues/new?template=feature_request.md)
- 📝 **改进文档**: PR 欢迎，特别是参考文档和代码示例

## 🆘 获取帮助 (Getting Help)

- 📖 查看 [故障排查](#故障排查-troubleshooting) 部分
- 📚 阅读 [references/](references/) 目录下的方法论文档
- 💬 在 [Issues](https://github.com/AliDujie/Quantitative-UX-Research/issues) 中提问

## 📜 许可 (License)

基于《Quantitative User Experience Research》by Jeff Sauro & James R. Lewis (2023)。
本技能仅供内部学习和研究使用。

## 👨‍💻 作者 (Credits)

- 基于《Quantitative User Experience Research》by Jeff Sauro & James R. Lewis
- 技能开发：AliDujie 团队
- **GitHub**: [@AliDujie](https://github.com/AliDujie)
- **Emp ID**: 27768
- **Nickname**: 渡劫

---

**版本 / Version**: v2.3.4

---

## 🔗 Skill Ecosystem Workflow

QuantUX is the quantitative research layer of the **AliDujie UX Research Skills Ecosystem**. Here are typical workflows combining it with other skills:

### 🧭 Quick Decision Guide

Not sure which skill to use? Follow these steps:

| Your Question | Recommended Skill |
|---------------|------------------|
| "I need to validate a hypothesis" | → **Quantitative UX Research** (this skill) — A/B testing, sample size, HEART framework |
| "I don't know what research to do" | → [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) — Method recommendation |
| "I want to understand why users do this" | → [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) — Uncover the underlying "jobs" |
| "I need to know who my users are" | → [Web Persona](https://github.com/AliDujie/web-persona-skill) — Create concrete personas |
| "Is my product value strong enough?" | → [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) — Fit diagnosis |
| "How do I present research results clearly?" | → [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) — Data storytelling |

### Workflow 1: Research → Quantitative Validation → Story

```
UDM/JTBD (qualitative insights) → QuantUX (quantitative validation) → SWD (storytelling)
```

**Scenario**: Validating user research findings
1. Use UDM or JTBD to collect qualitative user insights
2. Use QuantUX to design surveys, A/B tests, and calculate statistical significance
3. Use SWD to transform validated results into compelling data narratives

### Workflow 2: HEART Metrics → Business Decisions

```
QuantUX (HEART framework) → VPD (value validation) → CEO review
```

**Scenario**: Product direction decisions
1. Use QuantUX to build HEART metrics system (Happiness, Engagement, Adoption, Retention, Task success)
2. Use VPD to validate value proposition hypotheses
3. Use CEO review framework to assess business impact

### Workflow 3: User Segments → Targeted Testing

```
Persona (user segments) → QuantUX (stratified A/B testing) → JTBD (opportunity scoring)
```

**Scenario**: Personalized product optimization
1. Use Persona to create user segments
2. Use QuantUX to design stratified A/B tests for each segment
3. Use JTBD to calculate opportunity scores per segment

> 💡 **Tip**: QuantUX's CEO-perspective reporting is especially powerful for presenting research results to executive stakeholders.

---

## 🔗 技能生态工作流 (Skill Ecosystem Workflow)

本技能是 **AliDujie UX 研究技能生态系统** 的定量研究层。以下是与其他技能配合使用的典型工作流：


### 🧭 快速决策指南 (Quick Decision Guide)

不确定该用哪个技能？按以下步骤选择：

| 你的问题 | 推荐技能 |
|----------|----------|
| "我不知道该研究什么" | → **Universal Design Methods** — 方法推荐帮你找到方向 |
| "我需要验证一个假设" | → **Quantitative UX Research** — A/B 测试和样本量计算 |
| "我想理解用户为什么这样做" | → **JTBD Knowledge** — 挖掘用户背后的"工作" |
| "我需要知道用户是谁" | → **Web Persona** — 创建具体的人物角色 |
| "我的产品价值够不够？" | → **Value Proposition Design** — 契合度诊断 |
| "我怎么把研究结果讲清楚？" | → **Storytelling with Data** — 数据叙事和图表改造 |
| "我需要一个完整的流程" | → **组合使用** — 见下方工作流 |

> 💡 **提示**: 这些技能设计为可组合使用。从 UDM 或 JTBD 开始，用 QuantUX 验证，用 SWD 呈现。

### 工作流 1: 定性 → 定量三角验证

```
UDM (定性研究) → QuantUX (定量验证) → SWD (结果呈现)
```

**场景**: 研究结论验证
1. 用 UDM 进行用户访谈，发现假设
2. 用 QuantUX 设计定量验证（A/B 测试 + 样本量计算）
3. 用 SWD 将验证结果可视化

### 工作流 2: 指标体系 → 业务决策

```
QuantUX (HEART 框架) → VPD (价值验证) → CEO 审查
```

**场景**: 产品方向决策
1. 用 QuantUX 构建 HEART 指标体系
2. 用 VPD 验证价值主张假设
3. 用 CEO 审查框架评估业务影响

### 工作流 3: 用户细分 → 精准测试

```
Persona (用户细分) → QuantUX (分层 A/B 测试) → JTBD (机会评分)
```

**场景**: 个性化产品优化
1. 用 Persona 创建用户细分
2. 用 QuantUX 为每个细分设计 A/B 测试
3. 用 JTBD 计算各细分的机会分数

> 💡 **提示**: QuantUX 的 CEO 视角报告功能特别适合向高管层汇报研究结果。


## 📋 版本历史 (Changelog)

| 版本 | 日期 | 变更 |
|------|------|------|
| v2.3.4 | 2026-05-03 | 仓库维护：为英文 Related Skills 添加生态系统 ASCII 图和集成模式说明，增强 Why Choose 部分描述 |
| v2.3.3 | 2026-05-02 | 仓库维护：为英文版添加 Quick Decision Guide 导航表，增强技能间交叉引用 |
| v2.3.2 | 2026-05-02 | 仓库维护：优化英文示例代码格式，增强工作流 3 描述，统一交叉引用格式，补充 CEO 能力英文版表格 |
| v2.3.1 | 2026-05-02 | 修复 Python 版本不一致 (3.9+→3.8+)，添加 Last Updated badge，补充 CEO 能力到英文能力表 |
| v2.2.10 | 2026-05-01 | 统一交叉引用为 GitHub 绝对链接，更新 Last Updated 日期 |
| v2.2.9 | 2026-04-28 | 添加 Badges、技能生态系统图、双语支持 |
| v2.2.0 | 2026-04-23 | 添加版本历史、快速参考、CEO 视角扩展 |
| v1.0 | 2026-04-22 | 初始版本 |

---

*Last Updated: 2026-05-03 | AliDujie Skill Ecosystem | v2.3.4*
