from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_product_C_in_basket_page(self):
        assert self.browser.find_element(*BasketPageLocators.FIRST_BASKET_ITEM).text == self.browser.find_element(
            *BasketPageLocators.FIRST_BASKET_ITEM).text

    def should_be_product_Java_in_basket_page(self):
        assert self.browser.find_element(*BasketPageLocators.SECOND_BASKET_ITEM).text == self.browser.find_element(
            *BasketPageLocators.SECOND_BASKET_ITEM).text

    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, "There is not basket in url"

    def delete_first_item(self):
        first_item_input = self.browser.find_element(*BasketPageLocators.INPUT_QUANTITY_PRODUCT_FIRST_ITEM)
        first_item_input.clear()
        first_item_input.send_keys(0)

    def delete_second_item(self):
        second_item_input = self.browser.find_element(*BasketPageLocators.INPUT_QUANTITY_PRODUCT_SECOND_ITEM)
        second_item_input.clear()
        second_item_input.send_keys(0)

    def should_be_text_the_basket_is_empty(self):
        assert 'empty' in self.browser.find_element(*BasketPageLocators.EMPTY_BASKET).text, \
            'Basket not empty, but should be'

    def update_button(self):
        button = self.browser.find_element(*BasketPageLocators.BUTTON_UPDATE_BASKET)
        button.click()
