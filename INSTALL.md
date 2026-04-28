# Installation Guide

## Quick Install (30 seconds)

```bash
# Clone the repository
git clone https://github.com/AliDujie/Quantitative-UX-Research.git

# Navigate to the directory
cd Quantitative-UX-Research

# Verify installation
python3 -c "from quantux import QuantUXSkill; print('✅ Installation successful')"
```

## Detailed Installation

### Prerequisites

- Python >= 3.8
- No external dependencies required (pure standard library)

### Step-by-Step

#### 1. Clone the Repository

```bash
git clone https://github.com/AliDujie/Quantitative-UX-Research.git
cd Quantitative-UX-Research
```

#### 2. Verify Python Version

```bash
python3 --version  # Should be >= 3.8
```

#### 3. Test the Installation

```bash
# Run the test suite
python3 quantux/tests/test_all.py

# Or with pytest
python3 -m pytest quantux/tests/test_all.py -v
```

#### 4. Use as Python Package

```python
import sys
sys.path.insert(0, "/path/to/Quantitative-UX-Research")
from quantux import QuantUXSkill

skill = QuantUXSkill("Your Product")
```

### AI Agent Integration

#### For OpenClaw Users

```bash
# Copy to your skills directory
cp -r Quantitative-UX-Research ~/.openclaw/skills/
```

#### For Other AI Platforms

Add the repository path to your platform's skill/plugin directory.

### Development Setup

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run linting
ruff check .

# Run tests
pytest -v
```

### Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError` | Ensure you're importing from the correct module name |
| `Python version` error | Upgrade to Python >= 3.8 |
| Permission denied | Use `chmod +x` on script files |

---

*For more information, see [README.md](README.md)*
