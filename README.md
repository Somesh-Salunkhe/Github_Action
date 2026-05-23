# GitHub Actions — Python CI with Unit Testing

![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python)
![pytest](https://img.shields.io/badge/Tested%20with-pytest-0A9EDC?logo=pytest)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI-2088FF?logo=githubactions)

A focused demonstration of **GitHub Actions** for automating Python unit tests. Every push or pull request to the `main` branch triggers a CI workflow that installs dependencies and runs the full `pytest` suite — ensuring math utility functions stay correct at every commit.

---

## Project Structure

```
Github_Action/
├── .github/
│   └── workflows/
│       └── unit_test.yaml      # GitHub Actions CI workflow
├── src/
│   ├── __init__.py
│   └── math_operations.py      # Core math utility functions
├── test/
│   ├── __init__.py
│   └── test_operations.py      # pytest unit tests
├── requirement.txt             # Python dependencies
└── README.md
```

---

## Source Code

`src/math_operations.py` provides two arithmetic utility functions:

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

Both functions support positive integers, negative integers, and mixed-sign inputs.

---

## Unit Tests

Tests live in `test/test_operations.py` and import directly from the `src` package:

```python
from src.math_operations import add, subtract

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(-1, -2) == -3

def test_sub():
    assert subtract(5, 3) == 2
    assert subtract(4, 3) == 1
    assert subtract(1, -1) == 2
    assert subtract(-1, -1) == 0
    assert subtract(1, 1) == 0
```

### Test Coverage Summary

| Function | Cases Tested |
|----------|-------------|
| `add` | Positive + positive, negative + positive, negative + negative |
| `subtract` | Positive − positive, positive − negative, negative − negative |

---

## CI Workflow

The pipeline is defined in [`.github/workflows/unit_test.yaml`](.github/workflows/unit_test.yaml) and runs on `ubuntu-latest`.

**Trigger:** Push or pull request to `main`

| Step | Action |
|------|--------|
| Checkout code | `actions/checkout@v6` |
| Set up Python 3.11 | `actions/setup-python@v6` |
| Install dependencies | `pip install -r requirement.txt` |
| Run tests | `pytest` |

The workflow ensures that no broken code reaches the `main` branch — the `pytest` step will fail the run if any assertion fails.

---

## Getting Started Locally

### Prerequisites

- Python 3.11+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/Somesh-Salunkhe/Github_Action.git
cd Github_Action

# Install dependencies
pip install -r requirement.txt
```

### Run Tests

```bash
pytest
```

You should see output like:

```
collected 2 items

test/test_operations.py ..   [100%]

2 passed in 0.XXs
```

---

## Dependencies

| Package | Purpose |
|---------|--------|
| `pytest` | Unit testing framework |
| `pandas` | Data manipulation (available for future extensions) |

---

## How It Works — CI Flow

```
Push to main / Open PR
        │
        ▼
  GitHub Actions triggers
        │
        ▼
  Checkout → Setup Python 3.11
        │
        ▼
  pip install -r requirement.txt
        │
        ▼
       pytest
        │
   ┌────┴────┐
   ✅ Pass   ❌ Fail
  (green)  (blocks merge)
```

---

## License

This project is open-source and available under the [MIT License](LICENSE).
