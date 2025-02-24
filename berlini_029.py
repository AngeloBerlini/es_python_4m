# Esercizio 29

class Parco:
    def __init__(self, nome):
        self.nome = nome
        self.ecosistemi = []
        self.zone = []
        self.sensori = []
        self.dispositivi = []

    def monitorare_parametri(self):
        parametri = {}
        for ecosistema in self.ecosistemi:
            parametri[ecosistema.nome] = ecosistema.monitorare_parametri()
        return parametri

    def gestire_dispositivi(self):
        for ecosistema in self.ecosistemi:
            ecosistema.gestire_dispositivi()

class Ecosistema:
    def __init__(self, nome):
        self.nome = nome
        self.zone = []

    def monitorare_parametri(self):
        parametri = {}
        for zona in self.zone:
            parametri[zona.nome] = zona.monitorare_parametri()
        return parametri

    def gestire_dispositivi(self):
        for zona in self.zone:
            zona.gestire_dispositivi()

        
class Zona:
    def __init__(self, nome, temperatura, umidita, qualita_aria):
        self.nome = nome
        self.temperatura = temperatura
        self.umidita = umidita
        self.qualita_aria = qualita_aria
        self.sensori = []
        self.dispositivi = []

    def monitorare_parametri(self):
        parametri = {
            "temperatura": self.temperatura,
            "umidita": self.umidita,
            "qualita_aria": self.qualita_aria
        }
        return parametri

    def gestire_dispositivi(self):
        for dispositivo in self.dispositivi:
            if dispositivo.tipo == "ventilatore" and self.temperatura > 30:
                dispositivo.attiva()
            elif dispositivo.tipo == "irrigatore" and self.umidita < 60:
                dispositivo.attiva()
            elif dispositivo.tipo == "ventilatore" and self.qualita_aria < 40:
                dispositivo.attiva()
            else:
                dispositivo.disattiva()


class Sensore:
    def __init__(self, nome, zona, valore):
        self.nome = nome
        self.zona = zona
        self.valore = valore

    def rileva(self):
        return self.valore


class Dispositivo:
    def __init__(self, tipo, zona, stato):
        self.tipo = tipo
        self.zona = zona
        self.stato = stato

    def attiva(self):
        self.stato = True

    def disattiva(self):
        self.stato = False

    def verifica_stato(self):
        return self.stato
    
# Esempio di implementazione
parco = Parco("Parco Naturale")

# Creazione di ecosistemi
foresta = Ecosistema("Foresta")
zona1 = Zona("Zona 1", 32, 55, 35)
zona2 = Zona("Zona 2", 28, 65, 45)

# Aggiunta di sensori e dispositivi alle zone
sensore_temp1 = Sensore("Temperatura", zona1, 32)
sensore_umid1 = Sensore("Umidità", zona1, 55)
sensore_qualita1 = Sensore("Qualità Aria", zona1, 35)
ventilatore1 = Dispositivo("ventilatore", zona1)
irrigatore1 = Dispositivo("irrigatore", zona1)

zona1.sensori.extend([sensore_temp1, sensore_umid1, sensore_qualita1])
zona1.dispositivi.extend([ventilatore1, irrigatore1])

# Aggiunta delle zone all'ecosistema
foresta.zone.extend([zona1, zona2])

# Aggiunta dell'ecosistema al parco
parco.ecosistemi.append(foresta)

# Monitoraggio dei parametri e gestione dei dispositivi
print(parco.monitorare_parametri())
parco.gestire_dispositivi()

# Verifica dello stato dei dispositivi
print(f"Ventilatore Zona 1 attivo: {ventilatore1.verifica_stato()}")
print(f"Irrigatore Zona 1 attivo: {irrigatore1.verifica_stato()}")