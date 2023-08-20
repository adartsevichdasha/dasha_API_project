import requests
from endpoints.status_check import StatusCheck


class CheckToken(StatusCheck):
    response = None

    def __init__(self, token=None, user=None):
        self.token = token
        self.user = user

    def get_token_info(self):
        response = requests.get(f'http://167.172.172.115:52355/authorize/{self.token}')
        self.response = response

    def token_is_alive(self):
        return self.response.text == f'Token is alive. Username is {self.user}'
