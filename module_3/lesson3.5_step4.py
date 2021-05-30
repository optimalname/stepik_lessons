from selenium import webdriver
import time
import math
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_class_name('btn.btn-primary')
    button.click()
    alert = browser.switch_to.alert
    alert.accept()
    time.sleep(1)
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    print(x)
    y = calc(x)
    print(y)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    button = browser.find_element_by_class_name('btn.btn-primary')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()