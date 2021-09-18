from spotify_refresh import Refresh
from bs4 import BeautifulSoup
from secret_tokens import * 
import requests,json
class Spotify(object):
    def __init__(self):
        r1 = Refresh()
        self.access_token = r1.refresh()
        self.header = {"Authorization": f"Bearer {self.access_token}"}
    def currentlyPlaying(self):
        query = "https://api.spotify.com/v1/me/player/currently-playing?market=TR&additional_types=track"
        response = requests.get(
            query,
            headers=self.header
        )
        response = json.loads(response.text)
        song_name = response["item"]["name"]
        artists_name = [artist["name"] for artist in response["item"]["artists"]]
        artists_name = ",".join(artists_name)
        return f"{artists_name} - {song_name}"
class Genius(object):
    def __init__(self):
        self.s1 = Spotify()
        self.access_token = access_token
        self.header = {"Authorization": f"Bearer {self.access_token}"}
    def searchUrl(self):
        query = "http://api.genius.com/search"
        response = requests.get(
            query,
            headers=self.header,
            params={"q":f"{self.s1.currentlyPlaying()}"}
        )
        response = json.loads(response.text)
        hits = response["response"]["hits"]
        for item in hits:
            if item["type"] == "song":
                url = item["result"]["url"]
            break
        return url
    def Lyric(self):
        while True:
            try:
                page = requests.get(self.searchUrl())
                html = BeautifulSoup(page.text,"html.parser")
                for h in html("script"):
                    h.extract()
                lyrics = html.find("div",{"class":"lyrics"}).text
                print(lyrics)
            except AttributeError:
                continue
g1 = Genius()
g1.Lyric()
