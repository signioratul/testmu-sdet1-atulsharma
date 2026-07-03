# AI Usage Log

This document records how AI tools were used throughout the development of the AI QA Automation Pipeline.

---

## AI Tool

ChatGPT (GPT-5.5)

### Purpose

Project planning and architecture design.

### Input

Requested a modular architecture for an AI-driven QA automation framework capable of generating test cases, Playwright scripts, validating UI screenshots, validating API responses and producing execution reports.

### Output

Suggested project folder structure, module organization and implementation workflow.

### Usage

Accepted and implemented.

---

## AI Tool

Google Gemini API

### Purpose

Regression Test Case Generation

### Input

Prompt requesting structured regression test cases for Login, Dashboard and API modules.

### Output

Generated structured JSON containing regression test cases.

### Usage

Saved as:

reports/login_testcases.json

---

## AI Tool

Google Gemini API

### Purpose

Playwright Login Automation

### Input

Prompt requesting executable pytest Playwright automation for Login functionality.

### Output

Generated Python Playwright automation script.

### Usage

Saved as:

tests/generated_login.py

---

## AI Tool

Google Gemini API

### Purpose

Dashboard Navigation Automation

### Input

Prompt requesting executable pytest Playwright automation for Dashboard navigation.

### Output

Generated Python Playwright automation script.

### Usage

Saved as:

tests/generated_dashboard.py

---

## AI Tool

Google Gemini API

### Purpose

UI Validation

### Input

Dashboard screenshot.

### Output

PASS/FAIL assessment with detected UI issues.

### Usage

Saved as:

reports/ui_validation.json

---

## AI Tool

Google Gemini API

### Purpose

API Validation

### Input

Sample API response.

### Output

Schema validation including missing fields, warnings and validation summary.

### Usage

Saved as:

reports/api_validation.json

---

## AI Tool

ChatGPT (GPT-5.5)

### Purpose

Debugging and Development Assistance

### Tasks

- Debugged Playwright automation.
- Improved Gemini prompts.
- Assisted with pytest integration.
- Assisted with subprocess orchestration.
- Improved reporting pipeline.
- Assisted with README documentation.
- Assisted with GitHub project preparation.

### Usage

Used throughout the project to resolve implementation issues and improve project structure.