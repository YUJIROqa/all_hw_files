import requests
import allure

@allure.feature('Delete post')
@allure.story('Posts')
def test_delete(new_post_id):
    requests.delete('https://jsonplaceholder.typicode.com/posts/1')

@allure.feature('Print')
@allure.story('Example')
def test_num(num):
    print(num)
