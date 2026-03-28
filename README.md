# QA Engineer Home Assignment - candidate-c27d4e92

This repository contains a focused submission for the Single Bet Placement feature described in the provided specification.

## Deliverables

- `docs/test_plan.md` — 6 prioritized manual test scenarios
- `docs/execution_results_and_bug_reports.md` — execution notes for top scenarios and exploratory findings
- `docs/strategy_and_recommendations.md` — automation strategy and scaling recommendations
- `tests/ui/test_place_single_bet_receipt.py` — Selenium + Pytest E2E UI test
- `tests/api/test_place_bet_validation.py` — Requests + Pytest API validation test
- lightweight automation framework with page objects, API client, fixtures, config, and helpers

## Tech stack

- Python 3.11+
- Pytest
- Selenium WebDriver
- Requests

## App under test

- Web app: `https://qae-assignment-tau.vercel.app/?user-id=candidate-c27d4e92`
- Swagger UI: `https://qae-assignment-tau.vercel.app/api/docs`

## Project structure

```text
candidate-c27d4e92-qa-project/
├── clients/
│   └── betting_api.py
├── docs/
│   ├── execution_results_and_bug_reports.md
│   ├── strategy_and_recommendations.md
│   └── test_plan.md
├── pages/
│   ├── base_page.py
│   ├── bet_slip_page.py
│   └── matches_page.py
├── tests/
│   ├── api/
│   │   └── test_place_bet_validation.py
│   ├── ui/
│   │   └── test_place_single_bet_receipt.py
│   └── conftest.py
├── utils/
│   ├── config.py
│   └── data_builders.py
├── requirements.txt
└── pytest.ini
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # macOS / Linux
# .venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

## Run all tests

```bash
pytest -v
```

## Run only UI test

```bash
pytest tests/ui -v
```

## Run only API test

```bash
pytest tests/api -v
```

## Notes and assumptions

- The framework is intentionally small and interview-friendly: enough structure to scale, without unnecessary abstraction.
- Locators are written to be resilient but may need small adjustments if the application markup changes.
- The API validation test uses direct HTTP calls with the required `x-user-id` header from the feature spec.
- The execution results document distinguishes between expected checks and observed issues, and calls out where behavior should be re-verified in a live run.
