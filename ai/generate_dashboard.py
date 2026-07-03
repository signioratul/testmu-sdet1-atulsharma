from utils.gemini_client import client

prompt = """
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
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

code = response.text.strip()

code = code.replace("```python", "").replace("```", "").strip()

code = code.replace("def run():", "def test_generated_dashboard():")

if 'if __name__ == "__main__":' in code:
    code = code.split('if __name__ == "__main__":')[0]

with open("tests/generated_dashboard.py", "w", encoding="utf-8") as f:
    f.write(code)

print("Dashboard Playwright test generated successfully!")