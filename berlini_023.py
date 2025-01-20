#Esercizio 23

from datetime import date

class Utente:
    def __init__(self, nome_utente, email, password, profilo):
        self._nome_utente = nome_utente
        self._email = email
        self._password = password
        self._profilo = profilo
        self._album = []
        self._foto = []
        self._commenti = []

    
    def get_nome_utente(self):
        return self._nome_utente

    def get_email(self):
        return self._email

    def get_password(self):
        return self._password

    def get_profilo(self):
        return self._profilo

    def get_album(self):
        return self._album

    def get_foto(self):
        return self._foto

    def get_commenti(self):
        return self._commenti

    
    def set_nome_utente(self, nome_utente):
        self._nome_utente = nome_utente

    def set_email(self, email):
        self._email = email

    def set_password(self, password):
        self._password = password

    def set_profilo(self, profilo):
        self._profilo = profilo

    def set_album(self, album):
        self._album = album

    def set_foto(self, foto):
        self._foto = foto

    def set_commenti(self, commenti):
        self._commenti = commenti


class Profilo:
    def __init__(self, immagine, biografia):
        self._immagine = immagine
        self._biografia = biografia

    
    def get_immagine(self):
        return self._immagine

    def get_biografia(self):
        return self._biografia

    
    def set_immagine(self, immagine):
        self._immagine = immagine

    def set_biografia(self, biografia):
        self._biografia = biografia


class Foto:
    def __init__(self, id, titolo, descrizione, data_caricamento, utente, album):
        self._id = id
        self._titolo = titolo
        self._descrizione = descrizione
        self._data_caricamento = data_caricamento
        self._utente = utente
        self._commenti = []
        self._album = album

    
    def get_id(self):
        return self._id

    def get_titolo(self):
        return self._titolo

    def get_descrizione(self):
        return self._descrizione

    def get_data_caricamento(self):
        return self._data_caricamento

    def get_utente(self):
        return self._utente

    def get_commenti(self):
        return self._commenti

    def get_album(self):
        return self._album

    
    def set_id(self, id):
        self._id = id

    def set_titolo(self, titolo):
        self._titolo = titolo

    def set_descrizione(self, descrizione):
        self._descrizione = descrizione

    def set_data_caricamento(self, data_caricamento):
        self._data_caricamento = data_caricamento

    def set_utente(self, utente):
        self._utente = utente

    def set_commenti(self, commenti):
        self._commenti = commenti

    def set_album(self, album):
        self._album = album


class Album:
    def __init__(self, titolo, descrizione, utente):
        self._titolo = titolo
        self._descrizione = descrizione
        self._utente = utente
        self._foto = []

    
    def get_titolo(self):
        return self._titolo

    def get_descrizione(self):
        return self._descrizione

    def get_utente(self):
        return self._utente

    def get_foto(self):
        return self._foto

    
    def set_titolo(self, titolo):
        self._titolo = titolo

    def set_descrizione(self, descrizione):
        self._descrizione = descrizione

    def set_utente(self, utente):
        self._utente = utente

    def set_foto(self, foto):
        self._foto = foto


class Commento:
    def __init__(self, descrizione, foto, utente):
        self._descrizione = descrizione
        self._foto = foto
        self._utente = utente

    
    def get_descrizione(self):
        return self._descrizione

    def get_foto(self):
        return self._foto

    def get_utente(self):
        return self._utente

    
    def set_descrizione(self, descrizione):
        self._descrizione = descrizione

    def set_foto(self, foto):
        self._foto = foto

    def set_utente(self, utente):
        self._utente = utente


# Programma di test
profilo = Profilo("immagine", "biografia")
utente = Utente("nome_utente", "email", "password", profilo)
foto = Foto("id", "titolo", "descrizione", date.today(), utente, [])
album = Album("titolo", "descrizione", utente)
commento = Commento("descrizione", foto, utente)
print("Utente: " + utente.get_nome_utente())
print("Email: " + utente.get_email())
print("Password: " + utente.get_password())
print("Profilo: " + utente.get_profilo().get_immagine() + " " + utente.get_profilo().get_biografia())
print("Foto: " + foto.get_id() + " " + foto.get_titolo() + " " + foto.get_descrizione() + " " + str(foto.get_data_caricamento()))
print("Album: " + album.get_titolo() + " " + album.get_descrizione())
print("Commento: " + commento.get_descrizione())
