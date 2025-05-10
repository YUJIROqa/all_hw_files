import requests

class BaseApi:
    def __init__(self, base_url, last_response=None):
        self.base_url = base_url
        self.last_response = last_response

    def check_status_code(self, expected_status_code):
        assert self.last_response.status_code == expected_status_code, f"Статус код не совпадает"
