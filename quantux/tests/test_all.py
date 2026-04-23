"""Quantitative UX Research Skill — 完整测试套件

覆盖 QuantUXSkill 全部 7 大执行能力，每个测试独立运行、包含明确断言。

运行方式::

    cd quant-ux-skill
    python -m pytest quantux/tests/test_all.py -v
    # 或直接
    python quantux/tests/test_all.py
"""

import sys
import os

# 确保能从项目根目录导入 quantux 包
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from quantux import QuantUXSkill
from quantux.heart import HEARTBuilder, GoalItem, SignalItem, MetricItem, HEARTFramework
from quantux.csat import CSatSurveyBuilder, CSatAnalyzer, CSatDataPoint
from quantux.maxdiff import MaxDiffDesigner, MaxDiffAnalyzer
from quantux.abtest import ABTestPlanner, ABTestAnalyzer
from quantux.logs import LogsAnalyzer
from quantux.research import ResearchPlanner, ReportBuilder


# ──────────────────────────────────────────────
# 测试1: HEART 框架与指标体系
# ──────────────────────────────────────────────
def test_build_heart_framework():
    """测试 HEART 框架构建：添加 Goal → Signal → Metric → 生成报告"""
    skill = QuantUXSkill("旅行平台")

    # 添加目标
    goal = skill.heart_builder.add_goal("happiness", "提升用户对预订流程的满意度")
    assert isinstance(goal, GoalItem)
    assert goal.dimension == "happiness"

    # 添加信号
    signal = skill.heart_builder.add_signal(
        "提升用户对预订流程的满意度", "预订后满意度评分", "success"
    )
    assert isinstance(signal, SignalItem)
    assert signal.signal_type == "success"

    # 添加指标
    metric = skill.heart_builder.add_metric(
        "预订后满意度评分", "预订满意度T2B", "Top-2-Box比例", "survey", True
    )
    assert isinstance(metric, MetricItem)
    assert metric.is_primary is True
    assert metric.data_source == "survey"

    # 构建框架
    framework = skill.heart_builder.build()
    assert isinstance(framework, HEARTFramework)
    assert len(framework.goals) >= 1
    assert len(framework.signals) >= 1
    assert len(framework.metrics) >= 1

    # 生成 Markdown 报告
    md = skill.build_heart_framework()
    assert isinstance(md, str)
    assert len(md) > 100
    assert "旅行平台" in md or "HEART" in md

    # 工作坊指南
    guide = skill.get_workshop_guide()
    assert isinstance(guide, str)
    assert len(guide) > 100

    print("✅ test_build_heart_framework passed")


# ──────────────────────────────────────────────
# 测试2: CSat 调查设计与分析
# ──────────────────────────────────────────────
def test_design_csat_survey():
    """测试 CSat 问卷设计 + 数据分析 + 报告生成"""
    skill = QuantUXSkill("旅行平台")

    # --- 问卷设计 ---
    survey_md = skill.design_csat_survey(
        "2024Q1满意度调查", mechanism="email", target="过去30天活跃用户"
    )
    assert isinstance(survey_md, str)
    assert "满意" in survey_md
    assert len(survey_md) > 100

    # 使用 Builder 直接构建
    builder = CSatSurveyBuilder("自定义调查", "in_product")
    builder.set_product("旅行平台")
    builder.set_target("全量用户")
    builder.add_satisfaction_rating(scale=7)
    builder.add_open_ended("你最希望改进什么？")
    builder.add_demographic("你的使用频率", ["每天", "每周", "每月", "更少"])
    survey = builder.build()
    assert len(survey.questions) == 3
    assert survey.mechanism == "in_product"

    # --- 数据分析 ---
    analyzer = CSatAnalyzer("旅行平台")
    dp1 = analyzer.add_data_point("2024Q1", 500, {1: 10, 2: 20, 3: 50, 4: 180, 5: 240})
    assert isinstance(dp1, CSatDataPoint)
    assert 0 < dp1.top2box < 1
    assert dp1.ci_lower < dp1.top2box < dp1.ci_upper

    dp2 = analyzer.add_data_point("2024Q2", 480, {1: 8, 2: 18, 3: 45, 4: 190, 5: 219})
    assert dp2.sample_size == 480

    # 趋势分析
    trend = analyzer.analyze_trend()
    assert isinstance(trend, str)
    assert "趋势" in trend or "Top-2-Box" in trend

    # 完整报告
    report = analyzer.generate_report()
    assert isinstance(report, str)
    assert "2024Q1" in report
    assert "2024Q2" in report
    assert len(report) > 200

    # 常见问题
    problems = CSatAnalyzer.get_common_problems()
    assert len(problems) >= 5

    print("✅ test_design_csat_survey passed")


# ──────────────────────────────────────────────
# 测试3: MaxDiff 设计与分析
# ──────────────────────────────────────────────
def test_design_maxdiff():
    """测试 MaxDiff 调查设计 + 数据分析 + 排序输出"""
    items = [
        "快速搜索", "价格对比", "评价可信", "退款便捷", "客服响应",
        "界面美观", "个性推荐", "行程规划", "优惠提醒", "地图导航",
    ]

    # --- 调查设计 ---
    designer = MaxDiffDesigner("功能优先级调研", "选择旅行APP时")
    designer.add_items(items)
    designer.set_display_params(items_per_screen=4, appearances=3)
    designer.set_sample_target(300)

    screens = designer.calculate_screens()
    assert screens > 0

    warnings = designer.validate_design()
    assert isinstance(warnings, list)

    design = designer.build()
    assert len(design.items) == 10
    assert design.items_per_screen == 4
    assert design.sample_size_target == 300

    design_md = MaxDiffDesigner.render_markdown(design)
    assert isinstance(design_md, str)
    assert "功能优先级" in design_md
    assert len(design_md) > 100

    # 通过 QuantUXSkill 快捷方式
    skill = QuantUXSkill("旅行平台")
    quick_md = skill.design_maxdiff("快速测试", items, items_per_screen=5)
    assert isinstance(quick_md, str)
    assert len(quick_md) > 50

    # --- 数据分析 ---
    analyzer = MaxDiffAnalyzer("功能优先级", [i for i in items])
    best_counts = [80, 60, 70, 50, 30, 10, 40, 35, 20, 5]
    worst_counts = [5, 10, 8, 15, 20, 60, 25, 30, 40, 87]
    analyzer.load_counts(best_counts, worst_counts)
    analysis = analyzer.analyze_counts()
    assert len(analysis.results) == 10
    # 第一名的 diff_score 应该最高
    assert analysis.results[0].rank == 1
    assert analysis.results[0].diff_score >= analysis.results[-1].diff_score

    result_md = MaxDiffAnalyzer.render_markdown(analysis)
    assert isinstance(result_md, str)
    assert "排名" in result_md

    print("✅ test_design_maxdiff passed")


# ──────────────────────────────────────────────
# 测试4: A/B 测试样本量计算与结果分析
# ──────────────────────────────────────────────
def test_calculate_ab_sample_size():
    """测试 A/B 测试样本量计算 + 结果分析 + 业务解读"""
    skill = QuantUXSkill("旅行平台")

    # --- 样本量计算 ---
    n = skill.calculate_ab_sample_size(baseline=0.35, mde=0.03)
    assert isinstance(n, int)
    assert n > 1000  # 对于 baseline=0.35, mde=0.03 应该需要几千个样本

    # 直接使用 Planner
    planner = ABTestPlanner("结账流程优化")
    planner.set_hypothesis("简化结账步骤将提高转化率")
    planner.set_user_definition("完成商品选择的登录用户")
    planner.set_primary_metric("结账完成率", baseline_rate=0.35)
    planner.add_guardrail_metric("页面加载时间")
    planner.add_guardrail_metric("客服投诉率")
    planner.add_variant("A-对照组", "当前3步结账流程")
    planner.add_variant("B-实验组", "新2步结账流程")
    planner.add_confound("季节性流量波动")
    n2 = planner.calculate_sample_size(0.35, 0.03)
    assert n2 == n  # 相同参数应得到相同结果

    design = planner.build()
    assert len(design.variants) == 2
    assert len(design.guardrail_metrics) == 2
    assert design.minimum_sample_size == n

    plan_md = ABTestPlanner.render_markdown(design)
    assert "结账流程优化" in plan_md
    assert "护栏指标" in plan_md

    # --- 结果分析 ---
    analyzer = ABTestAnalyzer("结账流程优化")
    analyzer.set_variant_a("对照组", 5000, 1750)
    analyzer.set_variant_b("实验组", 5000, 1900)
    result = analyzer.analyze()
    assert result.rate_a == 0.35
    assert result.rate_b == 0.38
    assert result.absolute_diff > 0
    assert result.relative_diff > 0
    assert result.ci_lower < result.absolute_diff < result.ci_upper
    assert 0 < result.p_value < 1

    # 通过 QuantUXSkill 快捷方式
    result_md = skill.analyze_ab_test("对照组", 5000, 1750, "实验组", 5000, 1900)
    assert isinstance(result_md, str)
    assert "转化率" in result_md
    assert "置信区间" in result_md

    # 业务解读
    interpretation = ABTestAnalyzer.interpret_result(result)
    assert isinstance(interpretation, str)
    assert len(interpretation) > 20

    print("✅ test_calculate_ab_sample_size passed")


# ──────────────────────────────────────────────
# 测试5: 日志序列路径分析
# ──────────────────────────────────────────────
def test_logs_analyzer():
    """测试日志分析：事件加载 → 会话化 → 序列频率 → Markov → 报告"""
    skill = QuantUXSkill("旅行平台")
    la = skill.logs_analyzer

    # 用户1：完整预订流程
    la.add_event("u1", "2024-01-01 10:00:00", "首页")
    la.add_event("u1", "2024-01-01 10:02:00", "搜索")
    la.add_event("u1", "2024-01-01 10:05:00", "详情页")
    la.add_event("u1", "2024-01-01 10:08:00", "预订")
    la.add_event("u1", "2024-01-01 10:10:00", "支付成功")

    # 用户2：浏览后放弃
    la.add_event("u2", "2024-01-01 11:00:00", "首页")
    la.add_event("u2", "2024-01-01 11:03:00", "搜索")
    la.add_event("u2", "2024-01-01 11:06:00", "详情页")

    # 用户3：同样完整流程（产生重复路径）
    la.add_event("u3", "2024-01-01 12:00:00", "首页")
    la.add_event("u3", "2024-01-01 12:02:00", "搜索")
    la.add_event("u3", "2024-01-01 12:05:00", "详情页")
    la.add_event("u3", "2024-01-01 12:08:00", "预订")
    la.add_event("u3", "2024-01-01 12:10:00", "支付成功")

    # 用户1 第二个会话（间隔超过15分钟）
    la.add_event("u1", "2024-01-01 11:00:00", "首页")
    la.add_event("u1", "2024-01-01 11:01:00", "搜索")

    # 会话化
    sessions = la.sessionize()
    assert len(sessions) >= 3  # 至少3个用户各一个会话 + u1的第二个会话

    # 序列频率
    sequences = la.build_sequences()
    assert len(sequences) > 0
    assert all(seq.count > 0 for seq in sequences)

    # Top 路径
    top = la.get_top_paths(n=3)
    assert len(top) <= 3
    assert top[0].count >= top[-1].count  # 按频率降序

    # 常见起始页面
    starts = la.get_common_starts(n=3)
    assert len(starts) > 0

    # 转移矩阵
    matrix = la.build_transition_matrix()
    assert len(matrix.states) > 0
    # 非终端状态的转移概率之和应约等于1（终端状态无后续转移，跳过）
    for state in matrix.states:
        if state in matrix.matrix and matrix.matrix[state]:
            total_prob = sum(matrix.matrix[state].values())
            assert abs(total_prob - 1.0) < 0.01, f"{state} 转移概率之和 = {total_prob}"

    # Sunburst 数据
    sunburst = la.prepare_sunburst_data()
    assert isinstance(sunburst, list)
    assert len(sunburst) > 0
    assert "sequence" in sunburst[0]
    assert "count" in sunburst[0]

    # 完整报告
    report = skill.analyze_logs()
    assert isinstance(report, str)
    assert len(report) > 200

    print("✅ test_logs_analyzer passed")


# ──────────────────────────────────────────────
# 测试6: 研究规划与利益相关者诊断
# ──────────────────────────────────────────────
def test_diagnose_request():
    """测试利益相关者请求诊断 + 方法推荐 + 研究计划"""
    skill = QuantUXSkill("旅行平台")

    # --- 请求诊断 ---
    diagnosis_md = skill.diagnose_request("验证我们的新设计方向是否正确")
    assert isinstance(diagnosis_md, str)
    assert "诊断" in diagnosis_md
    assert len(diagnosis_md) > 50

    # 直接使用 Planner
    planner = ResearchPlanner("旅行平台")
    planner.set_stakeholder("产品经理张三")

    diag = planner.diagnose_request("用户为什么不用新功能？")
    assert diag.original_request == "用户为什么不用新功能？"
    assert isinstance(diag.is_user_centered, bool)
    assert isinstance(diag.recommendation, str)
    assert len(diag.recommendation) > 0

    # --- 方法推荐 ---
    methods = planner.recommend_method("用户满意度如何变化", "post_launch")
    assert isinstance(methods, list)
    assert len(methods) > 0

    methods2 = planner.recommend_method("哪个功能最重要", "planning")
    assert isinstance(methods2, list)

    # --- 研究计划 ---
    planner.add_question(
        original="用户为什么不用新功能？",
        refined="新功能的采纳障碍是什么？",
        decision="决定是否重新设计引导流程",
        method="survey"
    )
    plan = planner.build()
    assert len(plan.questions) >= 1
    assert plan.product == "旅行平台"

    plan_md = ResearchPlanner.render_markdown(plan)
    assert isinstance(plan_md, str)
    assert len(plan_md) > 100

    print("✅ test_diagnose_request passed")


# ──────────────────────────────────────────────
# 测试7: 研究报告生成
# ──────────────────────────────────────────────
def test_build_report():
    """测试研究报告构建：逐步添加内容 → 生成完整 Markdown 报告"""
    builder = ReportBuilder("旅行平台2024Q1用户满意度研究")

    builder.set_executive_summary(
        "本研究通过CSat调查收集了500名用户反馈，发现整体满意度Top-2-Box为84%，"
        "较上季度提升2个百分点。预订流程和客服响应是用户最关注的两个维度。"
    )

    builder.add_question("用户对旅行平台的整体满意度如何？")
    builder.add_question("哪些因素对满意度影响最大？")

    builder.set_methods(
        "通过邮件向过去30天内活跃用户发送CSat问卷（5点量表+开放式问题），"
        "共收到500份有效回复（响应率12%）。"
    )

    builder.add_finding("整体满意度稳中有升", "Top-2-Box从82%上升至84%，置信区间[81%, 87%]。")
    builder.add_finding("预订流程是首要关注点", "35%的开放式评论提及预订流程，其中60%为正面评价。")
    builder.add_finding("客服响应时间有待改善", "15%的负面评论集中在客服响应速度。")

    builder.add_recommendation("优化客服响应：将平均首次响应时间从5分钟降至2分钟以内")
    builder.add_recommendation("持续监控预订流程满意度，作为HEART框架Task Success的核心指标")

    builder.add_limitation("样本可能偏向高频用户，低频用户代表性不足")
    builder.add_limitation("邮件调查存在非响应偏差，响应者可能更积极或更不满")

    report = builder.build()
    assert report.title == "旅行平台2024Q1用户满意度研究"
    assert len(report.questions) == 2
    assert len(report.findings) == 3
    assert len(report.recommendations) == 2
    assert len(report.limitations) == 2

    report_md = ReportBuilder.render_markdown(report)
    assert isinstance(report_md, str)
    assert "执行摘要" in report_md
    assert "关键发现" in report_md or "发现" in report_md
    assert "建议" in report_md
    assert "局限" in report_md
    assert "84%" in report_md
    assert len(report_md) > 500

    # 通过 QuantUXSkill 快捷方式
    skill = QuantUXSkill("旅行平台")
    quick_md = skill.build_report("快速测试报告")
    assert isinstance(quick_md, str)
    assert len(quick_md) > 50

    print("✅ test_build_report passed")


# ──────────────────────────────────────────────
# 主入口：运行全部测试
# ──────────────────────────────────────────────
def run_all_tests():
    tests = [
        test_build_heart_framework,
        test_design_csat_survey,
        test_design_maxdiff,
        test_calculate_ab_sample_size,
        test_logs_analyzer,
        test_diagnose_request,
        test_build_report,
    ]

    print("=" * 60)
    print("Quantitative UX Research Skill — 测试套件")
    print("=" * 60)
    print()

    passed = 0
    failed = 0
    errors = []

    for test_fn in tests:
        try:
            test_fn()
            passed += 1
        except Exception as e:
            failed += 1
            errors.append((test_fn.__name__, str(e)))
            print(f"❌ {test_fn.__name__} FAILED: {e}")

    print()
    print("=" * 60)
    print(f"测试结果: {passed} 通过 / {failed} 失败 / 共 {len(tests)} 个")
    print("=" * 60)

    if errors:
        print("\n失败详情:")
        for name, err in errors:
            print(f"  - {name}: {err}")

    if failed == 0:
        print("\n🎉 全部测试通过！QuantUXSkill 7 大执行能力运行正常。")

    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
