from playwright.sync_api import Page, expect

def test_2(page: Page):

    try:
        page.goto('https://www.qa-practice.com/')
        print('Шаг 1: Перешли на страницу https://www.qa-practice.com/ (Success)')
    except Exception as e:
        print(f'Ошибка при переходе на страницу https://www.qa-practice.com/: {e}')

    try:
        button_simple_button = page.locator('//*[@href="/elements/button/simple"]')
        button_simple_button.click()
        print('Шаг 2: Переход на страницу Simple button (Success)')
    except Exception as e:
        print(f'Ошибка при переходе на страницу Simple button: {e}')

    try:
        expect(page).to_have_title('Buttons | Simple Button | QA Practice')
        print('Шаг 3: Проверка заголовка страницы (Success)')
    except Exception as e:
        print(f'Ошибка при проверке заголовка страницы: {e}')

    try:
        expect(page).to_have_url('https://www.qa-practice.com/elements/button/simple')
        print('Шаг 3.1: Проверка URL страницы (Success)')
    except Exception as e:
        print(f'Ошибка при проверке URL страницы: {e}')

    try:
        button_click_1 = page.locator('//*[@id="submit-id-submit"]')
        expect(button_click_1).to_be_enabled()
        print('Шаг 4: Проверка активности кнопки 1 (Success)')
    except Exception as e:
        print(f'Ошибка при проверке активности кнопки 1: {e}')

    try:
        button_click_1.click()
        print('Шаг 5: Клик на кнопку 1 (Success)')
    except Exception as e:
        print(f'Ошибка при клике на кнопку 1: {e}')

    try:
        result = page.get_by_text('Submitted')
        expect(result).to_be_visible()
        print('Шаг 6: Проверка результата (Success)')
    except Exception as e:
        print(f'Ошибка при проверке результата: {e}')

    try:
        button_click_like_button = page.get_by_text('Looks like a button')
        expect(button_click_like_button).to_be_visible()
        print('Шаг 7: Проверка видимости кнопки 2 (Success)')
    except Exception as e:
        print(f'Ошибка при проверке видимости кнопки 2: {e}')

    try:
        button_click_like_button.click()
        print('Шаг 8: Клик на кнопку 2 (Success)')
    except Exception as e:
        print(f'Ошибка при клике на кнопку 2: {e}')

    try:
        expect(page).to_have_title('Buttons | Like a Button | QA Practice')
        print('Шаг 9: Проверка заголовка страницы (Success)')
    except Exception as e:
        print(f'Ошибка при проверке заголовка страницы: {e}')

    try:
        expect(page).to_have_url('https://www.qa-practice.com/elements/button/like_a_button')
        print('Шаг 9.1: Проверка URL страницы (Success)')
    except Exception as e:
        print(f'Ошибка при проверке URL страницы: {e}')
        
    try:
        button_click_like_button_2 = page.locator('//*[@class="a-button"]')
        expect(button_click_like_button_2).to_be_enabled()
        print('Шаг 10: Проверка активности кнопки 3 (Success)')
    except Exception as e:
        print(f'Ошибка при проверке активности кнопки 3: {e}')

    try:
        button_click_like_button_2.click()
        print('Шаг 11: Клик на кнопку 3 (Success)')
    except Exception as e:
        print(f'Ошибка при клике на кнопку 3: {e}')

    try:
        result_2 = page.locator('//*[@id="result-text"]')
        expect(result_2).to_have_text('Submitted')
        print('Шаг 12: Проверка результата (Success)')
    except Exception as e:
        print(f'Ошибка при проверке результата: {e}')

    try:
        button_disabled = page.get_by_text('Disabled')
        button_disabled.click()
        print('Шаг 13: Клик на кнопку 4 (Success)')
    except Exception as e:
        print(f'Ошибка при клике на кнопку 4: {e}')

    try:
        expect(page).to_have_title('Buttons | Disabled Button | QA Practice')
        print('Шаг 14: Проверка заголовка страницы (Success)')
    except Exception as e:
        print(f'Ошибка при проверке заголовка страницы: {e}')
        
    try:
        expect(page).to_have_url('https://www.qa-practice.com/elements/button/disabled')
        print('Шаг 14.1: Проверка URL страницы (Success)')
    except Exception as e:
        print(f'Ошибка при проверке URL страницы: {e}')

    try:
        button_3 = page.locator('//*[@id="submit-id-submit"]')
        expect(button_3).to_be_disabled()
        print('Шаг 15: Проверка нактивности кнопки 5 (Success)')
    except Exception as e:
        print(f'Ошибка при проверке нактивности кнопки 5: {e}')
        
    try:
        dropdown = page.locator('//*[@id="id_select_state"]')
        print('Шаг 16: Поиск и проверка выпадающего списка (Success)')
    except Exception as e:
        print(f'Ошибка при проверке выпадающего списка: {e}')
        
    try:
        dropdown.select_option('Enabled')
        print('Шаг 17: Выбор опции в выпадающем списке (Success)')
    except Exception as e:
        print(f'Ошибка при выборе опции в выпадающем списке: {e}')
        
    try:
        expect(button_3).to_be_enabled()
        print('Шаг 18: Проверка активности кнопки 5 (Success)')
    except Exception as e:
        print(f'Ошибка при проверке активности кнопки 5: {e}')
        
    try:
        button_3.click()
        print('Шаг 19: Клик на кнопку 5 (Success)')
    except Exception as e:
        print(f'Ошибка при клике на кнопку 5: {e}')
    
    try:
        result_3 = page.locator('//*[@id="result-text"]')
        expect(result_3).to_have_text('Submitted')
        print('Шаг 20: Проверка результата (Success)')
    except Exception as e:
        print(f'Ошибка при проверке результата: {e}')
        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
