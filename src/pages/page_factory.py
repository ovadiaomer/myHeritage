from src.pages.google_search_page import GoogleSearchPage
from src.pages.myheritage_home_page import MyHeritageHomePage
from src.pages.myheritage_price_list_page import MyHeritagePriceListPage

class PageFactory:
    def __init__(self, driver):
        self.driver = driver

    @property
    def google_search_page(self):
        return GoogleSearchPage(self.driver)

    @property
    def myheritage_home_page(self):
        return MyHeritageHomePage(self.driver)

    @property
    def myheritage_price_list_page(self):
        return MyHeritagePriceListPage(self.driver)
