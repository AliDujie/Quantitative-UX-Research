"""研究规划与报告模块

对应执行能力：研究规划、利益相关者诊断、研究报告生成。
基于《Quantitative User Experience Research》(Chapman & Rodden, 2023)。

用法示例::

    # 研究规划
    planner = ResearchPlanner("搜索引擎")
    planner.set_stakeholder("产品经理")
    planner.add_question(
        original="用户喜欢新设计吗？",
        refined="新搜索结果页布局是否提升了用户的任务完成率和满意度？",
        decision="是否全量发布新布局",
        method="ab_test",
    )
    diagnosis = planner.diagnose_request("我们需要证明新设计更好")
    plan = planner.build()
    print(ResearchPlanner.render_markdown(plan))

    # 研究报告
    rb = ReportBuilder("搜索结果页改版效果评估")
    rb.set_executive_summary("新布局在任务完成率上提升了5%，但满意度无显著差异。")
    rb.add_question("新布局是否提升了任务完成率？")
    rb.set_methods("A/B测试，为期2周，覆盖5%流量")
    rb.add_finding("任务完成率提升", "实验组任务完成率为78%，对照组为73%，差异显著(p<0.01)。")
    rb.add_recommendation("建议全量发布新布局，同时监控满意度指标。")
    rb.add_limitation("实验仅覆盖桌面端用户。")
    report = rb.build()
    print(ReportBuilder.render_markdown(report))
"""

from dataclasses import dataclass, field
from typing import Dict, List

from .config import (
    RESEARCH_METHODS,
    LIFECYCLE_STAGES,
    LIFECYCLE_METHODS,
)


# ── 诊断请求的6个标准问题 ──

DIAGNOSIS_QUESTIONS: List[str] = [
    "是否以用户为中心？（问题是关于用户行为/态度，还是内部业务指标？）",
    "回答此问题会影响什么决策？（如果答案不改变任何行动，则无需研究）",
    "需要什么级别的精确度？（方向性判断 vs 精确数值）",
    "已有什么相关数据？（日志、历史调查、竞品分析等）",
    "时间和资源约束是什么？（截止日期、预算、工具可用性）",
    "机会成本是什么？（不做这个研究，团队可以做什么？）",
]

PRECISION_LEVELS = ("directional", "precise")


@dataclass
class ResearchQuestion:
    """一条研究问题，从利益相关者的原始问题转化而来。

    Attributes:
        original_question: 利益相关者的原始问题，通常较模糊。
        refined_question: 转化后的可研究问题，具备明确的测量目标。
        decision_point: 回答此问题将影响什么决策。
        method: 推荐的研究方法，应为 config.RESEARCH_METHODS 中的值。

    用法示例::

        rq = ResearchQuestion(
            original_question="用户喜欢新功能吗？",
            refined_question="新功能上线后，用户的7天留存率是否提升了2个百分点？",
            decision_point="是否继续投入资源迭代该功能",
            method="ab_test",
        )
        print(rq.refined_question)
    """

    original_question: str
    refined_question: str
    decision_point: str
    method: str


@dataclass
class ResearchPlan:
    """完整的研究计划。

    Attributes:
        title: 研究计划标题。
        stakeholder: 利益相关者名称或角色。
        product: 产品名称。
        questions: 研究问题列表。
        methods: 使用的研究方法列表。
        data_sources: 数据来源列表。
        timeline: 时间安排描述。
        sample_strategy: 抽样策略描述。
        deliverable_preview: 模拟结果预览描述，帮助利益相关者理解最终交付物。

    用法示例::

        plan = ResearchPlan(
            title="搜索体验优化研究",
            stakeholder="搜索产品经理",
            product="搜索引擎",
            questions=[],
            methods=["ab_test", "csat"],
            data_sources=["产品日志", "HaTS调查"],
            timeline="2周数据收集 + 1周分析",
            sample_strategy="随机抽取5%活跃用户",
            deliverable_preview="交付包含任务完成率对比和满意度变化的报告",
        )
    """

    title: str
    stakeholder: str
    product: str
    questions: List[ResearchQuestion] = field(default_factory=list)
    methods: List[str] = field(default_factory=list)
    data_sources: List[str] = field(default_factory=list)
    timeline: str = ""
    sample_strategy: str = ""
    deliverable_preview: str = ""


@dataclass
class StakeholderDiagnosis:
    """利益相关者请求的诊断结果。

    通过6个标准诊断问题评估利益相关者的研究请求，
    识别常见问题（如验证性研究、无决策标准等），并给出建议。

    Attributes:
        original_request: 利益相关者的原始请求。
        is_user_centered: 请求是否以用户为中心。
        decision_point: 该请求关联的决策点。
        precision_level: 所需精确度级别，"directional" 或 "precise"。
        existing_data: 已有的相关数据列表。
        opportunity_cost: 机会成本描述。
        recommendation: 综合建议。

    用法示例::

        diag = StakeholderDiagnosis(
            original_request="证明新设计更好",
            is_user_centered=False,
            decision_point="不明确",
            precision_level="directional",
            existing_data=["无"],
            opportunity_cost="延迟其他项目的数据分析",
            recommendation="建议先明确决策标准，再设计研究方案。",
        )
    """

    original_request: str
    is_user_centered: bool
    decision_point: str
    precision_level: str
    existing_data: List[str] = field(default_factory=list)
    opportunity_cost: str = ""
    recommendation: str = ""


@dataclass
class ResearchReport:
    """研究报告数据结构。

    按照书中推荐的报告结构组织：执行摘要、研究问题、方法概述、
    关键发现、建议、局限性、附录。

    Attributes:
        title: 报告标题。
        executive_summary: 执行摘要（1段）。
        questions: 研究问题列表。
        methods_summary: 方法概述。
        findings: 关键发现列表，每个 finding 含 title 和 description。
        recommendations: 建议列表。
        limitations: 局限性列表。
        appendix_links: 附录链接列表。

    用法示例::

        report = ResearchReport(
            title="移动端结账流程优化评估",
            executive_summary="新结账流程将转化率提升了3.2%。",
            questions=["新流程是否提升了转化率？"],
            methods_summary="A/B测试，2周，10%流量",
            findings=[{"title": "转化率提升", "description": "实验组12.1% vs 对照组8.9%"}],
            recommendations=["全量发布新流程"],
            limitations=["仅覆盖iOS用户"],
            appendix_links=["详细数据表: link1"],
        )
    """

    title: str
    executive_summary: str = ""
    questions: List[str] = field(default_factory=list)
    methods_summary: str = ""
    findings: List[Dict[str, str]] = field(default_factory=list)
    recommendations: List[str] = field(default_factory=list)
    limitations: List[str] = field(default_factory=list)
    appendix_links: List[str] = field(default_factory=list)


class ResearchPlanner:
    """研究规划器

    提供从利益相关者请求到结构化研究计划的完整流程，
    包括请求诊断、问题转化、方法推荐和计划构建。

    用法示例::

        planner = ResearchPlanner("旅行平台")
        planner.set_stakeholder("产品VP")
        planner.add_question(
            original="用户满意吗？",
            refined="平台用户的整体满意度(7点量表)是否高于行业基准5.2？",
            decision="是否需要启动体验优化专项",
            method="csat",
        )
        methods = planner.recommend_method("用户满意度如何？", "post_launch")
        diagnosis = planner.diagnose_request("帮我证明新首页设计更好")
        plan = planner.build()
        print(ResearchPlanner.render_markdown(plan))
    """

    def __init__(self, product: str):
        """初始化研究规划器。

        Args:
            product: 产品名称。
        """
        self._product = product
        self._stakeholder = ""
        self._questions: List[ResearchQuestion] = []
        self._methods: List[str] = []
        self._data_sources: List[str] = []
        self._timeline = ""
        self._sample_strategy = ""
        self._deliverable_preview = ""

    def set_stakeholder(self, name: str) -> None:
        """设置利益相关者名称或角色。

        Args:
            name: 利益相关者名称，如 "产品经理"、"VP of Product"。
        """
        self._stakeholder = name

    def add_question(
        self,
        original: str,
        refined: str = "",
        decision: str = "",
        method: str = "",
    ) -> ResearchQuestion:
        """添加一条研究问题。

        将利益相关者的原始问题转化为可研究的问题，并关联决策点和方法。

        Args:
            original: 利益相关者的原始问题。
            refined: 转化后的研究问题，若为空则使用原始问题。
            decision: 回答此问题将影响什么决策。
            method: 推荐的研究方法。

        Returns:
            创建的 ResearchQuestion 实例。

        用法示例::

            q = planner.add_question(
                original="新功能好不好？",
                refined="新功能上线后核心任务完成率是否提升？",
                decision="是否继续迭代该功能",
                method="ab_test",
            )
        """
        rq = ResearchQuestion(
            original_question=original,
            refined_question=refined or original,
            decision_point=decision,
            method=method,
        )
        self._questions.append(rq)
        if method and method not in self._methods:
            self._methods.append(method)
        return rq

    def diagnose_request(self, request: str) -> StakeholderDiagnosis:
        """诊断利益相关者请求。

        使用6个标准诊断问题逐一评估请求的质量，识别常见问题
        （如验证性研究、无决策标准、非用户中心等），并生成建议。

        6个诊断问题:
        1. 是否以用户为中心？
        2. 回答此问题会影响什么决策？
        3. 需要什么级别的精确度？
        4. 已有什么相关数据？
        5. 时间和资源约束？
        6. 机会成本是什么？

        Args:
            request: 利益相关者的原始请求文本。

        Returns:
            StakeholderDiagnosis 诊断结果。

        用法示例::

            diag = planner.diagnose_request("帮我证明新设计更好")
            print(diag.is_user_centered)  # False
            print(diag.recommendation)
        """
        request_lower = request.lower()

        # 1. 是否以用户为中心？
        user_keywords = ["用户", "客户", "体验", "满意", "使用", "完成", "user"]
        is_user_centered = any(kw in request_lower for kw in user_keywords)

        # 2. 决策点评估
        validation_keywords = ["证明", "验证", "confirm", "prove", "证实"]
        has_validation_bias = any(kw in request_lower for kw in validation_keywords)
        if has_validation_bias:
            decision_point = "⚠️ 疑似验证性研究 — 请求预设了结论，建议重新框定为开放式问题"
        else:
            decision_point = "待明确 — 请与利益相关者确认具体决策点"

        # 3. 精确度级别
        precise_keywords = ["精确", "具体数值", "百分比", "提升多少", "量化", "precise"]
        precision_level = "precise" if any(
            kw in request_lower for kw in precise_keywords
        ) else "directional"

        # 4. 已有数据（默认标记为待收集）
        existing_data = ["待收集 — 请确认是否有历史日志、调查数据或竞品分析"]

        # 5-6. 机会成本
        opportunity_cost = "待评估 — 请确认团队当前的优先级和资源分配"

        # 生成综合建议
        issues: List[str] = []
        if not is_user_centered:
            issues.append("请求未明确以用户为中心，建议从用户行为或态度角度重新表述")
        if has_validation_bias:
            issues.append(
                "请求带有验证偏差（预设结论），这是常见的利益相关者问题之一。"
                "建议将问题改为：'新设计对用户指标X的影响是什么？'"
            )
        if precision_level == "directional":
            issues.append("当前精确度为方向性，若需精确数值请考虑更大样本量或更严格的实验设计")

        if issues:
            recommendation = "诊断发现以下问题：\n" + "\n".join(
                f"  {i + 1}. {issue}" for i, issue in enumerate(issues)
            )
        else:
            recommendation = "请求质量良好，可直接进入研究设计阶段。"

        return StakeholderDiagnosis(
            original_request=request,
            is_user_centered=is_user_centered,
            decision_point=decision_point,
            precision_level=precision_level,
            existing_data=existing_data,
            opportunity_cost=opportunity_cost,
            recommendation=recommendation,
        )

    def recommend_method(
        self, question: str, lifecycle_stage: str = "post_launch"
    ) -> List[str]:
        """根据问题和产品生命周期阶段推荐研究方法。

        基于 config.LIFECYCLE_METHODS 中定义的阶段-方法映射，
        结合问题关键词智能推荐最合适的方法组合。

        Args:
            question: 研究问题文本。
            lifecycle_stage: 产品生命周期阶段，可选值见 config.LIFECYCLE_STAGES。
                            默认为 "post_launch"。

        Returns:
            推荐的方法列表，按相关性排序。

        Raises:
            ValueError: 当 lifecycle_stage 不在合法范围内时。

        用法示例::

            methods = planner.recommend_method(
                "用户对新功能的满意度如何？",
                lifecycle_stage="post_launch",
            )
            # ['csat', 'experience_sampling', 'logs_analysis', 'ab_test']
        """
        if lifecycle_stage not in LIFECYCLE_STAGES:
            raise ValueError(
                f"未知生命周期阶段: {lifecycle_stage}，可选: {LIFECYCLE_STAGES}"
            )

        stage_methods = list(LIFECYCLE_METHODS.get(lifecycle_stage, []))
        question_lower = question.lower()

        # 基于问题关键词调整排序
        keyword_method_map = {
            "满意": "csat",
            "satisfaction": "csat",
            "对比": "ab_test",
            "比较": "ab_test",
            "优先级": "maxdiff",
            "排序": "maxdiff",
            "偏好": "conjoint",
            "行为": "logs_analysis",
            "路径": "logs_analysis",
            "日志": "logs_analysis",
            "完成率": "ab_test",
            "转化": "ab_test",
            "留存": "logs_analysis",
            "调查": "survey",
        }

        boosted: List[str] = []
        for keyword, method in keyword_method_map.items():
            if keyword in question_lower and method not in boosted:
                boosted.append(method)

        # 合并：优先推荐关键词匹配的方法，再补充阶段默认方法
        result: List[str] = []
        for m in boosted:
            if m in RESEARCH_METHODS:
                result.append(m)
        for m in stage_methods:
            if m not in result:
                result.append(m)

        return result if result else list(stage_methods)

    def build(self) -> ResearchPlan:
        """构建研究计划。

        将已设置的所有信息汇总为一个 ResearchPlan 实例。

        Returns:
            构建完成的 ResearchPlan。

        用法示例::

            plan = planner.build()
            print(plan.title)
        """
        # 自动收集所有问题中使用的方法
        all_methods = list(self._methods)
        for q in self._questions:
            if q.method and q.method not in all_methods:
                all_methods.append(q.method)

        title = self._deliverable_preview or f"{self._product} 量化用户体验研究计划"

        return ResearchPlan(
            title=title,
            stakeholder=self._stakeholder,
            product=self._product,
            questions=list(self._questions),
            methods=all_methods,
            data_sources=list(self._data_sources),
            timeline=self._timeline or "待确定",
            sample_strategy=self._sample_strategy or "待确定",
            deliverable_preview=self._deliverable_preview or "待确定",
        )

    @staticmethod
    def render_markdown(plan: ResearchPlan) -> str:
        """将研究计划渲染为 Markdown 格式。

        Args:
            plan: ResearchPlan 实例。

        Returns:
            格式化的 Markdown 字符串。

        用法示例::

            md = ResearchPlanner.render_markdown(plan)
            print(md)
        """
        lines = [f"# {plan.title}\n"]
        lines.append(f"**产品:** {plan.product}  ")
        lines.append(f"**利益相关者:** {plan.stakeholder}  ")
        lines.append(f"**时间安排:** {plan.timeline}  ")
        lines.append(f"**抽样策略:** {plan.sample_strategy}\n")

        # 研究问题
        lines.append("## 研究问题\n")
        if plan.questions:
            lines.append("| # | 原始问题 | 研究问题 | 决策点 | 方法 |")
            lines.append("|---|---------|---------|--------|------|")
            for i, q in enumerate(plan.questions, 1):
                lines.append(
                    f"| {i} | {q.original_question} | {q.refined_question} "
                    f"| {q.decision_point} | {q.method} |"
                )
        else:
            lines.append("（尚未定义研究问题）")
        lines.append("")

        # 研究方法
        lines.append("## 研究方法\n")
        if plan.methods:
            for m in plan.methods:
                lines.append(f"- {m}")
        else:
            lines.append("（尚未确定方法）")
        lines.append("")

        # 数据来源
        lines.append("## 数据来源\n")
        if plan.data_sources:
            for ds in plan.data_sources:
                lines.append(f"- {ds}")
        else:
            lines.append("（尚未确定数据来源）")
        lines.append("")

        # 交付物预览
        lines.append("## 交付物预览\n")
        lines.append(plan.deliverable_preview or "（待确定）")
        lines.append("")

        return "\n".join(lines)


class ReportBuilder:
    """研究报告构建器

    按照书中推荐的报告结构构建量化UX研究报告：
    执行摘要 → 研究问题 → 方法概述 → 关键发现 → 建议 → 局限性 → 附录。

    报告原则（来自 config.REPORT_PRINCIPLES）：
    - short_and_focused: 简短聚焦
    - minimally_technical: 最小化技术术语
    - unbiased: 无偏呈现
    - reproducible: 可复现

    用法示例::

        rb = ReportBuilder("Q3 用户满意度追踪报告")
        rb.set_executive_summary("整体满意度维持在5.4/7，与上季度持平。")
        rb.add_question("Q3的用户满意度是否有显著变化？")
        rb.set_methods("HaTS产品内调查，7点量表，N=2,340")
        rb.add_finding("整体满意度稳定", "均值5.4，95%CI [5.3, 5.5]，与Q2无显著差异。")
        rb.add_finding("移动端满意度下降", "移动端均值从5.2降至4.8，差异显著(p<0.05)。")
        rb.add_recommendation("优先调查移动端满意度下降原因。")
        rb.add_limitation("调查响应率为12%，可能存在自选择偏差。")
        report = rb.build()
        print(ReportBuilder.render_markdown(report))
    """

    def __init__(self, title: str):
        """初始化报告构建器。

        Args:
            title: 报告标题。
        """
        self._title = title
        self._executive_summary = ""
        self._questions: List[str] = []
        self._methods_summary = ""
        self._findings: List[Dict[str, str]] = []
        self._recommendations: List[str] = []
        self._limitations: List[str] = []
        self._appendix_links: List[str] = []

    def set_executive_summary(self, summary: str) -> None:
        """设置执行摘要。

        执行摘要应为1段简洁文字，概括核心发现和建议，
        供高层快速了解结论。

        Args:
            summary: 执行摘要文本。
        """
        self._executive_summary = summary

    def add_question(self, question: str) -> None:
        """添加一条研究问题。

        Args:
            question: 研究问题文本。
        """
        self._questions.append(question)

    def set_methods(self, methods: str) -> None:
        """设置方法概述。

        Args:
            methods: 方法概述文本，包括研究设计、样本量、时间范围等。
        """
        self._methods_summary = methods

    def add_finding(self, title: str, description: str) -> None:
        """添加一条关键发现。

        Args:
            title: 发现的标题，简洁概括。
            description: 发现的详细描述，包含数据和统计结果。
        """
        self._findings.append({"title": title, "description": description})

    def add_recommendation(self, rec: str) -> None:
        """添加一条建议。

        Args:
            rec: 建议文本，应具有可操作性。
        """
        self._recommendations.append(rec)

    def add_limitation(self, limitation: str) -> None:
        """添加一条局限性说明。

        Args:
            limitation: 局限性描述。
        """
        self._limitations.append(limitation)

    def build(self) -> ResearchReport:
        """构建研究报告。

        Returns:
            构建完成的 ResearchReport 实例。

        用法示例::

            report = rb.build()
            print(report.title)
        """
        return ResearchReport(
            title=self._title,
            executive_summary=self._executive_summary,
            questions=list(self._questions),
            methods_summary=self._methods_summary,
            findings=list(self._findings),
            recommendations=list(self._recommendations),
            limitations=list(self._limitations),
            appendix_links=list(self._appendix_links),
        )

    @staticmethod
    def render_markdown(report: ResearchReport) -> str:
        """将研究报告渲染为 Markdown 格式。

        按照书中推荐的报告结构输出：
        1. 执行摘要（1段）
        2. 研究问题
        3. 方法概述
        4. 关键发现（每个配图表描述）
        5. 建议
        6. 局限性
        7. 附录

        Args:
            report: ResearchReport 实例。

        Returns:
            格式化的 Markdown 字符串。

        用法示例::

            md = ReportBuilder.render_markdown(report)
            print(md)
        """
        lines = [f"# {report.title}\n"]

        # 1. 执行摘要
        lines.append("## 执行摘要\n")
        lines.append(report.executive_summary or "（待撰写）")
        lines.append("")

        # 2. 研究问题
        lines.append("## 研究问题\n")
        if report.questions:
            for i, q in enumerate(report.questions, 1):
                lines.append(f"{i}. {q}")
        else:
            lines.append("（未列出研究问题）")
        lines.append("")

        # 3. 方法概述
        lines.append("## 方法概述\n")
        lines.append(report.methods_summary or "（待撰写）")
        lines.append("")

        # 4. 关键发现
        lines.append("## 关键发现\n")
        if report.findings:
            for i, f in enumerate(report.findings, 1):
                lines.append(f"### 发现 {i}: {f.get('title', '')}\n")
                lines.append(f.get("description", ""))
                lines.append("")
        else:
            lines.append("（暂无发现）")
            lines.append("")

        # 5. 建议
        lines.append("## 建议\n")
        if report.recommendations:
            for i, rec in enumerate(report.recommendations, 1):
                lines.append(f"{i}. {rec}")
        else:
            lines.append("（暂无建议）")
        lines.append("")

        # 6. 局限性
        lines.append("## 局限性\n")
        if report.limitations:
            for lim in report.limitations:
                lines.append(f"- {lim}")
        else:
            lines.append("（未列出局限性）")
        lines.append("")

        # 7. 附录
        lines.append("## 附录\n")
        if report.appendix_links:
            for link in report.appendix_links:
                lines.append(f"- {link}")
        else:
            lines.append("（无附录）")
        lines.append("")

        return "\n".join(lines)
