from spotify_connection import *
from musicas_db import *

token = get_token()
track_quantity = 2200
tracks = []
i = 0
#parei nesse loop. não testei direito rodando com o loop, mas chamando 10 sozinhos funcionou
while i < track_quantity:
    tracks.append(get_liked_tracks(token=token, offset= 0, limit= 50))
    i += 50

for track in tracks:
    nome_musica = track['name']
    nome_artistas = track['artists']
    id_musica = record_musica(nome_musica)
    ids_artista = [record_artista(nome) for nome in nome_artistas]

    ids_artista_musica = [record_artista_musica(id_artista=id_artista, id_musica=id_musica) for id_artista in ids_artista]

    print(nome_musica)
