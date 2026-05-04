---
name: quantitative-ux-research
description: 量化用户体验研究执行技能。基于 Jeff Sauro & James R. Lewis 方法论，提供实验设计、样本量计算、统计分析、调查设计、日志分析、满意度分析、研究报告生成等完整执行能力，以及CEO决策视角的业务影响评估、验证时间线与资源估算。
version: "2.3.16"
---

# Quantitative UX Research Skill

基于《Quantitative User Experience Research》(Jeff Sauro & James R. Lewis, 2023) 的量化用户体验研究执行技能。

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

纯 Python 实现，无外部依赖，仅需 Python 3.8+。

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
skill.logs_analyzer.add_event("user_1", "2024-01-01 10:00", "首页")
skill.logs_analyzer.add_event("user_1", "2024-01-01 10:02", "搜索")
skill.logs_analyzer.add_event("user_1", "2024-01-01 10:05", "详情页")
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

| 协作场景 | 协作 Skill | 工作流 |
|---------|-----------|--------|
| 研究报告可视化 | Storytelling with Data | Quant UXR 数据 -> SWD 图表 -> SWD 故事 |
| 价值主张验证 | Value Proposition Design | VPD 假设 -> Quant UXR 验证 -> SWD 汇报 |
| JTBD 研究量化 | JTBD Knowledge | JTBD 定性发现 -> Quant UXR 量化验证 -> JTBD 机会评分 |
| 研究方法论选择 | Universal Design Methods | UDM 方法推荐 -> Quant UXR 定量执行 -> UDM 综合报告 |
| 用户细分验证 | Web Persona | Persona 角色定义 -> Quant UXR 分层 A/B 测试 -> Persona 精化 |
| 结构化分析补充 | Structured Thinking Model | STM 分析框架 -> Quant UXR 数据验证 -> STM 决策建议 |

**协作示例（QuantUX + SWD）**：
```python
# Step 1: QuantUX 产出 HEART 指标
quant = QuantUXSkill("电商平台")
heart = quant.build_heart_framework()
# Step 2: SWD 将指标可视化
from swd import SWDSkill
swd = SWDSkill("HEART 指标汇报")
chart = swd.recommend_chart(data_type="categorical", category_count=5)
story = swd.build_story(protagonist="产品团队", imbalance="用户留存率低于目标")
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
