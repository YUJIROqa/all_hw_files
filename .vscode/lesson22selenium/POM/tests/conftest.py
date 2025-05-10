from selenium import webdriver
import pytest
from time import sleep
from selenium.webdriver.chrome.options import Options

@pytest.fixture() #создаем фикстуру которая будет открывать/закрывать браузер и передавать настройки
def driver2():
    options = Options() #создаем настройки для браузера
    options.add_argument("start-maximized") #максимизируем окно браузера
    # options.add_argument("--disable-cookie-encryption")
    # #options.add_argument("--disable-notifications")
    # options.add_argument("--disable-popup-blocking")
    # options.add_experimental_option("prefs", {
    #     "profile.default_content_setting_values.cookies": 2,
    #     "profile.block_third_party_cookies": False
    # })
    driver = webdriver.Chrome(options=options) #создаем драйвер браузера, который будет к нему обращаться
    yield driver #возвращаем драйвер браузера
    sleep(3) #ждем 3 секунды
    driver.quit() #закрываем браузер