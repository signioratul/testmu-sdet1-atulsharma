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