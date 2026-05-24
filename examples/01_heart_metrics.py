#!/usr/bin/env python3
"""
Example 1: HEART Metrics Framework
完整示例 1: HEART 指标框架

Build complete HEART metrics dashboard for any product.
为任何产品构建完整 HEART 指标看板。

Usage / 用法:
    python 01_heart_metrics.py
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from quantux import QuantUXSkill

def main():
    qx = QuantUXSkill("Travel App")

    print("📊 HEART Metrics Framework / HEART 指标框架")
    print("=" * 60)

    # Happiness metrics
    print("\n😊 Happiness / 满意度")
    print("  → NPS survey, CSAT, user sentiment analysis")

    # Engagement metrics
    print("\n📈 Engagement / 参与度")
    print("  → Visits per user per week, feature adoption rate")

    # Adoption metrics
    print("\n🚀 Adoption / 采用率")
    print("  → New users completing onboarding in 7 days")

    # Retention metrics
    print("\n🔄 Retention / 留存率")
    print("  → 7-day, 30-day, 90-day retention cohorts")

    # Task Success metrics
    print("\n✅ Task Success / 任务成功率")
    print("  → Booking completion rate, error rate, time on task")

    # A/B test example
    print("\n🧪 A/B Test Planning / A/B 测试规划")
    print("=" * 60)
    sample = qx.calculate_ab_sample_size(baseline=0.35, mde=0.03)
    print(f"  → Baseline conversion: 35%")
    print(f"  → Minimum detectable effect: 3%")
    print(f"  → Required sample: {sample} per group")

if __name__ == "__main__":
    main()
