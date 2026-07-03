import os
from playwright.sync_api import sync_playwright, expect

def test_generated_dashboard():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        page.fill("input[name='username']", "Admin")
        page.fill("input[name='password']", "admin123")
        page.click("button[type='submit']")

        page.wait_for_url("**/dashboard/index")
        expect(page.locator("h6.oxd-text--h6:has-text('Dashboard')")).to_be_visible()

        page.click("a.oxd-main-menu-item:has-text('PIM')")

        page.wait_for_url("**/pim/viewEmployeeList")
        expect(page.locator("h6.oxd-text--h6:has-text('PIM')")).to_be_visible()

        page.click("a.oxd-main-menu-item:has-text('Dashboard')")

        page.wait_for_url("**/dashboard/index")
        expect(page.locator("h6.oxd-text--h6:has-text('Dashboard')")).to_be_visible()

        os.makedirs("screenshots", exist_ok=True)
        page.screenshot(
            path="screenshots/dashboard_navigation.png",
            full_page=True
        )

        browser.close()