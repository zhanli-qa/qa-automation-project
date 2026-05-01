import allure
class BasePage:

    def __init__(self, page):
        self.page = page

    def screenshot(self, name="screenshot"):
        screenshot = self.page.screenshot(full_page=True)

        allure.attach(
            screenshot,
            name=name,
            attachment_type=allure.attachment_type.PNG
        )

        return screenshot

    def click(self, locator):
        locator.click()

    def fill(self, locator, text):
        locator.fill(text)

    def get_text(self, locator):
        return locator.inner_text()


