from playwright.sync_api import Page, expect
from time import sleep
import re
from playwright.sync_api import BrowserContext
from playwright.sync_api import Dialog

def test_visiable(page: Page):
    sleep(1)
    page.goto('https://www.qa-practice.com/elements/input/simple') #переходим на страницу
    sleep(1) 
    reqs =page.locator('#req_text') # # означает id. находим элемент
    expect(reqs).not_to_be_visible() #проверяем что элемент не виден
    expect(reqs).to_be_hidden() #проверяем что элемент скрыт
    page.locator('#req_header').click() #находим элемент и кликаем на него
    sleep(1)
    expect(reqs).to_be_visible() #проверяем что теперь элемент виден
    sleep(2)

def test_enabled_and_selected(page: Page):
    page.goto('https://www.qa-practice.com/elements/button/disabled') #переходим на страницу
    button = page.locator('#submit-id-submit') #находим элемент
    expect(button).to_be_disabled() #проверяем что элемент не активен
    page.locator('#id_select_state').select_option('Enabled')#selected_option значит что мы выбрали опцию в выпадающем списке
    expect(button).to_be_enabled() #проверяем что элемент активен
    expect(button).to_have_text('Submit') #проверяем что элемент имеет текст Submit
    expect(button).to_contain_text('Submit') #проверяем что элемент содержит текст Submit
    
def test_value(page: Page):
    text = 'qwerty'
    page.goto('https://www.qa-practice.com/elements/input/simple') #переходим на страницу   
    input_field = page.locator('#id_text_string') #находим элемент
    input_field.fill(text) #вводим текст
    expect(input_field, f'Input value is not {text}') #проверяем что элемент имеет текст qwerty

def test_sort_and_waits(page: Page):
    sleep(3)
    page.goto('https://magento.softwaretestingboard.com/men/tops-men/jackets-men.html') #переходим на страницу
    greet = page.locator('.greet.welcome').locator('nth=0') #нащли локатор котоырй загружается последним
    expect(greet).not_to_be_empty() #проверяем что элемент не пустой        
    first_man = page.locator('.product-item-link').locator('nth=0') #находим элемент который загружается последним
    print(first_man.inner_text()) #выводим текст элемента
    page.locator('#sorter').locator('nth=0').select_option('Price') #находим элемент который загружается последним и выбираем опцию в выпадающем списке
    expect(page).to_have_url(re.compile('price')) #проверяем что url содержит price
    print(first_man.inner_text()) #выводим текст элемента
    sleep(5)

def test_tabs(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/link')
    link = page.locator('#new-page-link')
    with context.expect_page() as new_page_event:
        link.click()
    sleep(3)   
    new_page = new_page_event.value
    result = new_page.locator('#result-text')
    expect(result).to_have_text('I am a new page in a new tab')
    page.get_by_role('link', name='New tab button').click()
    sleep(3)

def test_hover(page: Page):
    page.goto('https://magento.softwaretestingboard.com/')
    man = page.locator('#ui-id-5')
    tops = page.locator('#ui-id-17')
    jackets = page.locator('#ui-id-19')
    man.hover()
    tops.hover()
    jackets.hover()

    
def test_drag_and_drop(page: Page):
    page.goto('https://www.qa-practice.com/elements/dragndrop/boxes')
    drug_me = page.locator('#rect-draggable')
    drope_here = page.locator('#rect-droppable')
    drug_me.drag_to(drope_here)
    sleep(3)

def test_alerts(page: Page):

    def cancel_alert(alert: Dialog):
        print(alert.message)
        print(alert.type)
        alert.dismiss()

    def fill_and_accept(alert: Dialog):
        alert.accept('some text')

    #page.on('dialog', fill_and_accept)
    page.on('dialog', lambda alert: alert.accept('another text')) #переводится как сделай с алертом алерт ввод 
    page.goto('https://www.qa-practice.com/elements/alert/prompt')
    page.get_by_role('link', name='Click').click()
    sleep(3)

