from playwright.sync_api import Page, expect
from time import sleep
import re
from playwright.sync_api import BrowserContext
from playwright.sync_api import Dialog

def test_1(page: Page):
    page.goto('https://www.qa-practice.com/elements/checkbox/single_checkbox')
    checkbox = page.locator('#id_checkbox_0')
    expect(checkbox).not_to_be_checked()
    checkbox.click()
    expect(checkbox).to_be_checked()
    submit = page.locator('#submit-id-submit')
    expect(submit).to_be_enabled()
    submit.click()
    text = page.locator('#result-text')
    expect(text).to_have_text('select me or not')

def test_2(page: Page):
    page.goto('https://www.qa-practice.com/elements/input/simple')
    input = page.get_by_placeholder('Submit me')
    input.type('Playwright_Test')
    expect(input).to_have_value('Playwright_Test')
    input.press('Enter')
    text = page.locator('#result-text')
    expect(text).to_have_text('Playwright_Test')

def test_3(page: Page):
    page.goto('https://www.qa-practice.com/elements/dragndrop/boxes')
    drug_me = page.locator('//*[@class="rect-draggable ui-draggable ui-draggable-handle"]')
    drop_here = page.locator('//*[@id="rect-droppable"]')
    drug_me.drag_to(drop_here)
    try:
        success = page.get_by_text('Dropped!')
        expect(success).to_be_visible()
        print('Success')
    except Exception as e:
        print(e)
    sleep(3)

def test_4(page: Page):
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    page.on('dialog', lambda dialog: dialog.accept())
    click = page.get_by_text('Click')
    click.first.click()
    text = page.locator('#result-text')
    expect(text).to_have_text('Ok')
    sleep(3)

def test_5(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/link')
    link = page.locator('//*[@target="_blank"]') #находим ссылку
    with context.expect_page() as new_page_event: #ожидаем появление новой страницы
        link.click() #кликаем по ссылке
    sleep(3)
    new_page = new_page_event.value #получаем новую страницу
    result = new_page.locator('#result-text') #находим элемент на новой странице
    expect(result).to_have_text('I am a new page in a new tab') #проверяем что текст на новой странице соответствует ожидаемому
    page.bring_to_front() #возвращаемся на предыдущую страницу
    button_new = page.get_by_text('New tab button') #находим кнопку
    expect(button_new).to_be_visible() #проверяем что кнопка видима

    expect(new_page).to_have_url(re.compile('new_tab')) #проверяем что url соответствует ожидаемому
    sleep(3)

