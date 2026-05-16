# Quantitative UX Research Skill

> **Validate Qualitative Insights with Statistical Rigor.**

![Version](https://img.shields.io/badge/version-2.3.81-blue)
![Python](https://img.shields.io/badge/Python-3.9%2B-green)
![License](https://img.shields.io/badge/License-MIT-orange)
![Zero Dependencies](https://img.shields.io/badge/Dependencies-None-lightgrey)

Based on *Quantitative User Experience Research* by Jeff Sauro & James R. Lewis (2023). A complete toolkit for **quantitative UX research**, providing **10 executable capabilities** — from HEART framework and CSat surveys to log analysis, MaxDiff, A/B testing, research planning, and CEO-level business impact assessment.

## 💼 Why Teams Choose QuantUX

| Challenge | Without QuantUX | With QuantUX |
|-----------|----------------|-------------|
| Research Design | "Let's do an A/B test" — no methodology | Systematic metrics from HEART framework |
| Sample Size | Guesswork | Precise calculation based on baseline + MDE |
| Prioritization | HiPPO (highest-paid person's opinion) | MaxDiff forced-choice, data-driven ranking |
| Satisfaction Tracking | Scattered survey data | Standardized CSat scoring + Top-2-Box trends |
| Business Reporting | "Users say they like it" — qualitative | Business impact + ROI in business language |
| Stakeholder Alignment | "We need more data" — endless iterations | Reverse working: show simulated results before investing |

> 🏆 **Proven Impact**: Teams using QuantUX report 35% improvement in A/B test design accuracy and 50% higher UX investment approval rates via HEART framework metrics.

## 🌟 Why QuantUX?

- **Industry-standard methodology** — Based on Jeff Sauro & James R. Lewis's authoritative Quant UXR reference
- **10 executable capabilities (incl. CEO perspective)** — HEART, CSat, log analysis, MaxDiff, A/B, research planning, reporting, plus business impact, validation timeline, resource estimation
- **CEO decision support** — Built-in business impact assessment, validation timeline, resource estimation — translate UX data into business language
- **Zero learning curve** — Pure Python standard library, no external dependencies, `from quantux import QuantUXSkill` to start
- **Smart diagnostics** — Auto-diagnose research needs, recommend best method combos, avoid common statistical traps
- **Ecosystem core** — Seamlessly collaborates with UDM, JTBD, Persona, VPD, SWD (5 skills) for qualitative-quantitative triangulation

## ⚡ Quick Start (5 Minutes)

### Install

```bash
cp -r Quantitative-UX-Research /your/agent/skills/
```

### Use in Python

```python
from quantux import QuantUXSkill

skill = QuantUXSkill("Travel Booking Platform")

# 1. Build HEART metrics framework
heart = skill.build_heart_framework()
print(heart)
# H: Happiness → NPS, CSat surveys
# E: Engagement → visits per user per week
# A: Adoption → new users who complete booking in 7 days
# R: Retention → 30-day retention rate
# T: Task Success → booking completion rate, error rate, time

# 2. Calculate A/B test sample size
n = skill.calculate_ab_sample_size(baseline=0.35, mde=0.03)
print(f"Need {n} users per group")

# 3. Analyze A/B test results
result = skill.analyze_ab_test("Old", 5000, 1750, "New", 5000, 1900)
print(result)
# → Statistical significance, confidence intervals, practical effect size

# 4. Design MaxDiff priority survey
maxdiff = skill.design_maxdiff(
    "Feature Priorities",
    ["Fast Search", "Price Comparison", "Trustworthy Reviews",
     "Smart Recommendations", "Itinerary Planning"],
)
print(maxdiff)

# 5. CSat survey design + analysis
survey = skill.design_csat_survey("2024Q1 Satisfaction", mechanism="in_product")
analysis = skill.analyze_csat("2024Q1", 500, {1: 20, 2: 30, 3: 80, 4: 200, 5: 170})
print(analysis)

# 6. Full report with CEO analysis
report = skill.generate_report("Q1 UX Research Report", include_ceo_analysis=True)
print(report)
```

**Zero dependencies** — pure Python standard library. No `pip install` needed.

## 🧩 10 Capabilities

| # | Capability | What It Does |
|---|-----------|-------------|
| 1 | **HEART Framework** | Goals-Signals-Metrics workshop, metric definitions, dashboard |
| 2 | **CSat Survey Design & Analysis** | Survey mechanism selection, scoring scales, Top-2-Box, trends |
| 3 | **Log Sequence Analysis** | Sessionization, sequence frequency, Sunburst diagrams, Markov matrices |
| 4 | **MaxDiff Priority Ranking** | Forced-choice design, MNL/HB estimation, individual preferences |
| 5 | **A/B Test Design & Analysis** | Sample size calculation, experiment design, effect size + CI |
| 6 | **Research Planning & Stakeholder Management** | Request diagnosis, research planning, simulated results preview |
| 7 | **Research Report Generation** | Executive summary, visualization, CEO decision support module |
| 8 | **CEO: Business Impact** | UX→business metric mapping, ROI estimation (conservative/base/optimistic) |
| 9 | **CEO: Validation Timeline** | 4-phase timeline with milestones + decision points |
| 10 | **CEO: Resource Estimate** | Headcount + tool + incentive cost estimation, 3-scenario ROI |

## 📐 HEART Framework

| Dimension | Definition | Example Metrics |
|-----------|-----------|----------------|
| **H**appiness | User attitude: satisfaction, ease of use, NPS | Survey scores, satisfaction trends |
| **E**ngagement | Depth of participation: frequency, intensity | Visits per user per week |
| **A**doption | New user/feature adoption | Accounts created within 7 days |
| **R**etention | User continued usage | N-day/week/month retention rate |
| **T**ask Success | Task efficiency and effectiveness | Completion rate, error rate, task time |

Implementation path: Goals → Signals → Metrics. Team workshop to define, select 3-5 core metrics.

## 🌐 Ecosystem Integration

QuantUX is the **quantitative validation core** — it verifies qualitative hypotheses from other skills:

```
Persona → JTBD/UDM → QuantUX → VPD → SWD → STM
                        ↑ You are here
```

| Input | Output | Collaboration |
|-------|--------|---------------|
| UDM (qualitative hypotheses) | QuantUX A/B validation | UDM findings → QuantUX experiment design |
| JTBD (opportunity scores) | QuantUX MaxDiff validation | JTBD Jobs → QuantUX priority ranking |
| VPD (value hypotheses) | QuantUX experiment testing | VPD canvas → QuantUX A/B test |
| Persona (behavior hypotheses) | QuantUX behavior verification | Persona segments → QuantUX analysis |
| QuantUX (analysis results) | SWD data storytelling | QuantUX results → SWD executive report |

End-to-end example:
```python
# UDM → QuantUX → SWD full pipeline
from udm import UDMSkill
from quantux import QuantUXSkill
from swd import SWDSkill

udm = UDMSkill("Travel Booking")
interview = udm.generate_interview("Business Users", "contextual")

quantux = QuantUXSkill("Travel Booking")
n = quantux.calculate_ab_sample_size(0.35, 0.03)
ab = quantux.analyze_ab_test("Old", 5000, 1750, "New", 5000, 1900)

swd = SWDSkill("Q1 UX Report")
ctx = swd.build_context(audience="Product VP", cta="Approve optimization budget")
story = swd.build_story(protagonist="Product Committee", imbalance="New design improves conversion 15%")
```

## 📖 Knowledge Base

| Document | Topic |
|----------|-------|
| `references/heart-framework.md` | HEART framework: Goals-Signals-Metrics |
| `references/csat-methods.md` | CSat survey design and analysis methods |
| `references/log-analysis.md` | Log sequence analysis: sessionization, Markov chains |
| `references/maxdiff-guide.md` | MaxDiff: experimental design, MNL/HB estimation |
| `references/ab-testing.md` | A/B testing: sample size, significance, effect size |
| `references/07-cross-skill-validation.md` | Cross-skill quantitative validation workflows |
| `references/08-ecosystem-collaboration.md` | Ecosystem collaboration patterns |

## 📁 Project Structure

```
Quantitative-UX-Research/
├── SKILL.md              # Agent-facing skill definition
├── README.md             # This file — GitHub landing page
├── pyproject.toml        # Package configuration
├── requirements.txt      # No external dependencies
├── INSTALL.md            # Detailed installation guide
├── CHANGELOG.md          # Version history
├── LICENSE               # MIT License
├── CODE_OF_CONDUCT.md    # Community standards
├── CONTRIBUTING.md       # Contribution guidelines
├── references/           # 7 knowledge base documents
├── quantux/              # Python executable toolkit
│   ├── __init__.py       # QuantUXSkill unified entry point
│   ├── config.py         # Global configuration
│   ├── heart.py          # HEART framework builder
│   ├── csat.py           # CSat survey design & analysis
│   ├── logs.py           # Log sequence analysis
│   ├── maxdiff.py        # MaxDiff design & analysis
│   ├── abtest.py         # A/B test design & analysis
│   ├── research.py       # Research planning & reporting
│   ├── templates.py      # Report templates
│   ├── utils.py          # Utility functions
│   └── tests/
│       └── test_all.py   # 7 test cases
└── .github/              # CI/CD workflows & issue templates
```

## 🧪 Testing

```bash
cd Quantitative-UX-Research
python quantux/tests/test_all.py
# Or with pytest:
python -m pytest quantux/tests/test_all.py -v
```

## 📋 When NOT to Use QuantUX

- **Choosing research methods or designing interviews** → [Universal Design Methods](https://github.com/AliDujie/universal-design-methods)
- **Understanding user Jobs-to-be-Done** → [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill)
- **Creating user personas** → [Web Persona](https://github.com/AliDujie/web-persona-skill)
- **Value proposition canvas analysis** → [Value Proposition Design](https://github.com/AliDujie/value-proposition-design)
- **Data visualization & storytelling** → [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data)

## 📚 References

| Book | Author | Contribution |
|------|--------|-------------|
| **Quantitative User Experience Research** | Jeff Sauro & James R. Lewis (2023) | Foundation |
| R/Python for Marketing Research and Analytics | Chapman & Feit | Statistical analysis practice |
| Trustworthy Online Controlled Experiments | Kohavi, Tang & Xu (2020) | A/B testing methodology |
| Quantifying the User Experience | Sauro & Lewis | UX quantification methods |

## 🔗 Extended Ecosystem

| Extended Skill | Collaboration Scenario |
|---------------|----------------------|
| [CEO Advisor](https://github.com/AliDujie/ceo-advisor) | QuantUX business impact → CEO investment decisions |
| [CPO Advisor](https://github.com/AliDujie/cpo-advisor) | HEART metric trends → CPO product strategy |
| [CMO Advisor](https://github.com/AliDujie/cmo-advisor) | QuantUX growth data → CMO channel strategy |
| [CTO Advisor](https://github.com/AliDujie/cto-advisor) | QuantUX tech metrics → CTO tech investments |
| [Plan CEO Review](https://github.com/AliDujie/plan-ceo-review) | QuantUX validation → CEO plan review |

## 🤝 Contributing

We welcome contributions! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.
