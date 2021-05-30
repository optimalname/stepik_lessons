#1.1 добавить товар 'Expert C Programming' в Корзину
#1.2 перейти в окно Корзины
#1.3 убедиться что в Корзине есть товар 'Expert C Programming'

from selenium import webdriver

main_page_link = "http://selenium1py.pythonanywhere.com/ru/catalogue/category/books/non-fiction/essential-programming_6/"

search_button_add_in_basket = "//li[1]//button" # поиск кнопки "Добавить в корзину" для товара 'Expert C Programming' (не удалось найти нормального атрибута для поиска)
search_button_contents_of_basket = "//a[@class='btn btn-default']" # поиск кнопки "Посмотреть корзину"
search_product_in_basket = "//a[text()='Expert C Programming']" # поиск товара 'Expert C Programming' в корзине

def test_product_adding_in_basket():
    # Data
    search_text = "Expert C Programming"

    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(main_page_link)

        # Act
        browser.find_element_by_xpath(search_button_add_in_basket).click()
        browser.find_element_by_xpath(search_button_contents_of_basket).click()

        # Assert
        assert search_text in browser.find_element_by_xpath(search_product_in_basket).text, \
            "product 'Expert C Programming' not found"

    finally:
        browser.quit()

test_product_adding_in_basket()