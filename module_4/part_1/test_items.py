import pytest
from selenium import webdriver
coders_at_work = "//p[@class='instock availability']"

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_search_availability_of_product(browser):
    #Data
    search_text = "На складе"

    #Arrange
    browser.get(link)

    #Act даже не знаю что указать тут, т.к. действие одно - проверить наличие товара
    #browser.find_element_by_by_xpath(coders_at_work)

    # Assert
    assert search_text in browser.find_element_by_xpath(coders_at_work).text, \
        "продукта 'Coders at Work' нет на складе"

