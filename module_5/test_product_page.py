import pytest
from .pages.product_page import ProductPage
import time

class TestProductPage:
    @pytest.mark.parametrize('promo_offer', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
    def test_guest_can_add_product_to_basket(self, browser, promo_offer):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
        page = ProductPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open() # открываем страницу
        page.should_be_button_add_to_basket() # проверяем что есть кнопка добавления в корзину
        page.add_product_to_basket() # жмем кнопку добавить в корзину
        page.solve_quiz_and_get_code() # обработка alert
        page.should_be_product_price() # проверяем что есть сообщение с нужным текстом
        page.should_be_product_in_basket()  # проверяем что есть сообщение с нужным текстом