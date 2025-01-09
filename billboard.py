import requests
from bs4 import BeautifulSoup
from user_input import get_date

class Billboard:
    def __init__(self):
        self.url = "https://www.billboard.com/charts/hot-100"
        self.date = None

    def get_songs(self):
        try:
            self.date = get_date()

            print(f"getting songs for date: {self.date.strftime('%Y-%m-%d')}...")

            url = f"{self.url}/{self.date.strftime('%Y-%m-%d')}"

            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

            response = requests.get(url, headers=headers)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")

            songs_html = soup.select(".chart-results-list .o-chart-results-list__item h3.c-title")
            songs = [song.getText().strip() for song in songs_html] 

            print(f"[+] {len(songs)} songs found")

            return songs
        except Exception as e:
            print(e)
            return None