import pytest
from api.base_api import BaseApi
import requests

def test_get_post_by_id(base_url):
    # Создаём простой запрос к API для получения поста с ID=1
    response = requests.get(f"{base_url}/posts/1")
    
    # Создаём экземпляр BaseApi для проверки статус-кода
    api = BaseApi(base_url, response)
    
    # Проверяем статус-код
    api.check_status_code(200)
    
    # Проверяем, что в ответе есть нужные данные
    post_data = response.json()
    assert post_data["id"] == 1, "ID поста не соответствует ожидаемому"