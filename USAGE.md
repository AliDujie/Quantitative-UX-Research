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
maxdiff = qx.design_maxdiff(
    "Feature Priorities",
    ["Fast Search", "Price Alerts", "Loyalty Tiers", "Smart Recommendations"]
)

# Analyze responses (MNL estimation)
analysis = qx.analyze_maxdiff(responses)
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
| Feature prioritization | MaxDiff design → Analyze → Report | `design_maxdiff()` → `analyze_maxdiff()` |
| Quarterly UX health | CSat → HEART refresh → CEO report | `analyze_csat()` → `build_heart_framework()` → `generate_report(include_ceo_analysis=True)` |

## 🔗 Ecosystem Integration / 生态协作

```python
# JTBD/UDM (qualitative) → QuantUX (quantitative) → SWD (presentation)
from jtbd import JTBDSkill
from quantux import QuantUXSkill
from swd import SWDSkill

jtbd = JTBDSkill("Product")
score = jtbd.score_opportunity("Quick booking", struggle=4, alternative=3, market=5, budget=4)

quantux = QuantUXSkill("Product")
n = quantux.calculate_ab_sample_size(baseline=0.35, mde=0.03)
ab = quantux.analyze_ab_test("Old", 5000, 1750, "New", 5000, 1900)

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
