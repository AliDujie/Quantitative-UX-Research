# Contributing to Quantitative UX Research

Thank you for your interest in contributing! This skill is part of the [AliDujie Skill Ecosystem](https://github.com/AliDujie) — a collection of user research and design thinking tools.

## How to Contribute

### Reporting Issues
- Use GitHub Issues to report bugs or request features
- Include: skill version, Python version, steps to reproduce, expected vs actual behavior
- For statistical method questions, check the [references/](references/) directory first

### Code Contributions
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/method-name`)
3. Write tests for new functionality
4. Ensure all tests pass (`python -m pytest`)
5. Run linting (`ruff check .`)
6. Submit a Pull Request with a clear description

### Adding New Statistical Methods
- Follow the existing method structure in `quantux/`
- Include: formula, assumptions, use cases, output format, references
- Update SKILL.md with the new method
- Add references to the `references/` directory

### Documentation
- README.md: User-facing documentation, quick start, examples
- SKILL.md: Agent-facing instructions, detailed methodology
- Both should stay in sync when adding features

## Code Style
- Python 3.9+ compatible
- Standard library only (no external dependencies)
- Follow PEP 8 with 100-char line length
- Use type hints for new functions
- Docstrings in Chinese for method descriptions

## Testing
- All new methods should include test cases
- Run: `python -m pytest tests/`
- Coverage target: 80%+

## Ecosystem Integration
This skill integrates with:
- [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) — Research methodology
- [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) — Visualize findings
- [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) — Jobs-to-be-Done framework
- [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) — Product-market fit
- [Web Persona](https://github.com/AliDujie/web-persona-skill) — User persona creation

## License
By contributing, you agree that your contributions will be licensed under the MIT License.

---

*Questions? Open an issue or reach out to [@AliDujie](https://github.com/AliDujie)*
