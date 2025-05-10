from selenium.webdriver.common.by import By
from POM.pages.base_page import BasePage

class SalePage(BasePage):
    page_url = '/sale.html'
    # def __init__(self, driver2):
    #     self.driver2 = driver2

    # def open_page(self):
    #     self.driver2.get('https://magento.softwaretestingboard.com/sale.html')

    def check_page_header_title_is(self, text):
        header_title = self.driver2.find_element(By.TAG_NAME, 'h1')
        assert header_title.text == text
        