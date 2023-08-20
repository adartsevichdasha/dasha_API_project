import requests
import string
import random
from endpoints.status_check import StatusCheck


class PostNewMeme(StatusCheck):
    response = None
    meme_id = None
    text = None
    url = None
    tags = None
    info = None

    def __init__(self, token=None):
        self.token = token
        self.header = {'Authorization': f'{self.token}'}
        self.data = {
            "text": random.choice(string.ascii_lowercase),
            "url": f'https://{random.choice(string.ascii_lowercase)}.com',
            "tags": [
                random.choice(string.ascii_lowercase),
                random.choice(string.ascii_lowercase)
            ],
            "info": {
                "picture": f'https://{random.choice(string.ascii_lowercase)}.com',
                "video": f'https://{random.choice(string.ascii_lowercase)}.com'
            }
        }

    def post_meme(self):
        response = requests.post('http://167.172.172.115:52355/meme', headers=self.header, json=self.data)
        self.response = response
        self.meme_id = response.json()['id']
        self.text = response.json()['text']
        self.url = response.json()['url']
        self.tags = response.json()['tags']
        self.info = response.json()['info']

    def text_is_same_as_sent(self):
        return self.text == self.data['text']

    def url_is_same_as_sent(self):
        return self.url == self.data['url']

    def tags_are_same_as_sent(self):
        return self.tags == self.data['tags']

    def info_is_same_as_sent(self):
        return self.info == self.data['info']
