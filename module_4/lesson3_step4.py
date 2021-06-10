from selenium import webdriver
import unittest

main_page_link = "http://suninjuly.github.io/registration1.html"
second_page_link = "http://suninjuly.github.io/registration2.html"

input1 = '.first_block:nth-child(1) .form-control.first'
input2 = 'div .first_block .form-control.second'
input3 = 'div .first_block .form-control.third'
button = 'button.btn'

class TestUnittest(unittest.TestCase):
    def test_page_main(self):
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(main_page_link)

        # Act
        # Ваш код, который заполняет обязательные поля
        browser.find_element_by_css_selector(input1).send_keys("Ivan")
        browser.find_element_by_css_selector(input2).send_keys("Petrov")
        browser.find_element_by_css_selector(input3).send_keys("test@mail.ru")

        # Отправляем заполненную форму
        browser.find_element_by_css_selector(button).click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")
    def test_page_second(self):
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(second_page_link)

        # Act
        # Ваш код, который заполняет обязательные поля
        browser.find_element_by_css_selector(input1).send_keys("Ivan")
        browser.find_element_by_css_selector(input2).send_keys("Petrov")
        browser.find_element_by_css_selector(input3).send_keys("test@mail.ru")

        # Отправляем заполненную форму
        browser.find_element_by_css_selector(button).click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

if __name__ == "__main__":
    unittest.main()