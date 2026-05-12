# QuantUX 跨技能验证模式

> 如何用定量方法验证其他技能产出的定性假设

---

## QuantUX 在生态系统中的位置

QuantUX 是 7 技能工作流的 **定量验证引擎**：

```
Persona → JTBD → UDM → QuantUX (你在这里) → VPD → SWD
```

## 验证模式矩阵

| 来源技能 | 定性假设 | QuantUX 验证方法 | 关键指标 |
|---------|---------|-----------------|---------|
| UDM | "用户因为 X 而流失" | A/B 测试 | 转化率、p 值 |
| UDM | "功能 A 比 B 更重要" | MaxDiff 分析 | 偏好分数、置信区间 |
| JTBD | "这个 Job 机会很大" | HEART 指标 | 各维度得分、趋势 |
| JTBD | "用户愿意为此付费" | CSat 调查 | 满意度、NPS |
| Persona | "这个用户群行为独特" | 日志分析 | 行为频率、时长分布 |
| VPD | "价值主张有竞争力" | A/B 测试 + MaxDiff | 转化率、偏好份额 |

## UDM → QuantUX：定性到定量的桥梁

UDM 的定性发现是 QuantUX 假设的主要来源：

```
UDM 访谈发现: "搜索体验差是主要痛点"
    ↓
QuantUX 假设: "优化搜索可将转化率提升 15%"
    ↓
QuantUX 验证: A/B 测试 (n=10,000)
    ↓
结果: +12.3% 转化率, p<0.001 → 假设成立
```

### 典型验证流程

1. **UDM 阶段**：5-10 个用户访谈，发现 3 个核心痛点
2. **假设构建**：将每个痛点转化为可测试的假设
3. **QuantUX 阶段**：设计 A/B 测试验证每个假设
4. **决策**：基于统计显著性决定是否推进

### 样本量参考

| UDM 发现类型 | QuantUX 验证方法 | 建议样本量 |
|-------------|-----------------|-----------|
| 可用性痛点（SUS<60） | 改进后 A/B 测试 | 每组 2,000-5,000 |
| 用户偏好（3选1） | MaxDiff | n=200-500 |
| 体验满意度 | CSat 调查 | n=100-300 |
| 行为模式 | 日志分析 | 全量数据 |

## JTBD → QuantUX：机会评分的量化验证

JTBD 输出机会评分（Opportunity Score），QuantUX 验证该机会是否值得投入：

| JTBD 输出 | QuantUX 验证 | 决策标准 |
|-----------|-------------|---------|
| 机会评分 > 8 | HEART 基线测量 | 确认存在显著问题 |
| 机会评分 6-8 | MaxDiff 优先级 | 确认用户偏好排序 |
| 机会评分 < 6 | CSat 验证 | 可能不值得投入 |

## VPD → QuantUX：价值主张实验验证

VPD 设计的价值主张假设需要通过 QuantUX 实验验证：

| VPD 输出 | QuantUX 验证 | 成功标准 |
|---------|-------------|---------|
| 画布契合度 > 0.8 | A/B 测试 | 转化率提升 > 10% |
| 实验设计（CTA） | 样本量计算 | 统计功效 > 80% |
| 竞争战略 | 市场份额追踪 | 份额增长 > 5% |

## 端到端验证示例

### 场景：优化旅行平台搜索体验

```python
# === 阶段 1: UDM 定性发现 ===
from udm import UDMSkill

udm = UDMSkill("旅行平台")
interview = udm.generate_interview("搜索体验访谈", "contextual")
# 发现: "搜索筛选条件太少，找不到合适的酒店"
sus_score = udm.calculate_sus([3, 2, 4, 2, 3, 2, 4, 2, 3, 2])
# SUS = 45.0 (需要改进)

# === 阶段 2: QuantUX 假设验证 ===
from quantux import QuantUXSkill

quantux = QuantUXSkill("旅行平台")

# 构建 HEART 指标体系
heart = quantux.build_heart_framework(
    happiness="搜索满意度",
    engagement="筛选条件使用率",
    adoption="高级筛选功能使用",
    retention="7日回访率",
    task_success="搜索到预订转化率"
)

# 计算 A/B 测试样本量
sample = quantux.calculate_ab_sample_size(
    baseline=0.08,   # 当前搜索→预订转化率 8%
    mde=0.015         # 期望提升 1.5 个百分点
)
# → 每组需要 12,847 样本

# 设计 CSat 调查验证改进效果
csat = quantux.design_csat(
    product="搜索功能",
    context="搜索体验优化后"
)

# === 阶段 3: 日志分析验证行为变化 ===
log = quantux.analyze_logs(
    data_source="搜索日志",
    metrics=["搜索次数", "筛选使用率", "结果点击率"]
)

# === 阶段 4: SWD 呈现结果 ===
from swd import SWDSkill

swd = SWDSkill("搜索优化效果汇报")
story = swd.build_story(
    protagonist="搜索团队",
    imbalance="搜索 SUS 仅 45 分，转化率 8%",
    resolution="优化后 SUS 72 分，转化率 11.3%"
)
```

## 验证失败时的处理

不是所有假设都能被验证。当 QuantUX 验证不显著时：

| 情况 | 可能原因 | 下一步 |
|------|---------|--------|
| p > 0.05 | 样本量不足 | 增加样本或延长测试时间 |
| 效应量小 | 假设方向错误 | 回到 UDM 重新发现 |
| 指标不敏感 | 测量工具不当 | 换用 MaxDiff 或日志分析 |
| 行为无变化 | 改动不够显著 | 加大改动幅度重新测试 |

## 三角验证原则

最可靠的研究结论来自多种方法的交叉验证：

```
UDM (定性) + QuantUX (定量) + 行为数据 (客观) = 高信度结论
```

- **定性**：解释"为什么"——UDM 访谈、JTBD 洞察
- **定量**：证明"有多少"——QuantUX A/B 测试、HEART 指标
- **行为**：展示"做了什么"——日志分析、漏斗分析

至少使用 2 种方法，推荐 3 种。

---

*本文档是 AliDujie Quantitative UX Research 技能生态系统的补充参考。*
