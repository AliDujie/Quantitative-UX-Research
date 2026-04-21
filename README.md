# Quantitative UX Research Skill

> 📈 **用数据驱动产品决策，规模化理解用户**

基于《Quantitative User Experience Research: Informing Product Decisions by Understanding Users at Scale》(Chris Chapman & Kerry Rodden, Apress 2023) 构建的完整执行技能。

## 🌟 为什么使用这个技能？

- **全链路量化能力** — 从指标体系到 A/B 测试，覆盖 Quant UXR 全流程
- **7 大执行引擎** — HEART 框架、CSat 分析、日志序列、MaxDiff、A/B 测试、研究规划、报告生成
- **实战导向** — 内置统计计算、置信区间、样本量估算，无需手动公式
- **零依赖** — 纯 Python 标准库，5 分钟上手，即刻产出
- **专业可靠** — 基于 Apress 权威著作，T 型技能模型 (编程∩UX 研究∩统计)

## 🚀 5 分钟快速开始

### 步骤 1: 安装技能

```bash
# 复制到你的 AI Agent skills 目录
cp -r skills/quant-ux-research ~/.aoneclaw/skills/
```

### 步骤 2: 作为 Python 包使用

```python
import sys
sys.path.insert(0, "/path/to/Quantitative-UX-Research")
from quantux import QuantUXSkill

# 初始化技能
skill = QuantUXSkill("我的产品")
```

### 步骤 3: 开始使用

```python
# ===== 能力 1: HEART 框架与指标体系 =====
# 构建完整的指标体系
skill.heart_builder.add_goal("happiness", "提升用户对预订流程的满意度")
skill.heart_builder.add_signal("happiness", "预订后满意度评分", "success")
skill.heart_builder.add_metric("预订后满意度评分", "预订满意度 T2B", "Top-2-Box 比例", "survey", True)
print(skill.build_heart_framework())

# ===== 能力 2: CSat 调查设计与分析 =====
# 添加季度数据，自动计算趋势和置信区间
skill.csat_analyzer.add_data_point("2024Q1", 500, {1:10, 2:20, 3:50, 4:180, 5:240})
skill.csat_analyzer.add_data_point("2024Q2", 480, {1:8, 2:18, 3:45, 4:190, 5:219})
report = skill.csat_analyzer.generate_report()
print(report)  # 包含 T2B、置信区间、趋势分析

# ===== 能力 3: 日志序列路径分析 =====
# 添加用户行为事件，自动会话化和路径分析
skill.logs_analyzer.add_event("user_001", "2024-01-01 10:00:00", "首页")
skill.logs_analyzer.add_event("user_001", "2024-01-01 10:02:00", "搜索")
skill.logs_analyzer.add_event("user_001", "2024-01-01 10:05:00", "详情页")
skill.logs_analyzer.add_event("user_001", "2024-01-01 10:08:00", "预订")
print(skill.analyze_logs())  # 会话化、序列频率、Markov 转移矩阵

# ===== 能力 4: MaxDiff 功能优先级 =====
# 设计 MaxDiff 调查，自动计算最优屏幕数
items = ["快速搜索", "价格对比", "评价可信", "退款便捷", "客服响应",
         "界面美观", "个性推荐", "行程规划", "优惠提醒", "地图导航"]
design = skill.design_maxdiff("功能优先级", items)
print(design)  # 调查设计 + 验证

# 分析 MaxDiff 结果
skill.maxdiff_analyzer.add_response("user_001", best="快速搜索", worst="界面美观")
skill.maxdiff_analyzer.add_response("user_002", best="价格对比", worst="优惠提醒")
print(skill.maxdiff_analyzer.analyze())  # 计数分析、标准化分数、排序

# ===== 能力 5: A/B 测试设计与分析 =====
# 计算所需样本量
n = skill.calculate_ab_sample_size(baseline=0.35, mde=0.03)
print(f"每组需要 {n:,} 个样本")

# 分析 A/B 测试结果
result = skill.analyze_ab_test("对照组", 5000, 1750, "实验组", 5000, 1900)
print(result)  # 转化率差异、置信区间、p 值、业务解读

# ===== 能力 6: 研究规划与利益相关者诊断 =====
# 诊断研究请求，给出方法建议
diagnosis = skill.diagnose_request("验证我们的新设计方向是否正确")
print(diagnosis)  # 6 维度诊断 + 方法推荐

# 生成完整研究计划
plan = skill.research_planner.create_plan(
    objective="验证新设计方向",
    methods=["survey", "ab_test"],
    timeline="2 周"
)
print(plan)

# ===== 能力 7: 研究报告生成 =====
report = skill.report_builder.generate(
    title="2024 Q2 用户体验研究报告",
    findings=["满意度提升 15%", "流失率下降 8%"],
    recommendations=["继续优化搜索功能", "增加价格提醒"]
)
print(report)

# ===== 知识库搜索 =====
from quantux import search_knowledge
results = search_knowledge("置信区间")
print(results)
```

## 💡 7 大执行能力

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
Quantitative-UX-Research/
├── skills/quant-ux-research/
│   └── SKILL.md                 # AI Agent 技能定义
├── quantux/                     # Python 执行包（纯标准库）
│   ├── __init__.py              # 统一入口类 QuantUXSkill
│   ├── config.py                # 全局配置：HEART 维度、CSat/MaxDiff/AB 常量
│   ├── utils.py                 # 知识库搜索 + 统计工具（置信区间、样本量、T2B）
│   ├── templates.py             # 工作坊/调查/报告模板 + 数据质量检查清单
│   ├── heart.py                 # 能力 1: HEART 框架
│   ├── csat.py                  # 能力 2: CSat 调查
│   ├── logs.py                  # 能力 3: 日志序列
│   ├── maxdiff.py               # 能力 4: MaxDiff
│   ├── abtest.py                # 能力 5: A/B 测试
│   └── research.py              # 能力 6+7: 研究规划 & 报告
├── SKILL.md                     # 原始知识库文档
├── pyproject.toml
├── requirements.txt
└── README.md                    # 本文件
```

## 🔗 相关技能

本技能是 **AliDujie UX 研究技能生态系统** 的一部分：

- **[Universal-Design-Methods](https://github.com/AliDujie/universal-design-methods)** — 100 种设计研究方法（定性为主）
- **[JTBD-Knowledge-Skill](https://github.com/AliDujie/jtbd-knowledge-skill)** — Jobs-to-be-Done 理论、进步力量分析
- **[Value-Proposition-Design](https://github.com/AliDujie/value-proposition-design)** — 价值主张画布、商业模式设计
- **[Web-Persona-Skill](https://github.com/AliDujie/web-persona-skill)** — 人物角色创建、用户细分
- **[Storytelling-with-Data](https://github.com/AliDujie/storytelling-with-data)** — 数据叙事、可视化设计

**推荐组合使用**：
- **定性 + 定量三角测量**：Universal-Design-Methods (定性) + 本技能 (定量)
- **从洞察到呈现**：本技能 (分析) → Storytelling-with-Data (呈现)
- **完整用户理解**：JTBD (动机) + Web-Persona (画像) + 本技能 (行为量化)

## 📦 依赖

- Python >= 3.8
- **无外部依赖**（纯标准库实现）
- 兼容 macOS / Linux / Windows

## 🔑 核心理论基础

本技能基于以下核心框架：

- **HEART 框架** — Happiness / Engagement / Adoption / Retention / Task Success
- **GSM 流程** — Goals → Signals → Metrics
- **T 型技能模型** — 编程 ∩ UX 研究 ∩ 统计
- **以用户为中心五原则** — 用户视角、用户变量、认知方法、未满足需求、UX 行动
- **四大交付物原则** — 简短聚焦、最少技术、保持无偏、可复现

## 📚 关于原书

- **书名**: Quantitative User Experience Research: Informing Product Decisions by Understanding Users at Scale
- **作者**: Chris Chapman & Kerry Rodden
- **出版**: Apress, 2023
- **内容**: 15 章 + 3 个附录，覆盖 Quant UXR 的完整知识体系
- **适用**: UX 研究员、数据分析师、产品经理、增长团队

## 📜 许可

本技能仅供内部学习和研究使用。

## 👨‍💻 作者

- **GitHub**: [@AliDujie](https://github.com/AliDujie)
- **Emp ID**: 27768
- **Nickname**: 渡劫
