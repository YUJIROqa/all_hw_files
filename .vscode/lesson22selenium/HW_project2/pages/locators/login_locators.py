from selenium.webdriver.common.by import By
class login_locators:
    username_locator = (By.ID, 'username')
    password_locator = (By.ID, 'password')
    button_login_locator = (By.CSS_SELECTOR, '.fa.fa-2x.fa-sign-in')
    text_of_result_locator = (By.ID, 'flash')

login_locators = login_locators()