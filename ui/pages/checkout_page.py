from ui.pages.base_page import BasePage
from ui.pages.checkout_overview_page import CheckoutOverviewPage

class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        # Locators
        self.firstname_input = page.locator("#first-name")
        self.lastname_input = page.locator("#last-name")
        self.postcode_input = page.locator("#postal-code")
        self.cancel_button = page.get_by_role("button", name="Cancel")
        self.continue_button = page.get_by_role("button", name="Continue")
        self.cart_icon = page.locator(".shopping_cart_link")
        self.error_message = page.locator('[data-test="error"]')

    def checkout(self, firstname, lastname, postcode):
        self.fill(self.firstname_input, firstname)
        self.fill(self.lastname_input, lastname)
        self.fill(self.postcode_input, postcode)

        self.click(self.continue_button)

        if self.error_message.is_visible():
            return self
        else:
            return CheckoutOverviewPage(self.page)





