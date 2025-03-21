from datetime import date
from typing import List

class Utente:
    def __init__(self, nome: str, email: str, password: str):
        self.nome = nome
        self.email = email
        self.password = password
        self.canali: List[Canale] = []
        self.playlists: List[Playlist] = []
        self.abbonamento: Abbonamento = None
        self.commenti: List[Commento] = []
        self.videos: List[Video] = []

    def guarda_video(self, video):
        self.videos.append(video)

    def crea_playlist(self, playlist):
        self.playlists.append(playlist)

    def commenta_video(self, video, commento):
        video.aggiungi_commento(commento)
        self.commenti.append(commento)


class Video:
    def __init__(self, titolo: str, descrizione: str, url: str, durata: float):
        self.titolo = titolo
        self.descrizione = descrizione
        self.url = url
        self.durata = durata
        self.commenti: List[Commento] = []

    def aggiungi_commento(self, commento):
        self.commenti.append(commento)


class Playlist:
    def __init__(self, nome: str, creatore: str):
        self.nome = nome
        self.creatore = creatore
        self.video: List[Video] = []

    def aggiungi_video(self, video):
        self.video.append(video)


class Abbonamento:
    def __init__(self, tipo: str, prezzo: float, data_inizio: date, data_fine: date, utente: Utente):
        self.tipo = tipo
        self.prezzo = prezzo
        self.data_inizio = data_inizio
        self.data_fine = data_fine
        self.utente = utente


class Commento:
    def __init__(self, autore: Utente, testo: str, data_pubblicazione: date, video: Video):
        self.autore = autore
        self.testo = testo
        self.data_pubblicazione = data_pubblicazione
        self.video = video


class Canale:
    def __init__(self, nome: str, tipo: str, proprietario: Utente):
        self.nome = nome
        self.tipo = tipo
        self.proprietario = proprietario
        self.videos: List[Video] = []

    def aggiungi_video(self, video: Video):
        self.videos.append(video)


class Piattaforma:
    def __init__(self, nome: str):
        self.nome = nome
        self.utenti: List[Utente] = []
        self.videos: List[Video] = []
        self.playlists: List[Playlist] = []
        self.abbonamenti: List[Abbonamento] = []
        self.commenti: List[Commento] = []
        self.canali: List[Canale] = []

    def aggiungi_utente(self, utente: Utente):
        self.utenti.append(utente)

    def aggiungi_video(self, video: Video):
        self.videos.append(video)

    def aggiungi_playlist(self, playlist: Playlist):
        self.playlists.append(playlist)

    def aggiungi_abbonamento(self, abbonamento: Abbonamento):
        self.abbonamenti.append(abbonamento)

    def aggiungi_commento(self, commento: Commento):
        self.commenti.append(commento)

    def aggiungi_canale(self, canale: Canale):
        self.canali.append(canale)


