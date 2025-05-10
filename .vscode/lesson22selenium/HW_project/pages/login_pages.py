from pages.locators import login_locators
from pages.base_page import BasePage
class LoginPage(BasePage):


    def __init__(self, driver):
        super().__init__(driver, 'https://demowebshop.tricentis.com')
        self.url = 'https://demowebshop.tricentis.com/login'

    def open_page(self):
        super().open_page(self.url)

    def fill_email(self, email):
        self.driver.find_element(*login_locators.email_locator).send_keys(email)

    def fill_password(self, password):
        self.driver.find_element(*login_locators.password_locator).send_keys(password)

    def click_checkbox_remember(self):
        self.driver.find_element(*login_locators.checkbox_locator_remember).click()

    def click_login_button(self):
        self.driver.find_element(*login_locators.login_button_locator).click()

    def check_errors(self):
        return self.driver.find_element(*login_locators.error_text_locator).text
    
    def forgot_password(self):
        self.driver.find_element(*login_locators.forgot_password_locator).click()

    def check_your_authorized(self):
        return self.driver.find_element(*login_locators.you_authorized_locator).text

    

        