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

def test_first(driver): #передаем драйвер в тест(он будет открыт/закрыт автоматически и иметь настройки)
    driver.get(' https://the-internet.herokuapp.com/') #открываем сайт
    assert driver.title == 'The Internet' #проверяем что заголовок сайта соответствует ожидаемому
    print('driver.title: ', driver.title) #выводим заголовок сайта
    
    assert driver.current_url == 'https://the-internet.herokuapp.com/' #проверяем что текущий url соответствует ожидаемому
    print('driver.current_url: ', driver.current_url)

def test_second(driver):

    driver.get('https://www.saucedemo.com/')
    input_name = driver.find_element(By.ID, 'user-name')#находим элемент по id
    input_password = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Password"]')#находим элемент по css селектору
    botton_login = driver.find_element(By.NAME, 'login-button')#находим элемент по name

    assert input_name.is_displayed()#проверяем что элемент отображается
    assert input_password.is_displayed()#проверяем что элемент отображается
    assert botton_login.is_displayed()#проверяем что элемент отображается

    input_name.send_keys('standard_user')#вводим в поле стандартный пользователь
    assert input_name.get_attribute('value') == 'standard_user'#проверяем что в поле введен стандартный пользователь
    input_password.send_keys('secret_sauce')#вводим в поле секретный соус
    assert input_password.get_attribute('value') == 'secret_sauce'#проверяем что в поле введен секретный соус
    botton_login.click()#кликаем на кнопку входа

    assert driver.current_url == 'https://www.saucedemo.com/inventory.html'#проверяем что текущий url соответствует ожидаемому
    
    assert driver.title == 'Swag Labs'#проверяем что заголовок сайта соответствует ожидаемому

    check_all_cards = driver.find_elements(By.CLASS_NAME, 'inventory_item_description')#находим все элементы по классу
    print(check_all_cards[0].text)#выводим текст первого элемента
    print(check_all_cards[-1].text)#выводим текст последнего элемента

    selector = driver.find_element(By.CLASS_NAME, 'product_sort_container')#находим элемент по классу
    select = Select(selector)#создаем объект для работы с выпадающим списком
    select.select_by_value('hilo')#выбираем значение в выпадающем списке
    sleep(3)#ждем 3 секунды

    check_all_cards = driver.find_elements(By.CLASS_NAME, 'inventory_item_description')#находим все элементы по классу
    print(check_all_cards[0].text)#выводим текст первого элемента
    sleep(2)#ждем 2 секунды

    find_sauce_jacket = driver.find_element(By.ID, 'add-to-cart-sauce-labs-fleece-jacket')#находим элемент по id
    find_sauce_jacket.click()#кликаем на элемент
    sleep(3)#ждем 3 секунды
               
    find_basket = driver.find_element(By.CLASS_NAME, 'shopping_cart_link') #находим элемент по классу
    find_basket.click()#кликаем на элемент
    sleep(3)#ждем 3 секунды
    
    find_item = driver.find_element(By.ID, 'item_5_title_link')#находим элемент по id
    assert find_item.is_displayed()#проверяем что элемент отображается
    sleep(2)#ждем 2 секунды

    find_remove = driver.find_element(By.CSS_SELECTOR, '.btn.btn_secondary.btn_small.cart_button')#находим элемент по css селектору
    find_remove.click()#кликаем на элемент
    sleep(2)#ждем 2 секунды
    
    find_getting_back = driver.find_element(By.NAME, 'continue-shopping')#находим элемент по name       
    find_getting_back.click()#кликаем на элемент
    sleep(2)#ждем 2 секунды

def test_third(driver):
    driver.get('https://demoqa.com/elements')

    buttons1 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='item-4']")))
    buttons1.click() #ждем пока элемент станет видимым 10 секунд и кликаем на него
    sleep(2)

    wait = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "doubleClickBtn")))
    print(wait.text) #ждем пока элемент станет видимым 10 секунд и выводим текст элемента
    


    doubleClickBtn = driver.find_element(By.ID, 'doubleClickBtn') #находим элемент по id
    actions = ActionChains(driver) #создаем объект для работы с ActionChains(нужен для двойного клика,пкм и тд )
    actions.double_click(doubleClickBtn).perform() #выполняем двойной клик на элемент
    text1 = driver.find_element(By.ID, 'doubleClickMessage') #находим элемент по id
    sleep(2) #ждем 2 секунды
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", text1) #скролим к элементу(что бы он был видимым)

    checkDouble= WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "doubleClickMessage")))
    print(checkDouble.text) #ждем пока элемент станет видимым 10 секунд и выводим текст элемента


    rightClick = driver.find_element(By.ID, 'rightClickBtn') #находим элемент по id
    actions = ActionChains(driver) #создаем объект для работы с ActionChains(нужен для двойного клика,пкм и тд )
    actions.context_click(rightClick).perform() #выполняем пкм на элемент       
    text2 = driver.find_element(By.ID, 'rightClickMessage') #находим элемент по id
    sleep(2) #ждем 2 секунды
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", text2) #скролим к элементу(что бы он был видимым)
    checkRight= WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "rightClickMessage")))
    print(checkRight.text) #ждем пока элемент станет видимым 10 секунд и выводим текст элемента
 
    

    simpleClick = driver.find_element(By.XPATH, "//button[text()='Click Me']") #находим элемент по xpath
    simpleClick.click() #кликаем на элемент
    text3 = driver.find_element(By.ID, 'dynamicClickMessage') #находим элемент по id
    sleep(2) #ждем 2 секунды
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", text3) #скролим к элементу(что бы он был видимым)
    checkSimple= WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "dynamicClickMessage")))
    print(checkSimple.text) #ждем пока элемент станет видимым 10 секунд и выводим текст элемента


def test_fourth(driver):
    driver.get('https://demoqa.com/dynamic-properties')

    visible_after_5 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'visibleAfter')))
    visible_after_5.click()
    print(visible_after_5.text)

    enable_after_5 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'enableAfter')))
    enable_after_5.click()
    print(enable_after_5.text)

    change_color = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'text-danger')))
    print(change_color.value_of_css_property('color'))
      
def test_iframe(driver):
    driver.get('https://demoqa.com/frames') #открываем сайт
    driver.switch_to.frame('frame1') #переходим в iframe, в том случае у iframe есть id, по этому передаем сразу
    text = driver.find_element(By.ID, 'sampleHeading') #находим элемент iframe по id
    print(text.text) #выводим текст элемента
    driver.switch_to.default_content() #возвращаемся в основной контент

    driver.switch_to.frame('frame2') #переходим в другой iframe
    text2 = driver.find_element(By.ID, 'sampleHeading') #находим элемент iframe по id
    print(text2.text) #выводим текст элемента
    driver.switch_to.default_content() #возвращаемся в основной контент

def test_iframe2(driver):
    driver.get('https://www.qa-practice.com/elements/iframe/iframe_page')
    iframe = driver.find_element(By.TAG_NAME, 'iframe') #тут нет удобного айди для айфрейма, по этому ищем его
    driver.switch_to.frame(iframe) #переходим в iframe
    burger_menu = driver.find_element(By.CLASS_NAME, 'navbar-toggler-icon')
    burger_menu.click()
    sleep(3)
    driver.switch_to.default_content() #возвращаемся в основной контент(страницу)  
    driver.find_element(By.LINK_TEXT, 'Iframe').click()

def test_windows(driver):
    driver.get('https://demoqa.com/browser-windows') #открываем сайт
    original_window = driver.current_window_handle #получаем id текущего окна
    print(original_window) #выводим id текущего окна
    all_windows = driver.window_handles #получаем все окна
    print(all_windows) #выводим все окна
    new_tab = driver.find_element(By.ID, 'tabButton') #находим элемент по id
    new_tab.click() #кликаем на элемент
    driver.switch_to.window(driver.window_handles[-1]) #переходим в новое окно(последнее окно)
    original_window2 = driver.current_window_handle #получаем id текущего окна
    print(original_window2) #выводим id текущего окна
    text = driver.find_element(By.ID, 'sampleHeading') #находим элемент по id
    print(text.text) #выводим текст элемента
    driver.close() #закрываем окно
    driver.switch_to.window(original_window) #возвращаемся в основное окно

def test_windows2(driver):
    driver.get('https://www.qa-practice.com/elements/new_tab/link')
    link = driver.find_element(By.ID, 'new-page-link')
    link.click()
    driver.switch_to.window(driver.window_handles[-1])
    assert driver.current_url == 'https://www.qa-practice.com/elements/new_tab/new_page'
    text = driver.find_element(By.ID, 'result-text')
    assert text.text == 'I am a new page in a new tab'
    print(text.text)
    driver.close()

def test_dropdown_menu(driver):
    driver.implicitly_wait(3)
    driver.get('https://magento.softwaretestingboard.com/')
    women = driver.find_element(By.ID, 'ui-id-4')
    tops = driver.find_element(By.ID, 'ui-id-9')
    jackets = driver.find_element(By.ID, 'ui-id-11')
    #ActionChains(driver).move_to_element(women).move_to_element(tops).click(jackets).perform()
    action = ActionChains(driver)
    action.move_to_element(women)
    action.move_to_element(tops)
    action.click(jackets)
    action.perform()
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Jackets'
    

def test_stale_exeption(driver):
    driver.get('https://www.qa-practice.com/elements/checkbox/single_checkbox')
    checkbox = driver.find_element(By.ID, 'id_checkbox_0')
    checkbox.click()

    submit = driver.find_element(By.ID, 'submit-id-submit')
    submit.click()
    assert driver.find_element(By.ID, 'result-text').text == 'select me or not'
    checkbox.click()
    submit.click()
     

def test_alerts(driver):
    driver.get('https://demoqa.com/alerts') #открываем сайт
    alert1 = driver.find_element(By.ID, 'alertButton') #находим элемент по id
    alert1.click() #кликаем на элемент
    alert = driver.switch_to.alert #переходим в окно alert
    alert_text = alert.text #получаем текст окна alert
    print('alert1_text: ', alert_text) #выводим текст окна alert
    alert.accept() #закрываем окно alert(НАЖИМАЕМ НА ОК)

    alert2 = driver.find_element(By.ID, 'timerAlertButton') #находим элемент по id
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", alert2) #скролим к элементу(что бы он был видимым)
    alert2.click() #кликаем на элемент
    sleep(6) #ждем 6 секунд
    alert = driver.switch_to.alert #переходим в окно alert
    alert_text2 = alert.text #получаем текст окна alert
    print('alert2_text: ', alert_text2) #выводим текст окна alert
    alert.accept() #закрываем окно alert(НАЖИМАЕМ НА ОК)

    alert3 = driver.find_element(By.ID, 'confirmButton') #находим элемент по id
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", alert3) #скролим к элементу(что бы он был видимым)
    alert3.click() #кликаем на элемент
    alert = driver.switch_to.alert #переходим в окно alert
    alert_text3 = alert.text #получаем текст окна alert
    print('alert3_text: ', alert_text3) #выводим текст окна alert
    alert.dismiss() #закрываем окно alert(НАЖИМАЕМ НА ОТМЕНА)
    result = driver.find_element(By.ID, 'confirmResult') #находим элемент по id
    print('alert3_result: ', result.text) #выводим текст элемента
    assert result.text == 'You selected Cancel' #проверяем что текст элемента соответствует ожидаемому

    alert4 = driver.find_element(By.ID, 'promtButton') #находим элемент по id
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", alert4) #скролим к элементу(что бы он был видимым)
    alert4.click() #кликаем на элемент
    alert=driver.switch_to.alert #переходим в окно alert
    alert_text4 = alert.text #получаем текст окна alert
    print('alert4_text: ', alert_text4) #выводим текст окна alert
    alert.send_keys('Hello') #вводим текст в окно alert
    alert.accept() #закрываем окно alert(НАЖИМАЕМ НА ОК)
    result2 = driver.find_element(By.ID, 'promptResult') #находим элемент по id
    print('alert4_result: ', result2.text) #выводим текст элемента
    assert result2.text == 'You entered Hello' #проверяем что текст элемента соответствует ожидаемому

def test_screens(driver):
    log_path = os.path.join(os.getcwd(), 'test_log.log')#путь к лог-файлу
    logging.basicConfig(filename=log_path, level=logging.INFO)#настраиваем логирование
    print(f"Лог-файл будет создан здесь: {log_path}")#выводим путь к лог-файлу

    logging.info('start test')#логирование
    logging.info('open site')#логирование
    driver.get('https://demoqa.com/text-box')#открываем сайт
    logging.info('find elements')#логирование
    name = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Full Name"]')#находим элемент по css селектору
    logging.info('fill name')#логирование
    name.send_keys('Egor')#вводим текст в поле

    logging.info('find email')#логирование
    email = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="name@example.com"]')#находим элемент по css селектору
    logging.info('fill email')#логирование
    email.send_keys('egor@gmail.com')#вводим текст в поле

    logging.info('find current address')#логирование
    current_address = driver.find_element(By.CSS_SELECTOR, 'textarea[placeholder="Current Address"]')#находим элемент по css селектору
    logging.info('fill current address')#логирование
    current_address.send_keys('Minsk')#вводим текст в поле

    logging.info('find permanent address')#логирование
    permanent_address = driver.find_element(By.ID, 'permanentAddress')#находим элемент по id
    logging.info('scroll to permanent address')#логирование
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", permanent_address)#скролим к элементу(что бы он был видимым)
    logging.info('fill permanent address')#логирование
    permanent_address.send_keys('Taganrog')#вводим текст в поле

    logging.info('find button')#логирование
    button = driver.find_element(By.ID, 'submit')#находим элемент по id
    logging.info('scroll to button')#логирование
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)#скролим к элементу(что бы он был видимым)
    logging.info('click button')#логирование
    button.click()#кликаем на элемент

    logging.info('find element for screenshot')#логирование
    element_for_screen = driver.find_element(By.CLASS_NAME, 'col-md-6')#находим элемент по классу
    logging.info('screenshot')#логирование
    element_for_screen.screenshot('screenshot.png')#делаем скриншот элемента

    logging.info('close test') #логирование


    
    
    
