from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage
from src.enums.currency import Currency

class MyHeritagePriceListPage(BasePage):
    CURRENCY_DROPDOWN = (By.CLASS_NAME, "user_currency")
    CURRENCY_OPTION_TEMPLATE = "//li[@class='inverse selector_item' and text()='{}']"
    PLAN_NAMES = (By.CSS_SELECTOR, ".plan_name")
    PLAN_PRICES = (By.CSS_SELECTOR, ".plan_price .list_price")

    def select_currency(self, currency: Currency):
        self.click(self.CURRENCY_DROPDOWN)
        currency_option_locator = (By.XPATH, self.CURRENCY_OPTION_TEMPLATE.format(currency.value))
        self.click(currency_option_locator)

    def get_yearly_plan_prices(self):
        names = self.find_elements(self.PLAN_NAMES)
        prices = self.find_elements(self.PLAN_PRICES)
        plans = []
        for name, price in zip(names, prices):
            plan_name = name.text.strip()
            plan_price = int(price.text.split('/')[0].replace('$','').strip())
            plans.append((plan_name, plan_price))
        return plans

    def fetch_myheritage_plans(self, currency=Currency.USD):
        self.select_currency(currency)
        return self.get_yearly_plan_prices()
