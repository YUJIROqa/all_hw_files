from playwright.sync_api import Page, expect
#from conftest import logger

def test_1(page: Page):

    try:
        page.goto('https://www.qa-practice.com/')
        print('Шаг 1: Перешли на страницу https://www.qa-practice.com/ (Success)')
    except Exception as e:
        print(f'Ошибка при переходе на страницу https://www.qa-practice.com/: {e}')
    
    try:
        #page.get_by_text('Text input').click()
        button_text_input = page.locator('//*[@href="/elements/input/simple"]')
        button_text_input.click()
        print('Шаг 2: Переход на страницу Text input (Success)')
    except Exception as e:
        print(f'Ошибка при переходе на страницу Text input: {e}')

    try:
        expect(page).to_have_title('Input Field | Text Input | QA Practice')
        print('Шаг 3: Проверка заголовка страницы (Success)')
    except Exception as e:
        print(f'Ошибка при проверке заголовка страницы: {e}')

    try:
        expect(page).to_have_url('https://www.qa-practice.com/elements/input/simple')
        print('Шаг 3.1: Проверка URL страницы (Success)')
    except Exception as e:
        print(f'Ошибка при проверке URL страницы: {e}')
 
    try:
        submit_field = page.get_by_placeholder('Submit me')
        expect(submit_field).to_be_visible()
        print('Шаг 4: Поиск и проверка поля Submit me (Success)')
    except Exception as e:
        print(f'Ошибка при проверке поля Submit me: {e}')

    try:
        req_button = page.get_by_text('Requirements:')
        expect(req_button).to_be_enabled()
        print('Шаг 5: Поиск и проверка кнопки Requirements (Success)')
    except Exception as e:
        print(f'Ошибка при проверке кнопки Requirements: {e}')

    try:
        text= 'AaZz109_-'
        submit_field.fill(text)
        submit_field.press('Enter')
        result_field = page.locator('//*[@id="result-text"]')
        expect(result_field).to_have_text(text)
        print('Шаг 6: Позитивный тест кейс (Success)')
    except Exception as e:
        print(f'Ошибка при заполнении поля Submit me: {e}')

    try:
        text= 'z'
        submit_field.fill(text)
        submit_field.press('Enter')
        warning_field = page.locator('//*[@class="invalid-feedback"]')
        expect(warning_field).to_have_text('Please enter 2 or more characters')
        print('Шаг 7: Негативный тест кейс(Кириллица) (Success)')
    except Exception as e:
        print(f'Ошибка негативного тест кейса(Кириллица): {e}')

    try:
        text = 'егор'
        submit_field.fill(text)
        submit_field.press('Enter')
        warning_field = page.locator('//*[@class="invalid-feedback"]')
        expect(warning_field).to_have_text('Enter a valid string consisting of letters, numbers, underscores or hyphens.')
        print('Шаг 8: Негативный тест кейс(Короткая строка) (Success)')
    except Exception as e:
        print(f'Ошибка негативного тест кейса(Короткая строка): {e}')

    try:
        text = 'sdfsghdsfasfsdghfgsfdafsdgfhngfs'
        submit_field.fill(text)
        submit_field.press('Enter')
        warning_field = page.locator('//*[@class="invalid-feedback"]')
        expect(warning_field).to_have_text('Please enter no more than 25 characters')
        print('Шаг 9: Негативный тест кейс(Слишком длинная строка) (Success)')
    except Exception as e:
        print(f'Ошибка негативного тест кейса(Слишком длинная строка): {e}')
    
    try:
        text = '    '
        submit_field.fill(text)
        submit_field.press('Enter')
        warning_field = page.locator('//*[@class="invalid-feedback"]')
        expect(warning_field).to_have_text('This field is required.')
        print('Шаг 10: Негативный тест кейс(Пробелы) (Success)')
    except Exception as e:
        print(f'Ошибка негативного тест кейса(Пробелы): {e}')

    try:
        button_email_field = page.get_by_text('Email field')
        button_email_field.click()
        print('Шаг 11: Поиск и проверка кнопки Email field (Success)')
    except Exception as e:
        print(f'Ошибка при проверке кнопки Email field: {e}')

    try:
        expect(page).to_have_title('Input Field | Email Field | QA Practice')
        print('Шаг 12: Проверка заголовка страницы (Success)')
    except Exception as e:
        print(f'Ошибка при проверке заголовка страницы: {e}')

    try:
        expect(page).to_have_url('https://www.qa-practice.com/elements/input/email')
        print('Шаг 12.1: Проверка URL страницы (Success)')
    except Exception as e:
        print(f'Ошибка при проверке URL страницы: {e}')

    try:
        email_field = page.get_by_placeholder('Submit me')
        expect(email_field).to_be_visible()
        print('Шаг 13: Поиск и проверка поля Email field (Success)')
    except Exception as e:
        print(f'Ошибка при проверке поиска поля Email field: {e}')

    try:
        email = 'test@test.com'
        email_field.fill(email)
        email_field.press('Enter')
        result_field = page.locator('//*[@id="result-text"]')
        expect(result_field).to_have_text(email)
        print('Шаг 14: Позитивный тест кейс Почты(test@test.com) (Success)')
    except Exception as e:
        print(f'Ошибка при проверке ввода почты(test@test.com): {e}')

    try:
        email = 'test@test'
        email_field.fill(email)
        email_field.press('Enter')
        warning_field = page.locator('//*[@class="invalid-feedback"]')
        expect(warning_field).to_have_text('Enter a valid email address.')
        print('Шаг 15: Негативный тест кейс Почты(test@test) (Success)')
    except Exception as e:
        print(f'Ошибка при проверке ввода почты(test@test): {e}')

    try:
        email = 'тест@тест.рф'
        email_field.fill(email)
        email_field.press('Enter')
        warning_field = page.locator('//*[@class="invalid-feedback"]')
        expect(warning_field).to_have_text('Enter a valid email address.')
        print('Шаг 16: Негативный тест кейс Почты(test@test.com) (Success)') 
    except Exception as e:
        print(f'Ошибка при проверке ввода почты(тест@тест.рф): {e}')

    try:
        email = 'test@test@test.com'
        email_field.fill(email)
        email_field.press('Enter')
        warning_field = page.locator('//*[@class="invalid-feedback"]')
        expect(warning_field).to_have_text('Enter a valid email address.')
        print('Шаг 17: Негативный тест кейс Почты(test@test.com) (Success)') 
    except Exception as e:
        print(f'Ошибка при проверке ввода почты(test@test@test.com): {e}')

    try:
        email = 'тест@тест.рф'
        email_field.fill(email)
        email_field.press('Enter')
        warning_field = page.locator('//*[@class="invalid-feedback"]')
        expect(warning_field).to_have_text('Enter a valid email address.')
        print('Шаг 18: Негативный тест кейс Почты(тест@тест.рф) (Success)') 
    except Exception as e:
        print(f'Ошибка при проверке ввода почты(тест@тест.рф): {e}')

    try:
        email = 'test@test@test.com'
        email_field.fill(email)
        email_field.press('Enter')
        warning_field = page.locator('//*[@class="invalid-feedback"]')
        expect(warning_field).to_have_text('Enter a valid email address.')
        print('Шаг 19: Негативный тест кейс Почты(test@test@test.com) (Success)') 
    except Exception as e:
        print(f'Ошибка при проверке ввода почты(test@test@test.com): {e}')

    try:
        email = '11'
        email_field.fill(email)
        email_field.press('Enter')
        warning_field = page.locator('//*[@class="invalid-feedback"]')
        expect(warning_field).to_have_text('Enter a valid email address.')
        print('Шаг 20: Негативный тест кейс Почты(11) (Success)') 
    except Exception as e:
        print(f'Ошибка при проверке ввода почты(11): {e}')

    try:
        email = ' '
        email_field.fill(email)
        email_field.press('Enter')
        warning_field = page.locator('//*[@class="invalid-feedback"]')
        expect(warning_field).to_have_text('This field is required.')
        print('Шаг 21: Негативный тест кейс Почты(пробелы) (Success)') 
    except Exception as e:
        print(f'Ошибка при проверке ввода почты(пробелы): {e}')

    try:
        button_pass_field = page.get_by_text('Password field')
        button_pass_field.click()
        print('Шаг 22: Поиск и проверка кнопки Password field (Success)')
    except Exception as e:
        print(f'Ошибка при проверке кнопки Password field: {e}')

    try:
        expect(page).to_have_title('Input Field | Password Field | QA Practice')
        print('Шаг 23: Проверка заголовка страницы (Success)')
    except Exception as e:
        print(f'Ошибка при проверке заголовка страницы: {e}')

    try:
        expect(page).to_have_url('https://www.qa-practice.com/elements/input/passwd')
        print('Шаг 23.1: Проверка URL страницы (Success)')
    except Exception as e:
        print(f'Ошибка при проверке URL страницы: {e}')
        
    try:
        pass_field = page.get_by_placeholder('Submit me')
        expect(pass_field).to_be_visible()
        print('Шаг 24: Поиск и проверка поля Password (Success)')
    except Exception as e:
        print(f'Ошибка при проверке поля Password field: {e}')

    try:
        password = '65Ipehib228320!'
        pass_field.fill(password)
        pass_field.press('Enter')
        result_field = page.locator('//*[@id="result-text"]')
        expect(result_field).to_have_text(password)
        print('Шаг 25: Позитивный тест кейс Пароля(65Ipehib228320!) (Success)')
    except Exception as e:
        print(f'Ошибка при проверке ввода пароля(65Ipehib228320!): {e}')

    try:
        password = '1234567890'
        pass_field.fill(password)
        pass_field.press('Enter')
        warning_field = page.locator('//*[@class="invalid-feedback"]')
        expect(warning_field).to_have_text('Low password complexity')
        print('Шаг 26: Негативный тест кейс Пароля(1234567890) (Success)')
    except Exception as e:
        print(f'Ошибка при проверке ввода пароля(1234567890): {e}')

    try:
        password = 'егор228320егор'
        pass_field.fill(password)
        pass_field.press('Enter')
        warning_field = page.locator('//*[@class="invalid-feedback"]')
        expect(warning_field).to_have_text('Low password complexity')
        print('Шаг 27: Негативный тест кейс Пароля(егор228320егор) (Success)')
    except Exception as e:
        print(f'Ошибка при проверке ввода пароля(егор228320егор): {e}')

    try:
        password = 'qwerty12345'
        pass_field.fill(password)
        pass_field.press('Enter')
        warning_field = page.locator('//*[@class="invalid-feedback"]')
        expect(warning_field).to_have_text('Low password complexity')
        print('Шаг 28: Негативный тест кейс Пароля(qwerty12345) (Success)')
    except Exception as e:
        print(f'Ошибка при проверке ввода пароля(qwerty12345): {e}')
    
    try:
        password = ' '
        pass_field.fill(password)
        pass_field.press('Enter')
        warning_field = page.locator('//*[@class="invalid-feedback"]')
        expect(warning_field).to_have_text('This field is required.')
        print('Шаг 29: Негативный тест кейс Пароля(пробелы) (Success)')
    except Exception as e:
        print(f'Ошибка при проверке ввода пароля(пробелы): {e}')

    
        








    
        
        
