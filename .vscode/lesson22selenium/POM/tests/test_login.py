import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from POM.pages.customer_login import CustomerLogin
from time import sleep

def test_incorrect_login(driver2):
    login_page = CustomerLogin(driver2)
    login_page.open_page()
    login_page.fill_login_form('dsafg@sgsag.adgs', '12432rwgdsfg3q4')

    # email = driver2.find_element(By.ID, 'email')
    # password = driver2.find_element(By.ID, 'pass')
    # button = driver2.find_element(By.ID, 'send2')
    # email.send_keys('tertyuikol0987st@test.com')
    # password.send_keys('hjklk788jhb89087hj')
    # button.click()

    sleep(5)
    login_page.check_error_alert('The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.')
    # error_alert = driver2.find_element(By.CSS_SELECTOR, '[data-bind="html: $parent.prepareMessageForHtml(message.text)"]')
    # assert error_alert.text == 'The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.'
    sleep(3)

def test_correct_email(driver2):
    login_page = CustomerLogin(driver2)
    login_page.open_page()
    login_page.fill_login_form('tertyuikol0987st@test.com', 'hjklk788jhb89087hj')
    sleep(5)
    login_page.check_error_alert('The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.')
    sleep(3)
