#!/usr/bin/env python3
"""
Example 2: A/B Test Analysis
完整示例 2: A/B 测试分析

Design, calculate sample size, and analyze A/B test results.
设计、计算样本量并分析 A/B 测试结果。

Usage / 用法:
    python 02_ab_testing.py
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from quantux import QuantUXSkill

def main():
    qx = QuantUXSkill("E-commerce Platform")

    print("🧪 A/B Test: New Checkout Flow")
    print("=" * 60)

    # Step 1: Calculate required sample size
    print("\n📏 Step 1: Sample Size Calculation")
    n = qx.calculate_ab_sample_size(baseline=0.30, mde=0.05)
    print(f"  → Baseline: 30%, MDE: 5%")
    print(f"  → Required: {n} users per group")

    # Step 2: Analyze results
    print("\n📊 Step 2: Analyze Results")
    # Simulated: Control vs New variant
    result = qx.analyze_ab_test(
        control_name="Current Checkout",
        control_n=5000, control_conversions=1500,
        variant_name="New One-Click Checkout",
        variant_n=5000, variant_conversions=1750
    )
    print(result)

if __name__ == "__main__":
    main()
