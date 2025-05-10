import requests


def all_posts():
    # response = requests.request('GET', 'https://jsonplaceholder.typicode.com/posts')
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    assert len(response) == 100, 'Not all posts returned'


def one_post():
    post_id = new_post()
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}').json()
    assert response['id'] == post_id


def post_a_post():
    body = {
        "title": "fsakjdhfkasjdhflkajsdhlkfjashdfoo",
        "body": "barasdfaskdjfhlaksdfoiwueysdhgkjashdkfjhalskdjfhasdf",
        "userId": 1
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        json=body,
        headers=headers
    )
    assert response.status_code == 201, 'Status code is incorrect'
    assert response.json()['id'] == 101, 'Id is incorrect'


def new_post():
    body = {
        "title": "fsakjdhfkasjdhflkajsdhlkfjashdfoo",
        "body": "barasdfaskdjfhlaksdfoiwueysdhgkjashdkfjhalskdjfhasdf",
        "userId": 1
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        json=body,
        headers=headers
    )
    return response.json()['id']


def clear(post_id):
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')


def put_a_post():
    post_id = new_post()
    body = {
        "title": "fsakjdhfkasjdhflkajsdhlkfjashdfoo-UPD",
        "body": "barasdfaskdjfhlaksdfoiwueysdhgkjashdkfjhalskdjfhasdf-UPD",
        "userId": 1
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'https://jsonplaceholder.typicode.com/posts/{post_id}',
        json=body,
        headers=headers
    ).json()
    assert response['title'] == 'fsakjdhfkasjdhflkajsdhlkfjashdfoo-UPD'
    clear(post_id)


def patch_a_post():
    post_id = new_post()
    body = {
        "body": "barasdfaskdjfhlaksdfoiwueysdhgkjashdkfjhalskdjfhasdf-UPD",
        "userId": 7
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'https://jsonplaceholder.typicode.com/posts/{post_id}',
        json=body,
        headers=headers
    ).json()
    print(response)
    clear(post_id)


def delete_a_post():
    post_id = new_post()
    response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
    print(response.json())
    print(response.status_code)


print('w'*50)

def new_post():
    print('Post request')
    body = {
           "title": "football",
           "body": "baritone",
           "userId": 1488
       }
    headers = {'Content-type': 'application/json'}
    response = requests.post(
           'https://jsonplaceholder.typicode.com/posts',
           json=body,
           headers=headers
       )
    response_json = response.json()
    print("New post response:", response_json)
    return response_json['id']  # Возвращает только ID созданного поста

print('='*50)

def get_users():
    print('Getting user...')
    response = requests.get('https://jsonplaceholder.typicode.com/users/1')
    print(f"name: {response.json()['name']}") # выводим имя пользователя. {все данные['конкретно имя']}
    print(f"email: {response.json()['email']}") # выводим email пользователя. {все данные['конкретно email']}
    print('Status code:', response.status_code) # выводим статус код

get_users()

print('='*50)

def create_users():
    print('Creating user...')
    body = {       # создаём тело запроса
        "name": "Egor",
        "email": "egor@gmail.com",
        "phone": "+380671234567"
    }
    headers = {'Content-Type': 'application/json'} # добавляем заголовок
    response = requests.post('https://jsonplaceholder.typicode.com/users', json=body, headers=headers)
    print(response.json()) #выводим ответ в формате json
    print(response.status_code) #выводим статус код. Что бы он выводился, нужно изначальный ответ хранить не в json
    print(f"id: {response.json()['id']}") #выводим что-то похожее на id из респонса

create_users()

print('='*50)

def update_users_put():
    print('Full updating user...')
    user_id =1 # создаём нового пользователя
    body = {
        "name": "Pidor",
        "email": "pidor@pidor.gay",
        "username": "pidor_sosy",
        "phone": "+888888888888"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(f'https://jsonplaceholder.typicode.com/users/{user_id}', json=body, headers=headers)
    
    response_json = response.json()
    print(response_json)
    print(response.status_code)
    print(f"id: {response_json['id']}")

update_users_put()

print('='*50)

def update_users_patch():
    print('Partial updating user...')
    user_id =2 # создаём нового пользователя
    body = {
        "name": "Pidor",
        "email": "pidor@pidor.gay",
        
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(f'https://jsonplaceholder.typicode.com/users/{user_id}', json=body, headers=headers)
    
    response_json = response.json()
    print(response_json)
    print(response.status_code)
    print(f"id: {response_json['id']}")

update_users_patch()

print('='*50)

def delete_users():
    print('Deleting user...')
    user_id = 1
    response = requests.delete(f'https://jsonplaceholder.typicode.com/users/{user_id}')
    response_json = response.json()
    print(response_json)
    print(response.status_code)
    assert response.status_code == 200, 'Status code is incorrect'
delete_users()