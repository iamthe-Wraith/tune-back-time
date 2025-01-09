import os
import pprint
from dotenv import load_dotenv
from user_input import get_date
from spotify import Spotify
from billboard import Billboard
load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

try:
    sp = Spotify(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)
    billboard = Billboard()

    songs = billboard.get_songs()

    playlist = sp.create_playlist(f"Billboard 100 - {billboard.date.strftime('%Y-%m-%d')}", songs, billboard.date.year)
except Exception as e:
    print(e)