# Contributing Guide / 贡献指南

Thank you for your interest in contributing! This skill is part of the [AliDujie Skill Ecosystem](https://github.com/AliDujie) — a collection of user research and design thinking tools.
感谢你的贡献！本技能是 AliDujie 技能生态系统的一部分——一套用户研究和设计思维工具集。

## How to Contribute / 如何贡献

### Reporting Issues / 报告问题
- Use GitHub Issues to report bugs or request features / 使用 GitHub Issues 报告 bug 或请求功能
- Include: skill version, Python version, steps to reproduce, expected vs actual behavior / 包含：技能版本、Python 版本、复现步骤、预期与实际行为
- For statistical method questions, check the [references/](references/) directory first / 关于统计方法的问题，先查看 references/ 目录

### Code Contributions / 代码贡献
1. Fork the repository / Fork 仓库
2. Create a feature branch (`git checkout -b feature/method-name`) / 创建功能分支
3. Write tests for new functionality / 为新功能编写测试
4. Ensure all tests pass (`python -m pytest`) / 确保所有测试通过
5. Run linting (`ruff check .`) / 运行代码检查
6. Submit a Pull Request with a clear description / 提交带有清晰描述的 Pull Request

### Adding New Statistical Methods / 添加新的统计方法
- Follow the existing method structure in `quantux/` / 遵循 quantux/ 中已有的方法结构
- Include: formula, assumptions, use cases, output format, references / 包含：公式、假设、使用场景、输出格式、参考
- Update SKILL.md with the new method / 在 SKILL.md 中添加新方法
- Add references to the `references/` directory / 在 references/ 中添加参考文档

### Documentation / 文档贡献
- README.md: User-facing documentation, quick start, examples / 面向用户的文档、快速开始、示例
- SKILL.md: Agent-facing instructions, detailed methodology / 面向 Agent 的指令、详细方法论
- Both should stay in sync when adding features / 添加功能时两者应保持同步

## Code Style / 代码规范
- Python 3.9+ compatible / 兼容 Python 3.9+
- Standard library only (no external dependencies) / 仅使用标准库（无外部依赖）
- Follow PEP 8 with 100-char line length / 遵循 PEP 8，行长度 100 字符
- Use type hints for new functions / 新函数使用类型标注
- Docstrings in Chinese for method descriptions / 方法描述使用中文文档字符串

## Testing / 测试
- All new methods should include test cases / 所有新方法应包含测试用例
- Run: `python -m pytest tests/`
- Coverage target: 80%+ / 覆盖率目标：80%+

## Ecosystem Integration / 生态系统集成

This skill integrates with the broader AliDujie UX Research ecosystem:

- [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) — 定性研究方法，UDM 发现可用 QuantUX 定量验证
- [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) — 数据叙事，QuantUX 分析结果可交给 SWD 可视化
- [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) — JTBD 机会评分可用 QuantUX 量化验证
- [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) — VPD 价值假设可用 QuantUX 实验设计验证
- [Web Persona](https://github.com/AliDujie/web-persona-skill) — Persona 角色假设可用 QuantUX 行为数据验证

## License / 许可

By contributing, you agree that your contributions will be licensed under the MIT License.
通过贡献，你同意你的贡献将在 MIT 许可下授权。

---

*Questions? Open an issue or reach out to [@AliDujie](https://github.com/AliDujie)*
*有问题？请提交 issue 或联系 [@AliDujie](https://github.com/AliDujie)*
