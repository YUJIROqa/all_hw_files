from playwright.sync_api import Page, expect
import re
from time import sleep


def test_fiirst(page: Page):
    page.goto('https://www.google.com') #переходим на страницу
    search_field = page.get_by_role('combobox') #находим поле для ввода
    search_field.fill('cat') #вводим cat
    search_field.press('Enter') #нажимаем Enter
    #search_field.click()
    expect(page).to_have_title(re.compile('cat')) # проверяет, что в title есть cat

def test_by_role(page: Page): #
    page.goto('https://magento.softwaretestingboard.com/') #переходим на страницу   
    search_field = page.get_by_role('menuitem', name='What`s new').click() #находим элемент и кликаем на него
    page.get_by_role('link', name = 'Search Terms').click() #находим элемент и кликаем на него


def test_by_text(page: Page):
    page.goto('https://www.qa-practice.com/')#переходим на страницу
    page.get_by_text('Single UI Elements').click()#находим элемент и кликаем на него
    sleep(3)

def test_by_label(page: Page):
    sleep(2)
    page.goto('https://www.qa-practice.com/elements/input/simple')#переходим на страницу
    field = page.get_by_label('Text string')#находим элемент
    field.press_sequentially('sdgfadsfasdfasd', delay=500)#вводим текст
    sleep(2)
    field.press('Control+A')#выделяем текст
    sleep(2)
    field.press('Backspace')#удаляем текст
    sleep(3)

def test_by_placeholder(page: Page):
    page.goto('https://www.qa-practice.com/elements/input/simple')#переходим на страницу
    page.get_by_placeholder('Submit me').fill('test')#вводим текст
    sleep(3)

def test_by_alt_text(page: Page):
    page.goto('https://epam.com')#переходим на страницу
    page.get_by_alt_text('The Next Evolution of Software Engineering').click()#находим элемент и кликаем на него
    sleep(3)

def test_by_title(page: Page):
    page.goto('https://www.google.com')#переходим на страницу           
    sleep(5)
    search_field = page.get_by_title('Поиск')#находим элемент
    search_field.fill('test')#вводим текст
    search_field.press('Enter')#нажимаем Enter
    sleep(3)

def test_by_test_id(page: Page):
    sleep(3)
    page.goto('https://www.airbnb.com')#переходим на страницу
    sleep(3)
    page.get_by_test_id('header-tab-search-block-tab-EXPERIENCES').click()#находим элемент и кликаем на него
    sleep(3)

def test_by_locator(page: Page):
    page.goto('https://www.qa-practice.com/')#переходим на страницу
    page.locator('.has-sub').click() #Single UI Elements
    sleep(3)
    
def test_by_xpath(page: Page):
    page.goto('https://www.qa-practice.com/')#переходим на страницу 
    page.locator('//*[@class="has-sub"]').click() #Single UI Elements
    sleep(3)
