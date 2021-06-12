import pytest
from selenium import webdriver

search_text = {
    'ru': 'Добавить в корзину',
    'en-GB': 'Add to basket',
    'es': 'Añadir al carrito',
    'fr': 'Ajouter au panier'
}
page_lang = ".no-js"
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_search_availability_of_product(browser):

    # Arrange
    browser.get(link)

    # Act
    button_add_to_basket = browser.find_element_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket")
    browser.find_element_by_css_selector(page_lang).get_attribute("lang")

    # Assert
    assert button_add_to_basket.text in dict.values(search_text), "кнопка 'Добавить в корзину' отсутствует или текст не соответствует"
