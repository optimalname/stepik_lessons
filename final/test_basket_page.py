import pytest
from .pages.catalog_books_page import CatalogBooksPage
from .pages.basket_page import BasketPage
import time


@pytest.mark.personal_tests
class TestProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.page = CatalogBooksPage(browser,
                                     'http://selenium1py.pythonanywhere.com/catalogue/category/books/non-fiction/essential-programming_6/'
                                     )  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        self.page.open()  # открываем страницу
        self.page.should_be_button_add_to_basket_C()  # проверяем что есть кнопка добавления в корзину книги 'Expert C Programming'
        self.page.add_product_C_to_basket()  # жмем кнопку добавить в корзину
        self.page.should_be_product_C_in_basket()  # проверяем, что добавленный продукт - это книга 'Expert C Programming'
        self.page.should_be_button_add_to_basket_Java()  # проверяем что есть кнопка добавления в корзину книги 'Reviewing Java'
        self.page.add_product_Java_to_basket()  # жмем кнопку добавить в корзину
        self.page.should_be_product_Java_in_basket()  # проверяем, что добавленный продукт - это книга 'Reviewing Java'
        self.page.go_to_basket_page()  # выполняем метод страницы - переходим на страницу корзины

    def test_guest_can_add_product_to_basket(self, browser):
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_product_C_in_basket_page()  # проверяем, что товар 'Expert C Programming' находится в корзине
        basket_page.should_be_product_Java_in_basket_page()  # проверяем, что товар 'Reviewing Java' находится в корзине
        basket_page.should_be_basket_url()  # проверяем, что мы находимся на странице корзины

    def test_guest_can_delete_product_from_basket(self, browser):
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.delete_first_item()
        basket_page.delete_second_item()
        basket_page.update_button()
        #time.sleep(3)
        basket_page.should_be_text_the_basket_is_empty()
