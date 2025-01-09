import spotipy
from spotipy.oauth2 import SpotifyOAuth

class Spotify:
    def __init__(self, client_id, client_secret, redirect_uri="http://example.com"):
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=client_id,
                client_secret=client_secret,
                redirect_uri=redirect_uri,
                scope="playlist-modify-private",
            )
        )

    def create_playlist(self, name, songs, year=None):
        try:
            print("creating playlist...")
            song_uris = self.get_song_uris(songs, year)
            spotify_user = self.get_user()

            if spotify_user is None:
                print("[-] Failed to get user")
                return

            playlist = self.sp.user_playlist_create(spotify_user["id"], name, public=False)["id"]
            self.sp.playlist_add_items(playlist, song_uris)

            print(f"[+] Playlist created:")
            print(f"\turl: https://open.spotify.com/playlist/{playlist}")
            print(f"\tname: {name}")

            return playlist
        except Exception as e:
            print(e)
            return None

    def get_song_uris(self, songs, year=None):
        try:
            song_uris = []
            for song in songs:
                # Add year to search query if provided to improve accuracy
                query = f"{song} year:{year}" if year else song
                result = self.sp.search(query, type="track", limit=1)
                
                if result["tracks"]["items"]:
                    song_uris.append(result["tracks"]["items"][0]["uri"])
                    
            return song_uris
        except Exception as e:
            print(e)
            return None

    def get_user(self):
        try:
            return self.sp.current_user()
        except Exception as e:
            print(e)
            return None
