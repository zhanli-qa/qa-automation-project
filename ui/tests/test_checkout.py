import allure
from playwright.sync_api import expect
from test_data.ui.checkout import VALID_CHECKOUT_INFO, EMPTY_CHECKOUT_FIRSTNAME, EMPTY_CHECKOUT_LASTNAME
from common.utils.allure_helper import attach_screenshot, attach_current_url

@allure.feature("Checkout UI")
@allure.story("Checkout page displayed")
def test_checkout_page_displayed(inventory_page, cart_page, checkout_page):

    """
    E2E flow: login → inventory page → add product → go to cart page → checkout  → verify checkout page displayed
    """

    with allure.step("Add first product to cart"):
        inventory_page.add_first_product_to_cart()

    with allure.step("Go to cart page"):
        inventory_page.go_to_cart()

    with allure.step("Capture cart page state"):
        attach_current_url(cart_page)
        attach_screenshot(cart_page, "cart_page_state")

    with allure.step("Click checkout button"):
        cart_page.click_checkout()

    with allure.step("Verify checkout page displayed"):
        expect(checkout_page.firstname_input).to_be_visible()
        expect(checkout_page.lastname_input).to_be_visible()
        expect(checkout_page.postcode_input).to_be_visible()
        expect(checkout_page.cancel_button).to_be_visible()
        expect(checkout_page.continue_button).to_be_visible()
        expect(checkout_page.cart_icon).to_be_visible()

    with allure.step("Capture checkout page state"):
        attach_current_url(checkout_page)
        attach_screenshot(checkout_page, "checkout_page_state")


@allure.feature("Checkout UI")
@allure.story("checkout succeed")
def test_checkout_successfully_continue(inventory_page, cart_page, checkout_page, checkout_overview_page):
    """
        E2E flow: login → inventory page → add product → go to cart page → checkout
        → input valid firstname, lastname and postcode → navigate to checkout overview page
        """

    with allure.step("Add first product to cart"):
        inventory_page.add_first_product_to_cart()

    with allure.step("Go to cart page"):
        inventory_page.go_to_cart()

    with allure.step("Capture cart page state"):
        attach_current_url(cart_page)
        attach_screenshot(cart_page, "cart_page_state")

    with allure.step("Click checkout button"):
        cart_page.click_checkout()

    with allure.step("Capture checkout page state"):
        attach_current_url(checkout_page)
        attach_screenshot(checkout_page, "checkout_page_state")

    with allure.step("Fill up checkout information"):
        checkout_page = checkout_page.checkout(
            VALID_CHECKOUT_INFO["firstname"],
            VALID_CHECKOUT_INFO["lastname"],
            VALID_CHECKOUT_INFO["postcode"]
        )

    with allure.step("Verify navigate to checkout overview page"):
        expect(checkout_overview_page.shipping_information_label).to_be_visible()
        expect(checkout_overview_page.price_total_label).to_be_visible()
        expect(checkout_overview_page.price_total_label).to_be_visible()
        expect(checkout_overview_page.cancel_button).to_be_visible()
        expect(checkout_overview_page.finish_button).to_be_visible()

    with allure.step("Capture checkout overview page state"):
        attach_current_url(checkout_overview_page)
        attach_screenshot(checkout_overview_page, "checkout_overview_page_state")


@allure.feature("Checkout UI")
@allure.story("Checkout without firstname show error message")
def test_checkout_without_first_name(inventory_page, cart_page, checkout_page):
    """
    E2E flow: login → inventory page → add product → go to cart page → checkout
    → input valid lastname, postcode and empty firstname → error message
    """

    with allure.step("Add first product to cart"):
        inventory_page.add_first_product_to_cart()

    with allure.step("Go to cart page"):
        inventory_page.go_to_cart()

    with allure.step("Capture cart page state"):
        attach_current_url(cart_page)
        attach_screenshot(cart_page, "cart_page_state")

    with allure.step("Click checkout button"):
        cart_page.click_checkout()

    with allure.step("Fill up checkout information"):
        checkout_page = checkout_page.checkout(
            EMPTY_CHECKOUT_FIRSTNAME["firstname"],
            EMPTY_CHECKOUT_FIRSTNAME["lastname"],
            EMPTY_CHECKOUT_FIRSTNAME["postcode"]
        )

    with allure.step("Verify error message is displayed"):
        expect(checkout_page.error_message).to_be_visible()
        expect(checkout_page.error_message).to_contain_text(
            "First Name is required"
        )

    with allure.step("Capture checkout page verified state"):
        attach_current_url(checkout_page)
        attach_screenshot(checkout_page, "checkout_page_verified")


@allure.feature("Checkout UI")
@allure.story("Checkout without lastname show error message")
def test_checkout_without_first_name(inventory_page, cart_page, checkout_page):
    """
    E2E flow: login → inventory page → add product → go to cart page → checkout
    → input valid lastname, postcode and empty lastname → error message
    """

    with allure.step("Add first product to cart"):
        inventory_page.add_first_product_to_cart()

    with allure.step("Go to cart page"):
        inventory_page.go_to_cart()

    with allure.step("Capture cart page state"):
        attach_current_url(cart_page)
        attach_screenshot(cart_page, "cart_page_state")

    with allure.step("Click checkout button"):
        cart_page.click_checkout()

    with allure.step("Fill up checkout information"):
        checkout_page = checkout_page.checkout(
            EMPTY_CHECKOUT_LASTNAME["firstname"],
            EMPTY_CHECKOUT_LASTNAME["lastname"],
            EMPTY_CHECKOUT_LASTNAME["postcode"]
        )

    with allure.step("Verify error message is displayed"):
        expect(checkout_page.error_message).to_be_visible()
        expect(checkout_page.error_message).to_contain_text(
            "Last Name is required"
        )

    with allure.step("Capture checkout page verified state"):
        attach_current_url(checkout_page)
        attach_screenshot(checkout_page, "checkout_page_verified")



