from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import pytest
from selenium.webdriver.common.keys import Keys
import random
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import logging
import os

@pytest.fixture() #создаем фикстуру которая будет открывать/закрывать браузер и передавать настройки
def driver():
    options = Options() #создаем настройки для браузера
    options.add_argument("start-maximized") #максимизируем окно браузера
    options.add_argument("--disable-cookie-encryption")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.cookies": 2,
        "profile.block_third_party_cookies": False
    })
    driver = webdriver.Chrome(options=options) #создаем драйвер браузера, который будет к нему обращаться
    yield driver #возвращаем драйвер браузера
    sleep(3) #ждем 3 секунды
    driver.quit() #закрываем браузер


def test_scroll(driver):
    driver.get('https://www.onliner.by/')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    sleep(3)
   
def test_scroll_to_element(driver):
    driver.get('https://the-internet.herokuapp.com/')
    link = driver.find_element(By.LINK_TEXT, 'JQuery UI Menus')
    sleep(3)
    driver.execute_script("arguments[0].scrollIntoView();", link)
    sleep(3)

def test_upload_file(driver):
    driver.get('https://the-internet.herokuapp.com/upload')
    upload = driver.find_element(By.ID, 'file-upload')
    button = driver.find_element(By.ID, 'file-submit')
    upload.send_keys('C:\\Users\\admin\\test.txt')
    button.click()
    sleep(3)
    
   
    
    
    
    

