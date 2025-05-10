from playwright.sync_api import Page, expect, Request, Route, APIResponse
from time import sleep
import re
import json

def test_1(page: Page):

    # def print_request(request: Request):
    #     print('REQUEST: ', request.url, request.post_data)

    def print_response(response: APIResponse):#определяем функцию респонс
        print('RESPONSE: ', response.url, response.status) #выводим в консоль url и статус
    
    page.on('request', lambda request: print('REQUEST: ', request.url, request.post_data)) #определяем функцию реквес и сразу вызываем ее
    #page.on('response', lambda response: print('RESPONSE: ', response.url, response.status))

    #page.on('request', print_request)
    page.on('response', print_response)#вызываем функцию респонс
    # можно использовать и так. page.on("респорн/реквест", либо функция, либо лямбда)

    page.goto('https://www.qa-practice.com/')
    page.get_by_text('Text input').click()
    area = page.locator('#id_text_string')
    area.fill('fuck_off')
    area.press('Enter')
    text = page.locator('#result-text')
    expect(text).to_have_text('fuck_off')

def test_2(page: Page):

    def handle_css(route: Route):
        response = route.fetch()#получаем оригинальный ответ
        css_text = response.text()#извлекаем текстовое содержимое файла

        modified_css = css_text.replace('background-color: #fff', 'background-color: #d40000')
        #заменяем оригинальный цвет на новый

        route.fulfill(
        response=response,
        body=modified_css) #отправляем модифицированный css


# Регистрируем обработчик только для main.css
    page.route('**/static/home/styles/main.css', handle_css)
    page.goto('https://www.qa-practice.com/')

    page.get_by_text('Text input').click()
    sleep(10)


def test_3(page: Page):
    response = page.request.get('https://jsonplaceholder.typicode.com/users/1') #получаем ответ с этого эндпоинта
    expect(response).to_be_ok() #проверяем что ответ ок(200-299)
    assert response.json()['name'] == 'Leanne Graham' #проверяем что в ответе есть такой юзер
    request = page.request.post('https://jsonplaceholder.typicode.com/posts',
                                 data = {'userId': '666',
                                          'id': '16',
                                          'title':'gone',
                                          'body':'ебал ваш рот'}) #отправляем свой запрос с такими данными
    assert request.status == 201 #проверяем что ответ ок(201)     #они там не сохраняются в целом, но ответ приходит и можем проверить сохранение
    expect(request).to_be_ok() #проверяем что ответ ок(200-299)
    assert request.json()['title'] == 'gone' #проверяем что в ответе есть такой юзер

def test_4(page: Page): #

    def block_js(route: Route): #блокируем все js
        route.abort() #отменяем запрос. если перевести на русский, то роутниг(запросы) отменяется

    page.route("**/*.js", block_js)#запросы похожие на первый аргумент(регулярка(**/*.js)) отменяются(block_js)
    page.goto('https://www.qa-practice.com/')
    page.get_by_text('Text input').click()
    sleep(10)

