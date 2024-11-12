from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from src.pages.base_page import BasePage


class GoogleSearchPage(BasePage):
    SEARCH_INPUT = (By.NAME, "q")
    RESULT_LINKS = (By.CSS_SELECTOR, "a")
    URL = "https://www.google.com/"

    def search(self, text):
        self.enter_text(self.SEARCH_INPUT, text)
        self.driver.find_element(*self.SEARCH_INPUT).submit()
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )

    def click_non_ad_link(self, link_substring):
        results = self.find_elements(self.RESULT_LINKS)
        for result in results:
            href = result.get_attribute('href')
            if href and link_substring in href and "ad" not in result.get_attribute("class").lower():
                result.click()
                break

    def navigate(self):
        self.navigate_to(self.URL)

    def search_and_click_link(self, search_term, link_substring):
        self.search(search_term)
        self.click_non_ad_link(link_substring)