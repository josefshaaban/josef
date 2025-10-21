import random

class Auto:
    def __init__(self, rek, huippu):
        self.rek, self.huippu = rek, huippu
        self.nopeus = self.matka = 0

    def kiihdyta(self, muutos):
        self.nopeus = max(0, min(self.huippu, self.nopeus + muutos))

    def kulje(self):
        self.matka += self.nopeus


autot = [Auto(f"ABC-{i}", random.randint(100, 200)) for i in range(1, 11)]

while True:
    for a in autot:
        a.kiihdyta(random.randint(-10, 15))
        a.kulje()
        if a.matka >= 10000:
            print("Kilpailu ohi!\n")
            for x in autot:
                print(x.rek, x.huippu, x.nopeus, int(x.matka))
            exit()
