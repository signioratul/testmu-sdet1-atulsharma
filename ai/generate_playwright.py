from utils.gemini_client import client

prompt = """
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
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

code = response.text.strip()

# Remove markdown fences
code = code.replace("```python", "").replace("```", "").strip()

# Normalize common LLM mistakes
code = code.replace("def run():", "def test_generated_login():")

# Remove a main block if present
if 'if __name__ == "__main__":' in code:
    code = code.split('if __name__ == "__main__":')[0]

# Ensure screenshot path is correct
code = code.replace(
    'page.screenshot(path="dashboard.png")',
    'page.screenshot(path="screenshots/dashboard.png", full_page=True)'
)

with open("tests/generated_login.py", "w", encoding="utf-8") as f:
    f.write(code)

print("Playwright test generated successfully!")