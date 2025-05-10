import pytest


@pytest.mark.smoke
def test_success_login(login_page):
    login_page.open_page()
    login_page.login('tomsmith', 'SuperSecretPassword!')
    assert login_page.is_login_success()

@pytest.mark.smoke
def test_unsuccess_username(login_page):
    login_page.open_page()
    login_page.login('tomsmith1', 'SuperSecretPassword!')
    assert not login_page.is_login_success()

@pytest.mark.smoke
def test_unsuccess_password(login_page):
    login_page.open_page()
    login_page.login('tomsmith', 'SuperSecretPassword!1')
    assert not login_page.is_login_success()

