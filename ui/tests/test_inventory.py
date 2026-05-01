import allure
from playwright.sync_api import expect

@allure.feature("Products UI")
@allure.story("Product list is displayed")
def test_product_list_displayed(inventory_page):

    with allure.step("Verify product list is displayed"):
        expect(inventory_page.products).to_have_count(6)

    with allure.step("Verify each product has name, price, add to cart button"):
        for product in inventory_page.products.all():
            expect(product.locator(".inventory_item_name")).to_be_visible()
            expect(product.locator(".inventory_item_price")).to_be_visible()
            expect(product.locator("button")).to_be_visible()

        # allure attach
        inventory_page.screenshot("product_list_displayed")

@allure.feature("Products UI")
@allure.story("Add one product to cart")
def test_add_one_product_to_cart(inventory_page):

    product = inventory_page.products.first

    with allure.step("Verify initial state"):
        expect(product.get_by_role("button", name="Add to cart")).to_be_visible()
        expect(inventory_page.cart_badge).not_to_be_visible()

    with allure.step("Add product to cart"):
        product.get_by_role("button", name="Add to cart").click()

    with allure.step("Verify product added"):
        expect(product.get_by_role("button", name="Remove")).to_be_visible()
        expect(inventory_page.cart_badge).to_have_text("1")

        # allure attach
        inventory_page.screenshot("product_added_to_cart")

@allure.feature("Products UI")
@allure.story("Remove product from cart")
def test_remove_product_from_cart(inventory_page):

    product = inventory_page.products.first

    with allure.step("Verify initial state"):
        expect(product.get_by_role("button", name="Add to cart")).to_be_visible()
        expect(inventory_page.cart_badge).not_to_be_visible()

    with allure.step("Add product to cart"):
        product.get_by_role("button", name="Add to cart").click()

    with allure.step("Verify product added"):
        expect(product.get_by_role("button", name="Remove")).to_be_visible()
        expect(inventory_page.cart_badge).to_have_text("1")

    with allure.step("Remove product from cart"):
        product.get_by_role("button", name="Remove").click()

    with allure.step("Verify product removed"):
        expect(product.get_by_role("button", name="Add to cart")).to_be_visible()
        expect(inventory_page.cart_badge).not_to_be_visible()

        # allure attach
        inventory_page.screenshot("product_removed_from_cart")

@allure.feature("Products UI")
@allure.story("Add multiple products to cart")
def test_add_multiple_products_to_cart(inventory_page):

    with allure.step("Verify initial state"):
        expect(inventory_page.cart_badge).not_to_be_visible()

    with allure.step("Add multiple products to cart"):
        inventory_page.add_products_to_cart(3)

    with allure.step("Verify products added to cart"):
        expect(inventory_page.cart_badge).to_be_visible()
        expect(inventory_page.cart_badge).to_have_text("3")

        # allure attach
        inventory_page.screenshot("multiple_products_added_to_cart")

@allure.feature("Products UI")
@allure.story("Sort products by price low to high")
def test_sort_products_by_price_low_to_high(inventory_page):

    with allure.step("Select price low to high"):
        inventory_page.sort_dropdown.select_option("lohi")

    with allure.step("Get all product prices"):
        prices = inventory_page.get_product_prices()

    with allure.step("Verify prices are sorted ascending"):
        assert prices == sorted(prices)

        # allure attach
        inventory_page.screenshot("after_prices_sorted_ascending")










