#ESERCIZIO 1

class Persona:
    def __init__(self, nome : str, eta : int, citta : str) -> None:
        self.nome = nome
        self.eta = eta
        self.citta = citta
    
    def saluta(self) -> None:
        print (f"Ciao, mi chiamo {self.nome}")

    def descrizione(self) -> None:
        print (f"Ho {self.eta} anni e vivo a {self.citta}")

persona = Persona("Mario", 30, "Roma")
persona.saluta()
persona.descrizione()
