import requests
import string
import random
from endpoints.status_check import StatusCheck


class AuthorizeUser(StatusCheck):
    response = None
    token = None
    user = None

    def __init__(self, user_name=None):
        self.user_name = user_name
        if user_name:
            self.user_name = user_name
        else:
            self.user_name = random.choice(string.ascii_lowercase)

    def user_auth(self):
        body = {
            'name': self.user_name
        }
        response = requests.post('http://167.172.172.115:52355/authorize', json=body)
        self.response = response
        self.token = self.response.json()['token']
        self.user = self.response.json()['user']

    def name_is_same_as_sent(self):
        return self.user_name == self.response.json()['user']

    def token_is_not_empty(self):
        return len(self.token) > 0
