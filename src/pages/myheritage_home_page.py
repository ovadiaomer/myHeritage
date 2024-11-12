from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage


class MyHeritageHomePage(BasePage):
    PRICE_LIST_LINK = (By.CSS_SELECTOR, "a[data-automations='pricing']")

    def click_price_list(self):
        # Require extra scroll due to save cookie bar overlay causing element not interacting
        element = self.wait.until(EC.element_to_be_clickable(self.PRICE_LIST_LINK))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("window.scrollBy(0, 100);")
        element.click()
