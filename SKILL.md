---
name: quantitative-ux-research
description: 量化用户体验研究执行技能。基于 Jeff Sauro & James R. Lewis 方法论，提供实验设计、样本量计算、统计分析、调查设计、日志分析、满意度分析、研究报告生成等完整执行能力，以及CEO决策视角的业务影响评估、验证时间线与资源估算。
version: "2.3.56"
---

# Quantitative UX Research Skill

基于《Quantitative User Experience Research》(Jeff Sauro & James R. Lewis, 2023) 的量化用户体验研究执行技能。

## 🌐 AliDujie 技能生态系统

QuantUX 是 **定量研究核心**，负责用数据验证其他技能产生的定性假设：

```
UDM (定性发现) ──┐
                 ▼
JTBD (机会评分) ──► ┌────────────────┐
                    │  QuantUX 本技能  │ 📊 定量验证 — HEART/A-B测试/MaxDiff
VPD (价值假设) ────►│  · HEART 框架   │──────► SWD (数据故事汇报)
Persona (角色假设)─►│  · A-B 测试     │──────► CEO 决策(业务影响评估)
                    │  · 日志分析     │──────► STM (商业战略框架)
                    │  · MaxDiff      │
                    └────────────────┘
```

**QuantUX 的典型协作**：UDM 定性假设 → QuantUX A/B 验证 → SWD 数据汇报 → STM 战略决策；JTBD 机会评分 → QuantUX MaxDiff 优先级

## 🧭 快速决策：什么时候使用 QuantUX？

| 你的需求 | 推荐技能 |
|---------|---------|
| 需要定量验证假设、设计 A/B 测试、计算样本量 | ✅ **QuantUX（本技能）** |
| 需要选择研究方法、设计访谈、执行可用性测试 | → [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) |
| 需要理解用户"工作"、机会评分、竞争分析 | → [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) |
| 需要创建人物角色、用户细分、设计指导 | → [Web Persona](https://github.com/AliDujie/web-persona-skill) |
| 需要价值主张画布、实验验证、优先级排序 | → [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) |
| 需要将研究结果转化为数据叙事、图表呈现 | → [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) |
| 需要结构化商业分析框架 | → [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) |

> 💡 QuantUX 是验证引擎：用 HEART/A-B/MaxDiff 把定性假设转化为可量化的统计证据。

## 🌟 为什么选择 QuantUX？

- **行业标准方法** — 基于 Jeff Sauro & James R. Lewis《Quantitative User Experience Research》，量化 UX 研究的权威参考
- **7 大执行能力** — HEART 框架、CSat 调查、日志分析、MaxDiff、A/B 测试、研究规划、研究报告，一站式覆盖定量研究全流程
- **CEO 决策支持** — 内置业务影响评估、验证时间线、资源估算，把 UX 数据转化为业务语言
- **零学习成本** — 纯 Python 标准库，无外部依赖，`from quantux import QuantUXSkill` 即可使用
- **智能诊断** — 自动诊断研究需求，推荐最佳方法组合，避免常见统计陷阱
- **生态核心** — 与 UDM、JTBD、Persona、VPD、SWD 等 5 个技能无缝协作，实现定性定量三角验证

## ⚡ 快速上手 (Quick Start)

```python
from quantux import QuantUXSkill

skill = QuantUXSkill("你的产品名")

# HEART 指标体系
heart = skill.build_heart_framework()

# A/B 测试样本量计算
sample = skill.calculate_ab_sample_size(baseline=0.10, mde=0.02)

# MaxDiff 优先级分析
maxdiff = skill.run_maxdiff(items=["功能A", "功能B", "功能C"], n_respondents=200)

# CSat 调查设计
csat = skill.design_csat(product="核心功能")
```

> 💡 **5 分钟上手**: `from quantux import QuantUXSkill` → 纯标准库，零依赖，开箱即用。

## 一、核心理论

**量化用户体验研究 (Quant UXR)**：运用实证研究方法，在规模化场景下为以用户为中心的产品设计提供信息支持。

**T 型技能模型**：编程 + UX 研究 + 统计三领域交叉，广度覆盖基本能力，深度至少精通一个。

**HEART 框架** -- UX 指标体系：

| 维度 | 定义 | 示例指标 |
|------|------|----------|
| **H**appiness (愉悦) | 用户态度：满意度、易用性、NPS | 调查评分、满意度趋势 |
| **E**ngagement (参与) | 参与深度：频率、强度 | 每用户每周访问天数 |
| **A**doption (采纳) | 新用户/新功能采纳 | 7天内创建账户数 |
| **R**etention (留存) | 用户持续使用 | N天/周/月留存率 |
| **T**ask Success (任务成功) | 任务效率和效果 | 完成率、错误率、任务时间 |

实施路径：Goals -> Signals -> Metrics，团队工作坊定义，选择 3-5 个核心指标。

## 二、7 大执行能力

1. **HEART 框架构建** -- Goals-Signals-Metrics 工作坊、指标定义与仪表盘
2. **CSat 调查设计与分析** -- 调查机制选择、评分量表、Top-2-Box、时间趋势
3. **日志序列分析** -- 会话化、序列频率、Sunburst 图、Markov 转移矩阵
4. **MaxDiff 优先级排序** -- 强制选择设计、MNL/HB 估计、个体偏好
5. **A/B 测试设计与分析** -- 样本量计算、实验设计、效应量与置信区间
6. **研究规划与利益相关者管理** -- 请求诊断、方案设计、模拟结果预览
7. **研究报告生成** -- 执行摘要、可视化、CEO 决策支持模块

## 三、触发条件总表

| 触发词 / 场景 | 执行能力 | 输出物 |
|---|---|---|
| UX 指标 / HEART / 指标体系 | 一：HEART 框架 | 指标定义表、工作坊指南 |
| 满意度 / CSat / 调查 / NPS | 二：CSat 调查 | 调查方案、分析报告 |
| 用户路径 / 日志 / 行为序列 | 三：日志序列 | 序列频率、转移矩阵 |
| 功能优先级 / 偏好排序 / MaxDiff | 四：MaxDiff | 实验设计、偏好排名 |
| A/B 测试 / 实验 / 样本量 | 五：A/B 测试 | 测试方案、结果分析 |
| 研究计划 / 利益相关者 / 立项 | 六：研究规划 | 诊断报告、研究方案 |
| 汇报 / 报告 / CEO / 业务影响 | 七：研究报告 | 完整报告 (含 CEO 模块) |
| 综合定量 UX 研究任务 | 按顺序执行一 -> 七 | 完整研究方案 + 报告 |

## 四、目录结构

```
Quantitative-UX-Research/
├── SKILL.md                    # 本文件
├── quantux/                    # Python 工具包
│   ├── __init__.py             # QuantUXSkill 统一入口类
│   ├── config.py               # 全局配置和常量
│   ├── heart.py                # HEART 框架构建器
│   ├── csat.py                 # CSat 调查设计与分析
│   ├── logs.py                 # 日志序列分析
│   ├── maxdiff.py              # MaxDiff 设计与分析
│   ├── abtest.py               # A/B 测试设计与分析
│   ├── research.py             # 研究规划与报告
│   ├── templates.py            # 报告模板
│   ├── utils.py                # 工具函数
│   └── tests/
│       └── test_all.py         # 7 个测试用例
├── pyproject.toml
└── README.md
```

---

## 五、Python 工具包

### 5.1 安装与依赖

纯 Python 实现，无外部依赖，仅需 Python 3.9+。

```bash
import sys; sys.path.insert(0, "/path/to/Quantitative-UX-Research")
from quantux import QuantUXSkill
```

### 5.2 QuantUXSkill 方法一览

```python
from quantux import QuantUXSkill
skill = QuantUXSkill("旅行平台")  # 或 "SaaS产品" 等任意产品名
```

| 方法 | 能力 | 关键参数 | 返回 |
|------|------|---------|------|
| `build_heart_framework()` | HEART 框架 | -- | Markdown |
| `get_workshop_guide()` | HEART 工作坊 | -- | Markdown |
| `design_csat_survey(title, mechanism, target)` | CSat 设计 | title | Markdown |
| `analyze_csat(period, sample_size, ratings)` | CSat 分析 | period, sample_size, ratings(Dict) | Markdown |
| `analyze_logs()` | 日志序列 | (先 `logs_analyzer.add_event`) | Markdown |
| `design_maxdiff(title, items, items_per_screen)` | MaxDiff | title, items(List) | Markdown |
| `calculate_ab_sample_size(baseline, mde)` | A/B 样本量 | baseline, mde | int |
| `analyze_ab_test(name_a, n_a, conv_a, name_b, n_b, conv_b)` | A/B 分析 | 全部必填 | Markdown |
| `diagnose_request(request)` | 请求诊断 | request | Markdown |
| `plan_research()` | 研究规划 | -- | Markdown |
| `build_report(title)` | 基础报告 | title | Markdown |
| `generate_report(title, include_ceo_analysis)` | 完整报告 | title | Markdown |
| `generate_business_impact(metrics)` | 业务影响 | -- | Markdown |
| `generate_validation_timeline()` | 验证时间线 | -- | Markdown |
| `generate_resource_estimate()` | 资源估算 | -- | Markdown |
| `search_knowledge(keyword)` | 知识检索 | keyword | Dict |

### 5.3 核心模块代码示例

```python
# -- 能力 1: HEART 框架 (heart.py) --
heart_md = skill.build_heart_framework()
guide = skill.get_workshop_guide()

# -- 能力 2: CSat 调查 (csat.py) --
survey_md = skill.design_csat_survey("2024Q1 满意度", mechanism="email")
result = skill.analyze_csat("2024Q1", 500, {1: 20, 2: 30, 3: 80, 4: 200, 5: 170})

# -- 能力 3: 日志序列 (logs.py) --
skill.logs_analyzer.add_event("user_1", "2024-01-01 10:00:00", "首页")
skill.logs_analyzer.add_event("user_1", "2024-01-01 10:02:00", "搜索")
skill.logs_analyzer.add_event("user_1", "2024-01-01 10:05:00", "详情页")
logs_md = skill.analyze_logs()

# -- 能力 4: MaxDiff (maxdiff.py) --
design_md = skill.design_maxdiff(
    "功能优先级",
    ["快速搜索", "价格对比", "评价可信", "智能推荐", "行程规划",
     "在线客服", "退款便捷", "社区分享", "地图导航", "多语言"],
)

# -- 能力 5: A/B 测试 (abtest.py) --
n = skill.calculate_ab_sample_size(0.35, 0.03)  # 基线 35%, MDE 3%
result = skill.analyze_ab_test("原版", 5000, 1750, "新版", 5000, 1900)

# -- 能力 6: 研究规划 (research.py) --
diag = skill.diagnose_request("验证我们的新设计方向")
plan = skill.plan_research()

# -- 能力 7: 研究报告 --
report = skill.build_report("用户满意度研究")
full_report = skill.generate_report("定量 UX 研究报告", include_ceo_analysis=True)
```

### 5.4 CEO 决策支持模块

将 UX 研究成果转化为业务语言，帮助管理层做出数据驱动的决策。

| 方法 | 输出内容 |
|------|---------|
| `generate_business_impact(metrics)` | UX->业务指标映射、ROI 估算 (保守/基准/乐观)、敏感性分析 |
| `generate_validation_timeline()` | 4 阶段时间线 (准备2周->收集4周->分析3周->验证2周) + 里程碑 + 决策点 |
| `generate_resource_estimate()` | 人力 + 工具 + 激励成本估算、三场景投入产出比 |
| `generate_report(title, include_ceo_analysis=True)` | 完整报告，自动附加以上三个模块 |

```python
# CEO 级完整报告 (含业务影响 + 时间线 + 资源估算)
report = skill.generate_report("Q1 用户体验研究报告", include_ceo_analysis=True)

# 单独调用各模块
impact = skill.generate_business_impact()
timeline = skill.generate_validation_timeline()
estimate = skill.generate_resource_estimate()
```

### 5.5 完整使用示例

```python
from quantux import QuantUXSkill

skill = QuantUXSkill("旅行平台")

# Step 1-2: 指标体系 + 满意度调查
heart = skill.build_heart_framework()
survey = skill.design_csat_survey("2024Q1 用户满意度", mechanism="in_product")

# Step 3: 日志序列分析
for user, time, page in [("u1", "10:00", "首页"), ("u1", "10:02", "搜索"),
                          ("u1", "10:05", "详情页"), ("u1", "10:08", "下单")]:
    skill.logs_analyzer.add_event(user, f"2024-01-01 {time}", page)
logs = skill.analyze_logs()

# Step 4-5: MaxDiff + A/B 测试
maxdiff = skill.design_maxdiff("核心功能优先级",
    ["快速搜索", "价格对比", "评价可信", "智能推荐", "行程规划",
     "在线客服", "退款便捷", "社区分享", "地图导航", "多语言"])
n = skill.calculate_ab_sample_size(0.35, 0.03)

# Step 6-7: 诊断 + CEO 级报告
diag = skill.diagnose_request("我们想知道新首页设计是否更好")
report = skill.generate_report("2024Q1 用户体验研究报告", include_ceo_analysis=True)
```

### 5.6 AI Agent 调用规则

| # | 规则 | 说明 |
|---|------|------|
| 1 | **统一入口** | 始终通过 `QuantUXSkill` 类调用，不直接实例化子模块 |
| 2 | **返回值** | 所有方法返回 Markdown 字符串，可直接展示给用户 |
| 3 | **触发映射** | 根据用户意图选择对应能力 (参见触发条件总表) |
| 4 | **组合调用** | 综合任务按 能力一 -> 七 顺序依次执行 |
| 5 | **知识优先** | 理论问题先 `search_knowledge()` 查询 |
| 6 | **CEO 模块** | 管理层受众时用 `generate_report(include_ceo_analysis=True)` |
| 7 | **诊断先行** | 利益相关者请求先 `diagnose_request()` 再规划 |
| 8 | **数据驱动** | A/B 测试先算样本量再设计实验 |

### 5.7 测试说明

```bash
python quantux/tests/test_all.py          # 直接运行
python -m pytest quantux/tests/test_all.py -v  # pytest
```

| 测试用例 | 覆盖能力 | 验证内容 |
|---------|---------|---------|
| `test_heart_framework` | HEART 框架 | 构建、渲染 |
| `test_csat_survey` | CSat | 设计、分析、报告 |
| `test_logs_analyzer` | 日志序列 | 事件、会话化、频率 |
| `test_maxdiff_design` | MaxDiff | 设计、屏幕数计算 |
| `test_ab_test` | A/B 测试 | 样本量、结果分析 |
| `test_research_planner` | 研究规划 | 诊断、方案生成 |
| `test_report_builder` | 报告 | 基础报告、CEO 模块 |

### 5.8 与其他 Skill 协作

QuantUX 是 AliDujie UX 研究技能生态系统的定量研究核心，与其他技能组合形成完整的用户洞察到数据决策工作流：

| 协作场景 | 协作 Skill | 工作流 |
|---------|-----------|--------|
| 研究报告可视化 | [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) | Quant UXR 数据 → SWD 图表选择 → SWD 数据故事构建 |
| 价值主张验证 | [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) | VPD 假设 → Quant UXR A/B 验证 → SWD 高管汇报 |
| JTBD 研究量化 | [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) | JTBD 定性发现 → Quant UXR 量化验证机会分数 |
| 用户研究方法三角测量 | [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) | UDM 定性发现 → Quant UXR 定量验证 → 综合报告 |
| 角色数据验证 | [Web Persona](https://github.com/AliDujie/web-persona-skill) | Persona 角色假设 → Quant UXR 行为验证 → 角色迭代 |

**协作示例（UDM → QuantUX → SWD 端到端）**：
```python
# Step 1: UDM 定性研究收集用户洞察
from udm import UDMSkill
udm = UDMSkill("旅行预订")
interview = udm.generate_interview("商务用户访谈", "contextual")

# Step 2: QuantUX 定量验证假设
from quantux import QuantUXSkill
quantux = QuantUXSkill("旅行预订平台")
n = quantux.calculate_ab_sample_size(0.35, 0.03)  # 计算样本量
ab_result = quantux.analyze_ab_test("原版", 5000, 1750, "新版", 5000, 1900)

# Step 3: SWD 构建数据故事汇报
from swd import SWDSkill
swd = SWDSkill("Q1 用户体验研究报告")
ctx = swd.build_context(audience="产品VP", cta="批准体验优化预算")
story = swd.build_story(protagonist="产品委员会", imbalance="新设计提升转化15%")
```

**协作示例（JTBD → QuantUX）**：
```python
# Step 1: JTBD 发现高机会 Job
from jtbd import JTBDSkill
jtbd = JTBDSkill("旅行预订")
opportunity = jtbd.score_opportunity("快速找住处", struggle=4, alternative=3, market=4, budget=4)

# Step 2: QuantUX 设计 MaxDiff 验证功能优先级
from quantux import QuantUXSkill
quantux = QuantUXSkill("旅行预订")
maxdiff = quantux.design_maxdiff("功能优先级", ["快速搜索", "智能推荐", "价格日历"])
```

---

## 六、最佳实践

| # | 原则 | 说明 |
|---|------|------|
| 1 | 聚焦决策 | 研究应服务于具体的产品/设计/业务决策 |
| 2 | 反向工作 | 先展示模拟结果预览，确认有价值再投入 |
| 3 | 以用户为中心 | 研究问题首先从用户角度考虑 |
| 4 | 实际显著性优先 | 效应量和置信区间比 p 值更有用 |
| 5 | 最少技术细节 | 报告不含方程/模型输出，技术放附录 |

**常见陷阱**：

| 陷阱 | 应对 |
|------|------|
| "看看数据怎么说" | 先定义研究问题，任何数据分析后都会"说些什么" |
| 跨群体比较 CSat 绝对值 | 在同一群体内跟踪时间变化 |
| 过度优化单一指标 | Goodhart 法则：度量成为目标就不再是好的度量 |
| 统计显著性误解 | 用置信区间和实际效应替代 p 值 |
| 验证性研究 | 转化为具体的用户中心问题 |

---

## 七、参考资料

| 书名 | 作者 | 关键贡献 |
|------|------|---------|
| **Quantitative User Experience Research** | Jeff Sauro & James R. Lewis (2023) | 本 Skill 理论基础 |
| R/Python for Marketing Research and Analytics | Chapman & Feit | 统计分析实践 |
| Trustworthy Online Controlled Experiments | Kohavi, Tang & Xu | A/B 测试方法论 |
| Quantifying the User Experience | Sauro & Lewis | UX 量化方法 |
| Surveys That Work | Jarrett | 调查设计方法论 |

**术语速查**：Quant UXR = 量化用户体验研究 | HEART = Happiness/Engagement/Adoption/Retention/Task Success | GSM = Goals-Signals-Metrics | CSat = Customer Satisfaction | MaxDiff = Maximum Difference Scaling | HB = Hierarchical Bayes | MNL = Multinomial Logit | EDA = Exploratory Data Analysis | T2B = Top-2-Box | MDE = Minimum Detectable Effect

---

## 八、与其他 Skill 协作

QuantUX 是 AliDujie UX 研究技能生态系统的定量研究层，与其他技能配合实现定性定量三角验证：

| 协作场景 | 协作 Skill | 工作流 |
|---------|-----------|--------|
| 定量验证定性假设 | [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) | UDM 定性发现 → QuantUX 定量验证 → SWD 数据故事 |
| 数据可视化呈现 | [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) | QuantUX 分析结果 → SWD 图表选择 → SWD 叙事构建 |
| JTBD 机会分数验证 | [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) | JTBD 机会评分 → QuantUX A/B 测试验证 → 决策支持 |
| 角色定量验证 | [Web Persona](https://github.com/AliDujie/web-persona-skill) | Persona 细分 → QuantUX 行为分析 → Persona 精化 |
| 价值主张实验验证 | [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) | VPD 价值假设 → QuantUX 实验设计 → VPD 验证结果 |
| 结构化决策支持 | [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) | QuantUX 数据洞察 → STM 战略分析 → STM 决策建议 |

### AliDujie 技能生态

QuantUX 是 **AliDujie UX 研究技能生态系统** 的定量研究核心，负责用数据验证其他技能产生的定性假设：

| 技能 | 定位 | 协作模式 |
|------|------|---------|
| [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) | 方法论核心 | UDM 定性发现 → QuantUX 定量验证 → SWD 数据故事 |
| [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) | 需求洞察 | JTBD 机会分数 → QuantUX A/B 测试验证 → 决策支持 |
| [Web Persona](https://github.com/AliDujie/web-persona-skill) | 用户角色 | Persona 假设 → QuantUX 行为验证 → 角色迭代 |
| [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) | 价值验证 | VPD 价值假设 → QuantUX 实验设计 → VPD 验证结果 |
| [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) | 数据叙事 | QuantUX 分析结果 → SWD 图表选择 → SWD 叙事构建 |
| [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) | 战略框架 | QuantUX 数据洞察 → STM 战略分析 → STM 决策建议 |

### 🔗 扩展生态 (Extended Ecosystem)

QuantUX 定量数据可与管理层技能结合，将业务指标转化为战略决策：

| 扩展技能 | 协作场景 |
|---------|----------|
| [CEO Advisor](https://github.com/AliDujie/ceo-advisor) | QuantUX 业务影响 → CEO 资源分配与投资决策 |
| [CPO Advisor](https://github.com/AliDujie/cpo-advisor) | HEART 指标趋势 → CPO 产品战略调整 |
| [CMO Advisor](https://github.com/AliDujie/cmo-advisor) | QuantUX 增长数据 → CMO 渠道与获客策略 |
| [CTO Advisor](https://github.com/AliDujie/cto-advisor) | QuantUX 技术指标 → CTO 技术投资决策 |
