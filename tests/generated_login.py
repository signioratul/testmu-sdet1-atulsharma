from playwright.sync_api import sync_playwright, expect

def test_generated_login():

    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)

        page = browser.new_page()

        page.set_default_timeout(120000)
        page.set_default_navigation_timeout(120000)

        print("Opening login page...")

        page.goto(URL, wait_until="domcontentloaded")

        print("Current URL:", page.url)
        print("Page Title:", page.title())

        page.screenshot(
            path="screenshots/debug_login_page.png",
            full_page=True
        )

        page.wait_for_selector(
            'input[name="username"]',
            timeout=120000
        )

        page.locator('input[name="username"]').fill("Admin")
        page.locator('input[name="password"]').fill("admin123")

        page.locator('button[type="submit"]').click()

        expect(
            page.locator("h6")
        ).to_have_text("Dashboard", timeout=120000)

        page.screenshot(
            path="screenshots/dashboard.png",
            full_page=True
        )

        browser.close()