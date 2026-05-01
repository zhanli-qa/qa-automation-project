import allure
from playwright.sync_api import expect
from test_data.ui.login_user import (VALID_USER, INVALID_USER_NAME,
                                     INVALID_USER_PASSWORD, EMPTY_USER_PASSWORD, EMPTY_USER_USERNAME)

# Verify login success
@allure.feature("Login UI")
@allure.story("Login Success")
def test_login_success(login_page):

    with allure.step("Login in with valid username and password"):
        inventory_page = login_page.login(
            VALID_USER["username"],
            VALID_USER["password"]
        )

        # allure attach which has already defined in base_page and inherited by login_page
        login_page.screenshot("after_success_login")

    with allure.step("Verify login success and redirect to inventory page"):
        expect(inventory_page.title).to_have_text("Products")


# Negative case: Verify login failed with invalid username
@allure.feature("Login UI")
@allure.story("Invalid username shows error message")
def test_login_failed_with_invalid_username(login_page):

    with allure.step("Login with invalid username"):
        login_page.login(
            INVALID_USER_NAME["username"],
            INVALID_USER_NAME["password"]
        )

        login_page.screenshot("invalid_username_error_message")

    with allure.step("Verify error message is displayed"):
        expect(login_page.error_message).to_be_visible()
        expect(login_page.error_message).to_contain_text(
            "Username and password do not match any user in this service"
        )


# Negative case: Verify login failed with invalid password
@allure.feature("Login UI")
@allure.story("Invalid password shows error message")
def test_login_failed_with_invalid_password(login_page):

    with allure.step("Login with invalid password"):
        login_page.login(
            INVALID_USER_PASSWORD["username"],
            INVALID_USER_PASSWORD["password"]
        )

        login_page.screenshot("invalid_password_error_message")

    with allure.step("Verify error message is displayed"):
        expect(login_page.error_message).to_be_visible()
        expect(login_page.error_message).to_contain_text(
            "Username and password do not match any user in this service"
        )


# Negative case: Verify login failed with empty password
@allure.feature("Login UI")
@allure.story("Empty password shows error message")
def test_login_failed_with_empty_password(login_page):

    with allure.step("Login with empty password"):
        login_page.login(
            EMPTY_USER_PASSWORD["username"],
            EMPTY_USER_PASSWORD["password"]
        )

        login_page.screenshot("empty_password_error_message")

    with allure.step("Verify error message is displayed"):
        expect(login_page.error_message).to_be_visible()
        expect(login_page.error_message).to_contain_text("Password is required")


# Negative case: Verify login failed with empty username
@allure.feature("Login UI")
@allure.story("Empty username shows error message")
def test_login_failed_with_empty_username(login_page):

    with allure.step("Login with empty username"):
        login_page.login(
            EMPTY_USER_USERNAME["username"],
            EMPTY_USER_USERNAME["password"]
        )

        login_page.screenshot("empty_username_error_message")

    with allure.step("Verify error message is displayed"):
        expect(login_page.error_message).to_be_visible()
        expect(login_page.error_message).to_contain_text("Username is required")