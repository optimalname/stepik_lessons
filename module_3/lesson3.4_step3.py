from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
def calc(x):
    return str(int(num1)+int(num2))

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x=0
    num1_element = browser.find_element_by_id("num1")
    num1 = num1_element.text
    print(num1)
    num2_element = browser.find_element_by_id("num2")
    num2 = num2_element.text
    print(num2)
    y = calc(x)
    print(y)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(y) # ищем элемент равных сумме num1 и num2
    button = browser.find_element_by_class_name('btn.btn-default')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
