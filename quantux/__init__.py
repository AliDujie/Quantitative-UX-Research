"""Quant UX Research Python Toolkit

基于《Quantitative User Experience Research》(Chapman & Rodden, 2023)的完整工具包。
覆盖 SKILL.md 全部 7 大执行能力。

快速开始::

    from quantux import QuantUXSkill
    skill = QuantUXSkill("飞猪旅行")

    # 能力1: HEART框架
    heart = skill.build_heart_framework()

    # 能力2: CSat调查
    survey_md = skill.design_csat_survey("2024Q1满意度")

    # 能力3: 日志序列分析
    skill.logs_analyzer.add_event("u1", "2024-01-01 10:00", "首页")

    # 能力4: MaxDiff设计
    design_md = skill.design_maxdiff("功能优先级", ["快速搜索", "价格对比", "评价可信"])

    # 能力5: A/B测试
    n = skill.calculate_ab_sample_size(0.35, 0.03)

    # 能力6: 研究规划
    diagnosis = skill.diagnose_request("验证我们的新设计方向")

    # 能力7: 研究报告
    report_md = skill.build_report("用户满意度研究")
"""

__version__ = "2.0.0"

from .config import AnalysisConfig, HEART_DIMENSIONS, HEART_LABELS, KNOWLEDGE_FILES
from .utils import load_knowledge, load_all_knowledge, search_knowledge
from .templates import (
    HEART_WORKSHOP_TEMPLATE, GSM_TABLE_TEMPLATE,
    CSAT_SURVEY_TEMPLATE, CSAT_REPORT_TEMPLATE,
    MAXDIFF_DESIGN_TEMPLATE, AB_TEST_PLAN_TEMPLATE,
    RESEARCH_REPORT_TEMPLATE, STAKEHOLDER_DIAGNOSIS_QUESTIONS,
    DATA_QUALITY_CHECKLIST,
)
from .heart import HEARTBuilder, HEARTFramework, GoalItem, SignalItem, MetricItem
from .csat import CSatSurveyBuilder, CSatAnalyzer, CSatSurvey, CSatAnalysis, CSatDataPoint
from .maxdiff import MaxDiffDesigner, MaxDiffAnalyzer, MaxDiffDesign, MaxDiffAnalysis
from .abtest import ABTestPlanner, ABTestAnalyzer, ABTestDesign, ABTestResult
from .research import ResearchPlanner, ReportBuilder, ResearchPlan, ResearchReport
from .logs import LogsAnalyzer, SessionSequence, SequenceFrequency, TransitionMatrix

from typing import Dict, List, Optional


class QuantUXSkill:
    """Quant UX 统一入口类 — 封装全部 7 大执行能力"""

    def __init__(self, product_name: str, config: Optional[AnalysisConfig] = None):
        self.product = product_name
        self.config = config or AnalysisConfig()
        self.heart_builder = HEARTBuilder(product_name)
        self.csat_analyzer = CSatAnalyzer(product_name)
        self.logs_analyzer = LogsAnalyzer()
        self.research_planner = ResearchPlanner(product_name)

    # ── 能力1: HEART框架 ──
    def build_heart_framework(self) -> str:
        framework = self.heart_builder.build()
        return HEARTBuilder.render_markdown(framework)

    def get_workshop_guide(self) -> str:
        return self.heart_builder.render_workshop_guide()

    # ── 能力2: CSat调查 ──
    def design_csat_survey(self, title: str, mechanism: str = "email",
                           target: str = "") -> str:
        builder = CSatSurveyBuilder(title, mechanism)
        builder.set_product(self.product)
        if target:
            builder.set_target(target)
        builder.add_satisfaction_rating()
        builder.add_open_ended()
        survey = builder.build()
        return CSatSurveyBuilder.render_markdown(survey)

    def analyze_csat(self, period: str, sample_size: int,
                     ratings: Dict[int, int]) -> str:
        self.csat_analyzer.add_data_point(period, sample_size, ratings)
        return self.csat_analyzer.generate_report()

    # ── 能力3: 日志序列分析 ──
    def analyze_logs(self) -> str:
        return self.logs_analyzer.render_markdown()

    # ── 能力4: MaxDiff ──
    def design_maxdiff(self, title: str, items: List[str],
                       items_per_screen: int = 4) -> str:
        designer = MaxDiffDesigner(title)
        designer.add_items(items)
        designer.set_display_params(items_per_screen=items_per_screen)
        design = designer.build()
        return MaxDiffDesigner.render_markdown(design)

    # ── 能力5: A/B测试 ──
    def calculate_ab_sample_size(self, baseline: float, mde: float) -> int:
        planner = ABTestPlanner(f"{self.product} A/B测试")
        return planner.calculate_sample_size(baseline, mde)

    def analyze_ab_test(self, name_a: str, n_a: int, conv_a: int,
                        name_b: str, n_b: int, conv_b: int) -> str:
        analyzer = ABTestAnalyzer(f"{self.product} A/B测试")
        analyzer.set_variant_a(name_a, n_a, conv_a)
        analyzer.set_variant_b(name_b, n_b, conv_b)
        result = analyzer.analyze()
        return ABTestAnalyzer.render_markdown(result)

    # ── 能力6: 研究规划 ──
    def diagnose_request(self, request: str) -> str:
        diag = self.research_planner.diagnose_request(request)
        lines = [f"# 利益相关者请求诊断\n"]
        lines.append(f"**原始请求:** {diag.original_request}")
        lines.append(f"**以用户为中心:** {'✅ 是' if diag.is_user_centered else '❌ 否'}")
        lines.append(f"**决策点:** {diag.decision_point}")
        lines.append(f"**精确度需求:** {diag.precision_level}")
        lines.append(f"**机会成本:** {diag.opportunity_cost}")
        lines.append(f"\n**建议:** {diag.recommendation}")
        return "\n".join(lines)

    def plan_research(self) -> str:
        plan = self.research_planner.build()
        return ResearchPlanner.render_markdown(plan)

    # ── 能力7: 研究报告 ──
    def build_report(self, title: str) -> str:
        builder = ReportBuilder(title)
        report = builder.build()
        return ReportBuilder.render_markdown(report)

    # ── 知识库搜索 ──
    def search_knowledge(self, keyword: str) -> Dict[str, List[str]]:
        return search_knowledge(keyword)


__all__ = [
    "QuantUXSkill",
    "AnalysisConfig", "HEART_DIMENSIONS", "HEART_LABELS", "KNOWLEDGE_FILES",
    "load_knowledge", "load_all_knowledge", "search_knowledge",
    "HEARTBuilder", "HEARTFramework", "GoalItem", "SignalItem", "MetricItem",
    "CSatSurveyBuilder", "CSatAnalyzer", "CSatSurvey", "CSatAnalysis",
    "MaxDiffDesigner", "MaxDiffAnalyzer", "MaxDiffDesign", "MaxDiffAnalysis",
    "ABTestPlanner", "ABTestAnalyzer", "ABTestDesign", "ABTestResult",
    "ResearchPlanner", "ReportBuilder", "ResearchPlan", "ResearchReport",
    "LogsAnalyzer", "SessionSequence", "SequenceFrequency", "TransitionMatrix",
]
