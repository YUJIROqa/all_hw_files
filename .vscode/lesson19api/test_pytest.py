import requests
import pytest
import allure

@pytest.fixture
def new_post_id():
    body = {"title": "fsakjdhfkasjdhflkajsdhlkfjashdfoo", "body": "barasdfaskdjfhlaksdfoiwueysdhgkjashdkfjhalskdjfhasdf", "userId": 1}
    headers = {'Content-Type': 'application/json'}
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json=body, headers=headers)
    post_id = response.json()['id'] 
    print(post_id)
    yield post_id
    print('Deliting the post')
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')


@pytest.fixture(scope='session') #scope - область видимости фикстуры. function - перед каждой функцией где ее обозначили
def hello():                     # sesseion - для всех функций(то есть обертка для всех функций)
    print('hello')               #вызывается перед той функцией куда ее засунули а постусловие после выполнения всех
    yield
    print('bye')

@allure.feature('Get one post')
@allure.story('Posts')
@pytest.mark.smoke
def test_get_one_post(new_post_id): #new_post_id - это фикстура, которая будет вызываться перед каждым тестом
    print('Test one post')
    with allure.step(f'Run get requests for post with id {new_post_id}'): #steps - шаги в allure
        response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{new_post_id}').json()
    with allure.step(f'Check that post id is {new_post_id}'):
        assert response['id'] == new_post_id

@allure.feature('Get all posts')
@allure.story('Posts')
@pytest.mark.regression
def test_get_all_posts(hello):
    print('Test get all posts')
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    assert len(response) == 100

@allure.feature('Posts')
def test_add_post():
    print('Test add post')
    with allure.step('Prepare test data'):
        body = {
            "title": "foo",
            "body": "bar",
            "userId": 1
        }
    headers = {'Content-Type': 'application/json'}
    with allure.step('Run request ot create post'):
        response = requests.post('https://jsonplaceholder.typicode.com/posts', json=body, headers=headers)
    with allure.step('Check response code is 201'):
        assert response.status_code == 201
    with allure.step('Check that post id is 101'):
        assert response.json()['id'] == 101

@allure.feature('Equal')
@allure.story('Example')
@pytest.mark.regression
def test_one():
    assert 1 == 1

@allure.feature('Equal')
@allure.story('Example')
@pytest.mark.parametrize('logins', ['', ' ', '(*&)'])
def test_two(logins):
    print(logins)
    assert 2 == 2

@allure.feature('Equal')
@allure.story('Example')
@pytest.mark.smoke
def test_three():
    assert 3 == 3
    
    
