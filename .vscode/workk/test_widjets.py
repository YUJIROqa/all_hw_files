import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def test_widget_spain():
    driver = webdriver.Chrome()
    try:
        driver.get("https://prod-tretya.webflow.io/")
        
        # Находим и выделяем заголовок
        heading = driver.find_element(By.TAG_NAME, "h1")
        actions = ActionChains(driver)
        actions.double_click(heading).perform()
        
        # Ждем модальное окно и кликаем по кнопке
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.button.js-send-analytics'))
        )
        button.click()
        
        # Ждем загрузку новой страницы
        time.sleep(5)
        
    finally:
        driver.quit()

def test_widget_brazil():
    driver = webdriver.Chrome()
    try:
        driver.get("https://prod-tretya.webflow.io/")
        
        # Находим и выделяем заголовок
        heading = driver.find_element(By.TAG_NAME, "h1")
        actions = ActionChains(driver)
        actions.double_click(heading).perform()
        
        # Ждем модальное окно и кликаем по кнопке
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.button.js-send-analytics'))
        )
        button.click()
        
        # Ждем загрузку новой страницы
        time.sleep(5)
        
    finally:
        driver.quit()

if __name__ == "__main__":
    test_widget_spain()
    test_widget_brazil()