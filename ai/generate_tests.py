from utils.gemini_client import client
import json
import traceback
import sys

prompt = prompt = """
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
- Invalid Credentials
- Forgot Password
- Empty Username
- Empty Password
- Empty Username and Password
- Password Visibility Toggle
- Session Expiry
- Logout
- Account Lockout after Multiple Failed Attempts
- SQL Injection Validation
- Cross-Site Scripting (XSS) Validation

DASHBOARD
- Dashboard Loads Successfully
- Dashboard Widgets Display Correctly
- Dashboard Data Accuracy
- Search Functionality
- Filter Functionality
- Sort Functionality
- Left Navigation Menu
- User Profile Menu
- Permission-Based Visibility
- Responsive Layout

API
- Authentication Token Validation
- GET Request Validation
- POST Request Validation
- PUT Request Validation
- DELETE Request Validation
- Status Code Validation
- Required Fields Validation
- Missing Fields Validation
- Invalid Data Type Validation
- Unauthorized Request
- Forbidden Request
- Invalid Endpoint
- Empty Response Validation
- Server Error (5xx) Validation
- Rate Limiting Validation
- Response Time Validation

Return ONLY JSON.
Do not use markdown.
Do not include explanations.
"""

try:
    print("Calling Gemini...")
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    print("Gemini responded.")

    text = response.text.strip()

    text = text.replace("```json", "").replace("```", "").strip()

    data = json.loads(text)

    with open(
        "reports/login_testcases.json",
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(data, f, indent=4)

    print(f"Login Tests      : {len(data['login'])}")
    print(f"Dashboard Tests  : {len(data['dashboard'])}")
    print(f"API Tests        : {len(data['api'])}")

except Exception:
    traceback.print_exc()
    sys.exit(1)