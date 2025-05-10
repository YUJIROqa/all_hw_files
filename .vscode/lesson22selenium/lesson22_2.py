from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest

@pytest.fixture()
def driver():
    browser_driver = webdriver.Chrome()
    sleep(3)
    browser_driver.maximize_window()
    yield browser_driver
    sleep(3)

def test_id_name(driver):
    input_data = 'Hello'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    sleep(3)
    text_string = driver.find_element(By.ID, 'id_text_string')
    #text_string = driver.find_element(By.NAME, 'text_string')
    text_string.send_keys(input_data)
    sleep(3)
    #text_string.submit() #отправляет форму путем отправки
    text_string.send_keys(Keys.ENTER) #отправляет форму путем нажатия Enter
    result_text = driver.find_element(By.ID, 'result-text')
    assert result_text.text == input_data


def test_by_classname(driver):
    input_data = 'Hello'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    sleep(3)
    text_string = driver.find_element(By.CLASS_NAME, 'textInput')
    text_string.send_keys(input_data)
    sleep(3)
    text_string.send_keys(Keys.ENTER) #отправляет форму путем нажатия Enter
    result_text = driver.find_element(By.CLASS_NAME, 'result-text')
    assert result_text.text == input_data


def test_tagname(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Input field'


def test_link_text(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    contact_link = driver.find_element(By.LINK_TEXT, 'Contact')
    #contact_link = driver.find_element(By.PARTIAL_LINK_TEXT, 'act')# частичное совпадение
    contact_link.click()
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Contact us'


def test_css_selector(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    #text_string = driver.find_element(By.CSS_SELECTOR, "[placeholder = 'Submit me']")
    text_string = driver.find_element(By.CSS_SELECTOR, '.form-control')
    text_string.send_keys('Hello')
    #text_string.send_keys(Keys.ENTER)
    print(text_string.value_of_css_property('border-color'))
    assert text_string.get_attribute('placeholder') == 'Submit me'


def test_xpath(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_string = driver.find_element(By.XPATH, '//*[@id="id_text_string"]')
    text_string.send_keys('Hello')
    text_string.send_keys(Keys.ENTER)









   








sleep(3)