from ui.pages.base_page import BasePage

class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        # Locators
        self.title = page.locator(".title")
        self.products = page.locator(".inventory_item")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.sort_dropdown = page.locator(".product_sort_container")

    def add_products_to_cart(self, count):
        """
        Add multiple products to cart
        """
        for i in range(count):
            self.products.nth(i).get_by_role("button", name="Add to cart").click()


    def get_product_prices(self):
        """
        Get all product prices
        """
        price_elements = self.page.locator(".inventory_item_price").all()

        prices = []
        for element in price_elements:
            text = element.inner_text()
            price = float(text.replace("$", ""))
            prices.append(price)

        return prices
