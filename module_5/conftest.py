import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime

# Добавляем поддержку параметра language
#def pytest_addoption(parser):
    #parser.addoption('--language', action='store', default='en-GB',
                     #help="Choose language: ru, en-GB, es, fr")

# Добавляем фикстуру для передачи выбора браузера и локали сайта
#@pytest.fixture(scope="function")
#def browser(request):
    #language = request.config.getoption("language")
    #browser_name = request.config.getoption("browser")
    #print(f"\nstart {language} version site")

    #options = Options()
    #options.add_experimental_option('prefs', {'intl.accept_languages': language})
    #browser = webdriver.Chrome(options=options)

    #yield browser
    #print("\nquit browser..")
    #browser.quit()

# Добавляем поддержку параметра browser
def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
        browser.maximize_window()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
        browser.maximize_window()
    else:
        print("Browser {} still is not implemented".format(browser_name))
    yield browser
    print("\nquit browser..")
    # получаем переменную с текущей датой и временем в формате ГГГГ-ММ-ДД_ЧЧ-ММ-СС
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    # делаем скриншот с помощью команды Selenium'а и сохраняем его с именем "screenshot-ГГГГ-ММ-ДД_ЧЧ-ММ-СС"
    browser.save_screenshot('screenshot-%s.png' % now)
    browser.quit()