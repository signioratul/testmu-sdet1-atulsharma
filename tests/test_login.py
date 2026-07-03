from playwright.sync_api import sync_playwright

BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

USERNAME = "Admin"
PASSWORD = "admin123"

def test_valid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        page.goto(BASE_URL)

        page.wait_for_selector('input[name="username"]')

        page.fill('input[name="username"]', USERNAME)
        page.fill('input[name="password"]', PASSWORD)

        page.click('button[type="submit"]')

        # Wait a few seconds after login
        page.wait_for_timeout(5000)

        print("Current URL:", page.url)

        error = page.locator(".oxd-alert-content-text")

        if error.count() > 0:
            print("Login Error:", error.inner_text())

        browser.close()