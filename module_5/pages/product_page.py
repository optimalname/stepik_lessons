from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_in_basket()
        self.should_be_product_price()

    def should_be_product_in_basket(self):
        assert self.is_element_present(*ProductPageLocators,)

    def go_to_product_page(self):
        button = self.browser.find_element(*ProductPageLocators.ADDING_TO_BASKET)
        button.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)