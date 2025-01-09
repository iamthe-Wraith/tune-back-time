import os
import pprint
from dotenv import load_dotenv
from user_input import get_date, get_name
from spotify import Spotify
from billboard import Billboard
load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

try:
    sp = Spotify(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)
    billboard = Billboard()

    date = get_date()
    name = get_name(date)

    songs = billboard.get_songs(date)

    playlist = sp.create_playlist(name, songs, date.year)
except Exception as e:
    print(e)