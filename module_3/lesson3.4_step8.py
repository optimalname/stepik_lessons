from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Evgeny")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Spasov")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("test@gmail.com")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    element = browser.find_element_by_id("file")
    element.send_keys(file_path)
    button = browser.find_element_by_class_name('btn.btn-primary')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()