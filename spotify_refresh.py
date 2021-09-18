import requests,json
from secret_tokens import *
class Refresh(object):
    def __init__(self):
        self.refresh_token = refresh_token
        self.base_64 = base_64
    def refresh(self):
        query = "https://accounts.spotify.com/api/token"
        response = requests.post(
            query,
            data={"grant_type": "refresh_token",
                  "refresh_token": self.refresh_token},
            headers={"Authorization": "Basic "+self.base_64})
        response_json = json.loads(response.text)
        return response_json["access_token"]