class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        print(f"Kirja: {self.nimi}, {self.kirjoittaja}, {self.sivumaara} sivua")

class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print(f"Lehti: {self.nimi}, päätoimittaja {self.paatoimittaja}")

class Auto:
    def __init__(self, rekisteri, huippunopeus):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def aseta_nopeus(self, nopeus):
        self.nopeus = min(nopeus, self.huippunopeus)

    def kulje(self, tunnit):
        self.matka += self.nopeus * tunnit

class Sahkoauto(Auto):
    def __init__(self, rekisteri, huippunopeus, akku):
        super().__init__(rekisteri, huippunopeus)
        self.akku = akku

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteri, huippunopeus, tankki):
        super().__init__(rekisteri, huippunopeus)
        self.tankki = tankki

# Pääohjelma
a = Lehti("Aku Ankka", "Aki Hyyppä")
k = Kirja("Hytti n:o 6", "Rosa Liksom", 200)
a.tulosta_tiedot()
k.tulosta_tiedot()

s = Sahkoauto("ABC-15", 180, 52.5)
p = Polttomoottoriauto("ACD-123", 165, 32.3)
s.aseta_nopeus(120); p.aseta_nopeus(95)
s.kulje(3); p.kulje(3)
print(f"Sähköauto {s.rekisteri}: {s.matka} km")
print(f"Polttomoottoriauto {p.rekisteri}: {p.matka} km")
