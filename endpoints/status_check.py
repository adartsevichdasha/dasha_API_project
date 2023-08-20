class StatusCheck:
    response = None

    def status_code_is_200(self):
        return self.response.status_code == 200
