import requests

class PostApi(BaseApi):
    def __init__(self, base_url, last_response=None):
        super().__init__(base_url, last_response)

    def get_all_posts(self):
        response = requests.get(f"{self.base_url}/posts")
        return response.json()
    
    def get_post_by_id(self, post_id):
        

