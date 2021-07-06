from .base_page import BasePage
from .locators import CatalogBooksLocators


class CatalogBooksPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_C_in_basket()
        self.should_be_product_Java_in_basket()
        self.should_be_button_add_to_basket_C()
        self.should_be_button_add_to_basket_Java()

    def should_be_button_add_to_basket_C(self):
        assert self.is_element_present(
            *CatalogBooksLocators.BUTTON_ADD_TO_BASKET_NAME_C), "Button add to basket is not presented"

    def should_be_button_add_to_basket_Java(self):
        assert self.is_element_present(
            *CatalogBooksLocators.BUTTON_ADD_TO_BASKET_NAME_JAVA), "Button add to basket is not presented"

    def add_product_C_to_basket(self):
        add_product_C_to_basket = self.browser.find_element(*CatalogBooksLocators.BUTTON_ADD_TO_BASKET_NAME_C)
        add_product_C_to_basket.click()

    def add_product_Java_to_basket(self):
        add_product_Java_to_basket = self.browser.find_element(*CatalogBooksLocators.BUTTON_ADD_TO_BASKET_NAME_JAVA)
        add_product_Java_to_basket.click()

    def should_be_product_C_in_basket(self):
        assert 'Expert C Programming' in self.browser.find_element(
            *CatalogBooksLocators.PRODUCT_IN_BASKET).text, "Message with product 'C' in basket is not presented"

    def should_be_product_Java_in_basket(self):
        assert 'Reviewing Java' in self.browser.find_element(
            *CatalogBooksLocators.PRODUCT_IN_BASKET).text, "Message with product 'Java' in basket is not presented"
