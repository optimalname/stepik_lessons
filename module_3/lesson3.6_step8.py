from selenium import webdriver
import math
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = ("http://suninjuly.github.io/explicit_wait2.html")

try:
    browser = webdriver.Chrome()
    browser.get(link)

    optimal_x = WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.ID, 'price'), "$100"))
    button = browser.find_element_by_id("book")
    button.click()
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    print(x)
    y = calc(x)
    print(y)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    button = browser.find_element_by_id('solve')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()