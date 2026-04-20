"""日志序列分析模块

对应执行能力：用户行为路径分析、Sunburst可视化数据准备、Markov链分析。
基于《Quantitative User Experience Research》(Chapman & Rodden, 2023) 第5章。

用法示例::

    analyzer = LogsAnalyzer(max_sequence_length=4, session_gap_minutes=30)

    # 批量加载事件
    events = [
        {"user_id": "u1", "timestamp": "2024-01-15 10:00:00", "event_name": "首页"},
        {"user_id": "u1", "timestamp": "2024-01-15 10:02:00", "event_name": "搜索"},
        {"user_id": "u1", "timestamp": "2024-01-15 10:05:00", "event_name": "详情页"},
        {"user_id": "u1", "timestamp": "2024-01-15 10:08:00", "event_name": "加购"},
        {"user_id": "u1", "timestamp": "2024-01-15 11:00:00", "event_name": "首页"},
        {"user_id": "u2", "timestamp": "2024-01-15 09:00:00", "event_name": "首页"},
        {"user_id": "u2", "timestamp": "2024-01-15 09:03:00", "event_name": "搜索"},
    ]
    loaded = analyzer.load_events(events)
    print(f"加载了 {loaded} 条事件")

    # 会话化
    sessions = analyzer.sessionize()

    # 构建序列频率
    sequences = analyzer.build_sequences()

    # Top 路径
    top_paths = analyzer.get_top_paths(n=5)

    # Markov 转移矩阵
    matrix = analyzer.build_transition_matrix()

    # Sunburst 数据
    sunburst = analyzer.prepare_sunburst_data()

    # 输出完整报告
    print(analyzer.render_markdown())
"""

from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Optional, Tuple


@dataclass
class LogEvent:
    """单条日志事件。

    Attributes:
        user_id: 用户唯一标识。
        timestamp: 事件时间戳，格式为 "YYYY-MM-DD HH:MM:SS"。
        event_name: 事件名称，如 "首页"、"搜索"、"下单"。
        event_category: 事件类别，可选，用于分组筛选。

    用法示例::

        event = LogEvent(
            user_id="u001",
            timestamp="2024-01-15 10:30:00",
            event_name="搜索",
            event_category="导航",
        )
    """

    user_id: str
    timestamp: str
    event_name: str
    event_category: str = ""


@dataclass
class SessionSequence:
    """一个会话的事件序列。

    Attributes:
        session_id: 会话唯一标识，格式为 "{user_id}_s{n}"。
        user_id: 所属用户标识。
        events: 事件名称列表，按时间顺序排列。
        sequence_str: 连字符分隔的序列字符串，如 "首页-搜索-详情页"。

    用法示例::

        session = SessionSequence(
            session_id="u001_s1",
            user_id="u001",
            events=["首页", "搜索", "详情页"],
            sequence_str="首页-搜索-详情页",
        )
    """

    session_id: str
    user_id: str
    events: List[str] = field(default_factory=list)
    sequence_str: str = ""


@dataclass
class SequenceFrequency:
    """序列及其出现频率。

    Attributes:
        sequence: 连字符分隔的序列字符串。
        count: 出现次数。
        proportion: 占总序列数的比例（0.0~1.0）。

    用法示例::

        sf = SequenceFrequency(
            sequence="首页-搜索-详情页",
            count=42,
            proportion=0.15,
        )
    """

    sequence: str
    count: int
    proportion: float = 0.0


@dataclass
class TransitionMatrix:
    """Markov 转移概率矩阵。

    Attributes:
        states: 所有状态（事件名称）列表。
        matrix: 嵌套字典，from_state -> to_state -> probability。

    用法示例::

        tm = TransitionMatrix(
            states=["首页", "搜索", "详情页"],
            matrix={
                "首页": {"搜索": 0.7, "详情页": 0.3},
                "搜索": {"详情页": 0.8, "首页": 0.2},
                "详情页": {"首页": 1.0},
            },
        )
        print(tm.matrix["首页"]["搜索"])  # 0.7
    """

    states: List[str] = field(default_factory=list)
    matrix: Dict[str, Dict[str, float]] = field(default_factory=dict)


class LogsAnalyzer:
    """日志序列分析器

    提供完整的用户行为日志分析流程：事件加载 → 会话划分 →
    序列构建 → 频率统计 → Markov转移矩阵 → 可视化数据准备。

    用法示例::

        analyzer = LogsAnalyzer(max_sequence_length=5, session_gap_minutes=15)

        # 逐条添加
        analyzer.add_event("u1", "2024-01-15 10:00:00", "首页")
        analyzer.add_event("u1", "2024-01-15 10:02:00", "搜索")

        # 或批量加载
        analyzer.load_events([
            {"user_id": "u2", "timestamp": "2024-01-15 09:00:00", "event_name": "首页"},
        ])

        sessions = analyzer.sessionize()
        top = analyzer.get_top_paths(n=5)
        print(analyzer.render_markdown())
    """

    def __init__(self, max_sequence_length: int = 5, session_gap_minutes: int = 15):
        """初始化日志分析器。

        Args:
            max_sequence_length: 序列最大长度，超过此长度的序列会被截断。默认5。
            session_gap_minutes: 会话间隔阈值（分钟），两个相邻事件的时间间隔
                                 超过此值时开始新会话。默认15分钟。

        用法示例::

            analyzer = LogsAnalyzer(max_sequence_length=4, session_gap_minutes=30)
        """
        self.max_sequence_length = max_sequence_length
        self.session_gap_minutes = session_gap_minutes
        self._events: List[LogEvent] = []
        self._sessions: List[SessionSequence] = []
        self._sequences: List[SequenceFrequency] = []
        self._transition_matrix: Optional[TransitionMatrix] = None

    def add_event(
        self, user_id: str, timestamp: str, event_name: str, category: str = ""
    ) -> None:
        """添加单条日志事件。

        Args:
            user_id: 用户唯一标识。
            timestamp: 事件时间戳，格式为 "YYYY-MM-DD HH:MM:SS"。
            event_name: 事件名称。
            category: 事件类别，可选。

        用法示例::

            analyzer.add_event("u001", "2024-01-15 10:00:00", "首页", "导航")
        """
        self._events.append(
            LogEvent(
                user_id=user_id,
                timestamp=timestamp,
                event_name=event_name,
                event_category=category,
            )
        )

    def load_events(self, events: List[Dict]) -> int:
        """批量加载事件数据。

        Args:
            events: 事件字典列表，每个字典须包含 user_id、timestamp、event_name，
                    可选 event_category 或 category。

        Returns:
            成功加载的事件数量。

        用法示例::

            count = analyzer.load_events([
                {"user_id": "u1", "timestamp": "2024-01-15 10:00:00", "event_name": "首页"},
                {"user_id": "u1", "timestamp": "2024-01-15 10:02:00", "event_name": "搜索"},
            ])
            print(f"加载了 {count} 条事件")
        """
        loaded = 0
        for evt in events:
            user_id = evt.get("user_id", "")
            timestamp = evt.get("timestamp", "")
            event_name = evt.get("event_name", "")
            category = evt.get("event_category", evt.get("category", ""))
            if user_id and timestamp and event_name:
                self.add_event(user_id, timestamp, event_name, category)
                loaded += 1
        return loaded

    def _parse_timestamp(self, ts: str) -> datetime:
        """解析时间戳字符串为 datetime 对象。

        支持常见格式：
        - "YYYY-MM-DD HH:MM:SS"
        - "YYYY-MM-DDTHH:MM:SS"

        Args:
            ts: 时间戳字符串。

        Returns:
            解析后的 datetime 对象。
        """
        for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%dT%H:%M:%S"):
            try:
                return datetime.strptime(ts, fmt)
            except ValueError:
                continue
        raise ValueError(f"无法解析时间戳: {ts}，支持格式: YYYY-MM-DD HH:MM:SS")

    def sessionize(self) -> List[SessionSequence]:
        """按用户和时间间隔划分会话。

        实现逻辑：
        1. 按 user_id 分组
        2. 每组内按 timestamp 排序
        3. 当两个相邻事件的时间间隔超过 session_gap_minutes 时，开始新会话
        4. 将每个会话的事件名拼接为连字符分隔的字符串

        Returns:
            SessionSequence 列表，按 session_id 排序。

        用法示例::

            sessions = analyzer.sessionize()
            for s in sessions:
                print(f"{s.session_id}: {s.sequence_str}")
        """
        # 按 user_id 分组
        user_events: Dict[str, List[LogEvent]] = defaultdict(list)
        for evt in self._events:
            user_events[evt.user_id].append(evt)

        sessions: List[SessionSequence] = []

        for user_id in sorted(user_events.keys()):
            # 按 timestamp 排序
            sorted_events = sorted(
                user_events[user_id], key=lambda e: self._parse_timestamp(e.timestamp)
            )

            session_count = 1
            current_events: List[str] = [sorted_events[0].event_name]
            prev_time = self._parse_timestamp(sorted_events[0].timestamp)

            for evt in sorted_events[1:]:
                curr_time = self._parse_timestamp(evt.timestamp)
                gap_minutes = (curr_time - prev_time).total_seconds() / 60.0

                if gap_minutes > self.session_gap_minutes:
                    # 保存当前会话
                    seq_str = "-".join(current_events)
                    sessions.append(
                        SessionSequence(
                            session_id=f"{user_id}_s{session_count}",
                            user_id=user_id,
                            events=list(current_events),
                            sequence_str=seq_str,
                        )
                    )
                    session_count += 1
                    current_events = [evt.event_name]
                else:
                    current_events.append(evt.event_name)

                prev_time = curr_time

            # 保存最后一个会话
            seq_str = "-".join(current_events)
            sessions.append(
                SessionSequence(
                    session_id=f"{user_id}_s{session_count}",
                    user_id=user_id,
                    events=list(current_events),
                    sequence_str=seq_str,
                )
            )

        self._sessions = sessions
        return sessions

    def build_sequences(self, max_length: int = 0) -> List[SequenceFrequency]:
        """构建序列并统计频率。

        从已划分的会话中提取子序列（n-gram），统计每种序列的出现次数和比例。

        Args:
            max_length: 序列最大长度，0 表示使用初始化时设置的 max_sequence_length。

        Returns:
            SequenceFrequency 列表，按出现次数降序排列。

        用法示例::

            sequences = analyzer.build_sequences(max_length=3)
            for sf in sequences[:5]:
                print(f"{sf.sequence}: {sf.count} ({sf.proportion:.1%})")
        """
        if not self._sessions:
            self.sessionize()

        length = max_length if max_length > 0 else self.max_sequence_length
        seq_counter: Counter = Counter()

        for session in self._sessions:
            events = session.events
            # 提取所有长度从2到length的子序列
            for n in range(2, min(len(events) + 1, length + 1)):
                for i in range(len(events) - n + 1):
                    sub_seq = "-".join(events[i : i + n])
                    seq_counter[sub_seq] += 1

        total = sum(seq_counter.values()) if seq_counter else 1
        result = [
            SequenceFrequency(
                sequence=seq,
                count=count,
                proportion=round(count / total, 4),
            )
            for seq, count in seq_counter.most_common()
        ]

        self._sequences = result
        return result

    def build_transition_matrix(self) -> TransitionMatrix:
        """构建 Markov 转移概率矩阵。

        统计所有会话中相邻事件对的转移频率，计算条件概率。

        Returns:
            TransitionMatrix 实例，包含所有状态和转移概率。

        用法示例::

            matrix = analyzer.build_transition_matrix()
            for from_state, transitions in matrix.matrix.items():
                for to_state, prob in transitions.items():
                    print(f"  {from_state} → {to_state}: {prob:.2f}")
        """
        if not self._sessions:
            self.sessionize()

        # 统计转移频率
        transition_counts: Dict[str, Dict[str, int]] = defaultdict(
            lambda: defaultdict(int)
        )
        all_states: set = set()

        for session in self._sessions:
            for i in range(len(session.events) - 1):
                from_state = session.events[i]
                to_state = session.events[i + 1]
                transition_counts[from_state][to_state] += 1
                all_states.add(from_state)
                all_states.add(to_state)

        # 计算概率
        states = sorted(all_states)
        matrix: Dict[str, Dict[str, float]] = {}
        for from_state in states:
            total = sum(transition_counts[from_state].values())
            if total > 0:
                matrix[from_state] = {
                    to_state: round(count / total, 4)
                    for to_state, count in sorted(
                        transition_counts[from_state].items()
                    )
                }
            else:
                matrix[from_state] = {}

        result = TransitionMatrix(states=states, matrix=matrix)
        self._transition_matrix = result
        return result

    def get_top_paths(self, n: int = 10) -> List[SequenceFrequency]:
        """获取 Top N 路径。

        Args:
            n: 返回的路径数量，默认10。

        Returns:
            按出现次数降序排列的前 N 条 SequenceFrequency。

        用法示例::

            top = analyzer.get_top_paths(n=5)
            for path in top:
                print(f"{path.sequence}: {path.count}")
        """
        if not self._sequences:
            self.build_sequences()
        return self._sequences[:n]

    def get_common_starts(self, n: int = 5) -> List[Tuple[str, int]]:
        """获取最常见的起始页面。

        统计所有会话的第一个事件，返回出现频率最高的前 N 个。

        Args:
            n: 返回的数量，默认5。

        Returns:
            元组列表，每个元组为 (事件名称, 出现次数)。

        用法示例::

            starts = analyzer.get_common_starts(n=3)
            for name, count in starts:
                print(f"{name}: {count}次")
        """
        if not self._sessions:
            self.sessionize()

        start_counter: Counter = Counter()
        for session in self._sessions:
            if session.events:
                start_counter[session.events[0]] += 1

        return start_counter.most_common(n)

    def get_drop_off_points(self) -> List[Dict]:
        """识别用户放弃的位置。

        统计所有会话的最后一个事件（即用户离开前的最后操作），
        识别高频放弃点。

        Returns:
            字典列表，每个字典包含:
            - event: 事件名称
            - drop_count: 作为会话末尾的次数
            - drop_rate: 放弃率（该事件作为末尾的次数 / 该事件总出现次数）

        用法示例::

            drops = analyzer.get_drop_off_points()
            for d in drops:
                print(f"{d['event']}: 放弃{d['drop_count']}次, 放弃率{d['drop_rate']:.1%}")
        """
        if not self._sessions:
            self.sessionize()

        # 统计每个事件作为会话末尾的次数
        end_counter: Counter = Counter()
        total_counter: Counter = Counter()

        for session in self._sessions:
            if session.events:
                end_counter[session.events[-1]] += 1
            for evt in session.events:
                total_counter[evt] += 1

        result: List[Dict] = []
        for event, drop_count in end_counter.most_common():
            total = total_counter[event]
            drop_rate = round(drop_count / total, 4) if total > 0 else 0.0
            result.append(
                {
                    "event": event,
                    "drop_count": drop_count,
                    "drop_rate": drop_rate,
                }
            )

        return result

    def prepare_sunburst_data(self) -> List[Dict]:
        """准备 Sunburst 可视化数据。

        将序列频率数据转换为 Sunburst 图表所需的格式。

        Returns:
            字典列表，每个字典包含:
            - sequence: 连字符分隔的序列字符串
            - count: 出现次数

        用法示例::

            sunburst = analyzer.prepare_sunburst_data()
            # [{"sequence": "首页-搜索-详情页", "count": 42}, ...]
        """
        if not self._sequences:
            self.build_sequences()

        return [
            {"sequence": sf.sequence, "count": sf.count}
            for sf in self._sequences
            if sf.count > 0
        ]

    def render_markdown(self) -> str:
        """输出完整的日志分析报告。

        包含数据概览、Top 10 路径、常见起始页面、转移概率矩阵、放弃点分析。

        Returns:
            格式化的 Markdown 字符串。

        用法示例::

            print(analyzer.render_markdown())
        """
        # 确保数据已计算
        if not self._sessions:
            self.sessionize()
        if not self._sequences:
            self.build_sequences()
        if self._transition_matrix is None:
            self.build_transition_matrix()

        unique_users = len(set(evt.user_id for evt in self._events))

        lines = ["# 用户行为路径分析报告\n"]

        # 数据概览
        lines.append("## 数据概览\n")
        lines.append(f"- 总事件数: {len(self._events)}")
        lines.append(f"- 唯一用户数: {unique_users}")
        lines.append(f"- 会话数: {len(self._sessions)}")
        lines.append(f"- 会话间隔阈值: {self.session_gap_minutes} 分钟")
        lines.append(f"- 最大序列长度: {self.max_sequence_length}")
        lines.append("")

        # Top 10 路径
        top_paths = self.get_top_paths(10)
        lines.append("## Top 10 路径\n")
        lines.append("| 排名 | 路径 | 出现次数 | 占比 |")
        lines.append("|------|------|---------|------|")
        for i, sf in enumerate(top_paths, 1):
            lines.append(
                f"| {i} | {sf.sequence} | {sf.count} | {sf.proportion:.1%} |"
            )
        lines.append("")

        # 常见起始页面
        starts = self.get_common_starts(5)
        lines.append("## 常见起始页面\n")
        lines.append("| 排名 | 页面 | 出现次数 |")
        lines.append("|------|------|---------|")
        for i, (name, count) in enumerate(starts, 1):
            lines.append(f"| {i} | {name} | {count} |")
        lines.append("")

        # 转移概率矩阵
        lines.append("## 转移概率矩阵\n")
        if self._transition_matrix and self._transition_matrix.states:
            tm = self._transition_matrix
            # 表头
            header = "| From \\ To | " + " | ".join(tm.states) + " |"
            separator = "|" + "---|" * (len(tm.states) + 1)
            lines.append(header)
            lines.append(separator)
            for from_state in tm.states:
                row_values = []
                for to_state in tm.states:
                    prob = tm.matrix.get(from_state, {}).get(to_state, 0.0)
                    row_values.append(f"{prob:.2f}" if prob > 0 else "-")
                lines.append(f"| {from_state} | " + " | ".join(row_values) + " |")
        else:
            lines.append("（数据不足，无法构建转移矩阵）")
        lines.append("")

        # 放弃点分析
        drops = self.get_drop_off_points()
        lines.append("## 放弃点分析\n")
        lines.append("| 页面 | 放弃次数 | 放弃率 |")
        lines.append("|------|---------|--------|")
        for d in drops:
            lines.append(
                f"| {d['event']} | {d['drop_count']} | {d['drop_rate']:.1%} |"
            )
        lines.append("")

        return "\n".join(lines)
