from ui.pages.base_page import BasePage

class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        # Locators
        self.title = page.locator(".title")
        self.product = page.locator(".inventory_item")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.sort_dropdown = page.locator(".product_sort_container")
        self.cart_icon = page.locator(".shopping_cart_link")

    def get_product_name_text(self, product):
        """
        Get product name text
        """
        return product.locator(".inventory_item_name").inner_text()

    def get_product_name_locator(self, product):
        """
        Get product name locator
        """
        return product.locator(".inventory_item_name")

    def get_product_price(self, product):
        """
        Get product price
        """
        return product.locator(".inventory_item_price")

    def get_first_product(self):
        """
        Get first product
        """
        return self.product.first

    def add_first_product_to_cart(self):
        """
        Add first product to cart
        """
        return self.get_first_product().get_by_role("button", name="Add to cart").click()

    def remove_first_product_from_cart(self):
        """
        Remove first product from cart
        """
        return self.get_first_product().get_by_role("button", name="Remove").click()

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

    def get_add_to_cart_button(self, product):
        """
        Get add to cart button
        """
        return product.get_by_role("button", name="Add to cart")

    def get_remove_button(self, product):
        """
        Get remove button
        """
        return product.get_by_role("button", name="Remove")

    def add_products_to_cart(self, count):
        """
        Add multiple products to cart
        """
        for i in range(count):
            self.product.nth(i).get_by_role("button", name="Add to cart").click()

    def go_to_cart(self):
        """
        Click cart icon
        """
        self.cart_icon.click()
