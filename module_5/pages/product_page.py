from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_in_basket()
        self.should_be_product_price()
        self.should_be_button_add_to_basket()

    def should_be_button_add_to_basket(self):
        assert self.is_element_present(
            *ProductPageLocators.BUTTON_ADD_TO_BASKET), "Button add to basket is not presented"

    def add_product_to_basket(self):
        add_product_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        add_product_to_basket.click()

    def should_be_product_price(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text == self.browser.find_element(
            *ProductPageLocators.PRICE_OF_PRODUCT).text, "Message with price of product is not presented"

    def should_be_product_in_basket(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == self.browser.find_element(
            *ProductPageLocators.PRODUCT_IN_BASKET).text, "Message with product in basket is not presented"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.PRODUCT_IN_BASKET), "Success message is presented, but shold not be"

    def should_be_disappear_element(self):
        assert self.is_disappeared(
            *ProductPageLocators.PRODUCT_IN_BASKET), "Success message is presented, element is not disappeared"
