import allure
from playwright.sync_api import expect

@allure.feature("Cart UI")
@allure.story("Cart page display added product")
def test_cart_page_display_added_product(inventory_page, cart_page):

    """
    E2E flow: login → inventory page → add product → go to cart page → verify product displayed in cart
    """

    with allure.step("Get first product name from inventory page"):
        product = inventory_page.get_first_product()
        product_name = inventory_page.get_product_name_text(product)

    with allure.step("Add first product to cart"):
        inventory_page.add_first_product_to_cart()

    with allure.step("Go to cart page"):
        inventory_page.go_to_cart()

    with allure.step("Verify the first product displayed on cart page"):
        expect(cart_page.cart_badge).to_have_text("1")
        expect(cart_page.get_product_by_name(product_name)).to_be_visible()
        expect(cart_page.remove_button).to_be_visible()

        # allure attach
        cart_page.screenshot("added_product_displayed_in_cart_page")


@allure.feature("Cart UI")
@allure.story("Product is removed from cart page")
def test_remove_product_from_cart_page(inventory_page, cart_page):
    """
    E2E flow: login → inventory page → add product → go to cart page → remove → verify product is removed
    """

    with allure.step("Get first product name from inventory page"):
        product = inventory_page.get_first_product()
        product_name = inventory_page.get_product_name_text(product)

    with allure.step("Add first product to cart"):
        inventory_page.add_first_product_to_cart()

    with allure.step("Go to cart page"):
        inventory_page.go_to_cart()

    with allure.step("Verify the first product displayed on cart page"):
        expect(cart_page.remove_button).to_be_visible()
        expect(cart_page.get_product_by_name(product_name)).to_be_visible()
        expect(cart_page.cart_badge).to_have_text("1")

    with allure.step("Remove the product from cart page"):
        cart_page.remove_first_product_from_cart()

    with allure.step("Verify the product removed from cart page"):
        expect(cart_page.remove_button).not_to_be_visible()
        expect(cart_page.get_product_by_name(product_name)).not_to_be_visible()
        expect(cart_page.cart_badge).not_to_be_visible()

        # allure attach
        cart_page.screenshot("product_removed_from_cart_page")

@allure.feature("Cart UI")
@allure.story("Continue shopping from cart page")
def test_continue_shopping_from_cart_page(inventory_page, cart_page):
    """
    E2E flow: login → inventory page → go to cart page → continue shopping → verify redirect to inventory page
    """

    with allure.step("Go to cart page"):
        inventory_page.go_to_cart()

    with allure.step("Click continue shopping button"):
        cart_page.click_continue_shopping()

    with allure.step("Verify redirect to inventory page"):
        for product in inventory_page.product.all():
            expect(inventory_page.get_product_name_locator(product)).to_be_visible()
            expect(inventory_page.get_product_name_locator(product)).to_be_visible()
            expect(inventory_page.get_product_name_locator(product)).to_be_visible()

        # allure attach
        cart_page.screenshot("continue_shopping_from_cart_page")


@allure.feature("Cart UI")
@allure.story("Checkout from cart page")
def test_checkout_from_cart_page(inventory_page, cart_page, checkout_page):
    """
    E2E flow: login → inventory page → add product to cart → go to cart page → checkout → verify navigate to checkout page
    """

    with allure.step("Add first product to cart"):
        inventory_page.add_first_product_to_cart()

    with allure.step("Go to cart page"):
        inventory_page.go_to_cart()

    with allure.step("Click checkout button on cart page"):
        cart_page.click_checkout()

    with allure.step("Verify navigate to checkout page"):
        expect(checkout_page.firstname_input).to_be_visible()
        expect(checkout_page.lastname_input).to_be_visible()
        expect(checkout_page.postcode_input).to_be_visible()
        expect(checkout_page.cancel_button).to_be_visible()

        # allure attach
        cart_page.screenshot("checkout_from_cart_page")









