# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 2.x.x   | ✅ Yes             |
| 1.x.x   | ❌ No              |

## Reporting a Vulnerability

This skill is a pure Python statistical analysis toolkit with **no network access, no file system writes outside your workspace, and no external dependencies**. The attack surface is minimal, but we take security seriously.

If you discover a security vulnerability:

1. **Do NOT open a public GitHub issue**
2. Email: [contact via GitHub](https://github.com/AliDujie)
3. Include: description, impact, reproduction steps
4. We will respond within 48 hours

## Security Characteristics

- ✅ **Zero external dependencies** — uses only Python standard library
- ✅ **No network access** — runs entirely offline
- ✅ **No sensitive data handling** — analysis data stays local
- ✅ **No code execution** — outputs are statistical results, not executable code
- ✅ **Read-only references** — reference files are never modified

## Best Practices

When using this skill with sensitive user data:
- Run in an isolated environment (venv recommended)
- Do not include PII in reference files
- Review statistical outputs before sharing externally
- Anonymize data before analysis when possible

---

*Last updated: 2026-04-28*
