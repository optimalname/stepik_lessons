import pytest
from selenium import webdriver
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('link_param', ["?promo=newYear"])
class TestProductPage:
    def test_guest_can_go_to_product_page(self, browser, link_param):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/{link_param}/"
        page = ProductPage(browser,
                        link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open() # открываем страницу

    def test_guest_can_add_product_to_basket(self, browser, link_param):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/{link_param}/"
        page = ProductPage(browser,
                        link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open() # открываем страницу
        page.should_be_add_to_cart_button() # проверяем что есть кнопка добавления в корзину
        page.ADDING_TO_BASKET() # жмем кнопку добавить в корзину
        page.should_be_success_messege() # проверяем что есть сообщение с нужным текстом