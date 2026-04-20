"""Quant UX Skill 工具函数模块

提供知识库加载、文本处理、格式化输出、统计计算等通用工具。
基于《Quantitative User Experience Research》(Chapman & Rodden, 2023)。
"""

import math
from typing import Dict, List, Optional, Tuple

from .config import KNOWLEDGE_BASE_DIR, KNOWLEDGE_FILES


def load_knowledge(topic: str) -> str:
    """加载指定主题的知识库内容。

    Args:
        topic: 主题标识符，对应 config.KNOWLEDGE_FILES 的键。
               可选值: foundations, core_skills, heart, csat, logs,
               maxdiff, organizations, career, stakeholders, reference

    Returns:
        知识库文件的完整文本内容。

    Raises:
        KeyError: 当 topic 不在已知主题列表中时。
        FileNotFoundError: 当知识库文件不存在时。
    """
    if topic not in KNOWLEDGE_FILES:
        available = ", ".join(sorted(KNOWLEDGE_FILES.keys()))
        raise KeyError(f"未知主题 '{topic}'，可选主题: {available}")

    file_path = KNOWLEDGE_BASE_DIR / KNOWLEDGE_FILES[topic]
    if not file_path.exists():
        raise FileNotFoundError(f"知识库文件不存在: {file_path}")

    return file_path.read_text(encoding="utf-8")


def load_all_knowledge() -> Dict[str, str]:
    """加载全部知识库内容。

    Returns:
        字典，键为主题标识符，值为对应文件内容。
        若某文件不存在则对应值为空字符串。
    """
    result: Dict[str, str] = {}
    for topic in KNOWLEDGE_FILES:
        try:
            result[topic] = load_knowledge(topic)
        except FileNotFoundError:
            result[topic] = ""
    return result


def search_knowledge(keyword: str, topics: Optional[List[str]] = None) -> Dict[str, List[str]]:
    """在知识库中搜索包含关键词的段落。

    Args:
        keyword: 搜索关键词（大小写不敏感）。
        topics: 限定搜索的主题列表，为 None 时搜索全部。

    Returns:
        字典，键为主题标识符，值为包含关键词的段落列表。
    """
    search_topics = topics if topics else list(KNOWLEDGE_FILES.keys())
    results: Dict[str, List[str]] = {}

    for topic in search_topics:
        try:
            content = load_knowledge(topic)
        except (KeyError, FileNotFoundError):
            continue

        paragraphs = content.split("\n\n")
        matched = [p.strip() for p in paragraphs if keyword.lower() in p.lower()]
        if matched:
            results[topic] = matched

    return results


def extract_sections(content: str, level: int = 2) -> Dict[str, str]:
    """从 Markdown 文本中按标题级别提取章节。

    Args:
        content: Markdown 文本内容。
        level: 标题级别（2 表示 ##，3 表示 ###）。

    Returns:
        字典，键为标题文本，值为该章节的正文内容。
    """
    prefix = "#" * level + " "
    sections: Dict[str, str] = {}
    current_title: Optional[str] = None
    current_lines: List[str] = []

    for line in content.split("\n"):
        if line.startswith(prefix):
            if current_title is not None:
                sections[current_title] = "\n".join(current_lines).strip()
            current_title = line[len(prefix):].strip()
            current_lines = []
        elif current_title is not None:
            current_lines.append(line)

    if current_title is not None:
        sections[current_title] = "\n".join(current_lines).strip()

    return sections


def format_as_markdown(title: str, sections: Dict[str, str], level: int = 2) -> str:
    """将结构化内容格式化为 Markdown 文档。

    Args:
        title: 文档标题。
        sections: 章节字典，键为章节标题，值为章节内容。
        level: 章节标题级别。

    Returns:
        格式化的 Markdown 字符串。
    """
    prefix = "#" * level
    parts = [f"# {title}\n"]
    for section_title, body in sections.items():
        parts.append(f"{prefix} {section_title}\n\n{body}\n")
    return "\n".join(parts)


def format_list(items: List[str], numbered: bool = False) -> str:
    """将列表格式化为 Markdown 列表文本。

    Args:
        items: 列表项。
        numbered: 是否使用有序列表。

    Returns:
        格式化的列表字符串。
    """
    lines = []
    for i, item in enumerate(items, 1):
        marker = f"{i}." if numbered else "-"
        lines.append(f"{marker} {item}")
    return "\n".join(lines)


# ── 统计计算工具 ──


def calculate_confidence_interval(
    successes: int,
    n: int,
    confidence: float = 0.95,
) -> Tuple[float, float, float]:
    """计算二项式比例的置信区间（Wald 近似法）。

    适用于 CSat 满意度比例、任务完成率、Top-2-Box 比例等
    二项式指标的置信区间估计。当 n 较大（≥30）且比例不极端时
    Wald 近似足够准确。

    Args:
        successes: 成功/满意的样本数。
        n: 总样本数，须大于 0。
        confidence: 置信水平，默认 0.95（95%置信区间）。
                    支持 0.90、0.95、0.99。

    Returns:
        元组 (point_estimate, lower_bound, upper_bound)，
        point_estimate 为点估计比例，lower/upper 为置信区间上下界，
        所有值保留 4 位小数。

    Raises:
        ValueError: 当 n ≤ 0 或 successes > n 或 confidence 不合法时。

    Example:
        >>> calculate_confidence_interval(350, 500, 0.95)
        (0.7, 0.6598, 0.7402)
    """
    if n <= 0:
        raise ValueError(f"样本量 n 须大于 0，当前值: {n}")
    if successes < 0 or successes > n:
        raise ValueError(f"successes 须在 [0, n] 范围内，当前: successes={successes}, n={n}")

    z_values = {0.90: 1.645, 0.95: 1.960, 0.99: 2.576}
    if confidence not in z_values:
        raise ValueError(f"不支持的置信水平 {confidence}，可选: {list(z_values.keys())}")

    z = z_values[confidence]
    p = successes / n
    se = math.sqrt(p * (1 - p) / n)
    margin = z * se

    lower = max(0.0, round(p - margin, 4))
    upper = min(1.0, round(p + margin, 4))
    return (round(p, 4), lower, upper)


def calculate_sample_size(
    baseline_rate: float,
    mde: float,
    alpha: float = 0.05,
    power: float = 0.8,
) -> int:
    """计算 A/B 测试所需的每组最小样本量。

    基于双侧 Z 检验的比例差异检验公式，适用于转化率、
    点击率、任务完成率等二项式指标的 A/B 测试设计。

    公式: n = (Z_α/2 + Z_β)² × [p1(1-p1) + p2(1-p2)] / (p2 - p1)²

    Args:
        baseline_rate: 基线转化率（对照组预期比例），须在 (0, 1) 之间。
        mde: 最小可检测效应（Minimum Detectable Effect），
             即希望检测到的绝对差异，须大于 0。
             例如 0.02 表示期望检测到 2 个百分点的差异。
        alpha: 显著性水平（I 类错误率），默认 0.05。
               支持 0.01、0.05、0.10。
        power: 统计功效（1 - II 类错误率），默认 0.8。
               支持 0.80、0.90。

    Returns:
        每组所需的最小样本量（向上取整）。

    Raises:
        ValueError: 当参数不在合法范围时。

    Example:
        >>> calculate_sample_size(0.10, 0.02)
        3623
    """
    if not 0 < baseline_rate < 1:
        raise ValueError(f"baseline_rate 须在 (0, 1) 之间，当前值: {baseline_rate}")
    if mde <= 0:
        raise ValueError(f"mde 须大于 0，当前值: {mde}")

    z_alpha_map = {0.01: 2.576, 0.05: 1.960, 0.10: 1.645}
    z_beta_map = {0.80: 0.842, 0.90: 1.282}

    if alpha not in z_alpha_map:
        raise ValueError(f"不支持的 alpha={alpha}，可选: {list(z_alpha_map.keys())}")
    if power not in z_beta_map:
        raise ValueError(f"不支持的 power={power}，可选: {list(z_beta_map.keys())}")

    z_alpha = z_alpha_map[alpha]
    z_beta = z_beta_map[power]

    p1 = baseline_rate
    p2 = baseline_rate + mde

    if p2 >= 1:
        raise ValueError(f"baseline_rate + mde = {p2}，须小于 1")

    numerator = (z_alpha + z_beta) ** 2 * (p1 * (1 - p1) + p2 * (1 - p2))
    denominator = (p2 - p1) ** 2

    return math.ceil(numerator / denominator)


def top2box_score(
    ratings: List[int],
    top_values: Optional[List[int]] = None,
) -> Tuple[float, int, int]:
    """计算 Top-2-Box 得分。

    Top-2-Box 是 CSat / 满意度调查中最常用的汇总指标，
    表示选择量表最高两个选项的受访者比例。

    Args:
        ratings: 评分列表，每个元素为单个受访者的评分值。
        top_values: 视为"Top-2"的评分值列表。
                    默认为 None，此时自动取 ratings 中最大的两个唯一值。
                    例如 7 点量表中默认为 [6, 7]。

    Returns:
        元组 (score, top_count, total)，
        score 为 Top-2-Box 比例（保留 4 位小数），
        top_count 为落入 Top-2 的样本数，
        total 为总样本数。

    Raises:
        ValueError: 当 ratings 为空时。

    Example:
        >>> top2box_score([5, 6, 7, 7, 3, 6, 4, 7, 6, 5])
        (0.6, 6, 10)
    """
    if not ratings:
        raise ValueError("ratings 不能为空")

    if top_values is None:
        unique_sorted = sorted(set(ratings), reverse=True)
        top_values = unique_sorted[:2]

    top_set = set(top_values)
    top_count = sum(1 for r in ratings if r in top_set)
    total = len(ratings)
    score = round(top_count / total, 4)

    return (score, top_count, total)
