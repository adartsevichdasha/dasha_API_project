import requests
from endpoints.status_check import StatusCheck


class DeleteMeme(StatusCheck):
    response = None

    def __init__(self, token=None, meme_id=None):
        self.token = token
        self.header = {'Authorization': f'{self.token}'}
        self.meme_id = meme_id

    def delete_meme(self):
        response = requests.delete(f'http://167.172.172.115:52355/meme/{self.meme_id}', headers=self.header)
        self.response = response

    def check_the_response_message(self):
        return self.response.text == f'Meme with id {self.meme_id} successfully deleted'

    def check_that_meme_is_not_found(self):
        response = requests.get(f'http://167.172.172.115:52355/meme/{self.meme_id}', headers=self.header)
        return response.status_code == 404
