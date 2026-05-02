import pytest
import allure
from ui.pages.login_page import LoginPage
from test_data.ui.login_user import VALID_USER
from ui.pages.cart_page import CartPage
from ui.pages.checkout_page import CheckoutPage
from ui.pages.checkout_overview_page import CheckoutOverviewPage
from ui.pages.checkout_complete_page import CheckoutCompletePage

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

# Fixture cart page
@pytest.fixture
def cart_page(inventory_page):
    """
    cart page depends on inventory page
    """
    return CartPage(inventory_page.page)


@pytest.fixture
def checkout_page(cart_page):
    """
    checkout page depends on cart_page
    """
    return CheckoutPage(cart_page.page)


@pytest.fixture
def checkout_overview_page(checkout_page):
    """
    checkout overview page depends on checkout page
    """
    return CheckoutOverviewPage(checkout_page.page)


@pytest.fixture
def checkout_complete_page(checkout_overview_page):
    """
    checkout complete page depends on checkout overview page
    """
    return CheckoutCompletePage(checkout_overview_page.page)






