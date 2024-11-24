from lyricsgenius import Genius
from langdetect import detect

acess_token = "10LhD1KafxBBhvPcj6UyMywFIcRLpKHDs7eerBbcSN0JnhDCACheaVehMjK6qQb0"

def detectarLingua(nomeMusica, nomeArtista):
    try:
        genius = Genius(acess_token)
        song = genius.search_song(title=nomeMusica, artist=nomeArtista)
    except Exception as e:
        return "erro"
    if (song == None):
        return "NotFound"
    return detect(song.lyrics)