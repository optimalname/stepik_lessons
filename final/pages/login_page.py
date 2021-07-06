from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password, confirm_password):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        email_input.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_input.send_keys(password)
        password_input_confirm = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_INPUT)
        password_input_confirm.send_keys(confirm_password)
        self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER).click()
