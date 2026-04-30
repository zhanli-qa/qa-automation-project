from common.config.config import config
class LoginPage:

    def __init__(self, page):
        self.page = page
        self.username_input = page.get_by_role("textbox", name="Username")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error_message = page.locator('[data-test="error"]')

    def open(self):
        self.page.goto(config.UI_BASE_URL)

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

