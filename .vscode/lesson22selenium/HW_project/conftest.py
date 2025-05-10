from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from time import sleep

@pytest.fixture()
def driver():
    options = Options()
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.set_window_size(1920, 1080)
    chrome_driver.implicitly_wait(3)
    #options.add_argument('--headless')
    options.add_argument('--disable-dev-shm-usage')
    yield chrome_driver
    chrome_driver.quit()

@pytest.fixture()
def login_page(driver):
    from pages.login_pages import LoginPage
    return LoginPage(driver)