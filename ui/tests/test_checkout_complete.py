import allure
from playwright.sync_api import expect
from test_data.ui.checkout import VALID_CHECKOUT_INFO

@allure.feature("Finish UI")
@allure.story("Checkout complete displayed")
def test_checkout_completely(inventory_page, cart_page, checkout_page, checkout_overview_page, checkout_complete_page):

    """
    E2E flow: login → inventory page → add product → go to cart page → checkout
                    → fill up checkout firstname, lastname and postcode and click continue
                    → checkout overview page → click finish → checkout completely
    """

    with allure.step("Add first product to cart"):
        inventory_page.add_first_product_to_cart()

    with allure.step("Go to cart page"):
        inventory_page.go_to_cart()

    with allure.step("Click checkout button"):
        cart_page.click_checkout()

    with allure.step("Fill up checkout information"):
        checkout_page.checkout(
            VALID_CHECKOUT_INFO["firstname"],
            VALID_CHECKOUT_INFO["lastname"],
            VALID_CHECKOUT_INFO["postcode"]
        )

    with allure.step("Click finish button on checkout overview page"):
        checkout_overview_page.click_finish()

    with allure.step("Verify checkout completely in checkout complete page"):
        expect(checkout_complete_page.complete_header_label).to_be_visible()
        expect(checkout_complete_page.complete_text_label).to_be_visible()
        expect(checkout_complete_page.back_home_button).to_be_visible()

        # allure attach
        checkout_complete_page.screenshot("checkout completely")

