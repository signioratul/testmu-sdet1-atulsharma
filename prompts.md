# AI Prompt Library

This document contains the prompts used throughout the AI QA Automation Pipeline along with the prompt refinements performed during development.

---

# 1. Regression Test Case Generation

## Prompt

```text
You are a Senior QA Automation Engineer.

Generate comprehensive regression test cases for the following modules:

1. Login
2. Dashboard
3. API Validation

Return ONLY valid JSON.

Format:

{
  "login": [
    {
      "id": "LOGIN_TC001",
      "title": "",
      "steps": [
        "",
        ""
      ],
      "expected": ""
    }
  ],

  "dashboard": [
    {
      "id": "DASH_TC001",
      "title": "",
      "steps": [
        "",
        ""
      ],
      "expected": ""
    }
  ],

  "api": [
    {
      "id": "API_TC001",
      "title": "",
      "steps": [
        "",
        ""
      ],
      "expected": ""
    }
  ]
}

Requirements

LOGIN
- Successful Login
- Invalid Password
- Invalid Username
- Empty Fields
- Password Visibility
- Session Persistence
- Logout
- SQL Injection
- XSS Validation

DASHBOARD
- Dashboard loads successfully
- Verify Dashboard heading
- Verify Left Navigation
- Navigate to PIM
- Navigate to Leave
- Navigate back to Dashboard
- Search functionality
- User Profile menu
- Responsive layout

API
- Status Code Validation
- Required Fields Validation
- Missing Field Validation
- Invalid Data Type Validation
- Empty Response Validation
- Response Time Validation
- Unauthorized Request
- Invalid Endpoint
- Error Response Validation

Return ONLY JSON.
Do not use markdown.
Do not include explanations.
```

### Prompt Refinement

Iteration 1
- The initial prompt generated only Login test cases.

Iteration 2
- The prompt was expanded to generate Login, Dashboard, and API regression test cases.

Iteration 3
- Added a strict JSON schema and instructed the model to return only valid JSON without markdown or explanations to enable automated parsing.

---

# 2. Playwright Login Test Generation

## Prompt

```text
You are a Senior QA Automation Engineer.

Generate ONLY executable Python code.

Rules:
1. The output MUST be a valid pytest test.
2. The file MUST contain exactly ONE function.
3. The function name MUST be:

def test_generated_login():

4. Do NOT create:
   - run()
   - main()
   - if __name__ == "__main__":

5. Use the Playwright Sync API.

Application Details:
URL:
https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

Username:
Admin

Password:
admin123

Test Steps:
1. Open the login page.
2. Wait until the page loads.
3. Enter the username.
4. Enter the password.
5. Click the Login button.
6. Wait until the Dashboard page loads.
7. Verify the Dashboard heading is visible using an assertion.
8. Capture a full-page screenshot and save it as:
   screenshots/dashboard.png
9. Close the browser.

Screenshot code must be:

page.screenshot(
    path="screenshots/dashboard.png",
    full_page=True
)

Return ONLY Python code.
Do NOT include markdown.
Do NOT include explanations.
Do NOT include comments.
```

### Prompt Refinement

Iteration 1
- The model generated a run() function instead of a pytest test.

Iteration 2
- The prompt was updated to require exactly one pytest function named test_generated_login().

Iteration 3
- Added explicit instructions to return only executable Python code without markdown, comments, or explanations.

Iteration 4
- Included the screenshot path and Dashboard verification requirements to generate production-ready Playwright automation.
---

# 3. Dashboard Navigation Test Generation

## Prompt

```text
You are a Senior QA Automation Engineer.

Generate ONLY executable Python code.

Rules:

1. The output MUST be a valid pytest test.
2. The file MUST contain exactly ONE function.
3. The function name MUST be:

def test_generated_dashboard():

4. Do NOT generate:
   - run()
   - main()
   - if __name__ == "__main__":

5. Use Playwright Sync API.

Application Details

URL:
https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

Username:
Admin

Password:
admin123

Test Steps

1. Open the login page.
2. Login successfully.
3. Wait for the Dashboard page.
4. Verify the Dashboard heading is visible.
5. Click the PIM menu.
6. Verify the PIM page loads.
7. Click the Dashboard menu.
8. Verify the Dashboard heading is visible again.
9. Capture a full-page screenshot:

screenshots/dashboard_navigation.png

10. Close the browser.

Use:

page.screenshot(
    path="screenshots/dashboard_navigation.png",
    full_page=True
)

Return ONLY Python code.
Do NOT include markdown.
Do NOT include explanations.
Do NOT include comments.
```

### Prompt Refinement

Iteration 1
- The generated code included helper functions and a main block.

Iteration 2
- The prompt was refined to generate exactly one pytest function named test_generated_dashboard().

Iteration 3
- Navigation steps, Dashboard verification, PIM navigation, and screenshot capture requirements were explicitly added for consistent output.
---

# 4. UI Validation Prompt

## Prompt

```text
You are a QA Engineer.

Inspect this dashboard screenshot.

Verify

- Dashboard heading
- Left menu
- Search box
- User profile
- No visible error messages

Return JSON only.

Return ONLY JSON

{
"status":"",
"issues":[]
}
```

### Prompt Refinement

Iteration 1
- The model returned descriptive text instead of structured output.

Iteration 2
- A fixed JSON response format was introduced.

Iteration 3
- The prompt was refined to validate specific UI elements such as the Dashboard heading, left menu, search box, user profile, and visible errors.

---

# 5. API Validation Prompt

## Prompt

```text
Validate this API response.

Expected

id

name

email

Response

<API Response inserted dynamically>

Return ONLY JSON

{
  "status": "PASS",
  "missing_fields": [],
  "warnings": [],
  "summary": ""
}
```

### Prompt Refinement

Iteration 1
- The model returned explanatory text that was difficult to parse.

Iteration 2
- The prompt was updated to return only JSON.

Iteration 3
- Required fields, warnings, status, and summary were added to produce structured validation results for automated reporting.