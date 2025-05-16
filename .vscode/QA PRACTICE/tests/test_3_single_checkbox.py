from playwright.sync_api import Page, expect

def test_3(page: Page):
    try:
        page.goto('https://www.qa-practice.com')
        print('Шаг 1: Перешли на страницу https://www.qa-practice.com/ (Success)')
    except Exception as e:
        print(f'Ошибка при переходе на страницу https://www.qa-practice.com/: {e}')

    try:
        button_single_checkbox = page.locator('//*[@href="/elements/checkbox/single_checkbox"]')
        print('Шаг 2: Нашли кнопку перехода на страницу с чекбоксом (Success)')
    except Exception as e:
        print(f'Ошибка при нахождении кнопки: {e}')
    
    try:
        button_single_checkbox.click()
        print('Шаг 3: Клик на кнопку (Success)')
    except Exception as e:
        print(f'Ошибка при клике на кнопку: {e}')

    try:
        expect(page).to_have_title('Checkboxes | Single Checkbox | QA Practice')
        print('Шаг 4: Проверили, что заголовок страницы соответствует ожидаемому (Success)')
    except Exception as e:
        print(f'Ошибка при проверке заголовка страницы: {e}')   

    try:
        expect(page).to_have_url('https://www.qa-practice.com/elements/checkbox/single_checkbox')
        print('Шаг 5: Проверили, что URL страницы соответствует ожидаемому (Success)')
    except Exception as e:
        print(f'Ошибка при проверке URL страницы: {e}')

    try:
        checkbox = page.locator('//*[@id="id_checkbox_0"]')
        print('Шаг 5: Нашли чекбокс (Success)')
    except Exception as e:
        print(f'Ошибка при нахождении чекбокса: {e}')

    try:
        expect(checkbox).to_be_enabled()
        print('Шаг 6: Проверили, что чекбокс активен (Success)')
    except Exception as e:
        print(f'Ошибка при проверке активности чекбокса: {e}')

    try:
        checkbox.click()
        print('Шаг 7: Клик на чекбокс (Success)')
    except Exception as e:
        print(f'Ошибка при клике на чекбокс: {e}')  

    try:
        expect(checkbox).to_be_checked()
        print('Шаг 8: Проверили, что чекбокс отмечен (Success)')
    except Exception as e:
        print(f'Ошибка при проверке отметки чекбокса: {e}')

    try:
        button_submit = page.locator('//*[@id="submit-id-submit"]')
        print('Шаг 9: Нашли кнопку (Success)')
    except Exception as e:
        print(f'Ошибка при нахождении кнопки: {e}')

    try:
        button_submit.click()
        print('Шаг 10: Клик на кнопку (Success)')
    except Exception as e:
        print(f'Ошибка при клике на кнопку: {e}')

    try:
        result = page.locator('//*[@id="result-text"]')
        print('Шаг 11: Нашли результат (Success)')
    except Exception as e:
        print(f'Ошибка при нахождении результата: {e}')

    try:
        expect(result).to_have_text('select me or not')
        print('Шаг 12: Проверили, что результат соответствует ожидаемому (Success)')
    except Exception as e:
        print(f'Ошибка при проверке результата: {e}')

    try:
        expect(button_submit).to_be_enabled()
        print('Шаг 13: Проверили, что кнопка снова активна (Success)')
    except Exception as e:
        print(f'Ошибка при проверке активности кнопки: {e}')

    try:
        button_submit.click()
        print('Шаг 14: Клик на кнопку с невыбранным чекбоксом (Success)')
    except Exception as e:
        print(f'Ошибка при клике на кнопку: {e}')

    try:
        expect(result).to_be_hidden()
        print('Шаг 15: Проверили, что результат скрыт (Success)')
    except Exception as e:
        print(f'Ошибка при проверке скрытия результата: {e}')
        
    try:
        button_checkboxes = page.locator('//*[@href="/elements/checkbox/mult_checkbox"]')
        print('Шаг 16: Нашли кнопку (Success)')
    except Exception as e:
        print(f'Ошибка при нахождении кнопки: {e}')

    try:
        button_checkboxes.click()
        print('Шаг 17: Клик на кнопку (Success)')
    except Exception as e:
        print(f'Ошибка при клике на кнопку: {e}')
        
    try:
        expect(page).to_have_title('Checkboxes | Multiple Checkboxes | QA Practice')
        print('Шаг 18: Проверили, что заголовок страницы соответствует ожидаемому (Success)')
    except Exception as e:
        print(f'Ошибка при проверке заголовка страницы: {e}')
        
    try:
        expect(page).to_have_url('https://www.qa-practice.com/elements/checkbox/mult_checkbox')
        print('Шаг 19: Проверили, что URL страницы соответствует ожидаемому (Success)')
    except Exception as e:
        print(f'Ошибка при проверке URL страницы: {e}')
        
    try:
        checkbox_1 = page.locator('//*[@id="id_checkboxes_0"]')
        checkbox_2 = page.locator('//*[@id="id_checkboxes_1"]')
        checkbox_3 = page.locator('//*[@id="id_checkboxes_2"]')
        button_submit = page.locator('//*[@id="submit-id-submit"]')
        print('Шаг 20: Нашли чекбоксы и кнопку Submit (Success)')
    except Exception as e:
        print(f'Ошибка при нахождении чекбоксов и кнопки Submit: {e}')
        
    try:
        expect(checkbox_1).to_be_enabled()
        expect(checkbox_2).to_be_enabled()
        expect(checkbox_3).to_be_enabled()
        print('Шаг 21: Проверили, что чекбоксы активны (Success)')
    except Exception as e:
        print(f'Ошибка при проверке активности чекбоксов: {e}')
        
    try:
        checkbox_1.click()
        print('Шаг 22: Клик на чекбокс 1 (Success)')
    except Exception as e:
        print(f'Ошибка при клике на чекбокс 1: {e}')

    try:
        expect(checkbox_1).to_be_checked()
        print('Шаг 23: Проверили, что чекбокс 1 отмечен (Success)')
    except Exception as e:
        print(f'Ошибка при проверке отметки чекбокса 1: {e}')

    try:
        button_submit.click()
        print('Шаг 24: Клик на кнопку Submit (Success)')
    except Exception as e:
        print(f'Ошибка при клике на кнопку Submit: {e}')

    try:
        result = page.locator('//*[@id="result-text"]')
        print('Шаг 25: Нашли результат (Success)')
    except Exception as e:
        print(f'Ошибка при нахождении результата: {e}') 

    try:
        expect(result).to_have_text('one')
        print('Шаг 26: Проверили, что результат соответствует ожидаемому one (Success)')
    except Exception as e:
        print(f'Ошибка при проверке результата: {e}')
        
    try:
        checkbox_2.click()
        print('Шаг 27: Клик на чекбокс 2 (Success)')
    except Exception as e:
        print(f'Ошибка при клике на чекбокс 2: {e}')

    try:
        expect(checkbox_2).to_be_checked()
        print('Шаг 28: Проверили, что чекбокс 2 отмечен (Success)')
    except Exception as e:
        print(f'Ошибка при проверке отметки чекбокса 2: {e}')

    try:
        button_submit.click()
        print('Шаг 29: Клик на кнопку Submit (Success)')
    except Exception as e:
        print(f'Ошибка при клике на кнопку Submit: {e}')

    try:
        expect(result).to_have_text('two')
        print('Шаг 30: Проверили, что результат соответствует ожидаемому two (Success)')
    except Exception as e:
        print(f'Ошибка при проверке результата: {e}')

    
    try:
        checkbox_3.click()
        print('Шаг 31: Клик на чекбокс 3 (Success)')
    except Exception as e:
        print(f'Ошибка при клике на чекбокс 3: {e}')

    try:
        expect(checkbox_3).to_be_checked()
        print('Шаг 32: Проверили, что чекбокс 3 отмечен (Success)')
    except Exception as e:
        print(f'Ошибка при проверке отметки чекбокса 3: {e}')
        
    try:
        button_submit.click()
        print('Шаг 33: Клик на кнопку Submit (Success)')
    except Exception as e:
        print(f'Ошибка при клике на кнопку Submit: {e}')
        
    try:
        expect(result).to_have_text('three')
        print('Шаг 34: Проверили, что результат соответствует ожидаемому three (Success)')
    except Exception as e:
        print(f'Ошибка при проверке результата: {e}')
        
    try:
        checkbox_1.click()
        checkbox_2.click()
        checkbox_3.click()
        print('Шаг 35: Отметили все чекбоксы (Success)')
    except Exception as e:
        print(f'Ошибка при отметке всех чекбоксов: {e}')
    
    try:
        expect(checkbox_1).to_be_checked()
        expect(checkbox_2).to_be_checked()
        expect(checkbox_3).to_be_checked()
        print('Шаг 36: Проверили, что все чекбоксы отмечены (Success)')
    except Exception as e:
        print(f'Ошибка при проверке отметки всех чекбоксов: {e}')
        
    try:
        button_submit.click()
        print('Шаг 37: Клик на кнопку Submit (Success)')
    except Exception as e:
        print(f'Ошибка при клике на кнопку Submit: {e}')

    try:
        expect(result).to_have_text('one, two, three')
        print('Шаг 38: Проверили, что результат соответствует ожидаемому all (Success)')
    except Exception as e:
        print(f'Ошибка при проверке результата: {e}')
        
    try:
        button_submit.click()
        print('Шаг 39: Клик на кнопку Submit без отмеченных чекбоксов (Success)')
    except Exception as e:
        print(f'Ошибка при клике на кнопку Submit: {e}')
        
    try:
        expect(result).to_be_hidden()
        print('Шаг 40: Проверили, что результат скрыт (Success)')
    except Exception as e:
        print(f'Ошибка при проверке скрытия результата: {e}')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        


















