from playwright.sync_api import sync_playwright

def test_generated_login():
    # Application details
    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    USERNAME = "Admin"
    PASSWORD = "admin123"

    with sync_playwright() as p:
        # Launch browser (headless=False to see the browser UI)
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        print(f"1. Opening login page: {URL}")
        page.goto(URL)

        # Ensure the login form is loaded
        page.wait_for_selector('div.orangehrm-login-container')

        print("2. Logging in...")
        # Fill username
        page.fill('input[name="username"]', USERNAME)
        # Fill password
        page.fill('input[name="password"]', PASSWORD)
        # Click login button
        page.click('button[type="submit"]')

        print("3. Verifying dashboard opens...")
        # Wait for the URL to change to the dashboard or an element on the dashboard to appear
        # The URL usually contains '/dashboard' after successful login
        # Or, wait for a specific dashboard element, e.g., the 'Dashboard' header text
        try:
            page.wait_for_url("**/dashboard", timeout=10000)
            print("Login successful! Dashboard URL detected.")
        except Exception:
            # If URL doesn't change, try waiting for a common dashboard element
            page.wait_for_selector('h6.oxd-topbar-header-breadcrumb-module', timeout=10000)
            dashboard_header = page.locator('h6.oxd-topbar-header-breadcrumb-module').text_content()
            if "Dashboard" in dashboard_header:
                print(f"Login successful! Dashboard element found: '{dashboard_header}'")
            else:
                raise Exception("Dashboard did not open or verification element not found.")

        print("4. Capturing screenshot as dashboard.png")
        page.screenshot(path="screenshots/dashboard.png", full_page=True)
        print("Screenshot 'dashboard.png' captured.")

        browser.close()
        print("Browser closed.")

if __name__ == "__main__":
    test_generated_login()