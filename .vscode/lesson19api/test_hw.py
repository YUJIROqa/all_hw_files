import pytest
import requests
import allure
import json
w = '='*50

@pytest.fixture
def api_url():
    print('api_url')
    yield 'https://jsonplaceholder.typicode.com'
    print('bye')
    
def test_check():
    assert 'hello' in 'hello world'
    assert len('pytest') == 6

@pytest.mark.smoke
def test_check_title():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    response_json = response.json()
    assert response_json['title'] != None and response_json['title'] != '', 'Title is empty'
    assert response_json['id'] == 1, 'Id is not 1'
    assert response.status_code == 200, 'Status code is not 200'

def test_check_name(api_url):
    response = requests.get(f'{api_url}/users/1')
    response_json = response.json()
    assert response_json['name'] != None and response_json['name'] != '', 'Name is empty'
    assert response_json['id'] == 1, 'Id is not 1'
    assert response.status_code == 200, 'Status code is not 200'

@pytest.mark.parametrize('endpoint', ['/posts', '/users', '/comments'])
def test_check_ststus_cods(api_url, endpoint):
    response = requests.get(f'{api_url}{endpoint}')
    assert response.status_code == 200, f'Status code is not 200 for {endpoint}'

def test_create_check_delete(api_url):
    body = {"title": "title", "body": "body", "userId": 241}
    headers = {"Content-type": "application/json"}
    response_post = requests.post(f'{api_url}/posts', json=body, headers=headers)
    assert response_post.status_code == 201, 'Status code is not 201'

    response_get = requests.get(f'{api_url}/posts/{response_post.json()["id"]}')#берем переменную апиурл,/post/ далее из 
    get_data = response_get.json()              #ответа поста берем id и подставляем его
    assert get_data['title'] == body['title'], 'Title is not correct'
    assert get_data['body'] == body['body'], 'Body is not correct'
    assert get_data['userId'] == body['userId'], 'User id is not correct'

    response_delete = requests.delete(f'{api_url}/posts/{response_post.json()["id"]}')
    assert response_delete.status_code == 200, 'Status code is not 200'

    response_get_after_delete = requests.get(f'{api_url}/posts/{response_post.json()["id"]}')
    assert response_get_after_delete.status_code == 404, 'Status code is not 404'

print(w)

@pytest.mark.go
def test_hello():
    assert 'pytest' in 'hello, pytest', 'pytest is not in hello, pytest'
    print('Test hello is done')

@pytest.mark.go
def test_calculation():
    assert 2+2 == 4, '2+2 is not 4'
    assert 10-5 == 5, '10-5 is not 5'
    assert 3*3 == 9, '3*3 is not 9'
    print('Test calculation is done')

@pytest.mark.go
def test_check_users(api_url1):
    response = requests.get(f'{api_url1}/users/2')
    response_json = response.json()
    assert response_json['name'] != None and response_json['name'] != '', 'Name is empty'
    assert response_json['id'] == 2, 'Id is not 2'
    assert response.status_code == 200, 'Status code is not 200'
    print('Test check users is done')
    

@allure.feature('API tests')
@allure.story('Data Count Check')
@pytest.mark.go
@pytest.mark.parametrize('endpoint, expected_count', [('/posts',100), ('/users',10), ('/albums',100)], ids=['check post count', 'check user count', 'check album count'])
def test_endpoints(api_url1, endpoint, expected_count): #1 идет фикстура апиурл, 2 идет параметризация, 3 идет тест
    with allure.step(f'sending request to {endpoint}'):
        response = requests.get(f'{api_url1}{endpoint}')
    allure.attach(f'{api_url1}{endpoint}', name='Request', attachment_type=allure.attachment_type.TEXT)
    with allure.step(f'Transform response to json'):
        response_json = response.json()
    with allure.step(f'checking status code of {endpoint}'):
        assert response.status_code == 200, 'Status code is not 200'
    with allure.step(f'checking length of {endpoint}'):
        assert len(response_json) == expected_count, f'Number of {endpoint} is not {expected_count}'
    allure.attach('Asaslam aleikym bratia and sestri')
    with allure.step(f'printing result of test {endpoint}'):
        print(f'Test {endpoint} is done')


        
    


