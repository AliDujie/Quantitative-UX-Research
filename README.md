# Quantitative UX Research Skill

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Code style: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

> 📊 **HEART 框架 · CSat 调查 · A/B 测试 · MaxDiff · 日志分析 · 研究规划**

基于《Quantitative User Experience Research》(Chapman & Rodden, 2023) 的完整量化用户体验研究工具包。覆盖 7 大执行能力，从指标体系构建到研究报告生成，一站式解决量化研究需求。

[English](#english) | [中文](#中文说明)

---

## 中文说明

### 🌟 为什么使用这个技能？(Why Use This Skill?)

- **完整覆盖** — HEART 框架、CSat 调查、日志分析、MaxDiff、A/B 测试、研究规划
- **CEO 决策支持** — 内置业务影响评估、验证时间线、资源估算
- **零依赖** — 纯 Python 标准库实现，无外部依赖，5 分钟上手
- **智能诊断** — 研究需求自动诊断，推荐最佳研究方法组合
- **双语支持** — 完整中英文文档，适合国际化团队
- **零学习成本** — API 设计直观，代码示例丰富，即插即用

### ⚡ 5 分钟快速开始 (Quick Start)

#### 步骤 1: 安装技能

```bash
# 复制到你的 AI Agent skills 目录
cp -r Quantitative-UX-Research /your/agent/skills/
```

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
sample = skill.calculate_ab_sample_size(baseline_rate=0.15, mde=0.02)

# ===== 场景 6: 研究需求诊断 =====
diagnosis = skill.diagnose_request("验证我们的新设计方向")

# ===== 场景 7: 研究报告生成 =====
report = skill.generate_report("用户体验研究报告", include_ceo_analysis=True)
```

### 💡 7 大核心能力

| # | 能力 | 模块 | 功能 |
|---|------|------|------|
| 1 | **HEART 框架** | `heart.py` | Goals-Signals-Metrics 工作坊、指标定义与仪表盘 |
| 2 | **CSat 调查** | `csat.py` | 满意度调查设计、分析、报告生成 |
| 3 | **日志分析** | `logs.py` | 会话序列分析、频率统计、转移矩阵 |
| 4 | **MaxDiff** | `maxdiff.py` | 优先级排序设计、分析、结果可视化 |
| 5 | **A/B 测试** | `abtest.py` | 样本量计算、功效分析、结果解读 |
| 6 | **研究规划** | `research.py` | 研究需求诊断、方法推荐、时间线规划 |
| 7 | **报告生成** | `research.py` | 标准化研究报告、CEO 视角业务影响分析 |

### 🔧 实用示例

#### 示例 1: 完整 HEART 框架工作流

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

# 步骤 4: 计算 A/B 测试样本量
sample = skill.calculate_ab_sample_size(
    baseline_rate=0.15,   # 基准转化率 15%
    mde=0.02,             # 最小可检测效应 2%
    power=0.80,           # 统计功效 80%
    alpha=0.05            # 显著性水平 5%
)
print(f"每组需要 {sample} 个样本")
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
    alternatives_per_task=4,
    tasks=12
)

# 分析结果
features = ["智能推荐", "实时协作", "版本历史", "权限管理", "API 集成", "移动端优化"]
choices = [
    [0, 3],  # 任务 1: 最佳=智能推荐, 最差=权限管理
    [1, 5],  # 任务 2: 最佳=实时协作, 最差=移动端优化
    # ... 更多选择数据
]
analysis = skill.analyze_maxdiff(design, features, choices)
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
├── references/           # 知识库文档（待补充）
├── quantux/tests/        # 测试套件
```

### 🔗 相关技能

本技能是 **AliDujie UX 研究技能生态系统** 的量化研究层：

```
┌─────────────────────────────────────────────────────────────┐
│           AliDujie 技能生态系统 (Skill Ecosystem)            │
├─────────────────────────────────────────────────────────────┤
│   📊 Quantitative UX Research ←───→ 📖 Universal Design     │
│         (量化研究)   三角测量            Methods (通用设计)  │
│              ↑                          ↓                   │
│              │                    🎯 JTBD Knowledge          │
│              │                      (需求洞察)               │
│   📈 Storytelling with Data ←───→ 💎 Value Proposition      │
│         (数据叙事)   呈现              Design (价值设计)      │
│              ↑                          ↑                   │
│              │                    👤 Web Persona             │
│              └────────────────────  (人物角色)               │
└─────────────────────────────────────────────────────────────┘
```

**配合使用场景:**

- **QuantUX + UDM** — 定性定量三角测量，提升研究信度
- **QuantUX + SWD** — 用 SWD 呈现 QuantUX 的 HEART 指标和 A/B 测试结果
- **QuantUX + JTBD** — 用 QuantUX 数据验证 JTBD 机会分数
- **QuantUX + VPD** — 用 QuantUX 数据验证价值主张假设
- **QuantUX + Persona** — 用 QuantUX 数据量化人物角色行为特征

👉 **探索完整生态系统**: [通用设计方法](https://github.com/AliDujie/universal-design-methods) | [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) | [数据叙事](https://github.com/AliDujie/storytelling-with-data) | [价值主张设计](https://github.com/AliDujie/value-proposition-design) | [人物角色](https://github.com/AliDujie/web-persona-skill)

### 🛠️ 故障排查 (Troubleshooting)

#### 问题 1: A/B 测试样本量过大

**检查**:
- baseline_rate 和 mde 参数是否合理
- 较小的 MDE 需要更大的样本量

**解决**:
```python
# 样本量过大 (MDE 太小)
sample = skill.calculate_ab_sample_size(baseline_rate=0.15, mde=0.005)
# → 每组需要 ~50,000 样本

# 合理样本量 (MDE 适中)
sample = skill.calculate_ab_sample_size(baseline_rate=0.15, mde=0.03)
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

- **《Quantitative User Experience Research》** - Chapman & Rodden (2023)
- **《Trustworthy Online Controlled Experiments》** - Kohavi, Tang & Xu (A/B 测试经典)
- **《Practical Statistics for UX》** - Jeff Sauro (UX 统计入门)
- **《Bayesian Methods for Hackers》** - Cameron Davidson-Pilon (贝叶斯方法)

### 📚 关于《Quantitative User Experience Research》

- **书名**: Quantitative User Experience Research
- **作者**: Nigel Chapman & Garreth Rodden
- **出版**: 2023
- **内容**: HEART 框架、实验设计、统计分析、调查方法
- **适用**: UX 研究员、数据分析师、产品经理、实验科学家

### 📦 依赖

- Python >= 3.9
- **无外部依赖**（纯标准库实现）
- 兼容 macOS / Linux / Windows

---

## English

### 🌟 Why Use This Skill?

- **Complete Coverage** — HEART framework, CSat surveys, log analysis, MaxDiff, A/B testing, research planning
- **CEO Decision Support** — Built-in business impact assessment, validation timeline, resource estimation
- **Zero Dependencies** — Pure Python standard library, ready to use out of the box
- **Smart Diagnosis** — Auto-diagnose research needs and recommend best method combinations
- **Bilingual Support** — Complete CN/EN documentation for international teams
- **Zero Learning Curve** — Intuitive API, rich code examples, plug-and-play

### 🚀 Quick Start

#### Step 1: Install

```bash
cp -r Quantitative-UX-Research /your/agent/skills/
```

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
sample = skill.calculate_ab_sample_size(baseline_rate=0.15, mde=0.02)

# Research report with CEO analysis
report = skill.generate_report("UX Research Report", include_ceo_analysis=True)
```

### 🔗 Related Skills

This skill is part of the **AliDujie UX Research Skills Ecosystem**:

- **[Universal-Design-Methods](https://github.com/AliDujie/universal-design-methods)** — 100 design research methods
- **[JTBD-Knowledge-Skill](https://github.com/AliDujie/jtbd-knowledge-skill)** — Jobs-to-be-Done theory
- **[Storytelling-with-Data](https://github.com/AliDujie/storytelling-with-data)** — Data storytelling and visualization
- **[Value-Proposition-Design](https://github.com/AliDujie/value-proposition-design)** — Value proposition canvas
- **[Web-Persona-Skill](https://github.com/AliDujie/web-persona-skill)** — Persona creation

### 🌟 Why Choose AliDujie Skill Ecosystem?

This skill is part of the **AliDujie UX Research Skills Ecosystem**. Using the complete ecosystem provides:

- ✅ **Complete Coverage** — From user research to product design to data presentation
- ✅ **Seamless Integration** — All skills use consistent API design and data formats
- ✅ **Best Practices** — Based on classic theories and practical experience
- ✅ **Active Maintenance** — Regularly updated with new features and improvements
- ✅ **Zero Dependencies** — Pure Python standard library, ready to use out of the box
- ✅ **Bilingual Support** — Complete CN/EN documentation for international team collaboration

👉 **Explore More Skills**: [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) | [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) | [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) | [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) | [Web Persona](https://github.com/AliDujie/web-persona-skill)

### 📦 Dependencies

- Python >= 3.9
- **No external dependencies** (pure standard library)
- Cross-platform: macOS / Linux / Windows

---

## 运行测试

```bash
cd /path/to/Quantitative-UX-Research
python3 quantux/tests/test_all.py
# 或使用 pytest
python3 -m pytest quantux/tests/test_all.py -v
```

## 📜 许可 (License)

基于《Quantitative User Experience Research》by Chapman & Rodden (2023)。
本技能仅供内部学习和研究使用。

## 👨💻 作者 (Credits)

- 基于《Quantitative User Experience Research》by Chapman & Rodden
- 技能开发：AliDujie 团队
- **GitHub**: [@AliDujie](https://github.com/AliDujie)
- **Emp ID**: 27768
- **Nickname**: 渡劫

---

**版本 / Version**: v2.1.0

---

## 🔗 技能生态工作流 (Skill Ecosystem Workflow)

本技能是 **AliDujie UX 研究技能生态系统** 的定量研究层。以下是与其他技能配合使用的典型工作流：

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
