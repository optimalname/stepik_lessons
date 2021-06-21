import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Добавляем поддержку параметра language
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en-GB',
                     help="Choose language: ru, en-GB, es, fr")

# Добавляем фикстуру для передачи выбора браузера и локали сайта
@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    print(f"\nstart {language} version site")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)

    yield browser
    print("\nquit browser..")
    browser.quit()