from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form"),
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form"),
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")

class ProductPageLocators():
    ADDING_TO_BASKET = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_IN_BASKET = (By.XPATH, "//div[@id='messages']/div[1]/div[1]/strong")
    PRICE_OF_PRODUCT = (By.XPATH, "//div[@id='messages']/div[3]//p[1]")