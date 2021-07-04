import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime


# Добавляем поддержку параметра language
# Добавляем поддержку параметра browser
def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en-GB',
                     help="Choose language: ru, en-GB, es, fr")


# Добавляем фикстуру для передачи выбора браузера и локали сайта
@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser = request.config.getoption("browser")
    if browser == "chrome":
        print(f"\nstart {language} version site\nstart {browser} browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
        browser.maximize_window()
    elif browser == "firefox":
        print(f"\nstart {language} version site\nstart {browser} browser for test..")
        browser = webdriver.Firefox()
        browser.maximize_window()
    else:
        print("Browser {} still is not implemented".format(browser))
    yield browser
    print("\nquit browser..")
    # получаем переменную с текущей датой и временем в формате ГГГГ-ММ-ДД_ЧЧ-ММ-СС
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    # делаем скриншот с помощью команды Selenium'а и сохраняем его с именем "screenshot-ГГГГ-ММ-ДД_ЧЧ-ММ-СС"
    browser.save_screenshot('screenshot-%s.png' % now)
    browser.quit()
