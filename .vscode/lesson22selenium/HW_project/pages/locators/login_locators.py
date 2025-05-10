from selenium.webdriver.common.by import By

email_locator = (By.CSS_SELECTOR, 'input[autofocus = "autofocus"]')
password_locator = (By.CSS_SELECTOR, 'input[name="Password"]')
checkbox_locator_remember = (By.CSS_SELECTOR, 'input[type = "checkbox"]')
login_button_locator = (By.CSS_SELECTOR, '.button-1.login-button')
error_text_locator = (By.CSS_SELECTOR, '.validation-summary-errors')
forgot_password_locator = (By.LINK_TEXT, 'Forgot password?')
you_authorized_locator = (By.CLASS_NAME, 'account')
