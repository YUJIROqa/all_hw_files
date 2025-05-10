from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 

class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def open_page(self, page_url):
        self.page_url = page_url
        self.driver.get(self.page_url)

    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
            return True
        except:
            return False
        
    def wait_for_element(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        self.find_element(locator).click()

    def input_text(self, locator, text):
        self.find_element(locator).send_keys(text)

    def get_text(self, locator):
        return self.find_element(locator).text
    
 
        
        
