from ui.pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        # Locators
        self.product = page.locator(".cart_item")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.remove_button = page.get_by_role("button", name="Remove")
        self.continue_shopping_button = page.get_by_role("button", name="Continue Shopping")
        self.checkout_button = page.get_by_role("button", name="Checkout")

    def get_product_by_name(self, name):
        return self.page.locator(".inventory_item_name", has_text=name)

    def get_first_product(self):
        """
        Get first product from cart page
        """
        return self.product.first

    def remove_first_product_from_cart(self):
        """
        Remove first product from cart page
        """
        return self.get_first_product().get_by_role("button", name="Remove").click()

    def click_continue_shopping(self):

        self.continue_shopping_button.click()

    def click_checkout(self):

        self.checkout_button.click()


