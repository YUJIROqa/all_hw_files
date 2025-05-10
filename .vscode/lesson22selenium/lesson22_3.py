from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture()
def driver():
    browser_driver = webdriver.Chrome()
    browser_driver.maximize_window()
    browser_driver.implicitly_wait(10) #если в течении 5 секунд нет элемента, то выдает ошибку. это неявное ожидание
    yield browser_driver
    #sleep(3)

def test_clear(driver):
    input_data = 'Hello'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    sleep(3)
    text_string = driver.find_element(By.ID, 'id_text_string')
    text_string.send_keys(input_data)
    sleep(3)
    #text_string.clear()
    for i in range(len(input_data)):
        text_string.send_keys(Keys.BACK_SPACE)
    assert text_string.is_displayed()

def test_enabled_and_selected(driver):
    driver.get('https://www.qa-practice.com/elements/button/disabled')
    button = driver.find_element(By.NAME, 'submit')
    print(button.is_enabled())
    select = driver.find_element(By.ID, 'id_select_state')
    dropdown = Select(select)
    dropdown.select_by_value('enabled')

    print(button.is_enabled())


def test_5_seconds_wait(driver):
    driver.get('https://demoqa.com/dynamic-properties')
    button_click = driver.find_element(By.ID, 'visibleAfter')
    button_click.click()

def test_add_cart(driver):
    driver.get('https://magento.softwaretestingboard.com/olivia-1-4-zip-light-jacket.html')
    size = driver.find_element(By.ID, 'option-label-size-143-item-166')
    cplor = driver.find_element(By.ID, 'option-label-color-93-item-50')
    button_add = driver.find_element(By.ID, 'product-addtocart-button')
    size.click()
    cplor.click()
    button_add.click()
    WebDriverWait(driver, 5).until_not(
        EC.text_to_be_present_in_element_attribute(
            (By.CSS_SELECTOR, '.counter.qty'),
            'class', 
            'empty'
        )
    )

    counter = driver.find_element(By.CSS_SELECTOR, '.counter.qty')
    print(counter.text)



def test_5_seconds_2(driver):
    driver.get('https://demoqa.com/dynamic-properties')
    button_click = driver.find_element(By.ID, 'visibleAfter')
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button_click)
    #прокрутка страницы до элемента
    button_click.click()
    driver.add_cookie({'name': 'testname', 'value': 'testvalue'})
    print(driver.get_cookies())


def test_same_elements(driver):
    driver.get('https://magento.softwaretestingboard.com/men/bottoms-men/pants-men.html')
    product_link = driver.find_elements(By.CLASS_NAME, 'product-item-link')
    print(product_link[0].text) #распечатать текст 0(первого) элемента
    print(product_link[-1].text)#распечатать текст последнего элемента


    
def test_same_cards(driver):
    driver.get('https://magento.softwaretestingboard.com/men/bottoms-men/pants-men.html')
    product_link = driver.find_elements(By.CLASS_NAME, 'product-item-info')
    for cards in product_link:
        print(cards.find_element(By.CLASS_NAME, 'price').text)
    #print(product_link[0].find_element(By.CLASS_NAME, 'price').text)
   
