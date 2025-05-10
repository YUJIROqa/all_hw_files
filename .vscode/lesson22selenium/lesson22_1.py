from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


options = Options() #задаем опции для браузера. То есть переменная options принимает значение Options
option = webdriver.FirefoxOptions() #задаем опции для браузера. То есть переменная option принимает значение webdriver.FirefoxOptions
option.add_argument("start-maximized") #добавляем аргумент в опции для браузера. То есть переменная option принимает значение add_argument("start-maximized")
# options.experimental_options('detach', True)

driver = webdriver.Firefox(options=option)
sleep(2)
# driver.maximize_window()
# driver.set_window_size(1920, 1080)
driver.get('https://yandex.com/') #открываем страницу
print(driver.title) #выводим тайтл страницы
print(driver.current_url) #выводим url страницы
sleep(2)
search_input = driver.find_element(By.CSS_SELECTOR, '.search3__input.mini-suggest__input') #находим элемент по css селектору
search_input.send_keys('cats') #вводим в поиск cats
search_input.send_keys(webdriver.Keys.RETURN) #нажимаем Enter
sleep(2)
assert 'cats' in driver.title and 'Yandex' in driver.title #проверяем, что в тайтле есть cats и Yandex
print('Проверка тайтла прошла успешно') #выводим сообщение о проверке тайтла, если проверка не пройдет то до этой строчки не дойдет
driver.quit()
