"""Quant UX Skill 配置模块

定义知识库路径、分析维度、HEART框架常量等全局配置。
基于《Quantitative User Experience Research》(Chapman & Rodden, 2023)。
"""

from pathlib import Path
from dataclasses import dataclass, field
from typing import Dict, List

KNOWLEDGE_BASE_DIR = Path(__file__).parent.parent

KNOWLEDGE_FILES: Dict[str, str] = {
    "foundations": "01-foundations.md",
    "core_skills": "02-core-skills.md",
    "heart": "03-heart-framework.md",
    "csat": "04-csat-surveys.md",
    "logs": "05-logs-sequences.md",
    "maxdiff": "06-maxdiff.md",
    "organizations": "07-organizations.md",
    "career": "08-career.md",
    "stakeholders": "09-stakeholders.md",
    "reference": "10-quick-reference.md",
}

# ── HEART 框架常量 ──
HEART_DIMENSIONS = ("happiness", "engagement", "adoption", "retention", "task_success")

HEART_LABELS: Dict[str, str] = {
    "happiness": "愉悦 (Happiness)",
    "engagement": "参与 (Engagement)",
    "adoption": "采纳 (Adoption)",
    "retention": "留存 (Retention)",
    "task_success": "任务成功 (Task Success)",
}

HEART_DESCRIPTIONS: Dict[str, str] = {
    "happiness": "用户态度：满意度、感知易用性、NPS等主观评价",
    "engagement": "用户参与深度：使用频率、强度、交互深度",
    "adoption": "新用户或新功能的采纳情况",
    "retention": "用户在一段时间后是否继续使用",
    "task_success": "用户完成核心任务的效率和效果",
}

HEART_EXAMPLE_METRICS: Dict[str, List[str]] = {
    "happiness": ["整体满意度评分(1-7)", "感知易用性评分", "NPS净推荐值", "HaTS调查分数"],
    "engagement": ["每用户每周活跃天数", "平均会话时长", "每会话操作数", "核心功能使用率"],
    "adoption": ["7天内新注册用户数", "新功能首次使用率", "新用户完成引导比例"],
    "retention": ["N天留存率", "周留存率", "月留存率", "续费率"],
    "task_success": ["任务完成率", "任务错误率", "平均任务完成时间", "首次成功率"],
}

# ── GSM 流程常量 ──
GSM_STAGES = ("goals", "signals", "metrics")

GSM_LABELS: Dict[str, str] = {
    "goals": "目标 (Goals)",
    "signals": "信号 (Signals)",
    "metrics": "指标 (Metrics)",
}

# ── CSat 调查常量 ──
CSAT_MECHANISMS = ("email", "panel", "in_product")

CSAT_MECHANISM_LABELS: Dict[str, str] = {
    "email": "邮件调查",
    "panel": "第三方面板",
    "in_product": "产品内调查",
}

CSAT_SCALE_TYPES = ("five_point", "seven_point")

# ── MaxDiff 常量 ──
MAXDIFF_METHODS = ("counts", "mnl", "hierarchical_bayes")

MAXDIFF_METHOD_LABELS: Dict[str, str] = {
    "counts": "计数与差异分数",
    "mnl": "多项Logit模型 (MNL)",
    "hierarchical_bayes": "层次贝叶斯 (HB)",
}

# ── A/B 测试常量 ──
AB_DESIGN_ELEMENTS = (
    "user_definition", "sampling", "intervention",
    "confounds", "outcome_metric", "guardrail_metric",
)

# ── 研究方法常量 ──
RESEARCH_METHODS = (
    "survey", "logs_analysis", "ab_test", "maxdiff",
    "conjoint", "csat", "experience_sampling", "usability_test",
)

LIFECYCLE_STAGES = ("planning", "early_dev", "late_dev", "post_launch")

LIFECYCLE_METHODS: Dict[str, List[str]] = {
    "planning": ["logs_analysis", "maxdiff", "survey", "conjoint"],
    "early_dev": ["conjoint", "maxdiff", "survey"],
    "late_dev": ["ab_test", "usability_test"],
    "post_launch": ["csat", "logs_analysis", "experience_sampling", "ab_test"],
}

# ── 报告常量 ──
REPORT_PRINCIPLES = (
    "short_and_focused",
    "minimally_technical",
    "unbiased",
    "reproducible",
)

STAKEHOLDER_PROBLEMS = (
    "no_decision_criterion",
    "ad_hoc_projects",
    "validation_research",
    "statistical_significance_misuse",
    "cherry_picking",
    "coin",
)


@dataclass
class AnalysisConfig:
    """分析任务的运行时配置"""
    heart_dimensions: List[str] = field(default_factory=lambda: list(HEART_DIMENSIONS))
    output_format: str = "markdown"
    language: str = "zh"
    confidence_level: float = 0.95

    def validate(self) -> None:
        for d in self.heart_dimensions:
            if d not in HEART_DIMENSIONS:
                raise ValueError(f"未知HEART维度: {d}，可选: {HEART_DIMENSIONS}")
        if self.output_format not in ("markdown", "json", "text"):
            raise ValueError(f"未知输出格式: {self.output_format}")
        if not 0 < self.confidence_level < 1:
            raise ValueError(f"置信水平须在0-1之间: {self.confidence_level}")
