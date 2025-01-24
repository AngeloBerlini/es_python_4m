#Esercizio 25
import datetime

class Prenotazione:
    def __init__(self, nome_cliente, data, numero_persone, stato):
        self.__nome_cliente = nome_cliente
        self.__data = data
        self.__numero_persone = numero_persone
        self.__stato = stato

    
    @property
    def nome_cliente(self):
        return self.__nome_cliente
    
    @nome_cliente.setter
    def nome_cliente(self, nome_cliente):
        self.__nome_cliente = nome_cliente

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def numero_persone(self):
        return self.__numero_persone
    
    @numero_persone.setter
    def numero_persone(self, numero_persone):
        self.__numero_persone = numero_persone

    @property
    def stato(self):
        return self.__stato
    
    @stato.setter
    def stato(self, stato):
        self.__stato = stato


class Ristorante:
    def __init__(self):
        self.prenotazioni = []

    def aggiungi_prenotazione(self, prenotazione):
        self.prenotazioni.append(prenotazione)

    def cerca_prenotazione(self, nome_cliente):
        for prenotazione in self.prenotazioni:
            if prenotazione.nome_cliente == nome_cliente:
                return prenotazione
        return None
    
    def visualizza_prenotazioni(self):
        for prenotazione in self.prenotazioni:
            print(prenotazione)

    def numero_prenotazioni(self):
        return len(self.prenotazioni)
    
    @property
    def prenotazioni(self):
        return self.__prenotazioni
    
    @prenotazioni.setter
    def prenotazioni(self, prenotazioni):
        self.__prenotazioni = prenotazioni



if __name__ == "__main__":
    ristorante = Ristorante()
    prenotazione1 = Prenotazione("Mario Rossi", datetime.datetime(2021, 3, 15), 2, "Confermata")
    prenotazione2 = Prenotazione("Giuseppe Verdi", datetime.datetime(2021, 3, 16), 4, "Confermata")
    prenotazione3 = Prenotazione("Luca Bianchi", datetime.datetime(2021, 3, 17), 3, "Confermata")
    ristorante.aggiungi_prenotazione(prenotazione1)
    ristorante.aggiungi_prenotazione(prenotazione2)
    ristorante.aggiungi_prenotazione(prenotazione3)
    ristorante.visualizza_prenotazioni()
    print(ristorante.numero_prenotazioni())
    print(ristorante.cerca_prenotazione("Mario Rossi"))
    print(ristorante.cerca_prenotazione("Giuseppe Verdi"))
    print(ristorante.cerca_prenotazione("Luca Bianchi"))
    print(ristorante.cerca_prenotazione("Andrea Neri"))