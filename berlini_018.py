class Allenatore:
    def __init__(self, nome, cognome, specializzazione):
        self._nome = nome
        self._cognome = cognome
        self._specializzazione = specializzazione
        self.membri = []
        self.corsi = []  # 

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def cognome(self):
        return self._cognome

    @cognome.setter
    def cognome(self, cognome):
        self._cognome = cognome

    @property
    def specializzazione(self):
        return self._specializzazione

    @specializzazione.setter
    def specializzazione(self, specializzazione):
        self._specializzazione = specializzazione

    def allena_membro(self, membro):
        if membro not in self.membri:    
            self.membri.append(membro)
            membro.set_allenatore(self)

    def tieni_corso(self, corso):
        if corso not in self.corsi:    
            self.corsi.append(corso)
            corso.set_allenatore(self)

class Membro:
    def __init__(self, nome, cognome):
        self._nome = nome
        self._cognome = cognome
        self.corsi = []
        self.scheda_allenamento = None
        self.allenatore = None

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def cognome(self):
        return self._cognome

    @cognome.setter
    def cognome(self, cognome):
        self._cognome = cognome

    def iscrivi_corso(self, corso):
        if corso not in self.corsi:    
            self.corsi.append(corso)
            corso.set_membro(self)

    def set_scheda_allenamento(self, scheda_allenamento):
        self.scheda_allenamento = scheda_allenamento
        scheda_allenamento.membro = self

    def set_allenatore(self, allenatore):
        self.allenatore = allenatore
        if allenatore is not None:
            allenatore.allena_membro(self)  # Add the member to the coach's list

    def __str__(self):
        return f"{self.nome} {self.cognome}, Allenatore: {self.allenatore.nome if self.allenatore else 'N/A'}, Scheda Allenamento: {self.scheda_allenamento}"

class Corso:
    def __init__(self, nome, durata, allenatore):
        self.nome = nome
        self.durata = durata
        self.allenatore = allenatore
        self.iscritti = []  
        if allenatore is not None:
            allenatore.tieni_corso(self)  

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def durata(self):
        return self._durata

    @durata.setter
    def durata(self, durata):
        self._durata = durata

    def set_membro(self, membro):
        if membro not in self.iscritti:
            self.iscritti.append(membro)  
            membro.iscrivi_corso(self)

    def set_allenatore(self, allenatore):
        self.allenatore = allenatore

class SchedaAllenamento:
    def __init__(self, membro, lista_esercizi):
        self.membro = membro
        self.lista_esercizi = lista_esercizi

    def __str__(self):
        esercizi_str = "\n".join(self.lista_esercizi)
        return f"Scheda Allenamento di {self.membro.nome} {self.membro.cognome}:\n{esercizi_str}"


def main():
    # Creazione degli allenatori
    allenatore1 = Allenatore("Giovanni", "Rossi", "Fitness")
    allenatore2 = Allenatore("Luca", "Bianchi", "Yoga")

    # Creazione dei membri
    membro1 = Membro("Anna", "Verdi")
    membro2 = Membro("Marco", "Neri")

    # Assegnazione degli allenatori ai membri
    membro1.set_allenatore(allenatore1)
    membro2.set_allenatore(allenatore2)

    # Creazione dei corsi
    corso1 = Corso("Pilates", "3 mesi", allenatore1)
    corso2 = Corso("HIIT", "6 mesi", allenatore1)
    corso3 = Corso("Yoga Avanzato", "4 mesi", allenatore2)

    # Iscrizione dei membri ai corsi
    membro1.iscrivi_corso(corso1)
    membro1.iscrivi_corso(corso2)
    membro2.iscrivi_corso(corso3)

    # Creazione delle schede di allenamento
    scheda1 = SchedaAllenamento(membro1, ["Esercizio 1: Squat", "Esercizio 2: Push-up"])
    scheda2 = SchedaAllenamento(membro2, ["Esercizio 1: Plank", "Esercizio 2: Burpee"])

    # Assegnazione delle schede di allenamento ai membri
    membro1.set_scheda_allenamento(scheda1)
    membro2.set_scheda_allenamento(scheda2)

    # Stampa delle informazioni
    print(membro1)
    print(membro2)

if __name__ == "__main__":
    main()