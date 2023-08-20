import requests
import string
import random
from endpoints.status_check import StatusCheck


class UpdateMeme(StatusCheck):
    response = None
    meme_id = None
    id = None
    info = None
    tags = None
    text = None
    url = None

    def __init__(self, token=None, user=None, meme_id=None):
        self.token = token
        self.user = user
        self.meme_id = meme_id
        self.header = {'Authorization': f'{self.token}'}
        self.data = {
                "id": self.meme_id,
                "text": f'new_{random.choice(string.ascii_lowercase)}',
                "url": f'new_https://{random.choice(string.ascii_lowercase)}.com',
                "tags": [
                    f'new_{random.choice(string.ascii_lowercase)}',
                    f'new_{random.choice(string.ascii_lowercase)}'
                ],
                "info": {
                    "picture": f'new_https://{random.choice(string.ascii_lowercase)}.com',
                    "video": f'new_https://{random.choice(string.ascii_lowercase)}.com'
                }
            }

    def update_meme(self):
        response = requests.put(f'http://167.172.172.115:52355/meme/{self.meme_id}', json=self.data, headers=self.header
                                )
        self.response = response
        self.id = self.response.json()['id']
        self.info = self.response.json()['info']
        self.tags = self.response.json()['tags']
        self.text = self.response.json()['text']
        self.url = self.response.json()['url']

    def updated_info_is_same_as_sent(self):
        return self.response.json() == {
                        "id": self.data['id'],
                        "info": self.data['info'],
                        "tags": self.data['tags'],
                        "text": self.data['text'],
                        "updated_by": self.user,
                        "url": self.data['url']
                    }
