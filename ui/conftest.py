import pytest
import allure
from ui.pages.login_page import LoginPage

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    # only screenshot when the test failed
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






