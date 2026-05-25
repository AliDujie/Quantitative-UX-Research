#!/usr/bin/env python3
"""Example: MaxDiff Feature Prioritization Survey Design.

Scenario: A SaaS product has 12 candidate features but budget for only 3.
Use MaxDiff to determine which features users value most.
"""
from quantux import QuantUXSkill

qx = QuantUXSkill("SaaS Analytics Platform")

print("=" * 60)
print("MaxDiff Survey: Feature Prioritization")
print("=" * 60)

# Design MaxDiff survey for 8 features
features = [
    "Real-time dashboard",
    "Automated anomaly detection",
    "Custom report builder",
    "API access for raw data",
    "Collaborative annotations",
    "Scheduled email reports",
    "Mobile app",
    "Predictive forecasting"
]

survey = qx.design_maxdiff(
    feature_set_name="Analytics Features",
    features=features,
    num_sets=12  # Each respondent sees 12 choice sets
)
print(survey)

print("\n" + "=" * 60)
print("MaxDiff Design Principles")
print("=" * 60)
print("""
  - Each choice set shows 3-4 features
  - Respondent picks "Most Important" and "Least Important"
  - More discriminating than Likert scales — forces trade-offs
  - Recommended sample size: 200+ respondents
  - Analysis uses multinomial logit (MNL) for utility scores

  After collecting responses, use analyze_maxdiff() to get:
  → Feature utility scores (higher = more valued)
  → Confidence intervals for each feature
  → Willingness-to-pay estimates
""")
