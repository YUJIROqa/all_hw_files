import pytest

@pytest.mark.smoke
def test_incorrect_data(login_page):
    login_page.open_page()
    login_page.fill_email('test1325452@mail.ru')
    login_page.fill_password('111111')
    login_page.click_login_button()
    assert login_page.check_errors() == 'Login was unsuccessful. Please correct the errors and try again.\nNo customer account found'


@pytest.mark.validation
def test_empty_data(login_page):
    login_page.open_page()
    login_page.click_login_button()
    assert login_page.check_errors() == 'Login was unsuccessful. Please correct the errors and try again.\nNo customer account found'

@pytest.mark.smoke
def test_correct_login(login_page):
    test_email = 'egor.misha11111@mail.ru'
    login_page.open_page()
    login_page.fill_email(test_email)
    login_page.fill_password('111111')
    login_page.click_login_button()
    assert login_page.check_your_authorized() == test_email
