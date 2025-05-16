from playwright.sync_api import Page, expect

def test_4(page: Page):

    try:
        page.goto('https://www.qa-practice.com')
        print('Шаг 1: Перешли на страницу https://www.qa-practice.com/ (Success)')
    except Exception as e:
        print(f'Ошибка при переходе на страницу https://www.qa-practice.com/: {e}')

    try:
        button_area = page.locator('//*[@href="/elements/textarea/single"]')
        print('Шаг 2: Нашли кнопку перехода на страницу с текстовой областью (Success)')
    except Exception as e:
        print(f'Ошибка при нахождении кнопки: {e}')

    try:
        button_area.click()
        print('Шаг 3: Клик на кнопку (Success)')
    except Exception as e:
        print(f'Ошибка при клике на кнопку: {e}')

    try:
        expect(page).to_have_title('TextArea | Single TextArea | QA Practice')
        print('Шаг 4: проверили, что заголовок страницы соответствует ожидаемому (Success)')
    except Exception as e:
        print(f'Ошибка при проверке заголовка страницы: {e}')

    try:
        expect(page).to_have_url('https://www.qa-practice.com/elements/textarea/single')
        print('Шаг 5: проверили, что URL страницы соответствует ожидаемому (Success)')
    except Exception as e:
        print(f'Ошибка при проверке URL страницы: {e}')

    try:
        text_area = page.locator('//*[@class="textarea form-control"]')
        print('Шаг 6: Нашли текстовую область (Success)')
    except Exception as e:
        print(f'Ошибка при нахождении текстовой области: {e}')

    try:
        text = 'text'
        text_area.fill(text)
        print('Шаг 7: Заполнили текстовую область (Success)')
    except Exception as e:
        print(f'Ошибка при заполнении текстовой области: {e}')

    try:
        expect(text_area).to_have_value(text)
        print('Шаг 8: проверили, что текст в текстовой области соответствует ожидаемому (Success)')
    except Exception as e:
        print(f'Ошибка при проверке текста в текстовой области: {e}')
    
    try:
        submit_button = page.locator('//*[@id="submit-id-submit"]')
        print('Шаг 9: Нашли кнопку отправки (Success)')
    except Exception as e:
        print(f'Ошибка при нахождении кнопки отправки: {e}')

    try:
        submit_button.click()
        print('Шаг 10: Клик на кнопку отправки (Success)')
    except Exception as e:
        print(f'Ошибка при клике на кнопку отправки: {e}')
    
    try:
        result_area_1 = page.locator('//*[@id="result-text"]')
        print('Шаг 11: Нашли результат (Success)')
    except Exception as e:
        print(f'Ошибка при нахождении результата: {e}')

    try:
        expect(result_area_1).to_have_text(text)
        print('Шаг 12: проверили, что результат соответствует ожидаемому (Success)')
    except Exception as e:
        print(f'Ошибка при проверке результата: {e}')

    try:
        text_area.fill(' ')
        print('Шаг 13: Заполнили текстовую область пустым значением (Success)')
    except Exception as e:
        print(f'Ошибка при заполнении текстовой области пустым значением: {e}')

    try:
        expect(page).to_have_text('This field is required.')
        print('Шаг 14: проверили, что результат соответствует ожидаемому (Success)')
    except Exception as e:
        print(f'Ошибка при проверке результата: {e}')

    try:
        multiple_textareas_button = page.locator('//*[@href="/elements/textarea/textareas"]')
        print('Шаг 15: Нашли кнопку перехода на страницу с несколькими текстовыми областями (Success)')
    except Exception as e:
        print(f'Ошибка при нахождении кнопки перехода на страницу с несколькими текстовыми областями: {e}')
    
    try:
        multiple_textareas_button.click()
        print('Шаг 16: Клик на кнопку перехода на страницу с несколькими текстовыми областями (Success)')
    except Exception as e:
        print(f'Ошибка при клике на кнопку перехода на страницу с несколькими текстовыми областями: {e}')

    try:
        expect(page).to_have_title('TextArea | Multiple TextAreas | QA Practice')
        print('Шаг 17: проверили, что заголовок страницы соответствует ожидаемому (Success)')
    except Exception as e:
        print(f'Ошибка при проверке заголовка страницы: {e}')
    
    try:
        expect(page).to_have_url('https://www.qa-practice.com/elements/textarea/textareas')
        print('Шаг 18: проверили, что URL страницы соответствует ожидаемому (Success)')
    except Exception as e:
        print(f'Ошибка при проверке URL страницы: {e}')
    
    try:
        text_1 = 'text_1'
        text_2 = 'text_2'
        text_3 = 'text_3'
        first_textarea = page.locator('//*[@id="id_first_chapter"]')
        second_textarea = page.locator('//*[@id="id_second_chapter"]')
        third_textarea = page.locator('//*[@id="id_third_chapter"]')
        print('Шаг 19: Нашли текстовые области (Success)')
    except Exception as e:
        print(f'Ошибка при нахождении текстовых областей: {e}')
    
    try:
        submit_button = page.locator('//*[@id="submit-id-submit"]')
        print('Шаг 20: Нашли кнопку отправки (Success)')
    except Exception as e:
        print(f'Ошибка при нахождении кнопки отправки: {e}')
    
    try:
        first_textarea.fill(text_1) 
        print('Шаг 21: Заполнили первую текстовую область (Success)')
    except Exception as e:
        print(f'Ошибка при заполнении первой текстовой области: {e}')
    
    try:
        submit_button.click()
        print('Шаг 22: Клик на кнопку отправки (Success)')
    except Exception as e:
        print(f'Ошибка при клике на кнопку отправки: {e}')
    
    try:
        result_area_2  = page.locator('//*[@id="result-text"]')
        print('Шаг 23: Нашли результат (Success)')
    except Exception as e:
        print(f'Ошибка при нахождении результата: {e}')
    
    try:
        expect(result_area_2).to_have_text(text_1.capitalize())
        print('Шаг 24: проверили, что результат соответствует ожидаемому (Success)')
    except Exception as e:
        print(f'Ошибка при проверке результата: {e}')
    
    try:
        first_textarea.fill(text_1)
        second_textarea.fill(text_2)
        third_textarea.fill(text_3)
        print('Шаг 25: Заполнили все текстовые области (Success)')
    except Exception as e:
        print(f'Ошибка при заполнении всех текстовых областей: {e}')    
        
    try:
        submit_button.click()
        print('Шаг 26: Клик на кнопку отправки (Success)')
    except Exception as e:
        print(f'Ошибка при клике на кнопку отправки: {e}')      
        
    try:
        expect(result_area_2).to_have_text(text_1.capitalize() + text_2.capitalize() + text_3.capitalize())
        print('Шаг 27: проверили, что результат соответствует ожидаемому (Success)')
    except Exception as e:
        print(f'Ошибка при проверке результата: {e}')

    try:
        second_textarea.fill(text_2)
        third_textarea.fill(text_3)
        print('Шаг 28: Заполнили все текстовые области (Success)')
    except Exception as e:
        print(f'Ошибка при заполнении всех текстовых областей: {e}')

    try:
        submit_button.click()
        print('Шаг 29: Клик на кнопку отправки (Success)')
    except Exception as e:
        print(f'Ошибка при клике на кнопку отправки: {e}')

    try:
        assert text_2 not in result_area_2.text_content()
        assert text_3 not in result_area_2.text_content()
        print('Шаг 30: проверили, что при заполнении только 2го и 3го поля, результат не соответствует ожидаемому(тк 1е поле обязательное) (Success)')
    except Exception as e:
        print(f'Ошибка при проверке результата: {e}')
        
        
        
        
        
        
        
        
        
        
        
