from ui.pages.base_page import BasePage

class CheckoutOverviewPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        # Locators
        self.payment_information_label = page.locator('[data-test="payment-info-label"]')
        self.shipping_information_label = page.locator('[data-test="shipping-info-label"]')
        self.price_total_label = page.locator('[data-test="total-info-label"]')
        self.finish_button = page.get_by_role("button", name="Finish")
        self.cancel_button = page.get_by_role("button", name="Cancel")

    def click_finish(self):
        self.finish_button.click()
