import random

class Auto:
    def __init__(self, nimi):
        self.nimi = nimi
        self.nopeus = 0
        self.matka = 0
    def kulje(self):
        self.matka += self.nopeus

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for a in self.autot:
            a.nopeus = max(0, a.nopeus + random.randint(-10,10))
            a.kulje()

    def tulosta_tilanne(self):
        for a in self.autot:
            print(f"{a.nimi}: {a.matka} km, {a.nopeus} km/h")

    def kilpailu_ohi(self):
        return any(a.matka >= self.pituus for a in self.autot)

# Käyttö
autot = [Auto(f"Auto{i+1}") for i in range(3)]
kilpailu = Kilpailu("Mini-ralli", 100, autot)

tunti = 0
while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunti += 1
    if tunti % 5 == 0:
        kilpailu.tulosta_tilanne()

print("Kilpailu päättynyt!")
kilpailu.tulosta_tilanne()
