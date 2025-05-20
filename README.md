# Test CodeCov Project

A simple Python project to demonstrate CodeCov integration.

[![codecov](https://codecov.io/gh/YOUR_USERNAME/test-codecov/branch/main/graph/badge.svg)](https://codecov.io/gh/YOUR_USERNAME/test-codecov)

## Project Structure

- `mypackage/`: Main package
  - `calculator.py`: A simple calculator module
  - `tests/`: Test directory
    - `test_calculator.py`: Tests for calculator module

## Code Coverage

This project is set up with CodeCov to track code coverage. The configuration in `.codecov.yml` requires:

- Project coverage target: 70%
- Threshold: 10% (allows coverage to drop by up to 10% without failing)

## Running Tests Locally

To run tests and generate coverage reports:

```bash
# Install dependencies
pip install -r requirements.txt

# Run tests with coverage
pytest

# The coverage report will be generated as coverage.xml
```

## CI/CD

GitHub Actions is configured to:
1. Run tests on every push to main and on pull requests
2. Generate coverage reports
3. Upload coverage data to CodeCov

## Notes

- Some functions in the calculator module are intentionally not tested to demonstrate partial code coverage
- The CodeCov configuration ignores certain files (versioneer.py and monai/_version.py)
