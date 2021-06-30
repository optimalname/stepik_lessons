from selenium.webdriver.common.by import By


class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")

class ProductPageLocators():
    PRODUCT_NAME = (By.XPATH, "//div[@class='col-sm-6 product_main']/h1")
    PRODUCT_PRICE = (By.XPATH, "//div[@class='col-sm-6 product_main']/p[@class='price_color']")
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_IN_BASKET = (By.XPATH, "//div[@id='messages']/div[1]/div[1]/strong")
    PRICE_OF_PRODUCT = (By.XPATH, "//div[@id='messages']/div[@class='alert alert-safe alert-noicon alert-info  fade in']//strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_TO_BASKET = (By.XPATH, "//div[@class='page_inner']//a[@class='btn btn-default']")

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')
    EMPTY_BASKET = (By.CSS_SELECTOR, 'div#content_inner > p')