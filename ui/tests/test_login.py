import allure
import pytest
from playwright.sync_api import expect
from test_data.ui.login_user import (VALID_USER, INVALID_USER_NAME,
                                     INVALID_USER_PASSWORD, EMPTY_USER_PASSWORD, EMPTY_USER_USERNAME)
from common.utils.allure_helper import attach_screenshot, attach_current_url

pytestmark = pytest.mark.ui


# Verify login success
@allure.feature("Login UI")
@allure.story("Login Success")
def test_login_success(login_page):

    with allure.step("Login in with valid credentials"):
        inventory_page = login_page.login(
            VALID_USER["username"],
            VALID_USER["password"]
        )

    with allure.step("Capture post-login state"):
        attach_current_url(inventory_page)
        attach_screenshot(inventory_page, "after_success_login")

    with allure.step("Verify user redirect to inventory page"):
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

    with allure.step("Verify error message is displayed"):
        expect(login_page.error_message).to_be_visible()
        expect(login_page.error_message).to_contain_text(
            "Username and password do not match any user in this service"
        )

    with allure.step("capture failed state"):
        attach_current_url(login_page)
        attach_screenshot(login_page, "invalid_username_error_message")


# Negative case: Verify login failed with invalid password
@allure.feature("Login UI")
@allure.story("Invalid password shows error message")
def test_login_failed_with_invalid_password(login_page):

    with allure.step("Login with invalid password"):
        login_page.login(
            INVALID_USER_PASSWORD["username"],
            INVALID_USER_PASSWORD["password"]
        )

    with allure.step("Verify error message is displayed"):
        expect(login_page.error_message).to_be_visible()
        expect(login_page.error_message).to_contain_text(
            "Username and password do not match any user in this service"
        )

    with allure.step("capture failed state"):
        attach_current_url(login_page)
        attach_screenshot(login_page, "invalid_password_error_message")


# Negative case: Verify login failed with empty password
@allure.feature("Login UI")
@allure.story("Empty password shows error message")
def test_login_failed_with_empty_password(login_page):

    with allure.step("Login with empty password"):
        login_page.login(
            EMPTY_USER_PASSWORD["username"],
            EMPTY_USER_PASSWORD["password"]
        )

    with allure.step("Verify error message is displayed"):
        expect(login_page.error_message).to_be_visible()
        expect(login_page.error_message).to_contain_text("Password is required")

    with allure.step("capture failed state"):
        attach_current_url(login_page)
        attach_screenshot(login_page, "empty_password_error_message")


# Negative case: Verify login failed with empty username
@allure.feature("Login UI")
@allure.story("Empty username shows error message")
def test_login_failed_with_empty_username(login_page):

    with allure.step("Login with empty username"):
        login_page.login(
            EMPTY_USER_USERNAME["username"],
            EMPTY_USER_USERNAME["password"]
        )

    with allure.step("Verify error message is displayed"):
        expect(login_page.error_message).to_be_visible()
        expect(login_page.error_message).to_contain_text("Username is required")

    with allure.step("capture failed state"):
        attach_current_url(login_page)
        attach_screenshot(login_page, "empty_username_error_message")