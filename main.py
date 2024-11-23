from spotify_connection import *
from musicas_db import *

token = get_token()
track_quantity = 2201   # Colocar aqui a quantidade de músicas que você tem favoritadas
tracks = []
i = 0
while i < track_quantity:
    liked_tracks = get_liked_tracks(token=token, offset= i, limit= 50)
    for liked_track in liked_tracks:
        tracks.append(liked_track)
        i+=1
    

for track in tracks:
    nome_musica = track['name']
    nome_artistas = track['artists']
    id_musica = record_musica(nome_musica)
    ids_artista = [record_artista(nome) for nome in nome_artistas]

    ids_artista_musica = [record_artista_musica(id_artista=id_artista, id_musica=id_musica) for id_artista in ids_artista]

    print(nome_musica)
