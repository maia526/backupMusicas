import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
from urllib.parse import urlencode
import base64
import webbrowser

scope = "user-library-read"

client_id = ""
client_secret = ""

def get_token():
    code = get_authorization_code()

    encoded_credentials = base64.b64encode(client_id.encode() + b':' + client_secret.encode()).decode("utf-8")

    token_headers = {
        "Authorization": "Basic " + encoded_credentials,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    token_data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": "http://localhost/"
    }

    r = requests.post("https://accounts.spotify.com/api/token", data=token_data, headers=token_headers)
    token = r.json()["access_token"]

    return token

def get_authorization_code():
    auth_headers = {
        "client_id": client_id,
        "response_type": "code",
        "redirect_uri": "http://localhost/",
        "scope": "user-library-read"
    }

    webbrowser.open("https://accounts.spotify.com/authorize?" + urlencode(auth_headers))

    code = input("insert your authorization code here: ")
    return code

def get_liked_tracks(token, offset, limit):
    user_headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json"
    }

    user_params = {
        "limit": limit,
        "offset": offset
    }

    user_tracks_response = requests.get("https://api.spotify.com/v1/me/tracks", params=user_params, headers=user_headers)

    items = user_tracks_response.json()['items']
    tracks = [track["track"] for track in items]

    liked_tracks = []
    for track in tracks:
        musica = {
            "name" : track['name'],
            "artists" : [artist['name'] for artist in track['artists']],
            "spotify_id" : track['id']
        }
        liked_tracks.append(musica)
    return liked_tracks
