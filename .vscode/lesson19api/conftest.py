import pytest
import requests 

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

@pytest.fixture
def api_url1():
    yield 'https://jsonplaceholder.typicode.com'
    print('Api url is done')


