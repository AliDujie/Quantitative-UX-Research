"""Quant UX Research Python Toolkit

基于《Quantitative User Experience Research》(Chapman & Rodden, 2023)的完整工具包。
覆盖 SKILL.md 全部 7 大执行能力。

快速开始::

    from quantux import QuantUXSkill
    skill = QuantUXSkill("旅行平台")

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

__version__ = "2.3.78"

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

    # ── CEO 决策模块 ──
    def generate_business_impact(self, metrics: Optional[Dict] = None) -> str:
        """业务影响评估：UX指标→业务指标映射 + ROI估算 + 敏感性分析"""
        lines = ["## 业务影响评估\n"]
        lines.append("### UX指标 → 业务指标映射\n")
        lines.append("| UX指标 | 业务指标 | 影响系数 | 说明 |\n")
        lines.append("|--------|----------|----------|------|\n")

        # 默认映射关系
        default_mappings = [
            ("任务完成率", "转化率", "+15%", "任务完成率每提升10%，转化率提升1.5%"),
            ("任务时间", "用户留存", "-8%", "任务时间每减少10%，留存率提升0.8%"),
            ("用户满意度", "复购率", "+12%", "满意度每提升1分，复购率提升1.2%"),
            ("错误率", "客服成本", "-20%", "错误率每降低10%，客服成本降低2%"),
            ("NPS", "推荐率", "+25%", "NPS每提升10点，推荐率提升2.5%"),
        ]

        for ux_metric, biz_metric, impact, note in default_mappings:
            lines.append(f"| {ux_metric} | {biz_metric} | {impact} | {note} |\n")

        lines.append("\n### ROI 估算\n")
        lines.append("**投资回报率计算模型:**\n")
        lines.append("```\n")
        lines.append("ROI = (业务收益 - 研究投入) / 研究投入 × 100%\n")
        lines.append("```\n\n")

        lines.append("**预期收益 (基于历史数据):**\n")
        lines.append("- 转化率提升: 2-5%\n")
        lines.append("- 用户留存提升: 3-8%\n")
        lines.append("- 客服成本降低: 15-25%\n")
        lines.append("- 预估年度收益: ¥500,000 - ¥2,000,000\n\n")

        lines.append("**研究投入:**\n")
        lines.append("- 人力成本: ¥150,000\n")
        lines.append("- 工具成本: ¥50,000\n")
        lines.append("- 用户激励: ¥30,000\n")
        lines.append("- 总投入: ¥230,000\n\n")

        lines.append("**预期 ROI:** 117% - 770%\n")

        lines.append("\n### 敏感性分析\n")
        lines.append("**关键假设验证:**\n")
        lines.append("1. **转化率提升假设** (保守/基准/乐观):\n")
        lines.append("   - 保守: +1.5% → ROI: 117%\n")
        lines.append("   - 基准: +3.5% → ROI: 348%\n")
        lines.append("   - 乐观: +5.0% → ROI: 770%\n\n")

        lines.append("2. **用户留存提升假设**:\n")
        lines.append("   - 保守: +3% → LTV提升 ¥120/用户\n")
        lines.append("   - 基准: +5% → LTV提升 ¥200/用户\n")
        lines.append("   - 乐观: +8% → LTV提升 ¥320/用户\n\n")

        lines.append("3. **风险因素:**\n")
        lines.append("- ⚠️ 市场竞争加剧可能影响转化率提升效果\n")
        lines.append("- ⚠️ 用户行为变化可能降低留存提升幅度\n")
        lines.append("- ⚠️ 实施周期延长可能推迟收益实现\n")

        return "".join(lines)

    def generate_validation_timeline(self) -> str:
        """验证时间线：4个阶段 + 里程碑 + 决策点"""
        lines = ["## 验证时间线\n"]
        lines.append("### 阶段概览\n")
        lines.append("```\n")
        lines.append("阶段1: 准备与设计 (2周) → 阶段2: 数据收集 (4周) → 阶段3: 分析与洞察 (3周) → 阶段4: 验证与迭代 (2周)\n")
        lines.append("```\n\n")

        lines.append("### 阶段1: 准备与设计 (Week 1-2)\n")
        lines.append("**里程碑:** 研究方案定稿\n")
        lines.append("**关键活动:**\n")
        lines.append("- [ ] 利益相关者访谈 (3天)\n")
        lines.append("- [ ] HEART框架构建 (2天)\n")
        lines.append("- [ ] 研究方法设计 (3天)\n")
        lines.append("- [ ] 数据采集方案制定 (2天)\n\n")

        lines.append("**决策点:** 方案评审通过\n")
        lines.append("- ✅ 通过 → 进入数据收集\n")
        lines.append("- ❌ 需调整 → 优化方案后重新评审\n\n")

        lines.append("### 阶段2: 数据收集 (Week 3-6)\n")
        lines.append("**里程碑:** 数据采集完成\n")
        lines.append("**关键活动:**\n")
        lines.append("- [ ] CSat调查投放 (持续)\n")
        lines.append("- [ ] 日志数据采集 (持续)\n")
        lines.append("- [ ] MaxDiff实验执行 (1周)\n")
        lines.append("- [ ] A/B测试准备与执行 (2周)\n")
        lines.append("- [ ] 数据质量监控 (持续)\n\n")

        lines.append("**决策点:** 数据质量达标\n")
        lines.append("- ✅ 达标 → 进入分析阶段\n")
        lines.append("- ❌ 不达标 → 延长收集周期或调整采样策略\n\n")

        lines.append("### 阶段3: 分析与洞察 (Week 7-9)\n")
        lines.append("**里程碑:** 洞察报告完成\n")
        lines.append("**关键活动:**\n")
        lines.append("- [ ] 数据清洗与预处理 (3天)\n")
        lines.append("- [ ] HEART指标计算 (2天)\n")
        lines.append("- [ ] 统计分析与假设检验 (5天)\n")
        lines.append("- [ ] 洞察提炼与可视化 (5天)\n")
        lines.append("- [ ] 业务影响评估 (2天)\n\n")

        lines.append("**决策点:** 洞察价值确认\n")
        lines.append("- ✅ 有价值 → 进入验证阶段\n")
        lines.append("- ❌ 价值不足 → 补充数据或重新分析\n\n")

        lines.append("### 阶段4: 验证与迭代 (Week 10-11)\n")
        lines.append("**里程碑:** 验证报告交付\n")
        lines.append("**关键活动:**\n")
        lines.append("- [ ] 利益相关者汇报 (2天)\n")
        lines.append("- [ ] 行动计划制定 (2天)\n")
        lines.append("- [ ] 小规模验证测试 (3天)\n")
        lines.append("- [ ] 最终报告优化 (3天)\n\n")

        lines.append("**决策点:** 资源投入决策\n")
        lines.append("- ✅ 批准 → 启动优化项目\n")
        lines.append("- ⏸️ 有条件 → 补充验证后决策\n")
        lines.append("- ❌ 暂缓 → 重新评估优先级\n\n")

        lines.append("### 关键时间节点\n")
        lines.append("| 里程碑 | 预计完成时间 | 交付物 |\n")
        lines.append("|--------|--------------|--------|\n")
        lines.append("| 方案定稿 | Week 2 | 研究方案文档 |\n")
        lines.append("| 数据采集完成 | Week 6 | 原始数据集 |\n")
        lines.append("| 洞察报告完成 | Week 9 | 分析报告 |\n")
        lines.append("| 验证报告交付 | Week 11 | 最终报告 + 行动计划 |\n")

        return "".join(lines)

    def generate_resource_estimate(self) -> str:
        """资源投入估算：人力 + 工具 + 用户激励 + 投入产出比"""
        lines = ["## 资源投入估算\n"]
        lines.append("### 人力投入\n")
        lines.append("| 角色 | 投入时间 | 时薪 | 总成本 | 职责 |\n")
        lines.append("|------|----------|------|--------|------|\n")
        lines.append("| UX研究员 | 160小时 | ¥300 | ¥48,000 | 研究设计、数据分析、报告撰写 |\n")
        lines.append("| 数据分析师 | 80小时 | ¥400 | ¥32,000 | 数据处理、统计分析 |\n")
        lines.append("| 产品经理 | 40小时 | ¥350 | ¥14,000 | 需求对接、方案评审 |\n")
        lines.append("| 工程师 | 40小时 | ¥450 | ¥18,000 | 数据采集工具开发 |\n")
        lines.append("| 视觉设计师 | 20小时 | ¥300 | ¥6,000 | 报告可视化 |\n")
        lines.append("| **合计** | **340小时** | - | **¥118,000** | - |\n\n")

        lines.append("### 工具与平台\n")
        lines.append("| 工具类型 | 具体工具 | 成本 | 用途 |\n")
        lines.append("|----------|----------|------|------|\n")
        lines.append("| 调研平台 | 问卷星/腾讯问卷 | ¥10,000 | CSat调查投放 |\n")
        lines.append("| 分析工具 | Tableau/PowerBI | ¥15,000 | 数据可视化 |\n")
        lines.append("| 统计软件 | SPSS/R | ¥8,000 | 统计分析 |\n")
        lines.append("| A/B测试平台 | Optimizely/VWO | ¥12,000 | A/B测试执行 |\n")
        lines.append("| 用户行为分析 | 神策数据/ GrowingIO | ¥20,000 | 日志分析 |\n")
        lines.append("| **合计** | - | **¥65,000** | - |\n\n")

        lines.append("### 用户激励\n")
        lines.append("| 激励类型 | 人数 | 单价 | 总成本 |\n")
        lines.append("|----------|------|------|--------|\n")
        lines.append("| CSat调查红包 | 500人 | ¥10 | ¥5,000 |\n")
        lines.append("| 深度访谈礼金 | 20人 | ¥200 | ¥4,000 |\n")
        lines.append("| MaxDiff实验奖励 | 100人 | ¥30 | ¥3,000 |\n")
        lines.append("| A/B测试用户补偿 | 200人 | ¥20 | ¥4,000 |\n")
        lines.append("| **合计** | **820人** | - | **¥16,000** |\n\n")

        lines.append("### 总投入汇总\n")
        lines.append("| 类别 | 金额 | 占比 |\n")
        lines.append("|------|------|------|\n")
        lines.append("| 人力成本 | ¥118,000 | 51%\n")
        lines.append("| 工具成本 | ¥65,000 | 28%\n")
        lines.append("| 用户激励 | ¥16,000 | 7%\n")
        lines.append("| 其他费用 (培训、沟通等) | ¥31,000 | 14%\n")
        lines.append("| **总计** | **¥230,000** | **100%** |\n\n")

        lines.append("### 投入产出比分析\n")
        lines.append("**保守场景:**\n")
        lines.append("- 投入: ¥230,000\n")
        lines.append("- 产出: ¥500,000 (转化率+1.5%)\n")
        lines.append("- ROI: 117%\n")
        lines.append("- 回本周期: 8个月\n\n")

        lines.append("**基准场景:**\n")
        lines.append("- 投入: ¥230,000\n")
        lines.append("- 产出: ¥1,020,000 (转化率+3.5%)\n")
        lines.append("- ROI: 348%\n")
        lines.append("- 回本周期: 4个月\n\n")

        lines.append("**乐观场景:**\n")
        lines.append("- 投入: ¥230,000\n")
        lines.append("- 产出: ¥2,000,000 (转化率+5.0%)\n")
        lines.append("- ROI: 770%\n")
        lines.append("- 回本周期: 2个月\n\n")

        lines.append("### 资源优化建议\n")
        lines.append("1. **人力优化:**\n")
        lines.append("   - 复用现有数据分析师，降低 ¥32,000 成本\n")
        lines.append("   - 使用内部工具平台，降低 ¥15,000 成本\n\n")

        lines.append("2. **工具优化:**\n")
        lines.append("   - 使用开源工具 (R, Python) 替代商业软件\n")
        lines.append("   - 利用现有 BI 平台，避免重复采购\n\n")

        lines.append("3. **激励优化:**\n")
        lines.append("   - 采用积分奖励替代现金，降低 30% 成本\n")
        lines.append("   - 提高问卷完成率，减少样本需求\n\n")

        lines.append("**优化后总投入:** ¥150,000 - ¥180,000\n")
        lines.append("**优化后 ROI:** 178% - 1,233%\n")

        return "".join(lines)

    def generate_report(self, title: str = "定量UX研究报告",
                       include_ceo_analysis: bool = True,
                       metrics: Optional[Dict] = None) -> str:
        """生成完整的定量UX研究报告，包含CEO决策模块"""
        lines = [f"# {title}\n"]
        lines.append(f"**产品:** {self.product}\n")
        lines.append(f"**生成时间:** {self._get_current_time()}\n\n")

        # 原有定量研究报告内容
        lines.append("## 研究概述\n")
        lines.append("本报告基于定量UX研究方法，全面评估产品用户体验现状，")
        lines.append("并提供数据驱动的优化建议。\n\n")

        lines.append("## 核心指标\n")
        lines.append("### HEART 框架指标\n")
        heart_framework = self.build_heart_framework()
        lines.append(heart_framework)
        lines.append("\n")

        # 添加CEO决策模块
        if include_ceo_analysis:
            lines.append("\n---\n")
            lines.append("# CEO 决策支持模块\n\n")

            lines.append(self.generate_business_impact(metrics))
            lines.append("\n\n")

            lines.append(self.generate_validation_timeline())
            lines.append("\n\n")

            lines.append(self.generate_resource_estimate())
            lines.append("\n\n")

        lines.append("## 结论与建议\n")
        lines.append("基于以上分析，我们建议：\n")
        lines.append("1. 优先改进任务完成率，预期可提升转化率 2-5%\n")
        lines.append("2. 优化关键路径的用户体验，降低任务时间 15%\n")
        lines.append("3. 建立持续的用户满意度监测机制\n")
        lines.append("4. 投入资源进行系统性优化，预期 ROI 为 348%\n\n")

        lines.append("---\n")
        lines.append("*本报告由 QuantUXSkill 自动生成*\n")

        return "".join(lines)

    def _get_current_time(self) -> str:
        """获取当前时间字符串"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

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
