import pytest
from playwright.sync_api import sync_playwright
from src.config.credentials import Credentials

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

@pytest.fixture
def username():
    return Credentials.USERNAME

@pytest.fixture
def password():
    return Credentials.PASSWORD
