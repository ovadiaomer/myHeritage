from playwright.sync_api import Page, Locator as PlaywrightLocator

class Locator:
    def __init__(self, selector: str, page: Page):
        self.selector = selector
        self.page = page

    def get_locator(self) -> PlaywrightLocator:
        return self.page.locator(self.selector)

    def wait_for(self, state: str = "attached"):
        self.get_locator().wait_for(state=state)

    def click(self):
        self.get_locator().click()
