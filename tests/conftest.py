import pytest
from selenium import webdriver

from src.pages.page_factory import PageFactory


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def pages(driver):
    return PageFactory(driver)