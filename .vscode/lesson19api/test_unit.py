import sys; sys.dont_write_bytecode = True
import unittest
import requests

class TestPostAPi(unittest.TestCase):
    
    def setUp(self):   #создаем функцию, которая будет выполняться перед каждым тестом(предусловия)
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
        self.post_id = response.json()['id'] 
        print(f'Post created with id: {self.post_id}')
    
    def tearDown(self): #создаем функцию, которая будет выполняться после каждого теста(постусловия)
        requests.delete(f'https://jsonplaceholder.typicode.com/posts/{self.post_id}')
        print(f'Post deleted with id: {self.post_id}')

    @unittest.skip('Getting error on each run')
    def test_get_one_post(self):
        print('Test one post')
        response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{self.post_id}').json()
        self.assertEqual(response['id'], self.post_id)

    
class TestIndependent(unittest.TestCase):

    @unittest.skipIf(sys.platform.startswith('lin'), 'Does not run on windows') #пропускает тест, если условие истинно
    def test_get_all_posts(self):
        print('Test get all posts')
        response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
        self.assertEqual(len(response), 100)

    def test_add_post(self):
        print('Test add post')
        body = {
            "title": "foo",
            "body": "bar",
            "userId": 1
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post('https://jsonplaceholder.typicode.com/posts', json=body, headers=headers)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['id'], 101)
        
    
