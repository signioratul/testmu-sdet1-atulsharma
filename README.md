# AI-Powered QA Automation Pipeline

## Overview

This project demonstrates how Generative AI can automate repetitive Quality Assurance (QA) tasks by generating regression test cases, creating Playwright automation scripts, validating UI screenshots, validating API responses, and producing consolidated execution reports.

The objective is to reduce the manual effort involved in regression testing while providing a scalable and extensible automation framework.

---

## Features

- AI-generated regression test cases
- AI-generated Playwright automation scripts
- Automated Login testing
- Automated Dashboard navigation testing
- Screenshot capture during test execution
- AI-powered UI validation using Google Gemini
- AI-powered API response validation
- Automated execution report generation
- Single-command pipeline execution

---

## Architecture

```
                User Requirements
                       │
                       ▼
        AI Test Case Generation (Gemini)
                       │
                       ▼
    AI Playwright Script Generation (Gemini)
                       │
                       ▼
          Playwright + Pytest Execution
                       │
                       ▼
            Dashboard Screenshots
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
      AI UI Validation     AI API Validation
             │                   │
             └─────────┬─────────┘
                       ▼
             Final JSON Report
```

---

## Workflow

```
Generate Test Cases
        │
        ▼
Execute Login Test
        │
        ▼
Execute Dashboard Test
        │
        ▼
Capture Screenshots
        │
        ▼
Validate UI
        │
        ▼
Validate API
        │
        ▼
Generate Final Report
```

---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core Programming Language |
| Google Gemini API | AI Test Generation & Validation |
| Playwright | Browser Automation |
| Pytest | Test Execution |
| Requests | API Testing |
| JSON | Report Generation |

---

## Project Structure

```
AI-QA-Automation/

│
├── ai/
│   ├── generate_tests.py
│   ├── generate_playwright.py
│   ├── generate_dashboard.py
│   ├── validate_ui.py
│   └── validate_api.py
│
├── tests/
│   ├── generated_login.py
│   └── generated_dashboard.py
│
├── utils/
│   └── gemini_client.py
│
├── reports/
│   ├── generated_testcases.json
│   ├── ui_validation.json
│   ├── api_validation.json
│   └── final_report.json
│
├── screenshots/
│   ├── dashboard.png
│   └── dashboard_navigation.png
│
├── logs/
│
├── main.py
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore
```

---

## Installation

Clone the repository.

```bash
git clone https://github.com/<your-github-username>/AI-QA-Automation.git

cd AI-QA-Automation
```

Create a virtual environment.

```bash
python -m venv venv
```

Activate it.

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

Install all required packages.

```bash
pip install -r requirements.txt
```

Install Playwright browsers.

```bash
playwright install
```

---

## Environment Variables

Create a `.env` file in the project root.

Example:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

## Running the Project

Run the complete automation pipeline.

```bash
python main.py
```

The pipeline performs the following operations:

1. Generates AI regression test cases.
2. Executes the Login Playwright test.
3. Executes the Dashboard Playwright test.
4. Captures screenshots.
5. Validates the UI using Gemini.
6. Validates API responses using Gemini.
7. Generates the final execution report.

---

## Sample Pipeline Output

```
Generate Test Cases
----------------------------
Generated 26 test cases.

Execute Generated Login Test
----------------------------
1 Passed

Execute Generated Dashboard Test
----------------------------
1 Passed

Validate UI
----------------------------
PASS

Validate API
----------------------------
PASS

Generate Final Report
----------------------------
Completed Successfully

Pipeline Status : PASS
```

---

## Generated Outputs

### Reports

```
reports/

generated_testcases.json

ui_validation.json

api_validation.json

final_report.json
```

### Screenshots

```
screenshots/

dashboard.png

dashboard_navigation.png
```

---

## Sample Final Report

```json
{
    "generated_at": "2026-07-03 17:30:00",
    "overall_status": "PASS",
    "pipeline": {
        "login_test": "PASS",
        "dashboard_test": "PASS",
        "ui_validation": "PASS",
        "api_validation": "PASS"
    }
}
```

---

## Current Capabilities

- AI-generated regression test cases
- AI-generated Playwright automation
- Login automation
- Dashboard navigation automation
- Screenshot capture
- UI validation using AI
- API response validation using AI
- Consolidated report generation

---

## Future Improvements

- HTML reports
- GitHub Actions CI/CD integration
- Cross-browser execution
- Parallel Playwright execution
- Database validation
- Email notifications
- Slack notifications
- Performance testing support

---

## Limitations

- Requires a valid Google Gemini API key.
- AI generation depends on Gemini API availability and quotas.
- Generated Playwright scripts are intended to be reviewed before production use.

---

## License

This project is provided for educational and demonstration purposes.

---

## Author

**Atul Sharma**

GitHub: https://github.com/signioratul/AI-automation

LinkedIn: https://www.linkedin.com/in/atul-sharma-a228a6216/
