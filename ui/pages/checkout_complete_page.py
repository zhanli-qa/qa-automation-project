from ui.pages.base_page import BasePage

class CheckoutCompletePage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        # Locators
        self.complete_header_label = page.locator('[data-test="complete-header"]')
        self.complete_text_label = page.locator('[data-test="complete-text"]')
        self.back_home_button = page.get_by_role("button", name="Back Home")