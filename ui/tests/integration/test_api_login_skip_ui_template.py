import allure
import pytest
from playwright.sync_api import expect


@pytest.mark.skip(reason="Template only: SauceDemo does not support token-based cookie login")
@allure.feature("API+UI Integration")
@allure.story("API login then skip UI login by setting browser cookie")
def test_api_login_then_skip_ui_login(page, api_client):
    """
    Enterprise pattern:
    1. Login by API
    2. Get token
    3. Inject token into browser cookie
    4. Open protected UI page directly

    This works only when API and UI belong to the same system.
    """

    with allure.step("Login by API and get token"):
        token = api_client.login("test_user", "test_password")

    with allure.step("Inject token into browser cookie"):
        page.context.add_cookie([
            {
                "name": "token",
                "value": token,
                "domain": "example.com",
                "path": "/"
            }
        ])

    with allure.step("Open protected page directly"):
        page.goto("https://example.com/dashboard")

    with allure.step("Verify user is already logged in"):
        expect(page.locator("h1").to_have_text("Dashboard"))

