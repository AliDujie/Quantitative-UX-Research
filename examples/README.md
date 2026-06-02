# QuantUX Runnable Examples / 可运行示例

These examples demonstrate Quantitative UX Research capabilities with real-world scenarios.
这些示例用真实场景演示定量用户研究能力。

## Quick Start / 快速开始

```bash
cd examples/
python 01_heart_metrics.py
python 02_ab_testing.py
python 03_maxdiff.py
```

All examples use **zero dependencies** — pure Python standard library only.
所有示例使用**零依赖** — 仅 Python 标准库。

## Available Examples / 可用示例

### 01_heart_metrics.py
HEART framework setup: define Goals → Signals → Metrics across 5 dimensions.
HEART 框架搭建：在 5 个维度上定义目标 → 信号 → 指标。

**Use when / 适用场景**: You need to establish a quantitative UX metrics dashboard for any product.

```bash
python 01_heart_metrics.py
```

### 02_ab_testing.py
A/B test sample size calculation and result analysis with statistical rigor.
A/B 测试样本量计算和结果分析，带有统计严谨性。

**Use when / 适用场景**: You're designing or analyzing an A/B test and need precise statistical guidance.

```bash
python 02_ab_testing.py
```

### 03_maxdiff.py
MaxDiff (Maximum Difference) survey design for feature prioritization with budget constraints.
MaxDiff（最大差异）调查设计，用于预算约束下的功能优先级排序。

**Use when / 适用场景**: You need to prioritize features, benefits, or pain points from a large set.

```bash
python 03_maxdiff.py
```

## Tips / 提示

- All examples use relative imports — just run from the `examples/` directory
- No `pip install` required — QuantUX is zero-dependency
- Combine with UDM examples for qual → quant triangulation workflows
- See [USAGE.md](../USAGE.md) for detailed API documentation

## 🔗 Ecosystem Integration / 生态集成

QuantUX is the "validate" layer of the AliDujie UX Research Ecosystem. Chain it with other skills:

- **UDM → QuantUX**: [UDM](https://github.com/AliDujie/universal-design-methods) qualitative findings → QuantUX A/B validation
- **Persona → QuantUX**: [Persona](https://github.com/AliDujie/web-persona-skill) segments → QuantUX per-segment metrics
- **JTBD → QuantUX**: [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) opportunity scores → QuantUX feature prioritization experiments
- **VPD → QuantUX**: [VPD](https://github.com/AliDujie/value-proposition-design) experiment design → QuantUX statistical analysis
- **QuantUX → SWD**: QuantUX experiment data → [SWD](https://github.com/AliDujie/storytelling-with-data) executive narratives

See the [full pipeline example](../README.md#complete-pipeline-example) in README.md for a 6-skill end-to-end workflow.
