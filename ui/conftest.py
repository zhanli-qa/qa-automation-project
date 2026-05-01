import pytest
import allure
from ui.pages.login_page import LoginPage
from test_data.ui.login_user import VALID_USER

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    # auto screenshot only when the test failed
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page", None)

        if page is not None:

            allure.attach(
                page.screenshot(full_page=True),
                name=f"failure_{item.name}",
                attachment_type=allure.attachment_type.PNG
            )

# Fixture Open Login page
@pytest.fixture
def login_page(page):

    login_page = LoginPage(page)

    login_page.open()

    return login_page


# Fixture inventory page
@pytest.fixture
def inventory_page(login_page):
    """
    inventory page depends on login page
    """
    inventory_page = login_page.login(
        VALID_USER["username"],
        VALID_USER["password"]
    )

    return inventory_page






