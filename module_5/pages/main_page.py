from .base_page import BasePage
from .locators import ProductPageLocators


class MainPage(BasePage):
    def __int__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)