import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Добавляем поддержку параметра language
def pytest_addoption_lang(parser):
    parser.addoption_lang('--language', action='store', default=None,
                     help="Choose language: ru, en-GB, es, fr")

# Добавляем поддержку параметра browser
def pytest_addoption_browser(parser):
    parser.addoption_browser('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")

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

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser
    print("\nquit browser..")
    browser.quit()