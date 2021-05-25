from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute('valuex')
    print(x)
    y = calc(x)
    print(y)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    input2 = browser.find_element_by_css_selector("[id='robotCheckbox']")
    input2.click()
    Radio1 = browser.find_element_by_id("robotsRule")
    Radio1.click()
    button = browser.find_element_by_class_name('btn.btn-default')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
