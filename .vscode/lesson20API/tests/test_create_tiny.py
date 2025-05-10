import requests
from endpoints.CreateUrlEndpoint import CreateUrlEndpoint


def test_create_short_url(url_creator_endpoint):
    site_url = 'https://www.discovery.com/shark-week/sw-schedule-2023-pictures'

    #Send request to create a short url for url in 'site_url'
    url_creator_endpoint.create_short_url_for_long_url(long_url=site_url)

    #Check that response status is OK
    url_creator_endpoint.check_response_ststus_is_ok()

    #Check that long url in the response corresponds to the 'site_url'
    url_creator_endpoint.check_long_url_same_as_sent()

    #Check that 'code' parameter is not empty
    url_creator_endpoint.check_code_is_not_empty()


def test_custom_short_url(url_creator_endpoint, random_string):    
    site_url = 'https://www.discovery.com/shark-week/sw-schedule-2023-pictures'
    # code = '123poiwerjdjd12lkjh2'
    code = random_string()
    
    # response = requests.post(
    #     'https://gotiny.cc/api',
    #      headers={'Content-Type': 'application/json'}, 
    #      json={'long': site_url, 'custom': code})
    url_creator_endpoint.create_short_url_for_long_url(site_url, code)

    # assert response.status_code == 200
    url_creator_endpoint.check_response_ststus_is_ok()

    # assert response.json()[0]['long'] == site_url
    url_creator_endpoint.check_long_url_same_as_sent()

    # assert response.json()[0]['code'] == code
    url_creator_endpoint.check_short_code_is_same_as_sent()

