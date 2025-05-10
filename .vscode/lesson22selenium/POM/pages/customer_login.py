from POM.pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait

from POM.pages.locators
class CustomerLogin(BasePage):
    page_url = '/customer/account/login/'
    # def __init__(self, driver2):
    #     self.driver2 = driver2

    # def open_page(self):
    #     self.driver2.get('https://magento.softwaretestingboard.com/customer/account/login/')

    
    def fill_login_form(self, login, password):
        email_field = self.driver2.find_element(By.ID, 'email')
        email_field.send_keys(login)
        password_field = self.driver2.find_element(By.ID, 'pass')
        password_field.send_keys(password)
        button = self.driver2.find_element(By.ID, 'send2')
        button.click()

    def check_error_alert(self, text):
        error_alert = self.driver2.find_element(By.CSS_SELECTOR, '[data-bind="html: $parent.prepareMessageForHtml(message.text)"]')
        assert error_alert.text == text
