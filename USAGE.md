# Quantitative UX Research Skill — Usage Guide

> 定量 UX 研究 · 使用指南

## 📐 Where QuantUX Fits in the Pipeline

```
Persona (Who) → JTBD (What) → UDM (Research) → QuantUX (Validate) → VPD (Value) → SWD (Present)
                                                   ↑
                                            QuantUX sits here
```

- **After** UDM generates qualitative hypotheses
- **Before** VPD validates product-market fit and SWD presents results
- **QuantUX** provides statistical rigor — HEART metrics, A/B tests, MaxDiff, CSat

## ⚡ 5-Minute Quick Start / 5分钟快速开始

```bash
cp -r Quantitative-UX-Research /your/agent/skills/
python -c "from quantux import QuantUXSkill; print(QuantUXSkill('My Product').calculate_ab_sample_size(baseline=0.35, mde=0.03))"
```

## 🔑 Core Workflows / 核心工作流

### 1. HEART Framework / HEART 指标体系

```python
from quantux import QuantUXSkill

qx = QuantUXSkill("Mobile App")

# Build complete HEART dashboard
heart = qx.build_heart_framework()
# H: Happiness → NPS, CSat
# E: Engagement → sessions/week
# A: Adoption → 7-day activation rate
# R: Retention → 30-day retention
# T: Task Success → completion rate, error rate
```

### 2. A/B Testing / A/B 测试

```python
# Calculate required sample size
n = qx.calculate_ab_sample_size(baseline=0.35, mde=0.03)
print(f"Need {n} users per group")

# Analyze experiment results
result = qx.analyze_ab_test("Control", 5000, 1750, "Treatment", 5000, 1900)
# → Statistical significance, confidence intervals, effect size
```

### 3. MaxDiff Priority Ranking / MaxDiff 优先级

```python
# Design balanced choice sets
analysis = qx.design_maxdiff("Feature Priorities", ["Fast Search", "Price Alerts", "Loyalty Tiers", "Smart Recommendations"])
```

### 4. CSat Survey / CSat 满意度

```python
# Design survey
survey = qx.design_csat_survey("Q1 Satisfaction", mechanism="in_product")

# Analyze results (Top-2-Box + trends)
analysis = qx.analyze_csat("Q1", 500, {1: 20, 2: 30, 3: 80, 4: 200, 5: 170})
```

### 5. CEO Business Impact / CEO 商业影响

```python
# Auto-included in reports
report = qx.generate_report("Q1 UX Report", include_ceo_analysis=True)

# Or call directly
impact = qx.generate_business_impact(
    metric="conversion_rate", baseline=0.35, improvement=0.03, revenue_per_conversion=50
)
timeline = qx.generate_validation_timeline()
resources = qx.generate_resource_estimate(headcount=3, budget=100000)
```

## 📋 Common Scenarios / 常见场景

| Scenario | Flow | APIs |
|----------|------|------|
| HEART dashboard setup | Define goals → Choose metrics → Report | `build_heart_framework()` → `generate_report()` |
| A/B test design | Sample size → Run experiment → Analyze | `calculate_ab_sample_size()` → `analyze_ab_test()` |
| Feature prioritization | MaxDiff design → Report | `design_maxdiff()` → `generate_report()` |
| Quarterly UX health | CSat → HEART refresh → CEO report | `analyze_csat()` → `build_heart_framework()` → `generate_report(include_ceo_analysis=True)` |

## 🔗 Ecosystem Integration / 生态协作

QuantUX is the **quantitative validation core** of the AliDujie UX Research Ecosystem:

| Skill | Role | How It Connects with QuantUX |
|-------|------|----------------------------|
| [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) | Methodology core | UDM qualitative findings → QuantUX hypothesis validation via A/B tests and surveys |
| [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) | Demand insight | JTBD opportunity scores → QuantUX MaxDiff validates feature priorities |
| [Web Persona](https://github.com/AliDujie/web-persona-skill) | User definition | Persona behavioral hypotheses → QuantUX log analysis validates segments |
| [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) | Product-market fit | VPD experiment hypotheses → QuantUX A/B tests validate product-market fit |
| [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) | Data storytelling | QuantUX analysis results → SWD chart selection → executive narrative |

> 💡 **Recommended chain:** Persona (who) → JTBD (what Jobs) → UDM (qualitative research) → **QuantUX** (quantitative validation) → VPD (value mapping) → SWD (presentation)

### Cross-Skill Workflow Example / 跨技能工作流示例

```python
from jtbd import JTBDSkill
from quantux import QuantUXSkill
from swd import SWDSkill
from vpd import VPDSkill

# JTBD identifies high-opportunity Jobs
jtbd = JTBDSkill("Travel Booking")
score = jtbd.score_opportunity("Quick booking", struggle=4, alternative=3, market=5, budget=4)

# QuantUX validates with A/B test
quantux = QuantUXSkill("Travel Booking")
n = quantux.calculate_ab_sample_size(baseline=0.35, mde=0.03)
ab = quantux.analyze_ab_test("Old Flow", 5000, 1750, "New Flow", 5000, 1900)

# VPD maps validated needs to value proposition
vpd = VPDSkill("Travel Booking", "Business Travelers")
vpd.analyze_canvas(product_name="Travel Booking",
    jobs=[{"description": "Quick booking"}],
    pains=[{"description": "Too many steps", "severity": "critical"}])

# SWD presents results to leadership
swd = SWDSkill("Q1 Report")
story = swd.build_story(protagonist="Product VP",
    imbalance="Booking takes 90s vs 30s industry standard",
    call_to_action="Approve optimization budget")
```

## 🧪 Testing / 测试

```bash
cd Quantitative-UX-Research
python quantux/tests/test_all.py
```

## 📚 Resources / 资源

- [README.md](README.md) — Full documentation
- [SKILL.md](SKILL.md) — Agent-facing skill definition
- [INSTALL.md](INSTALL.md) — Installation guide
- [CHANGELOG.md](CHANGELOG.md) — Version history
- [SECURITY.md](SECURITY.md) — Security policy and responsible use

## 💡 Pro Tips / 专业技巧

1. **HEART before A/B — Measure the right thing first**
   Don't jump straight into experiment design. Use `build_heart_framework()` to define Goals→Signals→Metrics across all 5 dimensions, then narrow to 3-5 core metrics. Running an A/B test on the wrong metric is worse than not testing at all.
   *先搭 HEART 再设计实验——HEART 帮你定义正确的指标，避免「在错误的指标上做实验」。*

2. **Avoid p-hacking — commit your analysis plan upfront**
   `analyze_ab_test()` reports confidence intervals, not just p-values — use them. Decide your sample size and stopping rule before collecting data. Peeking at interim results inflates false-positive rates. If you must check early, use sequential testing corrections.
   *避免 p-hacking——提前确定样本量和停止规则，不要中途看结果后「挑」显著的时刻。置信区间比单一 p 值更可靠。*

3. **Sample size planning — power matters more than significance**
   A test with 80% power needs ~2× the sample of a 50% power test. Use `calculate_ab_sample_size()` with realistic MDE values (3-5% for conversion, 10-15% for UX task metrics). Underpowered tests waste time and produce misleading results.
   *功效(power)比显著性更重要——80% 功效的样本量约是 50% 的两倍。MDE 设置要现实：转化率实验 3-5%，UX 任务指标 10-15%。*

4. **HEART vs A/B — know when to use each**
   Use HEART when you need a holistic product health dashboard or when exploring which dimensions need improvement. Use A/B testing when you have a specific change to validate (e.g., a new checkout flow). HEART tells you *what* to measure; A/B tells you *whether* a change worked. They're complementary, not competing.
   *HEART 用于全局健康诊断，A/B 用于验证具体改动。HEART 告诉你「测什么」，A/B 告诉你「改没改对」——二者互补而非替代。*

