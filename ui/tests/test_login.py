from playwright.sync_api import expect
from ui.pages.login_page import LoginPage
from test_data.ui.login_user import (VALID_USER, INVALID_USER_NAME,
                                     INVALID_USER_PASSWORD, EMPTY_USER_PASSWORD, EMPTY_USER_USERNAME)

# Verify login success
def test_login_success(page):

    login_page = LoginPage(page)

    login_page.open()

    login_page.login(
        VALID_USER["username"],
        VALID_USER["password"]
    )

    expect(page.locator(".title")).to_have_text("Products")

# Negative case: Verify login failed with invalid username
def test_login_failed_with_invalid_username(page):

    login_page = LoginPage(page)

    login_page.open()

    login_page.login(
        INVALID_USER_NAME["username"],
        INVALID_USER_NAME["password"]
    )

    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text("Username and password do not match any user in this service")

# Negative case: Verify login failed with invalid password
def test_login_failed_with_invalid_password(page):
    login_page = LoginPage(page)

    login_page.open()

    login_page.login(
        INVALID_USER_PASSWORD["username"],
        INVALID_USER_PASSWORD["password"]
    )

    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text("Username and password do not match any user in this service")


# Negative case: Verify login failed with empty password
def test_login_failed_with_empty_password(page):
    login_page = LoginPage(page)

    login_page.open()

    login_page.login(
        EMPTY_USER_PASSWORD["username"],
        EMPTY_USER_PASSWORD["password"]
    )

    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text("Password is required")


# Negative case: Verify login failed with empty username
def test_login_failed_with_empty_username(page):
    login_page = LoginPage(page)

    login_page.open()

    login_page.login(
        EMPTY_USER_USERNAME["username"],
        EMPTY_USER_USERNAME["password"]
    )

    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text("Username is required")