#Esercizio 27 

import datetime

class Volo:
    def __init__(self,numero_volo,destinzaione,data_ora_partenza,max_passeggeri):
        self._numero_volo = numero_volo
        self._destinazione = destinzaione
        self._data_ora_partenza = data_ora_partenza
        self._max_passeggeri = max_passeggeri


    @property
    def numero_volo(self):
        return self._numero_volo
    
    numero_volo.setter
    def numero_volo(self,value):
        self._numero_volo = value

    @property
    def destinazione(self):
        return self._destinazione
    
    destinazione.setter
    def destinazione(self,value):
        self._destinazione = value

    @property
    def data_ora_partenza(self):
        return self._data_ora_partenza
    
    data_ora_partenza.setter
    def data_ora_partenza(self,value):
        self._data_ora_partenza = value

    @property
    def max_passeggeri(self):
        return self._max_passeggeri
    
    max_passeggeri.setter
    def max_passeggeri(self,value):
        self._max_passeggeri = value

    class Prenotazione:
        def __init__(self,nome_passeggero,tipo_classe, volo):
            self._nome_passeggero = nome_passeggero
            self._tipo_classe = tipo_classe
            self._volo = volo


        @property
        def nome_passeggero(self):
            return self._nome_passeggero
        
        nome_passeggero.setter
        def nome_passeggero(self,value):
            self._nome_passeggero = value

        @property
        def tipo_classe(self):
            return self._tipo_classe
        
        tipo_classe.setter
        def tipo_classe(self,value):
            self._tipo_classe = value

        @property
        def volo(self):
            return self._volo
        
        volo.setter
        def volo(self,value):
            self._volo = value

class Sistemaprenotazioni:
    def __init__(self):
        self._lista_prenotazioni= []
        self._lista_voli = []

    def aggiungi_prenotazione(self,prenotazione):
        self._lista_prenotazioni.append(prenotazione)

    def aggiungi_volo(self,volo):
        self._lista_voli.append(volo)

    def visualizza_prenotazioni(self):
        for prenotazione in self._lista_prenotazioni:
            print(prenotazione.nome_passeggero,prenotazione.tipo_classe,prenotazione.volo)

    def visualizza_voli(self):
        for volo in self._lista_voli:
            print(volo.numero_volo,volo.destinazione,volo.data_ora_partenza,volo.max_passeggeri)
