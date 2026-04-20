"""Quant UX Skill 模板定义模块

提供 HEART 工作坊、CSat 调查、研究报告等标准模板。
"""

from typing import Dict, List

HEART_WORKSHOP_TEMPLATE = """# HEART 指标工作坊执行指南

## 准备
- **参与者**: PM、设计师、工程师、UXR（4-8人）
- **时间**: 2-3小时
- **工具**: 白板/便签纸/在线协作文档

## 流程

### 第一阶段：介绍 HEART 框架（10分钟）
介绍五大维度：Happiness / Engagement / Adoption / Retention / Task Success

### 第二阶段：定义目标 Goals（30分钟）
1. 每人独立写下产品的用户体验目标（5分钟）
2. 逐一分享并讨论，合并相似目标（15分钟）
3. 将目标映射到 HEART 类别（10分钟）
   - 不需要覆盖所有类别，选择最相关的2-3个

### 第三阶段：识别信号 Signals（30分钟）
1. 为每个目标头脑风暴可观察的用户行为/态度信号
2. 同时考虑成功信号和失败信号
3. 评估信号的可测量性和灵敏度

### 第四阶段：定义指标 Metrics（40分钟）
1. 将信号转化为可追踪的具体数字
2. 优先使用比率/百分比（比原始计数更有用）
3. 确定数据来源（日志/调查/外部数据）
4. 标记主要指标（每个目标1-2个）

### 第五阶段：优先级与行动计划（20分钟）
1. 选择3-5个核心指标
2. 讨论数据获取可行性
3. 制定实施时间表

## 产出
- Goals-Signals-Metrics 映射表
- 核心指标清单及数据来源
- 实施优先级和时间表
"""

GSM_TABLE_TEMPLATE = """| HEART维度 | 目标 (Goal) | 信号 (Signal) | 指标 (Metric) | 数据来源 | 主要指标 |
|-----------|------------|--------------|--------------|----------|---------|
| {dimension} | {goal} | {signal} | {metric} | {source} | {primary} |
"""

CSAT_SURVEY_TEMPLATE = """# {title}

**调查方式:** {mechanism}
**目标人群:** {target}
**预计时长:** {estimated_time}

---

Q1. [评分量表 1-{scale}] 总体而言，你对{product}的满意程度如何？
   (1=非常不满意 / {mid}=一般 / {scale}=非常满意)

Q2. [开放题] 请告诉我们，你对{product}最满意和最不满意的地方分别是什么？

---

{closing}
"""

CSAT_REPORT_TEMPLATE = """# {title}

## 执行摘要
{executive_summary}

## 样本信息
{sample_info}

## 满意度评分分布
{score_distribution}

## 时间趋势
{trends}

## 关键发现
{key_findings}

## 建议
{recommendations}
"""

MAXDIFF_DESIGN_TEMPLATE = """# MaxDiff 调查设计: {title}

## 问题头部
"{question_head}"

## 项目列表 ({item_count} 个项目)
{items_list}

## 设计参数
- 每屏显示项目数: {items_per_screen}
- 每个项目出现次数: {appearances}
- 总屏幕数: {total_screens}
- 目标样本量: {sample_target}

## 样本量建议
- N=200: 样本级结果通常稳定
- N=1000: 支持分群分析和可靠性评估
- N=100/组: 已知分组时的目标
"""

AB_TEST_PLAN_TEMPLATE = """# A/B 测试计划: {title}

## 假设
{hypothesis}

## 用户定义
{user_definition}

## 实验方案
{variants}

## 主要指标
{primary_metric}

## 护栏指标
{guardrail_metrics}

## 样本量与时长
- 最小样本量: {min_sample_size}
- 预估持续时间: {duration}

## 已识别的混淆变量
{confounds}

## 分析计划
1. 检查随机化是否均衡
2. 计算主要指标的差异和置信区间
3. 检查护栏指标是否异常
4. 聚焦实际效应而非统计显著性
"""

RESEARCH_REPORT_TEMPLATE = """# {title}

## 1. 执行摘要
{executive_summary}

## 2. 研究问题
{questions}

## 3. 方法概述
{methods}

## 4. 关键发现
{findings}

## 5. 建议
{recommendations}

## 6. 局限性
{limitations}

## 附录
{appendix}
"""

STAKEHOLDER_DIAGNOSIS_QUESTIONS: Dict[str, List[str]] = {
    "user_centered": [
        "这个问题是否以用户为中心？",
        "是否关注用户行为/态度/需求，而非仅业务指标？",
        "研究结果是否能帮助改善用户体验？",
    ],
    "decision_point": [
        "回答这个问题会影响什么具体决策？",
        "决策者是谁？他们需要什么级别的证据？",
        "如果不做这个研究，决策会如何进行？",
    ],
    "precision": [
        "需要方向性指导还是精确数据？",
        "结果需要多大的置信度？",
        "是否需要可复现的定量证据？",
    ],
    "existing_data": [
        "已有什么相关数据（日志/调查/竞品数据）？",
        "之前是否做过类似研究？",
        "能否先做EDA再决定是否需要新数据？",
    ],
    "constraints": [
        "时间约束是什么？",
        "预算和人力资源如何？",
        "数据获取是否有技术障碍？",
    ],
    "opportunity_cost": [
        "做这个项目意味着不做什么？",
        "是否有更高优先级的研究需求？",
        "能否与其他项目合并以提高效率？",
    ],
}

DATA_QUALITY_CHECKLIST: List[str] = [
    "样本是否具有代表性？（非便利样本偏差）",
    "是否可假设随机抽样？",
    "是否存在混淆因素？",
    "数据效度：数据是否真的意味着我们认为的含义？",
    "数据信度：重复获取是否一致？",
    "异常值处理：是否有正当理由删除？",
    "数据管道准确性：是否有技术问题导致数据丢失？",
    "在线抽样：选择概率是否与使用频率成正比？",
    "序数数据是否被错误当作连续数据？",
    "跨群体比较是否考虑了文化差异和Simpson悖论？",
]
