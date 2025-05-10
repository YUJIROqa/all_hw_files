from locust import task, HttpUser
import random

class MemeUser(HttpUser):
    # token=None

    # def on_start(self):
    #     response = self.client.post('https://www.qa-practice.com/', json={'nsme': 'egor'})
    #     token=response.json()['token']

    # @task
    # def get_all_memes(self):
    #     self.client.get('https://www.qa-practice.com/'
    #                     headers={'Authorization': f'Bearer {self.token}'})
            

    
    @task(1)
    def get_all_memes(self):
        self.client.get('https://www.qa-practice.com/')

    # @task(3)
    # def get_all_memes(self):
    #     self.client.get(f'https://www.qa-practice.com/meme/{random.choice([21, 29, 276, 155])}')

