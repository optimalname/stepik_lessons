from selenium.webdriver.common.by import By


class LoginPageLocators():
    EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGISTER = (By.XPATH, "//button[@name='registration_submit']")


class CatalogBooksLocators():
    PRODUCT_NAME_C = (By.XPATH, "//a[@title='Expert C Programming']")
    PRODUCT_NAME_JAVA = (By.XPATH, "//a[@title='Reviewing Java']")
    BUTTON_ADD_TO_BASKET_NAME_C = (
    By.XPATH, "//div[@class='col-sm-8 col-md-9']//li[@class='col-xs-6 col-sm-4 col-md-3 col-lg-3'][1]//button")
    BUTTON_ADD_TO_BASKET_NAME_JAVA = (
    By.XPATH, "//div[@class='col-sm-8 col-md-9']//li[@class='col-xs-6 col-sm-4 col-md-3 col-lg-3'][3]//button")
    PRODUCT_IN_BASKET = (By.XPATH, "//div[@id='messages']/div[1]/div[@class='alertinner ']/strong")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BUTTON_TO_BASKET = (By.XPATH, "//div[@class='page_inner']//a[@class='btn btn-default']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    FIRST_BASKET_ITEM = (By.XPATH, "//div[@class='basket-items'][1]//h3/a")
    SECOND_BASKET_ITEM = (By.XPATH, "//div[@class='basket-items'][2]//h3/a")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET = (By.CSS_SELECTOR, "div#content_inner > p")
    INPUT_QUANTITY_PRODUCT_FIRST_ITEM = (By.CSS_SELECTOR, "#id_form-0-quantity")
    INPUT_QUANTITY_PRODUCT_SECOND_ITEM = (By.CSS_SELECTOR, "#id_form-1-quantity")
    BUTTON_UPDATE_BASKET = (By.XPATH, "//div[@class='basket-items'][1]//span[@class='input-group-btn']")
