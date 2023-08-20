import requests
from endpoints.status_check import StatusCheck


class GetAllMemes(StatusCheck):
    response = None

    def __init__(self, token=None):
        self.token = token
        self.header = {'Authorization': f'{self.token}'}

    def get_all_memes(self):
        response = requests.get('http://167.172.172.115:52355/meme', headers=self.header)
        self.response = response
