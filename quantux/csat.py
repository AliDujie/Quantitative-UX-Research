"""CSat 调查设计与分析模块

对应执行能力：设计CSat问卷、分析CSat数据、生成CSat报告。
基于《Quantitative User Experience Research》第8章。
"""

from dataclasses import dataclass, field
from typing import Dict, List
import math

from .config import CSAT_MECHANISMS, CSAT_MECHANISM_LABELS


@dataclass
class CSatQuestion:
    """单个CSat问卷题目"""
    question_type: str  # "rating", "open_ended", "demographic", "behavioral"
    text: str
    scale_points: int = 5
    options: List[str] = field(default_factory=list)
    required: bool = True


@dataclass
class CSatSurvey:
    """完整CSat问卷"""
    title: str
    mechanism: str
    product: str = ""
    target_population: str = ""
    questions: List[CSatQuestion] = field(default_factory=list)
    estimated_time: str = ""
    closing_text: str = "感谢您的参与！您的反馈将帮助我们改进产品。"


@dataclass
class CSatDataPoint:
    """单期CSat数据"""
    period: str
    sample_size: int
    ratings: Dict[int, int] = field(default_factory=dict)
    top2box: float = 0.0
    ci_lower: float = 0.0
    ci_upper: float = 0.0


@dataclass
class CSatAnalysis:
    """CSat分析结果"""
    product_name: str
    data_points: List[CSatDataPoint] = field(default_factory=list)
    key_findings: List[str] = field(default_factory=list)
    recommendations: List[str] = field(default_factory=list)


class CSatSurveyBuilder:
    """CSat问卷构建器

    用法示例::

        builder = CSatSurveyBuilder("2024Q1满意度调查", "email")
        builder.set_product("飞猪旅行")
        builder.set_target("过去30天内使用过飞猪的用户")
        builder.add_satisfaction_rating()
        builder.add_open_ended()
        survey = builder.build()
        print(CSatSurveyBuilder.render_markdown(survey))
    """

    def __init__(self, title: str, mechanism: str = "email"):
        if mechanism not in CSAT_MECHANISMS:
            raise ValueError(f"未知调查方式: {mechanism}，可选: {CSAT_MECHANISMS}")
        self.title = title
        self.mechanism = mechanism
        self._product = ""
        self._target = ""
        self._questions: List[CSatQuestion] = []

    def set_product(self, product: str) -> "CSatSurveyBuilder":
        self._product = product
        return self

    def set_target(self, population: str) -> "CSatSurveyBuilder":
        self._target = population
        return self

    def add_satisfaction_rating(self, text: str = "", scale: int = 5) -> "CSatSurveyBuilder":
        product = self._product or "该产品"
        if not text:
            text = f"总体而言，你对{product}的满意程度如何？"
        self._questions.append(CSatQuestion(
            question_type="rating", text=text, scale_points=scale))
        return self

    def add_open_ended(self, text: str = "") -> "CSatSurveyBuilder":
        product = self._product or "该产品"
        if not text:
            text = f"请告诉我们，你对{product}最满意和最不满意的地方分别是什么？"
        self._questions.append(CSatQuestion(
            question_type="open_ended", text=text, required=False))
        return self

    def add_demographic(self, text: str, options: List[str]) -> "CSatSurveyBuilder":
        self._questions.append(CSatQuestion(
            question_type="demographic", text=text, options=options))
        return self

    def add_behavioral(self, text: str, options: List[str]) -> "CSatSurveyBuilder":
        self._questions.append(CSatQuestion(
            question_type="behavioral", text=text, options=options))
        return self

    def build(self) -> CSatSurvey:
        if not self._questions:
            self.add_satisfaction_rating()
            self.add_open_ended()
        q_count = len(self._questions)
        estimated = f"{max(2, q_count)}~{q_count * 2}分钟"
        return CSatSurvey(
            title=self.title, mechanism=self.mechanism,
            product=self._product, target_population=self._target,
            questions=self._questions, estimated_time=estimated)

    @staticmethod
    def render_markdown(survey: CSatSurvey) -> str:
        mech_label = CSAT_MECHANISM_LABELS.get(survey.mechanism, survey.mechanism)
        lines = [f"# {survey.title}\n"]
        lines.append(f"**调查方式:** {mech_label}")
        if survey.target_population:
            lines.append(f"**目标人群:** {survey.target_population}")
        lines.append(f"**预计时长:** {survey.estimated_time}\n")
        lines.append("---\n")

        type_labels = {"rating": "评分量表", "open_ended": "开放题",
                       "demographic": "人口统计", "behavioral": "行为信息"}
        for i, q in enumerate(survey.questions, 1):
            fmt = type_labels.get(q.question_type, q.question_type)
            if q.question_type == "rating":
                lines.append(f"**Q{i}. [{fmt} 1-{q.scale_points}]** {q.text}")
                mid = (q.scale_points + 1) // 2
                lines.append(f"   (1=非常不满意 / {mid}=一般 / {q.scale_points}=非常满意)")
            elif q.question_type == "open_ended":
                lines.append(f"**Q{i}. [{fmt}]** {q.text}")
                if not q.required:
                    lines.append("   *（选填）*")
            else:
                lines.append(f"**Q{i}. [{fmt}]** {q.text}")
                for opt in q.options:
                    lines.append(f"   - {opt}")
            lines.append("")

        lines.append("---")
        lines.append(f"\n{survey.closing_text}")
        return "\n".join(lines)


class CSatAnalyzer:
    """CSat数据分析器

    用法示例::

        analyzer = CSatAnalyzer("飞猪旅行")
        analyzer.add_data_point("2024Q1", 500, {1: 10, 2: 20, 3: 50, 4: 180, 5: 240})
        analyzer.add_data_point("2024Q2", 480, {1: 8, 2: 18, 3: 45, 4: 190, 5: 219})
        print(analyzer.generate_report())
    """

    def __init__(self, product_name: str, confidence: float = 0.95):
        self.product_name = product_name
        self.confidence = confidence
        self._z = 1.96 if confidence == 0.95 else 2.576 if confidence == 0.99 else 1.645
        self.analysis = CSatAnalysis(product_name=product_name)

    def add_data_point(self, period: str, sample_size: int,
                       ratings: Dict[int, int]) -> CSatDataPoint:
        total = sum(ratings.values())
        if total != sample_size:
            sample_size = total
        top2_keys = sorted(ratings.keys(), reverse=True)[:2]
        top2_count = sum(ratings.get(k, 0) for k in top2_keys)
        t2b = top2_count / total if total > 0 else 0.0
        se = math.sqrt(t2b * (1 - t2b) / total) if total > 0 else 0.0
        ci_lower = max(0.0, t2b - self._z * se)
        ci_upper = min(1.0, t2b + self._z * se)
        dp = CSatDataPoint(
            period=period, sample_size=sample_size, ratings=ratings,
            top2box=round(t2b, 4), ci_lower=round(ci_lower, 4),
            ci_upper=round(ci_upper, 4))
        self.analysis.data_points.append(dp)
        return dp

    def analyze_trend(self) -> str:
        dps = self.analysis.data_points
        if len(dps) < 2:
            return "数据点不足，无法分析趋势。"
        first, last = dps[0], dps[-1]
        diff = last.top2box - first.top2box
        ci_overlap = last.ci_lower <= first.ci_upper and first.ci_lower <= last.ci_upper
        if abs(diff) < 0.02 or ci_overlap:
            trend = "保持稳定"
            detail = f"Top-2-Box从 {first.top2box:.1%} 到 {last.top2box:.1%}，置信区间重叠，变化不显著。"
        elif diff > 0:
            trend = "上升趋势"
            detail = f"Top-2-Box从 {first.top2box:.1%} 上升到 {last.top2box:.1%}。"
        else:
            trend = "下降趋势"
            detail = f"Top-2-Box从 {first.top2box:.1%} 下降到 {last.top2box:.1%}。"
        return f"**趋势: {trend}**\n\n{detail}"

    def generate_report(self) -> str:
        a = self.analysis
        lines = [f"# CSat 分析报告 — {a.product_name}\n"]

        lines.append("## 数据概览\n")
        lines.append("| 期间 | 样本量 | Top-2-Box | 95% CI |")
        lines.append("|------|--------|-----------|--------|")
        for dp in a.data_points:
            lines.append(
                f"| {dp.period} | {dp.sample_size} | {dp.top2box:.1%} "
                f"| [{dp.ci_lower:.1%}, {dp.ci_upper:.1%}] |")
        lines.append("")

        if len(a.data_points) >= 2:
            lines.append("## 趋势分析\n")
            lines.append(self.analyze_trend())
            lines.append("")

        for dp in a.data_points:
            lines.append(f"### {dp.period} 评分分布\n")
            total = sum(dp.ratings.values())
            for score in sorted(dp.ratings.keys()):
                count = dp.ratings[score]
                pct = count / total * 100 if total > 0 else 0
                bar = "█" * int(pct / 2)
                lines.append(f"  {score}分: {bar} {pct:.1f}% (n={count})")
            lines.append("")

        if a.key_findings:
            lines.append("## 关键发现\n")
            for i, f in enumerate(a.key_findings, 1):
                lines.append(f"{i}. {f}")
            lines.append("")

        if a.recommendations:
            lines.append("## 建议\n")
            for i, r in enumerate(a.recommendations, 1):
                lines.append(f"{i}. {r}")
            lines.append("")

        lines.append("## CSat 常见问题诊断\n")
        for problem in self.get_common_problems():
            lines.append(f"- {problem}")

        return "\n".join(lines)

    @staticmethod
    def get_common_problems() -> List[str]:
        return [
            "过长的调查 → 保持极简，1-2个评分+1个开放式问题",
            "跨群体比较绝对值 → 在同一群体内跟踪时间变化",
            "文化差异影响评分 → 美国/印度偏高，德国/日本偏低",
            "驱动因素分析 → 多重共线性使回归困难，建议聚焦定性评估",
            "高管薪酬与CSat挂钩 → 设定'拥有健全倾听项目'的目标",
            "序数数据当连续数据 → 使用Top-2-Box而非均值",
        ]
