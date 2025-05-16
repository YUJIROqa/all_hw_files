from playwright.sync_api import Page, expect

def test_5(page: Page):
    try:
        page.goto('https://www.qa-practice.com')
        print('Шаг 1: Перешли на страницу https://www.qa-practice.com/ (Success)')
    except Exception as e:
        print(f'Ошибка при переходе на страницу https://www.qa-practice.com/: {e}')

    try:
        button_select_input = page.locator('//*[@href="/elements/select/single_select"]')
        print('Шаг 2: Нашли кнопку перехода на страницу с выпадающим списком (Success)')
    except Exception as e:
        print(f'Ошибка при нахождении кнопки: {e}')
        
    try:
        button_select_input.click()
        print('Шаг 3: Клик на кнопку (Success)')
    except Exception as e:
        print(f'Ошибка при клике на кнопку: {e}')
        
    try:
        expect(page).to_have_title('Select Input | Single Select | QA Practice')
        print('Шаг 4: проверили, что заголовок страницы соответствует ожидаемому (Success)')
    except Exception as e:
        print(f'Ошибка при проверке заголовка страницы: {e}')
        
    try:
        expect(page).to_have_url('https://www.qa-practice.com/elements/select/single_select')
        print('Шаг 5: проверили, что URL страницы соответствует ожидаемому (Success)')
    except Exception as e:
        print(f'Ошибка при проверке URL страницы: {e}')
        
    try:
        selector_language = page.locator('//*[@name="choose_language"]')
        print('Шаг 6: Нашли выпадающий список (Success)')
    except Exception as e:
        print(f'Ошибка при нахождении выпадающего списка: {e}')

    try:
        submit_button = page.locator('//*[@id="submit-id-submit"]')
        print('Шаг 7: Нашли кнопку отправки (Success)')
    except Exception as e:
        print(f'Ошибка при нахождении кнопки отправки: {e}')

    try:
        selector_language.select_option('Python')
        print('Шаг 8: Выбрали Python (Success)')
    except Exception as e:
        print(f'Ошибка при выборе языка: {e}')
        
    try:
        submit_button.click()
        print('Шаг 9: Клик на кнопку отправки (Success)')
    except Exception as e:
        print(f'Ошибка при клике на кнопку отправки: {e}')
        
    try:
        result_area = page.locator('//*[@id="result-text"]')
        print('Шаг 10: Нашли результат (Success)')
    except Exception as e:
        print(f'Ошибка при нахождении результата: {e}')
        
    try:
        expect(result_area).to_have_text('Python')
        print('Шаг 11: проверили, что результат соответствует ожидаемому (Success)')
    except Exception as e:
        print(f'Ошибка при проверке результата: {e}')
        
    try:
        expect(selector_language) == ''
        print('Шаг 12: проверили, что в выпадающем списке ничего не выбрано (Success)')
    except Exception as e:
        print(f'Ошибка при проверке выпадающего списка: {e}')
        
        
    try:
        selector_language.select_option('Ruby')
        print('Шаг 13: Выбрали Ruby (Success)')
    except Exception as e:
        print(f'Ошибка при выборе языка: {e}')
        
    try:
        submit_button.click()
        print('Шаг 14: Клик на кнопку отправки (Success)')      
    except Exception as e:
        print(f'Ошибка при клике на кнопку отправки: {e}')
        
    try:
        expect(result_area).to_have_text('Ruby')
        print('Шаг 15: проверили, что результат соответствует ожидаемому (Success)')
    except Exception as e:
        print(f'Ошибка при проверке результата: {e}')
        
    try:
        expect(selector_language) == 'JavaScript'
        print('Шаг 16: проверили, что в выпадающем списке выбрано JavaScript (Success)')
    except Exception as e:
        print(f'Ошибка при проверке выпадающего списка: {e}')
        
    try:
        selector_language.select_option('JavaScript')
        print('Шаг 17: Выбрали JavaScript (Success)')
    except Exception as e:
        print(f'Ошибка при выборе языка: {e}')
        
    try:
        submit_button.click()
        print('Шаг 18: Клик на кнопку отправки (Success)')
    except Exception as e:
        print(f'Ошибка при клике на кнопку отправки: {e}')
        
    try:
        expect(result_area).to_have_text('JavaScript')
        print('Шаг 19: проверили, что результат соответствует ожидаемому (Success)')
    except Exception as e:
        print(f'Ошибка при проверке результата: {e}')
        
    try:
        expect(selector_language) == 'Java' 
        print('Шаг 20: проверили, что в выпадающем списке выбрано Java (Success)')
    except Exception as e:
        print(f'Ошибка при проверке выпадающего списка: {e}')
        
    try:
        selector_language.select_option('Java')
        print('Шаг 21: Выбрали Java (Success)')
    except Exception as e:
        print(f'Ошибка при выборе языка: {e}')

    try:
        submit_button.click()
        print('Шаг 22: Клик на кнопку отправки (Success)')
    except Exception as e:
        print(f'Ошибка при клике на кнопку отправки: {e}')

    try:
        expect(result_area).to_have_text('Java')
        print('Шаг 23: проверили, что результат соответствует ожидаемому (Success)')
    except Exception as e:
        print(f'Ошибка при проверке результата: {e}')
        
    try:
        button_multiple_select = page.locator('//*[@href="/elements/select/mult_select"]')
        print('Шаг 24: Нашли кнопку перехода на страницу с выпадающим списком (Success)')
    except Exception as e:
        print(f'Ошибка при нахождении кнопки перехода на страницу с выпадающим списком: {e}')
        
    try:
        button_multiple_select.click()
        print('Шаг 25: Клик на кнопку перехода на страницу с выпадающим списком (Success)')
    except Exception as e:
        print(f'Ошибка при клике на кнопку перехода на страницу с выпадающим списком: {e}')
        
    try:
        expect(page).to_have_title('Select Input | Multiple Selects | QA Practice')
        print('Шаг 26: проверили, что заголовок страницы соответствует ожидаемому (Success)')
    except Exception as e:
        print(f'Ошибка при проверке заголовка страницы: {e}')
        
    try:
        expect(page).to_have_url('https://www.qa-practice.com/elements/select/mult_select')
        print('Шаг 27: проверили, что URL страницы соответствует ожидаемому (Success)')
    except Exception as e:
        print(f'Ошибка при проверке URL страницы: {e}')
        
    try:
        first_select = page.locator('//*[@id="id_choose_the_place_you_want_to_go"]')
        second_select = page.locator('//*[@id="id_choose_how_you_want_to_get_there"]')
        third_selector = page.locator('//*[@id="id_choose_when_you_want_to_go"]')
        submit_button = page.locator('//*[@id="submit-id-submit"]')
        result_area = page.locator('//*[@id="result-text"]')
        print('Шаг 28: Нашли все выпадающие списки и кнопку отправки (Success)')
    except Exception as e:
        print(f'Ошибка при нахождении выпадающих списков и кнопки отправки: {e}')

    try:

        first_select.select_option('Sea')
        second_select.select_option('Car')
        third_selector.select_option('Today')
        print('Шаг 29: Выбрали значения для всех выпадающих списков (Success)')
    except Exception as e:
        print(f'Ошибка при выборе значений для выпадающих списков: {e}')
        
    try:
        submit_button.click()
        print('Шаг 30: Клик на кнопку отправки (Success)')
    except Exception as e:
        print(f'Ошибка при клике на кнопку отправки: {e}')
        
    try:
        expect(result_area).to_have_text('to go by car to the sea today')
        print('Шаг 31: проверили, что результат соответствует ожидаемому (Success)')
    except Exception as e:
        print(f'Ошибка при проверке результата: {e}')
        
    try:
        submit_button.click()
        print('Шаг 32: Клик на кнопку отправки без выбора значений (Success)')
    except Exception as e:
        print(f'Ошибка при клике на кнопку отправки: {e}')
        
        
        
        