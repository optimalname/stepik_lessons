from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            'Some items are in basket, but should not be'

    def should_be_text_the_basket_is_empty(self):
        assert 'empty' in self.browser.find_element(*BasketPageLocators.EMPTY_BASKET).text, \
            'Basket not empty, but should be'