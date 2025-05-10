import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def driver():
    options = Options()
    # options.add_argument("--headless")
    options.add_argument('--disable-dev-shm-usage')
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.set_window_size(1920, 1080)
    chrome_driver.implicitly_wait(10)
    
    yield chrome_driver
    
    chrome_driver.quit()

@pytest.fixture()
def login_page(driver):
    from pages.login_page import LoginPage
    return LoginPage(driver)