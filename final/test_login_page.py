from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import pytest
import time


@pytest.mark.personal_tests
class TestLoginPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.page = MainPage(browser, 'http://selenium1py.pythonanywhere.com/')  # начинае тест с запуска основной страницы
        self.page.open()

    def test_guest_can_authorized_user(self, browser):
        page = LoginPage(browser,
                         browser.current_url)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.go_to_login_page()  # переходим на страницу логина
        page.register_new_user(str(time.time()) + "@fakemail.org", "asdFHSA234", "asdFHSA234")   # регистрируем нового пользователя с валидными данными
        page.should_be_authorized_user()  # проверяем что пользователь зарегистрирован

    @pytest.mark.xfail(reason="The user is not authorized, but also should not be")
    def test_guest_input_wrong_email_for_authorized_user(self, browser):
        page = LoginPage(browser,
                         browser.current_url)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.go_to_login_page()
        page.register_new_user(str(time.time()) + "fakemail.org", "asdFHSA234", "asdFHSA234")   # вводим неверный email - отсутствует @
        page.should_not_be_authorized_user()  # проверяем что регистрация не пройдет

    @pytest.mark.xfail(reason="The password is too short")
    def test_guest_input_wrong_password_for_authorized_user(self, browser):
        page = LoginPage(browser,
                         browser.current_url)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.go_to_login_page()
        page.register_new_user(str(time.time()) + "@fakemail.org", "фывфыщщл", "фывфыщщл")   # вводим слабый пароль
        page.should_not_be_authorized_user()  # проверяем что регистрация не пройдет

    @pytest.mark.xfail(reason="The confirm password is empty")
    def test_guest_input_wrong_empty_password_for_authorized_user(self, browser):
        page = LoginPage(browser,
                         browser.current_url)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.go_to_login_page()
        page.register_new_user(str(time.time()) + "@fakemail.org", "passWord123", "")  # оставляем пустым поле для повтора пароля
        page.should_not_be_authorized_user()  # проверяем что регистрация не пройдет
