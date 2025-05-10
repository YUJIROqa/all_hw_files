from playwright.sync_api import Page, expect
import re
from time import sleep

def test_assert_title(page: Page):
    page.goto('https://www.qa-practice.com/')
    expect(page).to_have_title('Home Page | QA Practice')
    sleep(3)

def test_1(page: Page):
    page.goto('https://www.qa-practice.com/elements/button/simple')
    button = page.locator('//*[@class="btn btn-primary"]').click()
    sleep(3)
    text_result = page.get_by_text('Submitted')
    expect(text_result).to_have_text('Submitted')

def test_2(page: Page):
    page.goto('https://www.qa-practice.com/elements/input/simple')
    field = page.get_by_placeholder('Submit me')
    text = 'Playwright_Test'
    field.fill(text)
    field.press('Enter')
    result = page.locator('.result-text')
    expect(result).to_have_text(text)
    sleep(3)

def test_3(page: Page):

    page.goto('https://www.qa-practice.com/elements/checkbox/single_checkbox')
    box = page.locator('.form-check-input')
    is_checking = box.is_checked()
    print(f'Checkbox is checked: {is_checking}')
    box.click()
    new_state = box.is_checked()
    print(f'Checkbox is checked: {new_state}')
    submit = page.locator('.btn.btn-primary')
    submit.click()
    sleep(3)
    result_text = page.locator('.result-text')
    actual_text = result_text.text_content()
    print(f'Actual text: {actual_text}')

def test_4(page: Page):
    page.goto('https://www.qa-practice.com/elements/button/simple')
    try:
        button1 = page.locator('.btn.btn-primary')
        button1.click()
        print('Rutton1 successfully clicked')
    except Exception as error:
        print(f'Impossible to click Button1. The reason is{error}')
    
    try:
        button2 = page.locator('//*[@class="btn btn-primary"]')
        button2.click()
        print('Button2 successfully clicked')
    except Exception as error:
        print(f'Impossible to click Button2. The reason is{error}')

    try:
        button3 = page.get_by_text('Click')
        button3.first.click()
        print('Button3 successfully clicked')
    except Exception as error:
        print(f'Impossible to click Button3. The reason is{error}')

    try:
        button4 = page.locator('//*[@type="submit"]')
        button4.click()
        print('Button4 successfully clicked')
    except Exception as error:
        print(f'Impossible to click Button4. The reason is{error}') 

    try:
        button5 = page.locator('//*[@id="submit-id-submit"]') #условно //*[@ключ="значение"]
        button5.click()                     # * означает любой тег .// означает любой атрибут
        print('Button5 successfully clicked')
    except Exception as error:
        print(f'Impossible to click Button5. The reason is{error}')


    

