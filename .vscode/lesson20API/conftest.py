import pytest
from endpoints.CreateUrlEndpoint import CreateUrlEndpoint
from endpoints.get_url_endpoint import GetUrlEndpoint
import random
import string

@pytest.fixture()
def url_creator_endpoint():
    return CreateUrlEndpoint()

@pytest.fixture()
def url_getter_endpoint():
    return GetUrlEndpoint()

@pytest.fixture()
def random_string():
    return "".join(random.choices(string.ascii_lowercase) for _ in range(10)
                   
@pytest.fixture()
def create_tiny(url_creator_endpoint):
    long_url = f'https://{random_string()}.com'
    url_creator_endpoint.create_short_url_for_long_url()
    return url_creator_endpoint.code, long_url
