from playwright.sync_api import Page

from src.components.button import Button
from src.components.text_input import TextInput
from src.config.config import Config


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = TextInput('div[data-testid="text-field-email-input"] input', page)
        self.password_input = TextInput('div[data-testid="text-field-password-input"] input', page)
        self.login_button = Button('button[data-testid="bo-dsm-common-button-contained-submit"]', page)

    def navigate(self):
        self.page.goto(Config.BASE_URL)
        self.wait_for_page_loaded()

    def wait_for_page_loaded(self):
        self.username_input.get_locator().wait_for(state="visible")
        self.password_input.get_locator().wait_for(state="visible")
        self.login_button.get_locator().wait_for(state="visible")

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
