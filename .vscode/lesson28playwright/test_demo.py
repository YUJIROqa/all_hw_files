from playwright.sync_api import Page, expect, Request, Response, Route
from time import sleep
import re
from playwright.sync_api import BrowserContext
from playwright.sync_api import Dialog
import json

def test_listen(page: Page):
    def print_request(request: Request):
        print('Request', request.post_data, request.url)
    page.on('request', print_request)
    page.on('response', lambda response: print('Response', response.url, response.status))
    page.goto('https://www.qa-practice.com')
    page.get_by_role('link', name='Text input').click()
    input = page.locator('#id_text_string')
    input.fill('qwerty')
    input.press('Enter')
    
def test_catch_response(page: Page):
    page.goto('https://www.airbnb.ru/')
    # with page.expect_response(re.compile('autosuggestions'))
    with page.expect_response('**/autosuggestions**') as response_event:
        page.get_by_test_id('header-tab-search-block-tab-EXPERIENCES').click()

    response = response_event.value
    print(response.url)
    print(response.status)
    response_data = response.json()
    assert response_data['show_nearby'] is False
     
def test_weather(page: Page):
    page.set_viewport_size({"width": 1920, "height": 1080})  # Примерные размеры для полного экрана

    def handle_route(route: Route):
        response = route.fetch()
        body = response.json()
        body['temperature'] = '+32'
        body['icon'] = 'A2'
        body = json.dumps(body)
        route.fulfill(response=response, body=body)
    page.route('**/pogoda/**', handle_route)
    page.goto('https://www.onliner.by/')
    page.locator('[name="query"]').click()
    sleep(50)

def test_api(page: Page):
    response = page.request.get('https://jsonplaceholder.typicode.com/posts/42')
    print(response.json(), response.status)
    expect(response).to_be_ok()
    assert response.json()['id'] == 42
    print(type(response))


def test_change_request(page: Page):
    # Функция для обработки запросов
    def change_req(route: Route):
        url = route.request.url
        print(url)
        url = url.replace('&filter3=15p01', 'hyilo')
        
        # Здесь можно модифицировать запрос или ответ
        route.continue_(url=url)  # Разрешаем запросу продолжиться
    
    # Регистрируем перехватчик для URL, содержащих '/product/finder'
    page.route(re.compile('/product/finder'), change_req)
    
    # Открываем страницу Samsung с Galaxy Z
    page.goto('https://www.samsung.com/au/smartphones/galaxy-z/')
    sleep(2)
    
    # Находим чекбокс по атрибуту for
    p = page.locator('//*[@for="checkbox-series15p01"]')
    sleep(3)
    p.click()
    sleep(2)

def test_API(page: Page):
    response = page.request.get('https://jsonplaceholder.typicode.com/posts/42')
    print(response.json(), response.status)
    assert response.json()['id'] == 42
