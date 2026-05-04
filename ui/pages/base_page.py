
class BasePage:

    def __init__(self, page):
        self.page = page

    def screenshot(self):

        return self.page.screenshot(full_page=True)

    def click(self, locator):
        locator.click()

    def fill(self, locator, text):
        locator.fill(text)

    def get_text(self, locator):
        return locator.inner_text()


