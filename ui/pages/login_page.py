from ui.pages.inventory_page import InventoryPage
from ui.pages.base_page import BasePage
from common.config.config import config
class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        # Locators
        self.username_input = page.get_by_role("textbox", name="Username")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error_message = page.locator('[data-test="error"]')

    def login(self, username, password):
        self.fill(self.username_input, username)
        self.fill(self.password_input, password)
        self.click(self.login_button)
        return InventoryPage(self.page)

    def open(self):
        self.page.goto(config.UI_BASE_URL)




