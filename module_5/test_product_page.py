from .pages.product_page import ProductPage

class TestProductPage:
    def test_guest_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser,
                        link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open() # открываем страницу
        page.should_be_button_add_to_basket() # проверяем что есть кнопка добавления в корзину
        page.add_product_to_basket() # жмем кнопку добавить в корзину
        page.solve_quiz_and_get_code() # обработка alert
        page.should_be_product_price() # проверяем что есть сообщение с нужным текстом
        page.should_be_product_in_basket()  # проверяем что есть сообщение с нужным текстом