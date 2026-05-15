# QuantUX 跨技能协作指南

> Quantitative UX Research 如何与 AliDujie 生态系统中的其他技能协作

---

## QuantUX 在生态系统中的位置

QuantUX 是 7 技能工作流的 **定量验证引擎**，用数据验证其他技能产生的定性假设：

```
Persona → JTBD → UDM → QuantUX (你在这里) → VPD → SWD
```

## QuantUX 与其他技能的协作

### UDM → QuantUX：从定性发现到定量验证

UDM 的定性研究结果为 QuantUX 提供验证假设：

| UDM 输出 | → QuantUX 输入 | 验证方法 |
|----------|---------------|---------|
| 用户访谈痛点 | 假设列表 | A/B 测试 + 样本量计算 |
| 可用性测试 SUS 分数 | 基线指标 | CSat 追踪 + HEART 指标 |
| 体验历程图痛点 | 行为路径 | 日志序列分析 |
| 焦点小组发现 | 功能优先级 | MaxDiff 分析 |
| 日记研究模式 | 使用频率 | Log 分析 + 转化矩阵 |

### JTBD → QuantUX：从需求洞察到量化确认

JTBD 的机会评分需要 QuantUX 的统计验证：

| JTBD 输出 | → QuantUX 输入 | 验证方法 |
|-----------|---------------|---------|
| Opportunity Score | 优先级排序 | MaxDiff 实验设计 |
| 四力分析（推力/拉力） | 用户分群 | A/B 分层测试 |
| Job 满意度 | 基线测量 | HEART 指标体系 |
| 用户细分画像 | 受众分组 | 分群 CSat 调查 |

### QuantUX → VPD：从数据验证到价值设计

QuantUX 的统计结果为 VPD 的实验验证提供基线和方向：

| QuantUX 输出 | → VPD 输入 | VPD 应用 |
|--------------|-----------|---------|
| A/B 测试结果 | 价值假设 | 画布填充 + 实验设计 |
| HEART 基线 | 客户痛点 | 痛点缓解者设计 |
| MaxDiff 优先级 | 功能排序 | Gain Creator 优先级 |
| CSat 分析 | 用户满意度 | 价值主张契合度评分 |

### QuantUX → SWD：从分析结果到数据叙事

QuantUX 的研究报告是 SWD 数据叙事的原始材料：

| QuantUX 输出 | → SWD 输入 | SWD 应用 |
|--------------|-----------|---------|
| HEART 指标趋势 | 时间序列数据 | 折线图 + 故事构建 |
| A/B 测试对比 | 对比数据 | 柱状图 + 去杂乱 |
| MaxDiff 排序 | 优先级数据 | 排序图 + 注意力引导 |
| CSat 分布 | 分布数据 | 饼图替代方案 + 上下文分析 |
| 日志转化漏斗 | 漏斗数据 | 漏斗可视化 + 叙事结构 |

### Persona → QuantUX：从角色假设到行为验证

| Persona 输出 | → QuantUX 输入 | 验证方法 |
|--------------|---------------|---------|
| 角色行为假设 | 分群依据 | Log 分析 + 聚类 |
| 角色目标 | HEART 目标映射 | 指标定义 |
| 角色痛点 | CSat 调查重点 | 定制问卷 |

## 典型跨技能工作流

### 工作流 1：定性发现 → 定量验证 → 数据呈现

```
UDM (用户访谈发现 3 个痛点)
  → QuantUX (CSat 调查 + A/B 测试验证痛点影响)
  → SWD (将验证结果转化为高管汇报)
```

### 工作流 2：需求洞察 → 量化确认 → 价值设计

```
JTBD (机会评分发现 Top 3 未满足需求)
  → QuantUX (MaxDiff 验证优先级排序)
  → VPD (基于量化数据设计价值主张画布)
```

### 工作流 3：完整研究到商业决策

```
Persona (定义目标用户)
  → JTBD (发现核心 Jobs)
  → UDM (定性研究方法执行)
  → QuantUX (定量验证 + HEART 指标建立)
  → VPD (价值主张设计 + 实验验证)
  → SWD (数据叙事 → 商业决策)
```

## Python API 跨技能调用示例

```python
# Step 1: UDM 定性发现
from udm import UDMSkill
udm = UDMSkill("旅行平台")
methods = udm.recommend_methods("了解用户流失原因", phase=1)
interview = udm.generate_interview("流失用户访谈", "contextual")

# Step 2: QuantUX 定量验证
from quantux import QuantUXSkill
quantux = QuantUXSkill("旅行平台")

# 基于 UDM 发现的痛点，设计 CSat 调查
csat = quantux.design_csat_survey("Q1 用户满意度", mechanism="in_app")

# 验证改进效果
ab_result = quantux.analyze_ab_test(
    name_a="旧设计", n_a=5000, conv_a=1750,
    name_b="新设计", n_b=5000, conv_b=1900,
)

# 构建 HEART 指标体系追踪长期体验
heart = quantux.build_heart_framework()

# Step 3: SWD 数据叙事
from swd import SWDSkill
swd = SWDSkill("用户体验验证报告")
story = swd.build_story(
    protagonist="产品团队",
    imbalance="用户满意度低于行业基准",
    call_to_action="批准 UX 优化预算"
)
```

## 协作注意事项

1. **假设驱动**: QuantUX 最适合验证其他技能已经形成的定性假设，而非从零开始
2. **样本量前置**: 在用 QuantUX 之前，先用 `calculate_ab_sample_size()` 确定需要的用户数量
3. **指标一致性**: QuantUX 的 HEART 指标应与 UDM 的研究目标、JTBD 的 Jobs 保持一致
4. **迭代闭环**: QuantUX 验证结果可以反馈到 UDM 进行下一轮定性研究，形成迭代
5. **叙事转化**: QuantUX 的统计结果（p 值、效应量）需要 SWD 转化为高管可理解的语言

---

*最后更新: 2026-05-15 | AliDujie 技能生态系统 | Quantitative UX Research v2.3.67*
