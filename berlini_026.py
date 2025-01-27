# Esercizio 26

class Veicolo:
    def _init_(self, marca, modello, tipo_carburante):
        self.marca = marca
        self.modello = modello
        self.tipo_carburante = tipo_carburante

    @property
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self, value):
        self._marca = value

    @property
    def modello(self):
        return self._modello
    
    @modello.setter
    def modello(self, value):
        self._modello = value

    @property
    def tipo_carburante(self):
        return self._tipo_carburante
    
    @tipo_carburante.setter
    def tipo_carburante(self, value):
        self._tipo_carburante = value

class Auto(Veicolo):
    def _init_(self, marca, modello, tipo_carburante):
        super()._init_(marca, modello, tipo_carburante)
        

class Camion(Veicolo):
    def _init_(self, marca, modello, tipo_carburante):
        super()._init_(marca, modello, tipo_carburante)


class Flotta:
    def _init_(self):
        self.lista_veicoli = []

    def aggiungi_veicolo(self, veicolo):
        self.lista_veicoli.append(veicolo)

    def stampa_veicoli(self):
        for veicolo in self.lista_veicoli:
            print(veicolo.marca, veicolo.modello, veicolo.tipo_carburante)


if __name__ == "__main__":
    flotta = Flotta()
    auto1 = Auto("Fiat", "Panda", "Benzina")
    auto2 = Auto("Fiat", "500", "Benzina")
    camion1 = Camion("Iveco", "Daily", "Diesel")
    camion2 = Camion("Mercedes", "Actros", "Diesel")
    flotta.aggiungi_veicolo(auto1)
    flotta.aggiungi_veicolo(auto2)
    flotta.aggiungi_veicolo(camion1)
    flotta.aggiungi_veicolo(camion2)
    flotta.stampa_veicoli()
