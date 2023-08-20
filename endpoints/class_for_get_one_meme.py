import requests
from endpoints.status_check import StatusCheck


class GetOneMeme(StatusCheck):
    response = None

    def __init__(self, token=None, meme_id=None):
        self.token = token
        self.header = {'Authorization': f'{self.token}'}
        self.meme_id = meme_id

    def getting_one_meme(self):
        response = requests.get(f'http://167.172.172.115:52355/meme/{self.meme_id}', headers=self.header)
        self.response = response

    def check_meme_id_is_same_as_sent(self):
        return self.meme_id == self.response.json()['id']
