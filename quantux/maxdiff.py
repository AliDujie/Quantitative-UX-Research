"""MaxDiff 调查设计与分析模块

MaxDiff（最大差异缩放法）是一种强制选择调查方法，要求受访者从随机子集中
选择"最重要"和"最不重要"的项目，从而得到可靠的优先级排序。

相比直接评分或排序，MaxDiff 具有以下优势：
- 消除量表使用偏差（acquiescence bias）
- 强制区分，避免所有项目都被评为"重要"
- 产出比率尺度（ratio-scale）数据，便于解读

基于《Quantitative User Experience Research》(Chapman & Rodden, 2023) 第6章。

用法示例::

    # ── 设计阶段 ──
    designer = MaxDiffDesigner("搜索功能优先级", "产品规划")
    designer.set_question_head("以下哪个搜索功能对你最重要/最不重要？")
    designer.add_items([
        "快速搜索", "高级筛选", "搜索历史", "自动补全",
        "拼写纠错", "语音搜索", "图片搜索", "搜索结果排序",
        "搜索结果预览", "跨类目搜索", "同义词识别", "实时搜索建议",
    ])
    designer.set_display_params(items_per_screen=4, appearances=3)
    designer.set_sample_target(300)
    design = designer.build()
    print(MaxDiffDesigner.render_markdown(design))

    # ── 分析阶段 ──
    analyzer = MaxDiffAnalyzer("搜索功能优先级", [
        "快速搜索", "高级筛选", "搜索历史", "自动补全",
    ])
    analyzer.load_counts(
        best_counts=[156, 89, 45, 110],
        worst_counts=[12, 34, 120, 34],
    )
    analysis = analyzer.analyze_counts()
    print(MaxDiffAnalyzer.render_markdown(analysis))
"""

from dataclasses import dataclass, field
from typing import List

from .config import MAXDIFF_METHOD_LABELS


@dataclass
class MaxDiffItem:
    """MaxDiff 调查中的单个项目。

    Attributes:
        id: 项目唯一标识符。
        text: 项目文本描述，如"快速搜索"。
        count_best: 在所有响应中被选为"最重要"的次数。
        count_worst: 在所有响应中被选为"最不重要"的次数。

    Example::

        item = MaxDiffItem(id=1, text="快速搜索")
        item.count_best = 156
        item.count_worst = 12
    """

    id: int
    text: str
    count_best: int = 0
    count_worst: int = 0


@dataclass
class MaxDiffDesign:
    """MaxDiff 调查的完整设计方案。

    Attributes:
        title: 调查标题。
        question_head: 问题头部文本，展示给受访者的提示语。
        items: 待评估的项目列表。
        items_per_screen: 每屏展示的项目数（通常为 4 或 5）。
        appearances_per_item: 每个项目在调查中出现的次数。
        total_screens: 调查总屏幕数，由 calculate_screens 自动计算。
        sample_size_target: 目标样本量。

    Example::

        design = MaxDiffDesign(
            title="功能优先级",
            question_head="哪个功能对你最重要/最不重要？",
            items=[MaxDiffItem(id=1, text="快速搜索")],
            items_per_screen=4,
            appearances_per_item=3,
        )
    """

    title: str
    question_head: str
    items: List[MaxDiffItem] = field(default_factory=list)
    items_per_screen: int = 4
    appearances_per_item: int = 3
    total_screens: int = 0
    sample_size_target: int = 200


@dataclass
class MaxDiffResult:
    """单个项目的 MaxDiff 分析结果。

    Attributes:
        item_text: 项目文本。
        count_best: 被选为最重要的次数。
        count_worst: 被选为最不重要的次数。
        diff_score: 差异分数 = count_best - count_worst。
        std_diff_score: 标准化差异分数，范围 [-1, 1]。
            计算公式: diff_score / total_appearances，
            其中 total_appearances = sample_size × appearances_per_item。
        rank: 排名（1 为最重要）。

    Example::

        result = MaxDiffResult(
            item_text="快速搜索",
            count_best=156,
            count_worst=12,
            diff_score=144.0,
            std_diff_score=0.82,
            rank=1,
        )
    """

    item_text: str
    count_best: int
    count_worst: int
    diff_score: float = 0.0
    std_diff_score: float = 0.0
    rank: int = 0


@dataclass
class MaxDiffAnalysis:
    """MaxDiff 分析的完整结果。

    Attributes:
        title: 分析标题。
        results: 按排名排序的项目结果列表。
        sample_size: 实际样本量。
        method: 分析方法，对应 config.MAXDIFF_METHODS。

    Example::

        analysis = MaxDiffAnalysis(
            title="搜索功能优先级",
            results=[...],
            sample_size=300,
            method="counts",
        )
    """

    title: str
    results: List[MaxDiffResult] = field(default_factory=list)
    sample_size: int = 0
    method: str = "counts"


class MaxDiffDesigner:
    """MaxDiff 调查设计器。

    提供流式 API 构建 MaxDiff 调查方案，包括项目管理、
    显示参数配置、设计验证和 Markdown 输出。

    用法示例::

        designer = MaxDiffDesigner("搜索功能优先级", "产品规划")
        designer.set_question_head("以下哪个搜索功能对你最重要/最不重要？")
        designer.add_items([
            "快速搜索", "高级筛选", "搜索历史", "自动补全",
            "拼写纠错", "语音搜索", "图片搜索", "搜索结果排序",
            "搜索结果预览", "跨类目搜索", "同义词识别", "实时搜索建议",
        ])
        designer.set_display_params(items_per_screen=4, appearances=3)
        design = designer.build()
        print(MaxDiffDesigner.render_markdown(design))
    """

    def __init__(self, title: str, question_context: str = ""):
        """初始化 MaxDiff 设计器。

        Args:
            title: 调查标题。
            question_context: 问题背景描述，用于文档说明。
        """
        self._title = title
        self._question_context = question_context
        self._question_head = ""
        self._items: List[MaxDiffItem] = []
        self._items_per_screen = 4
        self._appearances = 3
        self._sample_target = 200
        self._next_id = 1

    def set_question_head(self, head: str) -> None:
        """设置问题头部文本。

        Args:
            head: 展示给受访者的提示语，
                  例如"以下哪个功能对你最重要/最不重要？"
        """
        self._question_head = head

    def add_item(self, text: str) -> MaxDiffItem:
        """添加单个待评估项目。

        Args:
            text: 项目文本描述。

        Returns:
            创建的 MaxDiffItem 实例。
        """
        item = MaxDiffItem(id=self._next_id, text=text)
        self._items.append(item)
        self._next_id += 1
        return item

    def add_items(self, texts: List[str]) -> None:
        """批量添加待评估项目。

        Args:
            texts: 项目文本列表。
        """
        for text in texts:
            self.add_item(text)

    def set_display_params(self, items_per_screen: int = 4, appearances: int = 3) -> None:
        """设置调查显示参数。

        Args:
            items_per_screen: 每屏展示的项目数（建议 4-5）。
            appearances: 每个项目在调查中出现的次数（建议 3-5）。
        """
        self._items_per_screen = items_per_screen
        self._appearances = appearances

    def set_sample_target(self, n: int = 200) -> None:
        """设置目标样本量。

        Args:
            n: 目标受访者数量。
        """
        self._sample_target = n

    def calculate_screens(self) -> int:
        """计算所需的屏幕数。

        公式: total_screens = K × T / M
        其中 K = 项目总数, T = 每项出现次数, M = 每屏项目数。

        Returns:
            总屏幕数（向上取整）。

        Raises:
            ValueError: 当项目列表为空或每屏项目数为 0 时。
        """
        k = len(self._items)
        if k == 0:
            raise ValueError("项目列表为空，无法计算屏幕数")
        if self._items_per_screen == 0:
            raise ValueError("每屏项目数不能为 0")

        import math
        return math.ceil(k * self._appearances / self._items_per_screen)

    def validate_design(self) -> List[str]:
        """验证 MaxDiff 调查设计的合理性。

        检查项包括：
        - 项目数量是否 >= 10（MaxDiff 的最低建议）
        - 项目文本是否简短（建议不超过 50 字符）
        - 每屏项目数是否在合理范围（3-6）
        - 是否设置了问题头部文本
        - 目标样本量是否充足

        Returns:
            警告信息列表，空列表表示设计合理。
        """
        warnings: List[str] = []

        if len(self._items) < 10:
            warnings.append(
                f"项目数量为 {len(self._items)}，建议至少 10 个项目。"
                "MaxDiff 在项目较多时效果更好。"
            )

        long_items = [item for item in self._items if len(item.text) > 50]
        if long_items:
            names = ", ".join(f'"{i.text[:20]}..."' for i in long_items[:3])
            warnings.append(
                f"发现 {len(long_items)} 个项目文本超过 50 字符（{names}），"
                "建议保持简短以减少认知负担。"
            )

        if not (3 <= self._items_per_screen <= 6):
            warnings.append(
                f"每屏项目数为 {self._items_per_screen}，"
                "建议在 3-6 之间，4 或 5 最常用。"
            )

        if not self._question_head:
            warnings.append("未设置问题头部文本，受访者将缺少引导。")

        if self._sample_target < 100:
            warnings.append(
                f"目标样本量为 {self._sample_target}，"
                "建议至少 200 人以获得稳定的计数分析结果。"
            )

        duplicate_texts = [
            text for text, count in
            {item.text: sum(1 for i in self._items if i.text == item.text)
             for item in self._items}.items()
            if count > 1
        ]
        if duplicate_texts:
            warnings.append(f"发现重复项目: {', '.join(duplicate_texts)}")

        return warnings

    def build(self) -> MaxDiffDesign:
        """构建 MaxDiff 调查设计方案。

        Returns:
            完整的 MaxDiffDesign 实例。

        Raises:
            ValueError: 当项目列表为空时。
        """
        if not self._items:
            raise ValueError("项目列表为空，无法构建设计")

        total_screens = self.calculate_screens()

        return MaxDiffDesign(
            title=self._title,
            question_head=self._question_head,
            items=list(self._items),
            items_per_screen=self._items_per_screen,
            appearances_per_item=self._appearances,
            total_screens=total_screens,
            sample_size_target=self._sample_target,
        )

    @staticmethod
    def render_markdown(design: MaxDiffDesign) -> str:
        """将 MaxDiff 设计方案输出为 Markdown 文档。

        Args:
            design: MaxDiffDesign 实例。

        Returns:
            格式化的 Markdown 字符串，包含完整的调查设计文档。

        Example::

            design = designer.build()
            md = MaxDiffDesigner.render_markdown(design)
            print(md)
        """
        lines = [f"# MaxDiff 调查设计: {design.title}\n"]

        # 调查概览
        lines.append("## 调查概览\n")
        lines.append(f"| 参数 | 值 |")
        lines.append(f"|------|------|")
        lines.append(f"| 项目总数 | {len(design.items)} |")
        lines.append(f"| 每屏项目数 | {design.items_per_screen} |")
        lines.append(f"| 每项出现次数 | {design.appearances_per_item} |")
        lines.append(f"| 总屏幕数 | {design.total_screens} |")
        lines.append(f"| 目标样本量 | {design.sample_size_target} |")
        lines.append("")

        # 问题设计
        lines.append("## 问题设计\n")
        if design.question_head:
            lines.append(f"**问题头部:** {design.question_head}\n")
        lines.append("**作答方式:** 受访者从每屏展示的项目中选择「最重要」和「最不重要」各一项。\n")

        # 项目列表
        lines.append("## 待评估项目\n")
        lines.append("| 编号 | 项目 |")
        lines.append("|------|------|")
        for item in design.items:
            lines.append(f"| {item.id} | {item.text} |")
        lines.append("")

        # 实施说明
        lines.append("## 实施说明\n")
        lines.append(
            f"1. 将 {len(design.items)} 个项目随机分配到 {design.total_screens} 个屏幕中，"
            f"每屏展示 {design.items_per_screen} 个项目。"
        )
        lines.append(
            f"2. 确保每个项目在整个调查中出现 {design.appearances_per_item} 次（实验设计平衡）。"
        )
        lines.append(
            f"3. 每位受访者需完成全部 {design.total_screens} 屏的选择。"
        )
        lines.append(f"4. 目标收集 {design.sample_size_target} 份有效响应。")
        lines.append("5. 项目在每屏中的顺序应随机化，避免位置偏差。\n")

        # 分析方法建议
        lines.append("## 推荐分析方法\n")
        for _, label in MAXDIFF_METHOD_LABELS.items():
            lines.append(f"- **{label}**")
        lines.append("")

        return "\n".join(lines)


class MaxDiffAnalyzer:
    """MaxDiff 分析器。

    支持基于计数的差异分数分析法，将原始响应数据转化为
    标准化的优先级排序。

    用法示例::

        analyzer = MaxDiffAnalyzer("搜索功能优先级", [
            "快速搜索", "高级筛选", "搜索历史", "自动补全",
        ])
        analyzer.load_counts(
            best_counts=[156, 89, 45, 110],
            worst_counts=[12, 34, 120, 34],
        )
        analysis = analyzer.analyze_counts()
        print(MaxDiffAnalyzer.render_markdown(analysis))
    """

    def __init__(self, title: str, items: List[str]):
        """初始化 MaxDiff 分析器。

        Args:
            title: 分析标题。
            items: 项目文本列表，顺序与计数数据对应。
        """
        self._title = title
        self._items = [
            MaxDiffItem(id=i + 1, text=text)
            for i, text in enumerate(items)
        ]
        self._sample_size = 0

    def add_response(self, best_idx: int, worst_idx: int) -> None:
        """添加单条响应数据。

        Args:
            best_idx: 被选为"最重要"的项目索引（从 0 开始）。
            worst_idx: 被选为"最不重要"的项目索引（从 0 开始）。

        Raises:
            IndexError: 当索引超出项目范围时。
            ValueError: 当 best_idx 与 worst_idx 相同时。
        """
        if best_idx < 0 or best_idx >= len(self._items):
            raise IndexError(
                f"best_idx={best_idx} 超出范围 [0, {len(self._items) - 1}]"
            )
        if worst_idx < 0 or worst_idx >= len(self._items):
            raise IndexError(
                f"worst_idx={worst_idx} 超出范围 [0, {len(self._items) - 1}]"
            )
        if best_idx == worst_idx:
            raise ValueError("best_idx 和 worst_idx 不能相同")

        self._items[best_idx].count_best += 1
        self._items[worst_idx].count_worst += 1
        self._sample_size += 1

    def load_counts(self, best_counts: List[int], worst_counts: List[int]) -> None:
        """批量加载已汇总的计数数据。

        Args:
            best_counts: 每个项目被选为"最重要"的次数列表。
            worst_counts: 每个项目被选为"最不重要"的次数列表。

        Raises:
            ValueError: 当列表长度与项目数不匹配时。
        """
        n = len(self._items)
        if len(best_counts) != n:
            raise ValueError(
                f"best_counts 长度 ({len(best_counts)}) 与项目数 ({n}) 不匹配"
            )
        if len(worst_counts) != n:
            raise ValueError(
                f"worst_counts 长度 ({len(worst_counts)}) 与项目数 ({n}) 不匹配"
            )

        for i, item in enumerate(self._items):
            item.count_best = best_counts[i]
            item.count_worst = worst_counts[i]

        self._sample_size = max(sum(best_counts), sum(worst_counts))

    def analyze_counts(self) -> MaxDiffAnalysis:
        """执行基于计数的差异分数分析。

        计算流程：
        1. diff_score = count_best - count_worst
        2. std_diff_score = diff_score / max_possible_diff（归一化到 [-1, 1]）
        3. 按 diff_score 降序排列并分配排名

        Returns:
            MaxDiffAnalysis 实例，包含排序后的结果。

        Raises:
            ValueError: 当没有数据可分析时。
        """
        if self._sample_size == 0 and all(
            item.count_best == 0 and item.count_worst == 0
            for item in self._items
        ):
            raise ValueError("没有可分析的数据，请先添加响应或加载计数")

        results: List[MaxDiffResult] = []

        for item in self._items:
            diff = item.count_best - item.count_worst
            # 标准化到 [-1, 1]：除以所有项目中的最大绝对差异
            max_abs_diff = max(
                abs(i.count_best - i.count_worst) for i in self._items
            )
            std_diff = round(diff / max_abs_diff, 2) if max_abs_diff > 0 else 0.0

            results.append(MaxDiffResult(
                item_text=item.text,
                count_best=item.count_best,
                count_worst=item.count_worst,
                diff_score=float(diff),
                std_diff_score=std_diff,
            ))

        # 按 diff_score 降序排序并分配排名
        results.sort(key=lambda r: r.diff_score, reverse=True)
        for rank, result in enumerate(results, 1):
            result.rank = rank

        return MaxDiffAnalysis(
            title=self._title,
            results=results,
            sample_size=self._sample_size,
            method="counts",
        )

    @staticmethod
    def render_markdown(analysis: MaxDiffAnalysis) -> str:
        """将 MaxDiff 分析结果输出为 Markdown 文档。

        Args:
            analysis: MaxDiffAnalysis 实例。

        Returns:
            格式化的 Markdown 字符串，包含排序后的优先级表格。

        Example::

            analysis = analyzer.analyze_counts()
            md = MaxDiffAnalyzer.render_markdown(analysis)
            print(md)
        """
        method_label = MAXDIFF_METHOD_LABELS.get(analysis.method, analysis.method)

        lines = [f"# MaxDiff分析结果: {analysis.title}\n"]
        lines.append(f"**分析方法:** {method_label}")
        lines.append(f"**样本量:** {analysis.sample_size}\n")

        # 结果表格
        lines.append("| 排名 | 项目 | 最重要次数 | 最不重要次数 | 差异分数 | 标准化分数 |")
        lines.append("|------|------|-----------|-------------|---------|-----------|")

        for r in analysis.results:
            lines.append(
                f"| {r.rank} | {r.item_text} "
                f"| {r.count_best} | {r.count_worst} "
                f"| {r.diff_score:.0f} | {r.std_diff_score:.2f} |"
            )
        lines.append("")

        # 解读说明
        lines.append("## 解读说明\n")
        lines.append("- **差异分数** = 最重要次数 − 最不重要次数，正值越大表示优先级越高。")
        lines.append("- **标准化分数** 范围 [-1, 1]，1 表示最重要，-1 表示最不重要。")

        if analysis.results:
            top = analysis.results[0]
            bottom = analysis.results[-1]
            lines.append(
                f"\n**最高优先级:** {top.item_text}（标准化分数 {top.std_diff_score:.2f}）"
            )
            lines.append(
                f"**最低优先级:** {bottom.item_text}（标准化分数 {bottom.std_diff_score:.2f}）"
            )

        return "\n".join(lines)
