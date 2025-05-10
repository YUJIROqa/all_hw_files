from selenium.webdriver.remote.webdriver import WebDriver

class BasePage:

    base_url = 'https://magento.softwaretestingboard.com/'
    base_url = None
    def __init__(self, driver2: WebDriver):
        self.driver2 = driver2

 
    def open_page(self):
        if self.page_url:
            self.driver2.get(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page url is not defined')

    def find(self, locator: tuple):
        self.driver2.find_element(*locator)

    def find_all(self, locator: tuple):
        self.driver2.find_elements(*locator)
