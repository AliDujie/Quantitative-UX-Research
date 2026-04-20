"""A/B 测试设计与分析模块

对应执行能力：实验设计、样本量计算、结果分析与解读。
基于《Quantitative User Experience Research》第5章。
"""

from dataclasses import dataclass, field
from typing import List
import math


@dataclass
class ABTestVariant:
    """实验变体"""
    name: str
    description: str = ""
    sample_size: int = 0
    conversions: int = 0
    metric_value: float = 0.0


@dataclass
class ABTestDesign:
    """A/B测试设计方案"""
    name: str
    hypothesis: str = ""
    user_definition: str = ""
    primary_metric: str = ""
    guardrail_metrics: List[str] = field(default_factory=list)
    variants: List[ABTestVariant] = field(default_factory=list)
    minimum_sample_size: int = 0
    estimated_duration: str = ""
    confounds: List[str] = field(default_factory=list)


@dataclass
class ABTestResult:
    """A/B测试分析结果"""
    variant_a: ABTestVariant = field(default_factory=lambda: ABTestVariant(name="A"))
    variant_b: ABTestVariant = field(default_factory=lambda: ABTestVariant(name="B"))
    rate_a: float = 0.0
    rate_b: float = 0.0
    absolute_diff: float = 0.0
    relative_diff: float = 0.0
    ci_lower: float = 0.0
    ci_upper: float = 0.0
    is_significant: bool = False
    p_value: float = 1.0


class ABTestPlanner:
    """A/B测试设计规划器

    用法示例::

        planner = ABTestPlanner("结账流程优化")
        planner.set_hypothesis("简化结账步骤将提高转化率")
        planner.set_user_definition("完成商品选择的登录用户")
        planner.set_primary_metric("结账完成率", baseline_rate=0.35)
        planner.add_guardrail_metric("页面加载时间")
        planner.add_variant("A-对照组", "当前3步结账流程")
        planner.add_variant("B-实验组", "新2步结账流程")
        n = planner.calculate_sample_size(0.35, 0.03)
        design = planner.build()
        print(ABTestPlanner.render_markdown(design))
    """

    def __init__(self, name: str):
        self.name = name
        self._hypothesis = ""
        self._user_def = ""
        self._primary_metric = ""
        self._baseline_rate = 0.0
        self._guardrails: List[str] = []
        self._variants: List[ABTestVariant] = []
        self._confounds: List[str] = []
        self._min_sample = 0

    def set_hypothesis(self, hypothesis: str) -> "ABTestPlanner":
        self._hypothesis = hypothesis
        return self

    def set_user_definition(self, definition: str) -> "ABTestPlanner":
        self._user_def = definition
        return self

    def set_primary_metric(self, metric: str, baseline_rate: float = 0.0) -> "ABTestPlanner":
        self._primary_metric = metric
        self._baseline_rate = baseline_rate
        return self

    def add_guardrail_metric(self, metric: str) -> "ABTestPlanner":
        self._guardrails.append(metric)
        return self

    def add_variant(self, name: str, description: str = "") -> ABTestVariant:
        v = ABTestVariant(name=name, description=description)
        self._variants.append(v)
        return v

    def add_confound(self, confound: str) -> "ABTestPlanner":
        self._confounds.append(confound)
        return self

    def calculate_sample_size(self, baseline_rate: float, mde: float,
                              alpha: float = 0.05, power: float = 0.8) -> int:
        """计算每组所需最小样本量。

        使用公式: n = (z_alpha + z_beta)^2 * 2 * p * (1-p) / mde^2
        """
        z_alpha = _z_score(1 - alpha / 2)
        z_beta = _z_score(power)
        p = baseline_rate
        n = ((z_alpha + z_beta) ** 2) * 2 * p * (1 - p) / (mde ** 2)
        self._min_sample = math.ceil(n)
        return self._min_sample

    def build(self) -> ABTestDesign:
        if not self._variants:
            self.add_variant("A-对照组", "当前版本")
            self.add_variant("B-实验组", "新版本")
        return ABTestDesign(
            name=self.name, hypothesis=self._hypothesis,
            user_definition=self._user_def, primary_metric=self._primary_metric,
            guardrail_metrics=self._guardrails, variants=self._variants,
            minimum_sample_size=self._min_sample, confounds=self._confounds)

    @staticmethod
    def render_markdown(design: ABTestDesign) -> str:
        lines = [f"# A/B 测试计划: {design.name}\n"]
        if design.hypothesis:
            lines.append(f"## 假设\n{design.hypothesis}\n")
        if design.user_definition:
            lines.append(f"## 用户定义\n{design.user_definition}\n")

        lines.append("## 实验方案\n")
        for v in design.variants:
            lines.append(f"- **{v.name}**: {v.description}")
        lines.append("")

        if design.primary_metric:
            lines.append(f"## 主要指标\n{design.primary_metric}\n")
        if design.guardrail_metrics:
            lines.append("## 护栏指标")
            for g in design.guardrail_metrics:
                lines.append(f"- {g}")
            lines.append("")

        if design.minimum_sample_size:
            lines.append(f"## 样本量\n- 每组最小样本量: **{design.minimum_sample_size:,}**\n")

        if design.confounds:
            lines.append("## 已识别的混淆变量")
            for c in design.confounds:
                lines.append(f"- {c}")
            lines.append("")

        lines.append("## 分析计划")
        lines.append("1. 检查随机化是否均衡")
        lines.append("2. 计算主要指标的差异和置信区间")
        lines.append("3. 检查护栏指标是否异常")
        lines.append("4. 聚焦实际效应大小而非统计显著性")
        return "\n".join(lines)


class ABTestAnalyzer:
    """A/B测试结果分析器

    用法示例::

        analyzer = ABTestAnalyzer("结账流程优化")
        analyzer.set_variant_a("对照组", 5000, 1750)
        analyzer.set_variant_b("实验组", 5000, 1900)
        result = analyzer.analyze()
        print(ABTestAnalyzer.render_markdown(result))
    """

    def __init__(self, name: str):
        self.name = name
        self._var_a = ABTestVariant(name="A")
        self._var_b = ABTestVariant(name="B")

    def set_variant_a(self, name: str, sample_size: int, conversions: int) -> None:
        self._var_a = ABTestVariant(name=name, sample_size=sample_size, conversions=conversions)

    def set_variant_b(self, name: str, sample_size: int, conversions: int) -> None:
        self._var_b = ABTestVariant(name=name, sample_size=sample_size, conversions=conversions)

    def analyze(self, confidence: float = 0.95) -> ABTestResult:
        a, b = self._var_a, self._var_b
        rate_a = a.conversions / a.sample_size if a.sample_size else 0
        rate_b = b.conversions / b.sample_size if b.sample_size else 0
        abs_diff = rate_b - rate_a
        rel_diff = (abs_diff / rate_a * 100) if rate_a else 0

        se = math.sqrt(
            rate_a * (1 - rate_a) / max(a.sample_size, 1)
            + rate_b * (1 - rate_b) / max(b.sample_size, 1))

        z = _z_score(1 - (1 - confidence) / 2)
        ci_lower = abs_diff - z * se
        ci_upper = abs_diff + z * se
        z_stat = abs_diff / se if se > 0 else 0
        p_value = 2 * (1 - _norm_cdf(abs(z_stat)))

        return ABTestResult(
            variant_a=a, variant_b=b, rate_a=rate_a, rate_b=rate_b,
            absolute_diff=abs_diff, relative_diff=rel_diff,
            ci_lower=ci_lower, ci_upper=ci_upper,
            is_significant=p_value < (1 - confidence),
            p_value=p_value)

    @staticmethod
    def render_markdown(result: ABTestResult) -> str:
        r = result
        lines = ["# A/B 测试分析结果\n"]
        lines.append("| 指标 | 对照组 | 实验组 |")
        lines.append("|------|--------|--------|")
        lines.append(f"| 名称 | {r.variant_a.name} | {r.variant_b.name} |")
        lines.append(f"| 样本量 | {r.variant_a.sample_size:,} | {r.variant_b.sample_size:,} |")
        lines.append(f"| 转化数 | {r.variant_a.conversions:,} | {r.variant_b.conversions:,} |")
        lines.append(f"| 转化率 | {r.rate_a:.2%} | {r.rate_b:.2%} |")
        lines.append("")
        lines.append("## 差异分析\n")
        lines.append(f"- **绝对差异**: {r.absolute_diff:+.4f} ({r.absolute_diff:+.2%})")
        lines.append(f"- **相对差异**: {r.relative_diff:+.1f}%")
        lines.append(f"- **95% 置信区间**: [{r.ci_lower:.4f}, {r.ci_upper:.4f}]")
        lines.append(f"- **p值**: {r.p_value:.4f}")
        sig = "✅ 是" if r.is_significant else "❌ 否"
        lines.append(f"- **统计显著**: {sig}")
        lines.append("")
        lines.append("## 业务解读\n")
        lines.append(ABTestAnalyzer.interpret_result(r))
        return "\n".join(lines)

    @staticmethod
    def interpret_result(result: ABTestResult) -> str:
        r = result
        if r.ci_lower > 0:
            return (f"实验组 ({r.variant_b.name}) 的转化率显著高于对照组，"
                    f"提升约 {r.relative_diff:.1f}%。置信区间不包含0，"
                    f"建议采用实验组方案。同时需检查护栏指标是否正常。")
        elif r.ci_upper < 0:
            return (f"实验组 ({r.variant_b.name}) 的转化率显著低于对照组，"
                    f"下降约 {abs(r.relative_diff):.1f}%。建议保留对照组方案。")
        else:
            return (f"实验组与对照组之间的差异不显著（置信区间包含0）。"
                    f"可能需要更大样本量或更长实验时间来检测差异，"
                    f"或者两个方案对用户行为的影响确实没有实质差别。")


def _z_score(p: float) -> float:
    """近似计算标准正态分布的z分数（Abramowitz & Stegun近似）。"""
    if p <= 0 or p >= 1:
        return 0.0
    if p > 0.5:
        return -_z_score(1 - p)
    t = math.sqrt(-2 * math.log(p))
    c0, c1, c2 = 2.515517, 0.802853, 0.010328
    d1, d2, d3 = 1.432788, 0.189269, 0.001308
    return t - (c0 + c1 * t + c2 * t * t) / (1 + d1 * t + d2 * t * t + d3 * t * t * t)


def _norm_cdf(x: float) -> float:
    """标准正态分布CDF近似。"""
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))
