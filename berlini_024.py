#Esercizio 24

class Film:
    def __init__(self, titolo, regista, anno_uscita, genere, valutazione):
        self.__titolo = titolo
        self.__regista = regista
        self.__anno_uscita = anno_uscita
        self.__genere = genere
        self.__valutazione = valutazione

    def __str__(self):
        return f"{self.__titolo} ({self.__anno_uscita}) di {self.__regista}, {self.__genere} "

    @property
    def valutazione(self):
        return self.__valutazione
    
    @valutazione.setter
    def valutazione(self, valutazione):
        if 0 <= valutazione <= 10:
            self.__valutazione = valutazione
        else:
            raise ValueError("La valutazione deve essere compresa tra 0 e 10")
        
    @property
    def anno(self):
        return self.__anno_uscita
    
    @anno.setter
    def anno(self, anno):
        if anno > 0:
            self.__anno_uscita = anno
        else:
            raise ValueError("L'anno deve essere un numero positivo")
        
    @property
    def genere(self):
        return self.__genere
    
    @genere.setter
    def genere(self, genere):
        self.__genere = genere
        
    @property
    def regista(self):
        return self.__regista
    
    @regista.setter
    def regista(self, regista):
        self.__regista = regista


class Libreria:
    def __init__(self):
        self.film = []

    def aggiungi_film(self, film):
        self.film.append(film)

    def cerca_film(self, titolo):
        for film in self.film:
            if film.titolo == titolo:
                return film
            
    def visualizza_film(self):
        for film in self.film:
            print(film)

    def valutazione_media_film(self):
        somma = 0
        for film in self.film:
            somma += film.valutazione
        return somma / len(self.film)
    

    @property
    def film(self):
        return self.__film
    

    @film.setter
    def film(self, film):
        self.__film = film


if __name__ == "__main__":
    libreria = Libreria()
    film1 = Film("Il Signore degli Anelli", "Peter Jackson", 2001, "Fantasy", 9)
    film2 = Film("Harry Potter", "Chris Columbus", 2001, "Fantasy", 8)
    film3 = Film("Pulp Fiction", "Quentin Tarantino", 1994, "Crime", 10)
    libreria.aggiungi_film(film1)
    libreria.aggiungi_film(film2)
    libreria.aggiungi_film(film3)
    libreria.visualizza_film()
    print(f"Valutazione media: {libreria.valutazione_media_film()}")
    
