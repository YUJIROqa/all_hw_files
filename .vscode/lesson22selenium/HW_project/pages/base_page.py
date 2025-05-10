from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def open_page(self, page_url):
        self.page_url = page_url
        self.driver.get(self.page_url)

    def get_title(self):
        return self.driver.title
    
    def is_element_present(self, locator):
       try:
           self.driver.find_element(*locator)
           return True
       except:
           return False
        
    def wait_for_element(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
    
    def take_screenshot(self, name):
        self.driver.save_screenshot(f'screenshots/{name}.png')
        
    
