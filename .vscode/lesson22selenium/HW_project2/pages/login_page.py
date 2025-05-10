from pages.base_page import BasePage
from pages.locators.login_locators import login_locators


class LoginPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver, 'https://the-internet.herokuapp.com')
        
    def open_page(self):
        super().open_page('https://the-internet.herokuapp.com/login')

    def login(self, username, password):
        self.input_text(login_locators.username_locator, username)
        self.input_text(login_locators.password_locator, password)
        self.click_element(login_locators.button_login_locator)

    def get_message(self):
        return self.get_text(login_locators.text_of_result_locator)
    
    def is_login_success(self):
        message = self.get_massage()
        return 'You logged into a secure area!' in message
        

    