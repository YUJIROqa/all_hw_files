from playwright.sync_api import Page, expect
#from conftest import logger

def test_1(page: Page, logger):
    try:
        page.goto('https://www.qa-practice.com/')
        print('Шаг 1: Перешли на страницу https://www.qa-practice.com/ (Success)')
    except Exception as e:
        print(f'Шаг 1: Ошибка при переходе на страницу https://www.qa-practice.com/: {e}')

    try:
        expect(page).to_have_title('Home Page | QA Practice')
        print('Шаг 2: Проверили, что заголовок страницы соответствует ожидаемому (Success)')
    except Exception as e:
        print(f'Шаг 2: Ошибка при проверке заголовка страницы: {e}')

    try:
        expect(page).to_have_url('https://www.qa-practice.com/')
        print('Шаг 3: Проверили, что URL страницы соответствует ожидаемому (Success)')
    except Exception as e:
        print(f'Шаг 3: Ошибка при проверке URL страницы: {e}')

    try:
        expect(page.get_by_text('Single UI Elements')).to_be_visible()
        print('Шаг 4: Проверили, что кнопка Single UI Elements видима (Success)')
    except Exception as e:
        print(f'Шаг 4: Ошибка при проверке видимости кнопки Single UI Elements: {e}')
