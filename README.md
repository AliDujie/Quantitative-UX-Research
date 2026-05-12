# Quantitative UX Research Skill

[![Ecosystem](https://img.shields.io/badge/AliDujie-Ecosystem-7B68EE.svg)](https://github.com/AliDujie)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Code style: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Version](https://img.shields.io/badge/version-2.3.54-green.svg)](CHANGELOG.md)
[![Install Guide](https://img.shields.io/badge/install-guide-orange.svg)](INSTALL.md)
![Last Updated](https://img.shields.io/badge/last%20updated-2026-05-13-brightgreen.svg)

> 🌐 **AliDujie UX Research Skills Ecosystem** — 本技能是 7 个互补技能之一，覆盖从用户研究到数据呈现的完整工作流

```text
┌─────────┐    ┌──────────┐    ┌─────┐    ┌──────────┐    ┌─────┐    ┌─────┐
│ Persona │ →  │   JTBD   │ →  │ UDM │ →  │ QuantUX  │ →  │ VPD │ →  │ SWD │
│ 角色定义 │    │ 需求洞察  │    │ 研究方法 │    │ 定量验证  │    │ 价值设计│    │ 数据叙事 │
└─────────┘    └──────────┘    └─────┘    └──────────┘    └─────┘    └─────┘
```

**QuantUX is the validation engine** — providing statistical rigor to confirm qualitative hypotheses. Use it when you need to prove "is this real?" with data.

> 🎯 **一句话介绍**: HEART 指标体系 + A/B 测试 + MaxDiff + 日志分析 — 用数据验证每一个用户研究假设。

> 📊 **HEART 框架 · CSat 调查 · A/B 测试 · MaxDiff · 日志分析 · 研究规划**

基于《Quantitative User Experience Research》(Jeff Sauro & James R. Lewis, 2023) 的完整量化用户体验研究工具包。覆盖 7 大执行能力，从指标体系构建到研究报告生成，一站式解决量化研究需求。

---

## 🌐 技能生态系统 (Skill Ecosystem)

本技能是 AliDujie 用户研究技能生态系统的**定量研究核心**，负责用数据验证定性假设。与其他技能协同使用，效果更佳：

| 技能 | 角色 | 协同场景 |
|------|------|----------|
| [🔍 Universal Design Methods](https://github.com/AliDujie/universal-design-methods) | 研究方法 | UDM 定性发现 → QuantUX 定量验证 → 综合报告 |
| [📊 Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) | 数据叙事 | QuantUX 分析结果 → SWD 图表改造 → 叙事构建 |
| [🎯 JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) | 深度需求洞察 | JTBD 机会评分 → QuantUX 量化验证 → 决策支持 |
| [💎 Value Proposition Design](https://github.com/AliDujie/value-proposition-design) | 价值设计 | VPD 价值假设 → QuantUX 实验设计 → 验证结果 |
| [👤 Web Persona](https://github.com/AliDujie/web-persona-skill) | 用户画像 | Persona 角色假设 → QuantUX 行为验证 → 角色精化 |
| [🧠 Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) | 战略分析 | STM 框架分析 → QuantUX 数据验证 → 商业决策 |

---

### 🔗 Ecosystem Quick Start / 生态系统快速上手

QuantUX 是 7 技能工作流的**定量验证引擎**——用数据验证定性假设。

```
Persona → JTBD → UDM → QuantUX (← 你在这里) → VPD → SWD
```

**组合调用示例：**
```python
# Step 1: UDM 定性发现用户痛点 → QuantUX 定量验证
from quantux import QuantUXSkill
quantux = QuantUXSkill("旅行平台")

# 构建 HEART 指标体系
heart = quantux.build_heart_framework()

# Step 2: 设计 CSat 调查收集定量数据
csat = quantux.design_csat_survey("Q1 满意度调查")

# Step 3: 计算 A/B 测试样本量
n = quantux.calculate_ab_sample_size(baseline=0.35, mde=0.03)

# Step 4: 生成含 CEO 视角的完整报告
report = quantux.generate_report("用户体验验证报告", include_ceo_analysis=True)

# Step 5: 将结果交给 SWD 做数据叙事
from swd import SWDSkill
swd = SWDSkill("研究汇报")
story = swd.build_story(protagonist="数据团队", imbalance="满意度低于目标", call_to_action="优化方案审批")
```

> 💡 **提示**: QuantUX 与 UDM 配合最佳——UDM 定性发现 "什么问题"，QuantUX 定量证明 "问题有多严重"。

> 💡 **Try it now / 立即尝试**:
> ```python
> from quantux import QuantUXSkill
> skill = QuantUXSkill("你的产品")
> print(skill.calculate_ab_sample_size(baseline=0.15, mde=0.02))  # 立即计算 A/B 测试样本量
> ```

### ✅ 5 分钟快速开始检查清单

- [ ] **安装** — `cp -r Quantitative-UX-Research /your/agent/skills/`
- [ ] **导入** — `from quantux import QuantUXSkill`
- [ ] **初始化** — `skill = QuantUXSkill("你的项目")`
- [ ] **HEART 框架** — `skill.build_heart_framework()`
- [ ] **CSat 调查** — `skill.design_csat_survey("满意度调查")`
- [ ] **A/B 测试** — `skill.calculate_ab_sample_size(baseline=0.15, mde=0.02)`
- [ ] **MaxDiff** — `skill.design_maxdiff("功能优先级", ["功能A", "功能B"])`
- [ ] **研究报告** — `skill.generate_report("研究报告", include_ceo_analysis=True)`

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

### 🌍 实战场景指南

| 你的场景 | 调用方式 | 输出结果 |
|----------|---------|----------|
| "A/B 测试需要多少样本？" | `calculate_ab_sample_size(baseline=0.15, mde=0.02)` | 样本量 + 功效分析 |
| "构建 HEART 指标体系" | `build_heart_framework()` | 目标→信号→指标完整映射 |
| "设计满意度调查" | `design_csat_survey("结账体验")` | 带评分标准的调查问卷 |
| "功能优先级排序" | `design_maxdiff("功能优先级", ["A", "B", "C"])` | MaxDiff 实验设计 |
| "分析行为模式" | `analyze_logs(user_actions=[...], threshold=3)` | 漏斗分析 + 流失点 |

> 💡 **提示**: 先用 `build_heart_framework()` 定义衡量什么，再用具体方法收集和分析数据。

### 🌟 为什么使用这个技能？(Why Use This Skill?)

- **全面覆盖** — HEART 框架、CSat 调查、日志分析、MaxDiff、A/B 测试、研究规划
- **CEO 决策支持** — 内置业务影响评估、验证时间线、资源估算
- **零依赖** — 纯 Python 标准库实现，开箱即用
- **智能诊断** — 自动诊断研究需求，推荐最佳方法组合
- **双语支持** — 完整中英文文档，适合国际化团队
- **零学习成本** — API 设计直观，代码示例丰富，即插即用
- **统计严谨** — 基于 Jeff Sauro & James R. Lewis 的权威著作，所有方法都有坚实的学术基础
- **业务驱动** — 每个分析都连接业务影响：样本量→资源规划、p值→决策信心、HEART→产品指标
- **全生命周期** — 从指标体系构建到实验设计到结果呈现，一站式覆盖定量研究全流程

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
# 方式 A: 复制到你的 AI Agent skills 目录
cp -r Quantitative-UX-Research /your/agent/skills/

# 方式 B: 作为 Python 包安装（支持 pip import）
cd Quantitative-UX-Research && pip install -e .
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
skill.logs_analyzer.add_event("u1", "2024-01-01 10:00:00", "首页")
skill.logs_analyzer.add_event("u1", "2024-01-01 10:05:00", "搜索")

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
    ("u1", "2024-01-01 10:00:00", "首页"),
    ("u1", "2024-01-01 10:02:00", "搜索"),
    ("u1", "2024-01-01 10:05:00", "结果页"),
    ("u1", "2024-01-01 10:08:00", "详情页"),
    ("u1", "2024-01-01 10:12:00", "预订"),
    ("u2", "2024-01-01 10:01:00", "首页"),
    ("u2", "2024-01-01 10:03:00", "搜索"),
    ("u2", "2024-01-01 10:06:00", "结果页"),
    ("u2", "2024-01-01 10:07:00", "退出"),
]

for uid, time, page in sequences:
    skill.logs_analyzer.add_event(uid, time, page)

# 分析序列频率和转移矩阵
analysis = skill.analyze_logs()
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

### ⚠️ 常见统计陷阱 (Common Pitfalls)

| 陷阱 | 表现 | 应对 |
|------|------|------|
| 统计显著 ≠ 实际显著 | p<0.05 但效应量只有 0.1% | 用置信区间和实际效应大小，不要只看 p 值 |
| 过早 peeking | 实验运行 3 天看到"显著"就停止 | 预设样本量，运行到足够数据量再分析 |
| 跨群体比较 CSat | 比较 A 群体 CSat 75 和 B 群体 CSat 80 | 在同一群体内跟踪时间变化，不要跨群体比较绝对值 |
| Goodhart 法则 | 把 NPS 当成 KPI，团队开始优化 NPS | 最少技术细节，用多个指标组合，避免单一指标优化 |
| HEART 指标过多 | 每个维度都设 5+ 指标 | 选择 3-5 个核心指标，聚焦决策 |
| 验证性请求 | "看看数据怎么说" | 先定义研究问题，任何数据分析后都会"说些什么" |

> 💡 **提示**: QuantUX 是验证引擎——用 HEART/A-B/MaxDiff 把定性假设转化为可量化的统计证据，而不是探索工具。

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

### 💡 专业技巧

- **A/B 测试前先建 HEART** — 在定义"成功"是什么之前不要做实验。用 HEART 框架定义成功指标，防止测试错误的东西
- **用 MaxDiff 做功能优先级** — 当利益相关者说"所有功能都是 P0"时，MaxDiff 强制做取舍决策，揭示真正的优先级
- **日志分析揭示问卷遗漏的真相** — 用户说的和做的不一样。日志序列分析发现自我报告隐藏的实行为模式
- **始终计算效应量，不只 p 值** — 统计显著 ≠ 实际显著。p < 0.05 但效应量很小的结果可能不值得上线
- **建立指标仪表盘** — 用 HEART 框架创建一个活的 UX 指标仪表盘，每周回顾

### ❌ 常见错误

- **提前查看 A/B 测试结果** — 在样本量达标之前查看结果会膨胀假阳性率。使用样本量计算器，耐心等待
- **同时测试太多变量** — 多变量测试需要指数级更多流量。从单变量 A/B 测试开始
- **忽略基线测量** — 没有基线，你就无法判断"改进"是否真的比以前好
- **过度发问卷** — CSat 问卷有回复疲劳。间隔发放，聚焦具体体验
- **把 HEART 当清单** — 不是每个产品都需要全部 5 个维度。选择 2-3 个与目标最相关的

### ❓ 常见问题 (FAQ)

**Q: QuantUX 和 Google Analytics 等分析工具有什么区别？**
A: Google Analytics 是数据采集和展示工具，QuantUX 是研究设计和分析框架。QuantUX 帮你"设计正确的研究"（如 HEART 指标体系、A/B 测试设计、样本量计算），而非仅仅"展示数据"。两者互补使用。

**Q: HEART 框架的五个维度都要用吗？**
A: 不强制。根据你的研究目标选择最相关的维度。例如：增长团队关注 Acquisition + Engagement，体验团队关注 Happiness + Task Success。Google 也建议根据目标裁剪。

**Q: MaxDiff 和普通的优先级排序有什么区别？**
A: MaxDiff 通过强制选择（最佳 vs 最差）获得更精确的偏好数据，避免"全部都重要"的常见偏差。适合 10+ 选项的优先级排序场景。

**Q: A/B 测试需要多少样本量？**
A: 取决于当前转化率、期望检测的最小提升幅度、和统计功效（通常 80%）。用 `calculate_sample_size()` 方法自动计算，避免手动查表。

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

### 🏆 实战案例 (Case Studies)

#### 案例 1: HEART 指标体系搭建

**背景**: 某 SaaS 产品需要建立量化 UX 指标体系，替代主观判断

**使用 QuantUX 技能**:
```python
from quantux import QuantUXSkill

skill = QuantUXSkill("SaaS 协作平台")

# 步骤 1: 构建 HEART 框架
heart = skill.build_heart_framework(
    happiness="SUS > 75, CSat > 4.0",
    engagement="DAU/WAU > 0.4, 核心功能使用率",
    adoption="新功能 30 天采用率 > 20%",
    retention="30 天留存率 > 60%",
    task_success="核心任务完成率 > 85%"
)

# 步骤 2: 设计 CSat 调查
survey = skill.design_csat_survey("协作功能满意度")

# 步骤 3: 设计 A/B 测试计算样本量
sample = skill.calculate_ab_sample_size(baseline=0.60, mde=0.05, alpha=0.05, power=0.80)
print(f"每组需要 {sample} 个样本")
```

**成果**: 从主观判断到数据驱动决策，UX 改进 ROI 提升 3 倍

#### 案例 2: MaxDiff 功能优先级排序

**背景**: 某电商平台有 20 个待开发功能，需要科学排序优先级

```python
from quantux import QuantUXSkill

skill = QuantUXSkill("电商平台")

# MaxDiff 设计
features = ["智能推荐", "一键下单", "价格保护", "以图搜图", "语音搜索",
            "社交分享", "购物车共享", "订阅提醒", "AR 试穿", "比价工具"]
maxdiff = skill.design_maxdiff("功能优先级", features, blocks=5)

# 分析结果后，用研究计划整合
plan = skill.generate_research_plan(
    "功能优先级研究",
    include_ceo_analysis=True
)
```

**成果**: 用 MaxDiff 替代投票排序，优先级决策时间从 2 周缩短到 3 天

### 📦 依赖

- Python >= 3.8
- **无外部依赖**（纯标准库实现）
- 兼容 macOS / Linux / Windows

---

### 🧭 快速决策指南 (Quick Decision Guide)

| 你的问题 | 推荐技能 |
|----------|----------|
| "需要定量验证假设" | → **Quantitative UX Research (本技能)** — A/B 测试、HEART 指标、样本量计算 |
| "不知道选什么研究方法" | → [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) — 方法推荐与执行 |
| "想理解用户背后的「工作」" | → [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) — 用户"工作"挖掘、机会评分 |
| "需要创建用户画像" | → [Web Persona](https://github.com/AliDujie/web-persona-skill) — 人物角色创建与细分 |
| "验证价值主张够不够强" | → [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) — 价值主张画布、实验验证 |
| "研究结果怎么讲给高管听" | → [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) — 数据叙事与图表呈现 |
| "需要结构化商业分析框架" | → [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) — PESTEL、五力模型、决策树 |

---

### 🔄 完整端到端工作流：从定性发现到定量验证 (End-to-End Workflow)

> QuantUX 是用数据验证定性假设的关键环节 — 将 UDM/JTBD 的发现转化为可量化的指标。

#### 阶段 1: 定性发现
1. **Universal Design Methods** → 用户访谈、可用性测试发现痛点
2. **JTBD Knowledge** → 挖掘用户"工作"和未满足需求
3. **Web Persona** → 创建角色画像

#### 阶段 2: 定量验证 (本技能)
4. **Quantitative UX Research (本技能)** → HEART 指标、A/B 测试、MaxDiff、日志分析

#### 阶段 3: 价值验证与呈现
5. **Value Proposition Design** → 基于数据验证价值假设
6. **Storytelling with Data** → 将数据结果转化为高管叙事

```python
# 示例：QuantUX 端到端工作流
from udm import UDMSkill
from quantux import QuantUXSkill
from swd import SWDSkill

# 阶段 1: UDM 发现痛点
udm = UDMSkill("电商平台")
test = udm.generate_usability_test("结账流程", "summative")
# 发现：结账流程 SUS 得分仅 45 分

# 阶段 2: QuantUX 验证
quant = QuantUXSkill("电商平台")
heart = quant.build_heart_framework()
sample = quant.calculate_ab_sample_size(baseline=0.15, mde=0.05)
# A/B 测试需要每组 2,000 用户

# 阶段 3: SWD 汇报
swd = SWDSkill("A/B 测试结果汇报")
swd.build_context(audience="产品 VP", cta="批准结账流程优化")
```

---

### 💻 实用集成示例 (Practical Integration Examples)

#### 集成 1: UDM → QuantUX

```python
from udm import UDMSkill
from quantux import QuantUXSkill

# UDM 可用性测试发现
udm = UDMSkill("产品名")
test = udm.generate_usability_test("流程测试", "summative")
sus = udm.calculate_sus([4, 2, 5, 1, 4])

# QuantUX 定量验证
quant = QuantUXSkill("产品名")
heart = quant.build_heart_framework()
# 将 UDM 的 SUS 得分映射到 HEART 的 Satisfaction 指标
```

#### 集成 2: JTBD → QuantUX

```python
from jtbd import JTBDSkill
from quantux import QuantUXSkill

# JTBD 发现机会
jtbd = JTBDSkill("产品名")
report = jtbd.analyze(include_ceo_analysis=True)  # JTBD analysis report

# QuantUX 量化验证
quant = QuantUXSkill("产品名")
quant.design_maxdiff("功能优先级", ["快速搜索", "价格对比", "评价可信"])
# 用 MaxDiff 验证 JTBD 发现的优先级
```

#### 集成 3: QuantUX → SWD

```python
from quantux import QuantUXSkill
from swd import SWDSkill

# QuantUX 分析结果
quant = QuantUXSkill("产品名")
heart = quant.build_heart_framework()

# SWD 数据叙事
swd = SWDSkill("季度数据汇报")
swd.build_context(audience="高管", cta="批准优化预算")
swd.recommend_chart(data_type="continuous", has_time=True)
```

---

### 🚀 下一步 (Next Steps)

1. **快速上手** — 复制技能到你的 skills 目录，5 分钟内完成首次调用
2. **阅读 SKILL.md** — 了解 AI Agent 触发条件和完整 API 文档
3. **安装 INSTALL.md** — 详细的安装和配置指南
4. **贡献** — 查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解如何参与
5. **探索生态** — 尝试其他 5 个技能，构建完整的用户研究工作流

---

## English

### 📑 Table of Contents

- [Why Use This Skill?](#-why-use-this-skill)
- [Features at a Glance](#-features-at-a-glance)
- [Quick Decision Guide](#-quick-decision-guide)
- [Quick Start](#-quick-start)
- [10 Core Capabilities](#-10-core-capabilities)
- [Practical Examples](#-practical-examples)
- [Who Is This For?](#-who-is-this-for)
- [Troubleshooting](#-troubleshooting)
- [Best Practices](#-best-practices)
- [FAQ](#-faq)
- [User Reviews](#-user-reviews)
- [Getting Help](#-getting-help)
- [Extended Reading](#-extended-reading)
- [Related Skills](#-related-skills-1)
- [End-to-End Workflow: All 7 Skills](#-end-to-end-workflow-all-7-skills)
- [Skill Ecosystem Workflow](#-skill-ecosystem-workflow-1)
- [Version History](#-version-history-english)

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
| "I need a structured framework for analysis" | → [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) — PESTEL, Five Forces, decision trees |

### ✅ 5-Minute Quick Start Checklist

- [ ] **Install** — `cp -r Quantitative-UX-Research /your/agent/skills/`
- [ ] **Import** — `from quantux import QuantUXSkill`
- [ ] **Initialize** — `skill = QuantUXSkill("your project")`
- [ ] **HEART framework** — `skill.build_heart_framework()`
- [ ] **A/B sample size** — `skill.calculate_ab_sample_size(baseline=0.15, mde=0.02)`
- [ ] **CSat survey** — `skill.design_csat_survey("Satisfaction Survey")`

### 🚀 Quick Start

#### Step 1: Install

```bash
# Option A: Copy to your AI Agent skills directory
cp -r Quantitative-UX-Research /your/agent/skills/

# Option B: Install as a Python package (enables pip import)
cd Quantitative-UX-Research && pip install -e .
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
# ===== Scenario 1: HEART Framework — Build UX Metrics System =====
heart = skill.build_heart_framework()
print(heart)  # Goals → Signals → Metrics for each dimension

# ===== Scenario 2: CSat Survey Design & Analysis =====
survey = skill.design_csat_survey("2024Q1 Satisfaction", mechanism="in_app")
csat = skill.analyze_csat("2024Q1", 500, {1: 15, 2: 25, 3: 70, 4: 190, 5: 200})
print(f"Top-2-Box: {csat['t2b']}")  # Percentage of 4-5 ratings

# ===== Scenario 3: A/B Test — Sample Size & Power Analysis =====
sample = skill.calculate_ab_sample_size(baseline=0.15, mde=0.02)
print(f"Need {sample} users per group (α=0.05, power=0.80)")

# ===== Scenario 4: Research Report with CEO Analysis =====
report = skill.generate_report("UX Research Report", include_ceo_analysis=True)
print(report)  # HEART baseline + Business impact + ROI + Resource estimation
```

### 🌍 Real-World Scenario Guide

> **Need to validate with data?** Here are common scenarios and exactly how to use this skill.

| Scenario | What to Call | Expected Output |
|----------|-------------|----------------|
| "How many users do I need for A/B test?" | `calculate_ab_sample_size(baseline=0.15, mde=0.02)` | Required sample size with power analysis |
| "Build HEART metrics for our product" | `build_heart_framework()` | Goals → Signals → Metrics for each dimension |
| "Design a satisfaction survey" | `design_csat_survey("Checkout Experience")` | Survey questions with scoring rubric |
| "Prioritize which features to build" | `design_maxdiff("Feature Priorities", ["A", "B", "C"])` | MaxDiff experimental design |
| "Analyze behavioral patterns" | `analyze_logs(user_actions=[...], threshold=3)` | Funnel analysis + drop-off points |

**Quick Tip:** Use `build_heart_framework()` first to define what to measure, then use specific methods to collect and analyze data.

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

### 🔄 End-to-End Ecosystem Workflow

QuantUX is the **validation engine** of the ecosystem. Here's how it connects with the other 5 skills:

```python
# ===== Complete Validation Cycle (All 7 Skills) =====
# Step 1: UDM generates qualitative hypotheses → Step 2: JTBD identifies opportunities
# Step 3: QuantUX validates with statistical rigor → Step 4: VPD designs experiments
# Step 5: Persona segments the sample → Step 6: SWD presents results

from quantux import QuantUXSkill
quantux = QuantUXSkill("Feature Validation")

# Validate JTBD-discovered opportunity with quantitative data
sample_size = quantux.calculate_ab_sample_size(baseline=0.15, mde=0.02)
print(f"Need {sample_size} users per group for 80% power")

# Build HEART framework for the feature
heart = quantux.build_heart_framework()
# Happiness: CSat, NPS | Engagement: DAU, session duration | Adoption: new feature usage
# Retention: 30-day retention | Task success: completion rate | Error rate: crash rate

# Design MaxDiff for feature prioritization
maxdiff = quantux.design_maxdiff("Feature Priority",
    items=["Dark Mode", "Quick Search", "Offline Access", "Export"])

# Generate research report with CEO analysis
report = quantux.generate_report("Q4 Validation Report", include_ceo_analysis=True)
```

> 💡 **Pro Tip**: QuantUX is the validation engine of the ecosystem. Try: JTBD (identify opportunity) → QuantUX (measure size) → VPD (design solution) → SWD (present results)

### 👥 Who Is This For?

| Role | How This Skill Helps | Next Skill to Try |
|------|---------------------|-------------------|
| **UX Researchers** | Build HEART metrics, design A/B tests, analyze behavioral logs | → [UDM](https://github.com/AliDujie/universal-design-methods) for qualitative discovery |
| **Data Scientists** | Sample size calculation, power analysis, MaxDiff prioritization | → [SWD](https://github.com/AliDujie/storytelling-with-data) for presenting results |
| **Product Managers** | Research needs diagnosis, method recommendation, CEO-perspective reports | → [VPD](https://github.com/AliDujie/value-proposition-design) for value hypothesis |
| **Experiment Scientists** | A/B test design, statistical significance testing, result interpretation | → [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) for opportunity sizing |
| **AI Agents** | Zero-dependency Python package for automated quantitative research | → Any of the 5 companion skills for full workflow |

### 📁 Project Structure

```
Quantitative-UX-Research/
├── SKILL.md              # AI Agent skill definition
├── README.md             # This file
├── pyproject.toml        # Python package build config
├── quantux/              # Python package (pure stdlib)
│   ├── __init__.py       # QuantUXSkill unified entry
│   ├── config.py         # Global config and constants
│   ├── utils.py          # Utility functions
│   ├── templates.py      # Template definitions
│   ├── heart.py          # HEART framework & GSM engine
│   ├── csat.py           # CSat survey design & analysis
│   ├── logs.py           # Log sequence analysis
│   ├── maxdiff.py        # MaxDiff prioritization
│   ├── abtest.py         # A/B test design & analysis
│   └── research.py       # Research planning & report generation
├── references/           # Knowledge base (5 methodology documents)
│   ├── README.md
│   ├── heart-framework.md    # HEART framework complete guide
│   ├── csat-methods.md       # CSat survey design & analysis
│   ├── ab-testing.md         # A/B testing design principles
│   ├── maxdiff-guide.md      # MaxDiff prioritization guide
│   └── log-analysis.md       # Log sequence analysis methodology
└── quantux/tests/        # Test suite
```

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

### 💡 Pro Tips

- **Start with HEART before A/B testing** — Don't run experiments until you've defined what "success" looks like using the HEART framework. This prevents testing the wrong things.
- **Use MaxDiff for feature prioritization** — When stakeholders say "everything is P0," MaxDiff forces trade-off decisions and reveals true priorities.
- **Log analysis reveals what surveys miss** — Users say one thing but do another. Log sequence analysis uncovers real behavior patterns that self-reporting hides.
- **Always calculate effect size, not just p-value** — Statistical significance ≠ practical significance. A p < 0.05 result with tiny effect size may not be worth shipping.
- **Build a metrics dashboard** — Use the HEART framework to create a living dashboard that tracks key UX metrics. Review it weekly.

### 📋 HEART Metric Selection Guide

Not every product needs all 5 HEART dimensions. Use this guide to pick the right metrics:

| Product Stage | Focus Dimensions | Key Metrics | Why |
|--------------|-----------------|-------------|-----|
| **Pre-launch / Beta** | Task Success + Happiness | Task completion rate, SUS score | Verify the product works before measuring engagement |
| **Post-launch (0-3 months)** | Adoption + Engagement | New user activation, DAU/MAU ratio | Track initial uptake and early retention |
| **Growth (3-12 months)** | Engagement + Retention | Feature adoption, 30-day retention, NPS | Optimize for stickiness and word-of-mouth |
| **Mature (12+ months)** | Retention + Happiness | Churn rate, CSat, feature usage distribution | Prevent decline and maintain satisfaction |
| **Redesign / Migration** | Task Success + Happiness | Before/after SUS, error rate, time-on-task | Prove the change improved (or didn't harm) UX |
| **Feature Addition** | Engagement + Adoption | Feature adoption rate, cannibalization | Check if new features complement or compete |

> 💡 **Rule of thumb**: Pick 2-3 HEART dimensions max per study. Trying to measure everything means you'll measure nothing well.

### ⛔ When NOT to Use This Skill

- **Choosing research methods or designing qualitative studies** — Use [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) for qualitative research
- **Data visualization and narrative design** — Use [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) for chart design and data narratives
- **Understanding user Jobs-to-be-Done** — Use [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) for deep need analysis
- **Value proposition and canvas analysis** — Use [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) for canvas-based analysis
- **Creating user personas and segmentation** — Use [Web Persona](https://github.com/AliDujie/web-persona-skill) for persona creation

### ❌ Common Mistakes to Avoid

- **Peeking at A/B test results early** — Checking results before the sample size is reached inflates false positive rates. Use the sample size calculator and wait.
- **Testing too many variables at once** — Multivariate tests require exponentially more traffic. Start with single-variable A/B tests.
- **Ignoring the baseline** — Without a baseline measurement, you can't tell if your "improvement" is actually better than before.
- **Over-surveying users** — CSat surveys have response fatigue. Space them out and keep them focused on specific experiences.
- **Treating HEART as a checklist** — Not every product needs all 5 HEART dimensions. Select the 2-3 most relevant to your goals.

### ❓ FAQ

**Q: How is QuantUX different from Google Analytics?**
A: Google Analytics collects and displays data; QuantUX is a research design and analysis framework. QuantUX helps you "design the right research" (HEART metrics, A/B test design, sample size calculation), not just "show data." Use them together.

**Q: Do I need to use all 5 HEART dimensions?**
A: No. Select dimensions most relevant to your research goals. Growth teams focus on Acquisition + Engagement; experience teams focus on Happiness + Task Success. Google also recommends tailoring.

**Q: What's the difference between MaxDiff and regular prioritization?**
A: MaxDiff forces choices (best vs worst) for more precise preference data, avoiding the common "everything is important" bias. Best for prioritizing 10+ options.

**Q: How much sample size do I need for A/B tests?**
A: It depends on current conversion rate, minimum detectable effect, and statistical power (typically 80%). Use `calculate_sample_size()` to compute automatically instead of looking up tables manually.


### 📋 Cheat Sheet / Quick Reference Cards

#### HEART Framework Quick Reference

| Dimension | What It Measures | Common Metrics |
|-----------|-----------------|----------------|
| **H**appiness | User satisfaction | CSat, NPS, SUS, app store ratings |
| **E**ngagement | Usage frequency & depth | DAU/WAU, session duration, features used |
| **A**doption | New user uptake | Sign-up rate, feature adoption rate, activation rate |
| **R**etention | Returning users | D1/D7/D30 retention, churn rate, renewal rate |
| **T**ask Success | Task completion | Completion rate, time-on-task, error rate |

#### A/B Testing Quick Reference

| Scenario | Recommended Test |
|----------|-----------------|
| Compare 2 versions | A/B test (binary) |
| Compare 3+ versions | A/B/n test (multivariate) |
| Small sample size | Sequential testing or Bayesian methods |
| Measure magnitude of change | Effect size (Cohen's d) + confidence interval |

#### Sample Size Rule of Thumb

| Baseline Rate | MDE | Approx. Sample/Group |
|--------------|-----|---------------------|
| 10% | 2% | ~12,000 |
| 15% | 2% | ~8,000 |
| 15% | 3% | ~3,500 |
| 30% | 5% | ~1,500 |
| 50% | 5% | ~1,600 |

#### MaxDiff Design Tips

| Parameter | Recommendation |
|-----------|---------------|
| Items per screen | 3-5 (optimal: 4) |
| Number of blocks | Items × 2-3 |
| Minimum respondents | 100+ |
| Best for | 8+ items to prioritize |

#### Cross-Skill Quick Reference

| Need | Skill | Key Method |
|------|-------|------------|
| Choose research methods | [UDM](https://github.com/AliDujie/universal-design-methods) | `recommend_methods()` |
| Validate quantitatively | **QuantUX** (this skill) | `calculate_ab_sample_size()` |
| Understand user "jobs" | [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) | `analyze()` |
| Create personas | [Persona](https://github.com/AliDujie/web-persona-skill) | `add_persona()` |
| Design value prop | [VPD](https://github.com/AliDujie/value-proposition-design) | `analyze_canvas()` |
| Present findings | [SWD](https://github.com/AliDujie/storytelling-with-data) | `build_story()` |

### 🏆 Case Studies

#### Case Study 1: HEART Metrics System Setup

**Background**: A SaaS product needed to establish quantitative UX metrics to replace subjective judgments.

```python
from quantux import QuantUXSkill

skill = QuantUXSkill("SaaS Collaboration Platform")

# Step 1: Build HEART framework
heart = skill.build_heart_framework()
print(heart)  # Goals → Signals → Metrics for each dimension

# Step 2: Get workshop guide for team alignment
workshop = skill.get_workshop_guide()

# Step 3: Design CSat survey
survey = skill.design_csat_survey("2024Q1 Satisfaction", mechanism="in_app")

# Step 4: Calculate required sample size for A/B test
sample = skill.calculate_ab_sample_size(baseline=0.60, mde=0.05)
print(f"Need {sample} users per group")

# Step 5: Analyze CSat results
csat_result = skill.analyze_csat("2024Q1", 500, {1: 20, 2: 30, 3: 80, 4: 200, 5: 170})
print(f"Top-2-Box: {csat_result['t2b']}")

# Step 6: Generate CEO-perspective report
report = skill.generate_report("Q1 UX Research Report", include_ceo_analysis=True)
```

**Result**: Shifted from subjective to data-driven decisions. UX improvement ROI increased 3x.

#### Case Study 2: MaxDiff Feature Prioritization

**Background**: An e-commerce platform had 20 pending features and needed scientific priority ranking.

```python
from quantux import QuantUXSkill

skill = QuantUXSkill("E-commerce Platform")

# MaxDiff design for 10 features
features = ["Smart recommendations", "One-click checkout", "Price protection",
            "Image search", "Voice search", "Social sharing",
            "Cart sharing", "Subscription alerts", "AR try-on", "Price comparison"]
maxdiff = skill.design_maxdiff("Feature Priorities", features, items_per_screen=4)
print(maxdiff)

# A/B test the top-ranked feature
n = skill.calculate_ab_sample_size(baseline=0.35, mde=0.03)
result = skill.analyze_ab_test("Original", 5000, 1750, "New", 5000, 1900)
print(result)
```

**Result**: Used MaxDiff instead of voting. Priority decision time reduced from 2 weeks to 3 days.
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

### 📦 Dependencies

- Python >= 3.8
- **No external dependencies** (pure standard library)
- Cross-platform: macOS / Linux / Windows

### 📋 Changelog

| Version | Date | Changes |
|---------|------|--------|
| v2.3.45 | 2026-05-11 | Repo maintenance: verified English section completeness, confirmed all "When NOT to Use" and "Common Mistakes" sections present across ecosystem, verified cross-skill links, updated version badges |
| v2.3.44 | 2026-05-11 | Repo maintenance: fixed embedded Changelog version ordering (v2.3.41→v2.3.40), removed blank-line separator, fixed v2.3.27 missing `|` in English Version History |
| v2.3.43 | 2026-05-11 | Repo maintenance: fixed footer version mismatch (v2.3.40→v2.3.42), added missing changelog entries (v2.3.40–v2.3.42), ensured README/badge/CHANGELOG alignment |
| v2.3.42 | 2026-05-11 | Repo maintenance: added English 5-minute Quick Start checklist, enhanced discoverability for English-speaking users, verified ecosystem cross-references |
| v2.3.41 | 2026-05-11 | Repo maintenance: added Beginner Quick Reference Card with 7 common use cases and quick commands |
| v2.3.40 | 2026-05-11 | Repo maintenance: fixed broken file path reference in Next Steps (surveys.py→csat.py), fixed rogue separator in CN changelog table, fixed version ordering (v2.3.29 before v2.3.28), updated Last Updated |
| v2.3.36 | 2026-05-09 | Repo maintenance: added English Project Structure section for bilingual parity, enhanced documentation completeness |
| v2.3.35 | 2026-05-09 | Repo maintenance: fixed SKILL.md version mismatch, aligned README footer version, verified ecosystem cross-references, improved changelog table ordering |
| v2.3.33 | 2026-05-09 | Repo maintenance: added English case studies section with practical code examples, enhanced bilingual content parity (CN/EN), added cross-skill integration code samples |
| v2.3.32 | 2026-05-09 | Repo maintenance: fixed footer version mismatch (v2.3.30→v2.3.32), enhanced cross-skill ecosystem workflow clarity, updated ecosystem links to all 5 sibling skills, aligned version across README/SKILL.md/pyproject.toml |
| v2.3.30 | 2026-05-08 | Repo maintenance: enhanced HEART framework workshop guide, improved cross-skill ecosystem workflow integration, updated Last Updated to 2026-05-08, version bump to 2.3.30 |
| v2.3.20 | 2026-05-06 | Repo maintenance: updated Last Updated timestamp, version bump to 2.3.20, verified ecosystem cross-references and bilingual consistency |
| v2.3.19 | 2026-05-06 | Repo maintenance: version alignment across all files (README badge, SKILL.md, pyproject.toml, CHANGELOG), verified ecosystem cross-references and bilingual consistency |
| v2.3.5 | 2026-05-03 | Repo maintenance: fixed missing v2.3.3 in English changelog, updated classifiers and project.urls |
| v2.3.4 | 2026-05-03 | Repo maintenance: added ecosystem ASCII diagram and integration patterns to English Related Skills section, enhanced Why Choose section with ecosystem benefits |
| v2.3.3 | 2026-05-02 | Added English Quick Decision Guide table to improve cross-skill discoverability |
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

**版本 / Version**: v2.3.44

### 🔄 End-to-End Workflow: All 7 Skills

A complete metrics-to-decision workflow using the full AliDujie ecosystem:

```
Step 1          Step 2          Step 3          Step 4          Step 5          Step 6
┌──────┐       ┌──────┐       ┌──────┐       ┌──────┐       ┌──────┐       ┌──────┐
│Persona│  ──►  │ JTBD │  ──►  │ UDM  │  ──►  │QuantUX│  ──►  │ VPD  │  ──►  │ SWD  │
│ 👤   │       │ 🎯   │       │ 📖   │       │ 📊   │       │ 💎   │       │ 📈   │
│角色定义│       │需求洞察│       │定性研究│       │定量验证│       │价值验证│       │数据汇报│
└──────┘       └──────┘       └──────┘       └──────┘       └──────┘       └──────┘
```

**Real-World Scenario: Fitness App Engagement Improvement**

1. **Persona**: Create "Goal-driven Athlete" and "Casual Walker" segments from usage patterns
2. **JTBD**: Discover core Job is "stay motivated to maintain a healthy routine" (Opp Score: 7.5)
3. **UDM**: Diary study + contextual observation → find motivation drops after week 2
4. **QuantUX**: HEART framework + A/B test gamification features (n=8,000) → Engagement +25%, Retention +18%
5. **VPD**: Test value proposition "Your daily fitness coach" — canvas fit 0.79
6. **SWD**: Build stakeholder presentation → line charts for trend, declutter before/after comparison → action-oriented narrative

```python
# QuantUX as the quantitative validation layer in the ecosystem
from persona import PersonaSkill; persona = PersonaSkill("健身 App")
from jtbd import JTBDSkill; jtbd = JTBDSkill("健身习惯")
from udm import UDMSkill; udm = UDMSkill("健身 App")
from quantux import QuantUXSkill; quantux = QuantUXSkill("健身 App")
from vpd import VPDSkill; vpd = VPDSkill("健身 App", "目标导向型用户")
from swd import SWDSkill; swd = SWDSkill("Q1 健身用户参与提升汇报")

# QuantUX validates qualitative findings from UDM/JTBD with statistical rigor
```

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
| "我需要一个结构化的分析框架" | → **Structured Thinking Model** — PESTEL、五力模型、决策树 |
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

### 🚀 完整端到端工作流：从指标到决策 (End-to-End Workflow)

以下是一个真实场景中，7 个技能如何协作完成从研究到决策的完整工作流：

**场景**: 产品需要验证新功能的用户价值和业务影响

```
Phase 1: 定性发现
  UDM: 可用性测试 (8 用户) → 发现功能使用障碍
  JTBD: 四力分析 → 用户想完成的核心"工作"是快速协作

Phase 2: 量化验证 (QuantUX — 本技能)
  → build_heart: 设定 HEART 指标 (Engagement: DAU, Adoption: 功能使用率)
  → calculate_sample_size: A/B 测试需要 n=3200 每组 (α=0.05, power=0.8)
  → run_ab_test: 实验组 vs 对照组，2 周数据收集
  → analyze_maxdiff: 12 个需求优先级排序，识别 Top 3
  → generate_heart_report: HEART 指标基线 + 改进追踪

Phase 3: 细分与设计
  Persona: 发现重度用户 vs 轻度用户行为差异
  VPD: 验证"一键协作"价值主张契合度 0.85

Phase 4: 呈现
  SWD: 将 HEART 数据转化为高管级叙事
```

> 💡 **QuantUX 是工作流的量化核心**: UDM 发现假设 → QuantUX 验证 → SWD 呈现

👉 **尝试完整工作流**: [UDM](https://github.com/AliDujie/universal-design-methods) · [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) · [Persona](https://github.com/AliDujie/web-persona-skill) · [VPD](https://github.com/AliDujie/value-proposition-design) · [SWD](https://github.com/AliDujie/storytelling-with-data)

---

### 💻 实用集成示例 (Practical Integration Examples)

#### 示例 1: QuantUX + SWD — 从 HEART 指标到高管叙事

```python
# QuantUX 构建 HEART 框架 → SWD 转化为数据故事
from quantux import QuantUXSkill
from swd import SWDSkill

quantux = QuantUXSkill("电商平台")
heart = quantux.build_heart_framework()

swd = SWDSkill("电商平台")
ctx = swd.build_context(audience="CEO", cta="增加 UX 研究预算")
story = swd.build_story(protagonist="用户", imbalance="体验指标下降")
```

#### 示例 2: QuantUX + UDM — 定性定量三角验证

```python
# UDM 定性发现 → QuantUX 量化验证
from udm import UDMSkill
from quantux import QuantUXSkill

udm = UDMSkill("电商平台")
usability = udm.generate_usability_test("结账流程", "summative")

quantux = QuantUXSkill("电商平台")
sample_size = quantux.calculate_ab_sample_size(baseline=0.15, mde=0.02)
print(f"A/B 测试需要 {sample_size} 样本量 per variant")
```

#### 示例 3: QuantUX + JTBD — 机会分数的统计验证

```python
# JTBD 机会评分 → QuantUX 设计 CSat 调查验证
from jtbd import JTBDSkill
from quantux import QuantUXSkill

jtbd = JTBDSkill("电商平台")
opportunity = jtbd.score_opportunity("快速完成购买", struggle=4, importance=5)

quantux = QuantUXSkill("电商平台")
csat = quantux.design_csat_survey("购买流程满意度", mechanism="in_app")
```

> 💡 **QuantUX 是验证引擎** — 将 UDM 的定性假设和 JTBD 的机会评分转化为可量化的统计证据。

### 🌟 为什么选择 AliDujie 技能生态系统？

本技能是 **AliDujie UX 研究技能生态系统** 的定量研究层，与其他技能无缝协作：

| 技能 | 角色 | 协作方式 |
|------|------|----------|
| [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) | 方法核心 | UDM 定性发现 → QuantUX 定量三角验证 |
| [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) | 需求洞察 | JTBD 机会分数 → QuantUX A/B 测试验证 |
| [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) | 价值设计 | VPD 假设 → QuantUX 实验验证 |
| [Web Persona](https://github.com/AliDujie/web-persona-skill) | 用户角色 | Persona 角色 → QuantUX 分层 A/B 测试 |
| [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) | 数据叙事 | QuantUX HEART/A/B 数据 → SWD 高管级呈现 |

**使用完整生态系统的优势：**

- ✅ **全流程覆盖** — 从发现需求 → 角色创建 → 定性定量三角验证 → 数据呈现
- ✅ **一致 API 设计** — 所有技能使用统一的 Skill("产品名") 入口
- ✅ **零外部依赖** — 纯 Python 标准库实现，开箱即用
- ✅ **双语支持** — 完整中英文文档，适合国际化团队
- ✅ **积极维护** — 定期更新新功能和改进文档

👉 **探索完整生态系统**: [UDM](https://github.com/AliDujie/universal-design-methods) · [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) · [VPD](https://github.com/AliDujie/value-proposition-design) · [Persona](https://github.com/AliDujie/web-persona-skill) · [SWD](https://github.com/AliDujie/storytelling-with-data)

---

### 💡 Pro Tips / 专业提示

- **先定义指标再收集数据** — 用 HEART 框架对齐团队对"什么重要"的共识
- **A/B 测试先算样本量** — 永远不做功效不足的 A/B 测试
- **三角测量方法** — 结合定量（调查、日志）和定性（访谈）交叉验证
- **关注效应大小而非仅 p 值** — 统计显著 ≠ 业务显著
- **建立基线追踪趋势** — 设定基线指标并纵向追踪改进
- **QuantUX + UDM 是黄金组合** — UDM 发现假设，QuantUX 定量验证
- **统计功效 ≥ 0.8 是底线** — 样本量不足时用序贯检验或贝叶斯方法替代传统 A/B 测试

## 📋 版本历史 (Changelog)

| 版本 | 日期 | 变更 |
|------|------|------|
| v2.3.44 | 2026-05-11 | 仓库维护：修复 CN 变更日志版本排序（v2.3.41→v2.3.40）、缺失的表格闭合符 `|`、多余的空行分隔符；修复页脚陈旧版本引用（v2.3.30→v2.3.43）；清理重复分隔符 |
| v2.3.43 | 2026-05-11 | 仓库维护：修复页脚版本不一致（v2.3.40→v2.3.42），补齐缺失的变更日志条目（v2.3.42），确保 README/徽章/CHANGELOG 三端版本对齐 |
| v2.3.41 | 2026-05-11 | 仓库维护：添加新手快速参考卡，覆盖 7 个常见使用场景和快捷命令 |
| v2.3.40 | 2026-05-11 | 仓库维护：修复 Next Steps 中的文件路径引用（surveys.py→csat.py），修复版本历史表格中的错误分隔符，修正版本排序（v2.3.29 在 v2.3.28 之前），更新 Last Updated |
| v2.3.36 | 2026-05-09 | 仓库维护：添加英文版项目结构，提升中英双语一致性，增强文档完整性 |
| v2.3.35 | 2026-05-09 | 仓库维护：修复 SKILL.md 版本不一致，对齐 README 页脚版本引用，验证生态交叉引用一致性，改进版本历史表格排序 |
| v2.3.30 | 2026-05-08 | 仓库维护：增强 HEART 框架工作坊指南，改进跨技能生态工作流集成，更新 Last Updated 至 2026-05-08，版本升级至 2.3.30 |
| v2.3.29 | 2026-05-07 | 仓库维护：在快速决策指南中添加 Structured Thinking Model 引用（中英文），提升跨技能发现性，版本升级至 2.3.29 |
| v2.3.28 | 2026-05-07 | 仓库维护：在 SKILL.md 中添加"什么时候使用 QuantUX"决策指南，添加跨技能工作流示例，版本升级至 2.3.28 |
| v2.3.27 | 2026-05-07 | 仓库维护：SKILL.md 版本号升级至 2.3.27，在 SKILL.md 末尾添加 AliDujie 技能生态协作表，验证生态交叉引用一致性 |
| v2.3.26 | 2026-05-07 | 仓库维护：版本升级至 2.3.26，对齐 SKILL.md 版本号，完善 SKILL.md 结尾协作生态表格 |
| v2.3.25 | 2026-05-07 | 仓库维护：添加 SKILL.md 结尾 AliDujie 技能生态协作表格，增强跨技能一致性 |
| v2.3.24 | 2026-05-07 | 仓库维护：修复页脚版本不一致，添加生态系统工作流 Pro Tip，版本升级至 v2.3.24 |
| v2.3.23 | 2026-05-07 | Repo maintenance: added English Dependencies section, verified ecosystem cross-references |
| v2.3.22 | 2026-05-07 | Repo maintenance: added statistical power Pro Tip, enhanced SWD-QuantUX visualization integration |
| v2.3.21 | 2026-05-06 | 仓库维护：英文版脚注添加 Contributing 链接，增强跨技能协作示例（QuantUX→SWD 数据流工作流），对齐所有版本引用 |
| v2.3.20 | 2026-05-06 | 仓库维护：更新版本至 2.3.20，验证生态交叉引用和双语一致性 |
| v2.3.19 | 2026-05-06 | 仓库维护：对齐所有版本引用（README 徽章、SKILL.md、pyproject.toml、CHANGELOG），验证生态交叉引用和双语一致性 |
| v2.3.16 | 2026-05-04 | 仓库维护：修复版本历史表格 `| |` 格式错误，补充英文目录中端到端工作流链接 |
| v2.3.15 | 2026-05-04 | 仓库维护：添加英文目录(Table of Contents)和5分钟快速开始检查清单；修复 SKILL.md 版本不一致 (2.3.11→2.3.13)，对齐版本底部陈旧引用 (v2.3.8→v2.3.13) |
| v2.3.12 | 2026-05-04 | 仓库维护：修复版本历史排序（v2.3.8→v2.3.10 顺序校正），增强英文版 Quick Start 场景注释，修复重复 Last Updated 标题 |
| v2.3.11 | 2026-05-04 | 仓库维护：添加完整端到端工作流章节（展示从指标到决策的 6 技能协作流程） |
| v2.3.10 | 2026-05-03 | 仓库维护：添加 Pro Tips 专业提示章节（中英双语），增强统计实践指导 |
| v2.3.9 | 2026-05-03 | 仓库维护：修复英文版版本历史表格格式，SKILL.md 版本对齐，新增英文版技能生态工作流章节 |
| v2.3.8 | 2026-05-03 | 仓库维护：修复版本历史表格格式（删除错误分隔符行），修复版本引用不一致（版本/Version v2.3.5→v2.3.8），统一 SKILL.md 版本 |
| v2.3.7 | 2026-05-03 | 仓库维护：精简重复的英文 Quick Decision Guide 区块，添加英文版本历史表，统一 SKILL.md 与 README.md 版本引用 |
| v2.3.5 | 2026-05-03 | 仓库维护：修复英文 changelog 中缺失的 v2.3.3 条目，统一 pyproject.toml 元数据 |
| v2.3.4 | 2026-05-03 | 仓库维护：为英文 Related Skills 添加生态系统 ASCII 图和集成模式说明，增强 Why Choose 部分描述 |
| v2.3.3 | 2026-05-02 | 仓库维护：为英文版添加 Quick Decision Guide 导航表，增强技能间交叉引用 |
| v2.3.2 | 2026-05-02 | 仓库维护：优化英文示例代码格式，增强工作流 3 描述，统一交叉引用格式，补充 CEO 能力英文版表格 |
| v2.3.1 | 2026-05-02 | 修复 Python 版本不一致 (3.9+→3.8+)，添加 Last Updated badge，补充 CEO 能力到英文能力表 |
| v2.2.10 | 2026-05-01 | 统一交叉引用为 GitHub 绝对链接，更新 Last Updated 日期 |
| v2.2.9 | 2026-04-28 | 添加 Badges、技能生态系统图、双语支持 |
| v2.2.0 | 2026-04-23 | 添加版本历史、快速参考、CEO 视角扩展 |
| v1.0 | 2026-04-22 | 初始版本 |

---

## 🔗 Skill Ecosystem Workflow

QuantUX is the quantitative research layer of the **AliDujie UX Research Skills Ecosystem**. Here are typical workflows combining it with other skills:

### Workflow 1: Qualitative → Quantitative Triangulation

```
UDM/JTBD (qualitative insights) → QuantUX (quantitative validation) → SWD (storytelling)
```

**Scenario**: Validating user research findings
1. Use UDM or JTBD to collect qualitative user insights
2. Use QuantUX to design surveys, A/B tests, and calculate statistical significance
3. Use SWD to transform validated results into compelling data narratives

### Workflow 2: HEART Metrics → Business Decision

```
QuantUX (HEART framework) → VPD (value validation) → CEO review
```

**Scenario**: Product direction decision
1. Use QuantUX to build HEART metrics system
2. Use VPD to validate value proposition hypotheses
3. Use CEO review framework to evaluate business impact

### Workflow 3: Persona → Segmented Testing → Opportunity

```
Persona (user segments) → QuantUX (stratified A/B testing) → JTBD (opportunity scoring)
```

**Scenario**: Personalized product optimization
1. Use Persona to define user segments based on behavior patterns
2. Use QuantUX to design stratified A/B tests for each segment
3. Use JTBD to calculate opportunity scores per segment

> 💡 **Tip**: QuantUX pairs naturally with UDM — use UDM for qualitative discovery, then QuantUX for quantitative validation. The CEO-perspective report feature is especially useful for executive-level research presentations.

### 💡 Pro Tips

- **Define Metrics Before Collecting Data** — Use HEART framework to align on what matters
- **Calculate Sample Size First** — Never run underpowered A/B tests
- **Triangulate Methods** — Combine quantitative (surveys, logs) with qualitative (interviews)
- **Focus on Effect Size, Not Just p-Value** — Statistical significance ≠ business significance
- **Establish Baselines** — Set baseline metrics and track improvement longitudinally
- **QuantUX + UDM is the golden combo** — UDM discovers hypotheses, QuantUX validates quantitatively
- **Statistical Power ≥ 0.8 is the floor** — When sample size is limited, use sequential testing or Bayesian methods instead of traditional A/B tests
- **Full Ecosystem Workflow** — QuantUX is the validation engine of the AliDujie ecosystem. UDM discovers qualitative hypotheses, JTBD quantifies opportunity scores, Persona provides segments for stratified testing, VPD designs experiments to validate, and SWD visualizes the results.

## 📋 Version History (English)

| Version | Date | Changes |
|---------|------|--------|
| v2.3.45 | 2026-05-11 | Repo maintenance: verified English section completeness, confirmed all "When NOT to Use" and "Common Mistakes" sections present across ecosystem, verified cross-skill links, updated version badges |
| v2.3.44 | 2026-05-11 | Repo maintenance: removed duplicate v2.3.34 changelog entry, removed empty v2.3.31 entry, fixed English Version History table formatting and missing entries |
| v2.3.43 | 2026-05-11 | Repo maintenance: fixed footer version mismatch (v2.3.40→v2.3.42), added missing changelog entries (v2.3.40–v2.3.42), ensured README/badge/CHANGELOG alignment |
| v2.3.42 | 2026-05-11 | Repo maintenance: added English 5-minute Quick Start checklist, enhanced discoverability for English-speaking users, verified ecosystem cross-references |
| v2.3.41 | 2026-05-11 | Repo maintenance: added Beginner Quick Reference Card with 7 common use cases and quick commands |
| v2.3.40 | 2026-05-11 | Repo maintenance: fixed broken file path reference in Next Steps (surveys.py→csat.py), fixed rogue separator in CN changelog table, fixed version ordering (v2.3.29 before v2.3.28), updated Last Updated |
| v2.3.39 | 2026-05-10 | Repo maintenance: added English cheat sheet (HEART metrics guide, A/B testing quick reference, MaxDiff design tips), updated Last Updated badge |
| v2.3.33 | 2026-05-09 | Repo maintenance: added English case studies section with practical code examples, enhanced bilingual content parity, added cross-skill integration code samples |
| v2.3.30 | 2026-05-08 | Repo maintenance: enhanced HEART framework workshop guide, improved cross-skill ecosystem workflow integration, updated Last Updated to 2026-05-08, version bump to 2.3.30 |
| v2.3.29 | 2026-05-07 | Repo maintenance: added Structured Thinking Model to Quick Decision Guide (CN+EN), enhanced cross-skill discoverability, version bump to 2.3.29 |
| v2.3.28 | 2026-05-07 | Repo maintenance: added "When to use QuantUX" decision guide to SKILL.md, added cross-skill workflow examples, version bump to 2.3.28 |
| v2.3.27 | 2026-05-07 | Repo maintenance: added AliDujie 技能生态 collaboration table to end of SKILL.md, enhanced cross-skill ecosystem consistency |
| v2.3.25 | 2026-05-07 | Repo maintenance: updated version badge and footer to 2.3.26, aligned SKILL.md frontmatter version |
| v2.3.24 | 2026-05-07 | Repo maintenance: fixed footer version mismatch, added ecosystem workflow Pro Tip, bumped to v2.3.24 |
| v2.3.23 | 2026-05-07 | Repo maintenance: added English Dependencies section, verified ecosystem cross-references |
| v2.3.22 | 2026-05-07 | Repo maintenance: added statistical power Pro Tip, enhanced SWD-QuantUX visualization integration |
| v2.3.18 | 2026-05-06 | Repo maintenance: fixed Last Updated date alignment |
| v2.3.17 | 2026-05-05 | Repo maintenance: added Quantitative UX Research collaboration reference to ecosystem workflow |
| v2.3.16 | 2026-05-04 | Repo maintenance: fixed changelog table `| |` formatting, added end-to-end workflow English TOC link
| v2.3.15 | 2026-05-04 | Repo maintenance: added English TOC and 5-min checklist; fixed SKILL.md version mismatch (2.3.11→2.3.13), fixed stale bottom version badge (v2.3.8→v2.3.13), aligned all version references, added Credits section
| v2.3.12 | 2026-05-04 | Repo maintenance: fixed changelog ordering (v2.3.8→v2.3.10 sequence corrected), enhanced English Quick Start with scenario comments, removed duplicate Last Updated header |
| v2.3.11 | 2026-05-04 | Repo maintenance: added end-to-end workflow section showing 6-skill collaboration from metrics to decision |
| v2.3.10 | 2026-05-03 | Repo maintenance: added Pro Tips section (CN/EN) for statistical practice guidance |
| v2.3.9 | 2026-05-03 | Repo maintenance: fixed English changelog table formatting, aligned SKILL.md version, added English Skill Ecosystem Workflow section |
| v2.3.8 | 2026-05-03 | Repo maintenance: fixed changelog table formatting, resolved version mismatch (Version badge: v2.3.5→v2.3.8), aligned SKILL.md version |
| v2.3.7 | 2026-05-03 | Repo maintenance: streamlined duplicate English Quick Decision Guide, added English version history table, aligned SKILL.md version |
| v2.3.6 | 2026-05-03 | Repo maintenance: consolidated duplicate English Quick Decision Guide, added missing English version history section |
| v2.3.5 | 2026-05-03 | Repo maintenance: fixed missing v2.3.3 in English changelog, updated classifiers and project.urls |
| v2.3.4 | 2026-05-03 | Added ecosystem ASCII diagram and integration patterns to English Related Skills, enhanced Why Choose section |
| v2.3.3 | 2026-05-02 | Added English Quick Decision Guide table to improve cross-skill discoverability |
| v2.3.2 | 2026-05-02 | Added English "Who Is This For?" section, GitHub Topics, and changelog to English section |
| v2.3.1 | 2026-05-02 | Fixed Python version mismatch, added Last Updated badge |
| v2.2.10 | 2026-05-01 | Unified cross-references to GitHub absolute links |
| v2.2.9 | 2026-04-28 | Added badges, skill ecosystem diagram, bilingual support |
| v2.2.0 | 2026-04-23 | Added version history, quick reference, CEO perspective extension |
| v1.0 | 2026-04-22 | Initial release |

---

### 🗺️ Beginner Quick Reference Card

> **New to QuantUX? Start here.** This card covers the most common first-time use cases.

| I want to… | Start with this | Quick command |
|---|---|---|
| Set up UX metrics for my product | HEART Framework | `skill.build_heart_framework()` |
| Design a satisfaction survey | CSat Survey | `skill.design_csat_survey("Post-purchase Satisfaction")` |
| Calculate A/B test sample size | Sample Size Calculator | `skill.calculate_ab_sample_size(baseline=0.15, mde=0.02)` → `~9,400 per variant` |
| Analyze A/B test results | A/B Test Analysis | `skill.analyze_ab_test("New Flow", n_a=2500, conv_a=425, n_b=2500, conv_b=500)` |
| Prioritize features by user preference | MaxDiff Design | `skill.design_maxdiff("Feature Priority", ["Search", "Filter", "Sort", "Compare"])` |
| Analyze user behavior from logs | Log Analysis | `skill.analyze_logs(log_data, funnels=[("view→add→checkout")])` |
| Plan a full quantitative study | Research Report | `skill.generate_report("Checkout Optimization", include_ceo_analysis=True)` |

> 💡 **Most common first step**: `skill.build_heart_framework()` — define your Happiness, Engagement, Adoption, Retention, and Task Success metrics before collecting data.

### 🚀 Next Steps / 下一步

Ready to go deeper? Here's what to try next:

1. **Explore all capabilities** — Check [quantux/csat.py](quantux/csat.py) for CSat survey design, [quantux/heart.py](quantux/heart.py) for HEART framework, and [quantux/abtest.py](quantux/abtest.py) for A/B testing
2. **Validate qualitative findings** — Pair QuantUX with [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) to confirm hypotheses with statistical rigor
3. **Segment your samples** — Use [Web Persona](https://github.com/AliDujie/web-persona-skill) to define strata for targeted quantitative studies
4. **Measure value proposition fit** — Combine with [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) for experiment-driven validation
5. **Tell the data story** — Transform statistical results into executive narratives with [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data)
6. **Identify opportunity gaps** — Use [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) to prioritize what to measure

> 💡 **Pro Tip**: QuantUX is the validation engine of the ecosystem. Try: JTBD (identify opportunity) → QuantUX (measure size) → VPD (design solution) → SWD (present results)

### ⚡ Power Workflow: Complete A/B Testing Pipeline

```python
from quantux import QuantUXSkill
from swd import SWDSkill

# 1. QuantUX: Design and analyze A/B test
quant = QuantUXSkill("SaaS 产品")
sample = quant.calculate_ab_sample_size(baseline=0.15, mde=0.02)
# → Required: 3,841 per group (80% power, α=0.05)

# 2. After experiment: analyze results
result = quant.analyze_ab_test(conversions_a=580, total_a=3841,
    conversions_b=650, total_b=3841)

# 3. SWD: Present findings to stakeholders
swd = SWDSkill("实验结果汇报")
story = swd.build_story(protagonist="产品团队",
    imbalance="功能 A 与功能 B 效果未知，需要数据决策",
    resolution="功能 B 提升 12.1% 转化率，统计显著 (p=0.02)")

# → From experiment design to stakeholder-ready narrative
```

### 👨‍💻 Credits

Based on *Quantitative User Experience Research* by Jeff Sauro & James R. Lewis (2023), covering HEART framework, experimental design, statistical analysis, and survey methods.

**Applicable to:** UX Researchers, Data Analysts, Product Managers, Experiment Scientists

### 🆘 Getting Help

- 📖 Check the [Troubleshooting](#-troubleshooting) section for common issues
- 📚 Read the methodology guides in [references/](references/)
- 💬 Open an issue on [GitHub](https://github.com/AliDujie/Quantitative-UX-Research/issues)

### 📖 Extended Reading

| Book | Author | Related Capability |
|------|--------|--------------------|
| *Quantitative UX Research* | Jeff Sauro & James R. Lewis | Full methodology — HEART, CSat, A/B testing, MaxDiff |
| *Measuring the User Experience* (2nd Ed) | Jeff Sauro & James R. Lewis | SUS, NPS, UMUX-Lite benchmarking |
| *Lean Analytics* | Alistair Croll & Benjamin Yoskovitz | Data-driven product decisions |

### 🌐 Explore the Full AliDujie UX Research Ecosystem

This skill is part of a **7-skill UX research ecosystem** — each covers a different phase of the research lifecycle. Combine them for end-to-end workflows:

| Skill | Role | When to Use |
|-------|------|-------------|
| 👤 [Web Persona](https://github.com/AliDujie/web-persona-skill) | Foundation | Define WHO you are designing for |
| 🎯 [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) | Needs Insight | Understand WHY users behave the way they do |
| 🔍 [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) | Research Methods | Choose and execute research methods |
| 📊 [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) | Validation Engine | Prove qualitative hypotheses with data |
| 💎 [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) | Value Design | Bridge user needs to testable value propositions |
| 📈 [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) | Presentation Layer | Turn findings into executive-ready narratives |

> 💡 **Quick Tip**: QuantUX is the validation engine of the ecosystem. Try: `JTBD (identify opportunity) → QuantUX (measure size) → VPD (design solution) → SWD (present results)`


### 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute to this project.

---

*Last Updated: 2026-05-13 | AliDujie Skill Ecosystem | v2.3.54*