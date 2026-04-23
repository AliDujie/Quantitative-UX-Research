"""HEART 框架执行模块

对应执行能力：实施 HEART 框架工作坊、定义 Goals-Signals-Metrics、
生成指标体系报告。

基于 Google HEART 框架（Kerry Rodden 等提出），结合
《Quantitative User Experience Research》(Chapman & Rodden, 2023) 的实践指导。

用法示例::

    builder = HEARTBuilder("旅行平台")
    goal = builder.add_goal("happiness", "提升用户对搜索结果的满意度")
    signal = builder.add_signal(goal.description, "用户在满意度调查中给出高分", "success")
    builder.add_metric(signal.description, "搜索满意度Top-2-Box", "Top2Box(ratings)", "survey", True)
    framework = builder.build()
    print(HEARTBuilder.render_markdown(framework))
"""

from dataclasses import dataclass, field
from typing import Dict, List

from .config import (
    HEART_DIMENSIONS,
    HEART_LABELS,
    HEART_DESCRIPTIONS,
    HEART_EXAMPLE_METRICS,
)


# ── 数据结构 ──


@dataclass
class GoalItem:
    """HEART 框架中的单个目标项。

    每个目标对应一个 HEART 维度，描述该维度下希望达成的用户体验目标。

    Attributes:
        dimension: HEART 维度标识符，须为 HEART_DIMENSIONS 中的值
                   ("happiness", "engagement", "adoption", "retention", "task_success")。
        description: 目标的自然语言描述，例如 "提升用户对搜索结果的满意度"。

    Example::

        goal = GoalItem(dimension="happiness", description="提升用户对搜索结果的满意度")
    """

    dimension: str
    description: str


@dataclass
class SignalItem:
    """HEART 框架中的信号项。

    信号是目标达成或未达成时可观察到的用户行为或态度变化。

    Attributes:
        goal_ref: 关联的目标描述文本，用于追溯信号与目标的映射关系。
        description: 信号的自然语言描述。
        signal_type: 信号类型，"success" 表示成功信号，"failure" 表示失败信号。

    Example::

        signal = SignalItem(
            goal_ref="提升用户对搜索结果的满意度",
            description="用户在满意度调查中给出高分",
            signal_type="success",
        )
    """

    goal_ref: str
    description: str
    signal_type: str = "success"


@dataclass
class MetricItem:
    """HEART 框架中的指标项。

    指标是对信号的量化定义，包含计算公式和数据来源。

    Attributes:
        signal_ref: 关联的信号描述文本。
        name: 指标名称，例如 "搜索满意度Top-2-Box"。
        formula: 计算公式描述，例如 "Top2Box(satisfaction_ratings)"。
        data_source: 数据来源，可选 "logs"（日志）、"survey"（调查）、"external"（外部数据）。
        is_primary: 是否为主要指标，默认 False。每个维度建议设置 1 个主要指标。

    Example::

        metric = MetricItem(
            signal_ref="用户在满意度调查中给出高分",
            name="搜索满意度Top-2-Box",
            formula="Top2Box(satisfaction_ratings)",
            data_source="survey",
            is_primary=True,
        )
    """

    signal_ref: str
    name: str
    formula: str
    data_source: str = "logs"
    is_primary: bool = False


@dataclass
class HEARTFramework:
    """完整的 HEART 指标体系。

    包含产品名称以及 Goals-Signals-Metrics 三层映射的全部数据。

    Attributes:
        product_name: 产品名称。
        goals: 目标列表。
        signals: 信号列表。
        metrics: 指标列表。

    Example::

        framework = HEARTFramework(
            product_name="旅行平台",
            goals=[GoalItem("happiness", "提升满意度")],
            signals=[SignalItem("提升满意度", "调查高分", "success")],
            metrics=[MetricItem("调查高分", "T2B", "Top2Box()", "survey", True)],
        )
    """

    product_name: str
    goals: List[GoalItem] = field(default_factory=list)
    signals: List[SignalItem] = field(default_factory=list)
    metrics: List[MetricItem] = field(default_factory=list)


# ── 数据来源标签 ──

_DATA_SOURCE_LABELS: Dict[str, str] = {
    "logs": "日志",
    "survey": "调查",
    "external": "外部数据",
}

_SIGNAL_TYPE_LABELS: Dict[str, str] = {
    "success": "成功信号",
    "failure": "失败信号",
}


# ── Builder ──


class HEARTBuilder:
    """HEART 框架构建器

    提供逐步构建 Goals-Signals-Metrics 映射的流式 API，
    并支持生成 Markdown 报告和工作坊执行指南。

    用法示例::

        builder = HEARTBuilder("旅行平台")

        # 定义目标
        g1 = builder.add_goal("happiness", "提升用户对搜索结果的满意度")
        g2 = builder.add_goal("task_success", "提高酒店预订流程完成率")

        # 定义信号
        s1 = builder.add_signal(g1.description, "用户在满意度调查中给出高分", "success")
        s2 = builder.add_signal(g1.description, "用户搜索后未点击任何结果", "failure")
        s3 = builder.add_signal(g2.description, "用户成功完成预订", "success")

        # 定义指标
        builder.add_metric(s1.description, "搜索满意度T2B", "Top2Box(ratings)", "survey", True)
        builder.add_metric(s2.description, "零点击率", "zero_click / total_search", "logs")
        builder.add_metric(s3.description, "预订完成率", "completed / started", "logs", True)

        framework = builder.build()
        print(HEARTBuilder.render_markdown(framework))
    """

    def __init__(self, product_name: str):
        """初始化构建器。

        Args:
            product_name: 产品名称，将用于报告标题。
        """
        self._product_name = product_name
        self._goals: List[GoalItem] = []
        self._signals: List[SignalItem] = []
        self._metrics: List[MetricItem] = []

    def add_goal(self, dimension: str, description: str) -> GoalItem:
        """添加一个 HEART 目标。

        Args:
            dimension: HEART 维度，须为 HEART_DIMENSIONS 中的值。
            description: 目标描述。

        Returns:
            创建的 GoalItem 实例。

        Raises:
            ValueError: 当 dimension 不在合法维度列表中时。

        Example::

            goal = builder.add_goal("happiness", "提升搜索满意度")
        """
        if dimension not in HEART_DIMENSIONS:
            raise ValueError(
                f"未知HEART维度: {dimension}，可选: {HEART_DIMENSIONS}"
            )
        item = GoalItem(dimension=dimension, description=description)
        self._goals.append(item)
        return item

    def add_signal(
        self, goal_description: str, description: str, signal_type: str = "success"
    ) -> SignalItem:
        """添加一个信号。

        Args:
            goal_description: 关联的目标描述文本，应与已添加的某个 GoalItem.description 一致。
            description: 信号描述。
            signal_type: 信号类型，"success" 或 "failure"，默认 "success"。

        Returns:
            创建的 SignalItem 实例。

        Raises:
            ValueError: 当 signal_type 不合法时。

        Example::

            signal = builder.add_signal("提升搜索满意度", "用户给出高分", "success")
        """
        if signal_type not in ("success", "failure"):
            raise ValueError(
                f"未知信号类型: {signal_type}，可选: 'success', 'failure'"
            )
        item = SignalItem(
            goal_ref=goal_description,
            description=description,
            signal_type=signal_type,
        )
        self._signals.append(item)
        return item

    def add_metric(
        self,
        signal_ref: str,
        name: str,
        formula: str,
        data_source: str = "logs",
        is_primary: bool = False,
    ) -> MetricItem:
        """添加一个指标。

        Args:
            signal_ref: 关联的信号描述文本。
            name: 指标名称。
            formula: 计算公式。
            data_source: 数据来源，可选 "logs"、"survey"、"external"，默认 "logs"。
            is_primary: 是否为主要指标，默认 False。

        Returns:
            创建的 MetricItem 实例。

        Raises:
            ValueError: 当 data_source 不合法时。

        Example::

            metric = builder.add_metric("用户给出高分", "满意度T2B", "Top2Box()", "survey", True)
        """
        valid_sources = ("logs", "survey", "external")
        if data_source not in valid_sources:
            raise ValueError(
                f"未知数据来源: {data_source}，可选: {valid_sources}"
            )
        item = MetricItem(
            signal_ref=signal_ref,
            name=name,
            formula=formula,
            data_source=data_source,
            is_primary=is_primary,
        )
        self._metrics.append(item)
        return item

    def build(self) -> HEARTFramework:
        """构建完整的 HEART 框架实例。

        Returns:
            包含所有已添加目标、信号和指标的 HEARTFramework 实例。

        Example::

            framework = builder.build()
        """
        return HEARTFramework(
            product_name=self._product_name,
            goals=list(self._goals),
            signals=list(self._signals),
            metrics=list(self._metrics),
        )

    @staticmethod
    def render_markdown(framework: HEARTFramework) -> str:
        """将 HEART 框架渲染为 Markdown 格式的指标体系文档。

        输出包含 GSM 映射表和分维度详情。

        Args:
            framework: 已构建的 HEARTFramework 实例。

        Returns:
            完整的 Markdown 格式报告字符串。

        Example::

            md = HEARTBuilder.render_markdown(framework)
            print(md)
        """
        lines: List[str] = []
        lines.append(f"# {framework.product_name} HEART指标体系\n")

        # ── 构建目标→维度映射 ──
        goal_dim: Dict[str, str] = {}
        for g in framework.goals:
            goal_dim[g.description] = g.dimension

        # ── 构建信号→目标映射 ──
        signal_goal: Dict[str, str] = {}
        for s in framework.signals:
            signal_goal[s.description] = s.goal_ref

        # ── GSM 映射表 ──
        lines.append("## Goals-Signals-Metrics 映射表\n")
        lines.append("| HEART维度 | 目标 | 信号 | 指标 | 数据来源 | 主要指标 |")
        lines.append("|-----------|------|------|------|----------|----------|")

        for m in framework.metrics:
            sig_desc = m.signal_ref
            goal_desc = signal_goal.get(sig_desc, "—")
            dim_key = goal_dim.get(goal_desc, "")
            dim_label = HEART_LABELS.get(dim_key, dim_key)
            source_label = _DATA_SOURCE_LABELS.get(m.data_source, m.data_source)
            primary = "✓" if m.is_primary else ""
            lines.append(
                f"| {dim_label} | {goal_desc} | {sig_desc} | {m.name} | {source_label} | {primary} |"
            )

        lines.append("")

        # ── 分维度详情 ──
        covered_dims = sorted(set(g.dimension for g in framework.goals))
        for dim in covered_dims:
            dim_label = HEART_LABELS.get(dim, dim)
            lines.append(f"## {dim_label}\n")

            dim_goals = [g for g in framework.goals if g.dimension == dim]
            for g in dim_goals:
                lines.append(f"### 目标: {g.description}\n")

                related_signals = [
                    s for s in framework.signals if s.goal_ref == g.description
                ]
                if related_signals:
                    lines.append("**信号:**\n")
                    for s in related_signals:
                        type_label = _SIGNAL_TYPE_LABELS.get(s.signal_type, s.signal_type)
                        lines.append(f"- [{type_label}] {s.description}")

                        related_metrics = [
                            met for met in framework.metrics if met.signal_ref == s.description
                        ]
                        for met in related_metrics:
                            source_label = _DATA_SOURCE_LABELS.get(met.data_source, met.data_source)
                            primary_tag = " ⭐主要指标" if met.is_primary else ""
                            lines.append(
                                f"  - **{met.name}**: `{met.formula}` ({source_label}){primary_tag}"
                            )
                    lines.append("")

        # ── 覆盖度检查 ──
        uncovered = [
            HEART_LABELS[d]
            for d in HEART_DIMENSIONS
            if d not in covered_dims
        ]
        if uncovered:
            lines.append("## 未覆盖维度\n")
            lines.append("以下 HEART 维度尚未定义目标，建议在后续迭代中补充：\n")
            for label in uncovered:
                lines.append(f"- {label}")
            lines.append("")

        return "\n".join(lines)

    def render_workshop_guide(self) -> str:
        """生成 HEART 工作坊执行指南。

        输出包含工作坊的完整流程：准备事项、各阶段步骤、
        时间分配、讨论问题和产出物说明。

        Returns:
            Markdown 格式的工作坊执行指南字符串。

        Example::

            guide = builder.render_workshop_guide()
            print(guide)
        """
        product = self._product_name
        lines: List[str] = []

        lines.append(f"# {product} HEART 工作坊执行指南\n")

        # ── 工作坊概览 ──
        lines.append("## 工作坊概览\n")
        lines.append(f"- **产品:** {product}")
        lines.append("- **总时长:** 约 2-3 小时")
        lines.append("- **参与者:** PM、UX 研究员、工程师、数据分析师（建议 5-8 人）")
        lines.append("- **产出物:** 完整的 HEART Goals-Signals-Metrics 映射表\n")

        # ── 准备事项 ──
        lines.append("## 准备事项\n")
        lines.append("1. 准备白板或在线协作工具（如 Miro/FigJam）")
        lines.append("2. 打印 HEART 维度参考卡片")
        lines.append("3. 收集现有的产品数据和指标")
        lines.append("4. 邀请跨职能团队成员\n")

        # ── 各阶段 ──
        stages = [
            {
                "title": "第一阶段：HEART 维度介绍与选择",
                "time": "20 分钟",
                "steps": [
                    "介绍 HEART 五个维度的定义和适用场景",
                    f"讨论并确定 {product} 最相关的 2-3 个维度",
                    "记录选择理由和优先级排序",
                ],
                "questions": [
                    f"对于 {product}，哪些维度对业务目标最关键？",
                    "当前用户体验的最大痛点属于哪个维度？",
                    "哪些维度已有数据支撑，哪些需要新建采集？",
                ],
            },
            {
                "title": "第二阶段：定义 Goals（目标）",
                "time": "30 分钟",
                "steps": [
                    "为每个选定维度定义 1-2 个具体目标",
                    "确保目标以用户体验为中心而非业务指标",
                    "检查目标是否可观测、可量化",
                ],
                "questions": [
                    "在这个维度上，理想的用户体验是什么样的？",
                    "用户在什么情况下会觉得体验好/差？",
                    "这个目标如何与产品战略对齐？",
                ],
            },
            {
                "title": "第三阶段：识别 Signals（信号）",
                "time": "30 分钟",
                "steps": [
                    "为每个目标列举成功信号和失败信号",
                    "区分态度信号（调查）和行为信号（日志）",
                    "优先选择可自动化采集的信号",
                ],
                "questions": [
                    "如果用户达成了这个目标，我们能观察到什么行为变化？",
                    "如果用户体验糟糕，会出现什么信号？",
                    "哪些信号是现有系统已经在记录的？",
                ],
            },
            {
                "title": "第四阶段：定义 Metrics（指标）",
                "time": "40 分钟",
                "steps": [
                    "将信号转化为可计算的指标",
                    "定义每个指标的计算公式和数据来源",
                    "为每个维度选定 1 个主要指标（Primary Metric）",
                    "讨论指标的基线值和目标值",
                ],
                "questions": [
                    "这个信号如何量化为一个具体数字？",
                    "数据从哪里获取？日志、调查还是外部来源？",
                    "指标的更新频率应该是多少？",
                    "如何区分指标的自然波动和真实变化？",
                ],
            },
            {
                "title": "第五阶段：回顾与优先级排序",
                "time": "20 分钟",
                "steps": [
                    "回顾完整的 GSM 映射表",
                    "检查指标间的冗余和遗漏",
                    "确定首批实施的指标（建议 3-5 个）",
                    "分配指标的负责人和上线时间表",
                ],
                "questions": [
                    "这套指标体系是否全面覆盖了关键用户体验？",
                    "哪些指标可以在一周内开始采集？",
                    "是否存在指标间的冲突或矛盾？",
                ],
            },
        ]

        for stage in stages:
            lines.append(f"## {stage['title']}\n")
            lines.append(f"**时间:** {stage['time']}\n")

            lines.append("**步骤:**\n")
            for i, step in enumerate(stage["steps"], 1):
                lines.append(f"{i}. {step}")
            lines.append("")

            lines.append("**讨论问题:**\n")
            for q in stage["questions"]:
                lines.append(f"- {q}")
            lines.append("")

        # ── HEART 维度参考 ──
        lines.append("## 附录：HEART 维度参考\n")
        lines.append("| 维度 | 说明 | 示例指标 |")
        lines.append("|------|------|----------|")
        for dim in HEART_DIMENSIONS:
            label = HEART_LABELS[dim]
            desc = HEART_DESCRIPTIONS[dim]
            examples = "、".join(HEART_EXAMPLE_METRICS[dim][:2])
            lines.append(f"| {label} | {desc} | {examples} |")
        lines.append("")

        return "\n".join(lines)
