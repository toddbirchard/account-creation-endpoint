import requests
import os


class UserAccounts:
    """Create user accounts from submissions."""

    def __init__(self, username, email, gravatar):
        self.username = str(username)
        self.email = str(email)
        self.gravatar = gravatar
        self.headers = {
            'access_token': os.environ['HEADER_ACCESS_TOKEN'],
            'Content-Type': os.environ['HEADER_CONTENT_TYPE'],
            'client_id': os.environ['HEADER_CLIENT_ID'],
        }

    def create_account(self):
        body = {
            "resource": {
                "username": self.username,
                "email": self.email,
                "gravatar": self.gravatar
            }
         }
        r = requests.post('https://apisentris.com/api/v1/readers', data=body, headers=self.headers)
        return r.json()
