![QA Automation](https://img.shields.io/badge/QA-Automation-blue)
![Python](https://img.shields.io/badge/Python-3.x-green)
![Pytest](https://img.shields.io/badge/Pytest-Framework-yellow)
![Allure](https://img.shields.io/badge/Report-Allure-orange)

# QA Automation Project

A scalable end-to-end QA automation framework covering API testing, UI testing, and API + UI integration, built with Python, Pytest, Requests, Playwright, and Allure.
---

## 🚀 Tech Stack

- Python
- Pytest
- Requests (API Testing)
- JSONSchema (Response Validation)
- Allure Report (Test Reporting)
- Playwright (UI Automation with POM)

---

## 📁 Project Structure

    api/
    ├── client/          # API client (request handling, auth, headers)
    ├── services/        # Service layer (business API abstraction)
    ├── schemas/         # Request & response schemas (JSONSchema)
    
    tests/
    ├── conftest.py      # API fixtures (api_client, auth, services)
    ├── auth/            # Authentication API tests
    ├── user/            # User API tests (CRUD)
    ├── product/         # Product API tests
    ├── cart/            # Cart API tests
    
    ui/
    ├── pages/           # Page Objects (Login, Inventory, Cart, Checkout)
    ├── tests/           # UI test cases
    ├── conftest.py      # UI fixtures (browser, page, login setup)
    
    common/
    ├── config/          # Environment configuration
    ├── logger/          # Logging setup
    ├── utils/           # Shared utilities (Allure helpers, validation tools)
    
    test_data/
    ├── api/             # API test payloads (JSON)
    ├── ui/              # UI test data (Python dicts)
    
    docs/
    ├── allure-report/   # Allure screenshots for README
    
    reports/             # Generated Allure results (gitignored)

---

## ✨ Features

- 🔹 API Client abstraction with reusable request methods  
- 🔹 Service layer for clean test logic separation  
- 🔹 JSON schema validation for response verification  
- 🔹 Positive & negative test coverage  
- 🔹 Allure reporting with:
  - Step-level execution
  - Feature / Story categorization
  - Request & response attachments
- 🔹 Centralized logging
- 🔹 UI automation with Playwright (POM design)
- 🔹 Automatic failure debugging (screenshot + URL)

## 🧠 Design Highlights

- Layered architecture across API and UI
  - API: client → service → test layer  
  - UI: page object (POM) → test layer  

- Separation of concerns for maintainability
  - API logic, UI interactions, and test assertions are decoupled  
  - Shared utilities (Allure, validation) centralized under common/  

- Reusable validation and reporting utilities
  - JSON schema validation for API responses  
  - Allure helpers for structured reporting and debugging  

- Strong debugging capabilities
  - Step-level execution tracking with Allure  
  - Automatic screenshot and URL capture on failure  
  - Request/response and UI state attachments  

- Scalable structure for API and UI automation
  - Easy to extend for new endpoints and UI pages  
  - Designed for end-to-end automation framework evolution  

---

## 📊 Allure Report (Test Execution & Debugging)

The project integrates Allure reporting to provide clear visibility into test execution and simplify debugging.

### 🔹 Test Overview
![Overview](docs/allure-report/overview.png)

### 🔹 Test Steps
![Steps](docs/allure-report/test-step.png)

### 🔹 Request / Response Attachments
![Attachments](docs/allure-report/attachments.png)

### 🔹 UI Debugging (Screenshot & URL)
![UI Screenshot](docs/allure-report/ui-screenshot.png)

### 🔹 Failure Debugging
![Failure](docs/allure-report/ui-failure.png)

---

### 🔍 Key Capabilities

- Step-level execution tracking  
- API request & response visibility  
- UI screenshot and current URL capture  
- Automatic failure debugging  

Enables fast root cause analysis without re-running tests.
UI tests include both manual and automatic screenshot capture strategies to ensure full visibility of test execution and failures


## API + UI Integration Testing

This project also demonstrates API and UI integration testing.

Instead of preparing test data through slow UI steps, APIs are used to create or prepare test data first. Then the UI test verifies the user-facing behavior.

Example strategy:

- Use API to prepare test data
- Use UI to verify business flow
- Reduce UI dependency
- Improve test speed and stability

In real enterprise projects, API-based login can also be used to obtain an authentication token and inject it into the browser context to skip repetitive UI login steps.

## ⚙️ Test Configuration

This project uses `pytest.ini` to centralize test configuration and enable flexible test execution.

```ini
[pytest]
testpaths =
    api/tests
    ui/tests

addopts = -v --strict-markers

markers =
    api: API tests
    ui: UI tests
    smoke: Smoke tests
    regression: Regression tests
```

This configuration allows:

* Separation of API and UI tests
* Selective test execution using markers
* Better scalability and CI/CD integration

---

## 🚀 Run Tests and Generate Allure Report

### Run all tests

```bash
pytest --alluredir=allure-results --clean-alluredir
```

### Run only API tests

```bash
pytest -m api --alluredir=allure-results --clean-alluredir
```

### Run only UI tests

```bash
pytest -m ui --alluredir=allure-results --clean-alluredir
```

---

## 📊 View Allure Report

### Generate and open report (recommended)

```bash
allure serve allure-results
```

### Generate report without rerunning tests

```bash
allure generate allure-results -o allure-report --clean
allure open allure-report
```

---

## 🧪 Test Strategy

* **API Tests** → validate backend logic, schema, and error handling
* **UI Tests** → validate user flows and UI behavior using Playwright
* **Markers** → enable test categorization (`api`, `ui`, `smoke`, `regression`)
* **Allure Reporting** → provide detailed execution steps, logs, and screenshots

This setup is designed to support:

* Smoke tests on every commit
* Regression tests on scheduled runs
* Scalable test execution in CI pipelines


Report provides:

- Step-level execution visibility  
- Full request & response data for debugging  
- Structured test grouping (Feature / Story)  
- Clear failure diagnostics 

---

## ▶️ How to Run

Install dependencies:

    pip install -r requirements.txt

## ⚡ One Command (Run + Report)

```bash
pytest --alluredir=allure-results --clean-alluredir && allure serve allure-results
```

---
