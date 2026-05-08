# Installation Guide / 安装指南

## Quick Install (30 seconds) / 快速安装（30 秒）

```bash
# Clone the repository / 克隆仓库
git clone https://github.com/AliDujie/Quantitative-UX-Research.git

# Navigate to the directory / 进入目录
cd Quantitative-UX-Research

# Verify installation / 验证安装
python3 -c "from quantux import QuantUXSkill; print('✅ Installation successful')"
```

## Detailed Installation / 详细安装

### Prerequisites / 前置要求

- Python >= 3.8
- No external dependencies required (pure standard library) / 无需外部依赖（纯标准库）

### Step-by-Step / 分步指南

#### 1. Clone the Repository / 克隆仓库

```bash
git clone https://github.com/AliDujie/Quantitative-UX-Research.git
cd Quantitative-UX-Research
```

#### 2. Verify Python Version / 确认 Python 版本

```bash
python3 --version  # Should be >= 3.8 / 应为 >= 3.8
```

#### 3. Test the Installation / 测试安装

```bash
# Run the test suite / 运行测试套件
python3 quantux/tests/test_all.py

# Or with pytest / 或使用 pytest
python3 -m pytest quantux/tests/test_all.py -v
```

#### 4. Use as Python Package / 作为 Python 包使用

```python
import sys
sys.path.insert(0, "/path/to/Quantitative-UX-Research")
from quantux import QuantUXSkill

skill = QuantUXSkill("Your Product")
```

### AI Agent Integration / AI Agent 集成

#### For OpenClaw Users / 适用于 OpenClaw 用户

```bash
# Copy to your skills directory / 复制到你的技能目录
cp -r Quantitative-UX-Research ~/.openclaw/skills/
```

#### For Other AI Platforms / 适用于其他 AI 平台

Add the repository path to your platform's skill/plugin directory.
将仓库路径添加到你的平台的技能/插件目录。

### Development Setup / 开发环境

```bash
# Install dev dependencies / 安装开发依赖
pip install -e ".[dev]"

# Run linting / 代码检查
ruff check .

# Run tests / 运行测试
pytest -v
```

### Troubleshooting / 故障排查

| Issue / 问题 | Solution / 解决方案 |
|-------|----------|
| `ModuleNotFoundError` | Ensure you're importing from the correct module name / 确保从正确的模块名导入 |
| `Python version` error / Python 版本错误 | Upgrade to Python >= 3.8 / 升级到 Python >= 3.8 |
| Permission denied / 权限被拒绝 | Use `chmod +x` on script files / 对脚本文件使用 `chmod +x` |

## Related Skills / 相关技能

This skill is part of the AliDujie UX Research ecosystem:
本技能是 AliDujie UX 研究生态系统的一部分：

- [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) — UDM 定性发现可用 QuantUX 定量验证
- [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) — QuantUX 分析结果可交给 SWD 进行数据叙事
- [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) — JTBD 机会评分可用 QuantUX 量化验证
- [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) — VPD 价值假设可用 QuantUX 实验设计验证
- [Web Persona](https://github.com/AliDujie/web-persona-skill) — Persona 角色假设可用 QuantUX 行为数据验证

---

*For more information, see [README.md](README.md) / 更多信息请查看 README.md*
