class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin

    def kerros_ylös(self):
        if self.kerros < self.ylin:
            self.kerros += 1

    def kerros_alas(self):
        if self.kerros > self.alin:
            self.kerros -= 1

    def siirry_kerrokseen(self, kohde):
        while self.kerros < kohde: self.kerros_ylös()
        while self.kerros > kohde: self.kerros_alas()

class Talo:
    def __init__(self, alin, ylin, hissien_lkm):
        self.hissit = [Hissi(alin, ylin) for _ in range(hissien_lkm)]

    def aja_hissiä(self, num, kohde):
        self.hissit[num].siirry_kerrokseen(kohde)

    def palohälytys(self):
        for h in self.hissit:
            h.siirry_kerrokseen(h.alin)

# Käyttö
talo = Talo(1, 10, 2)
talo.aja_hissiä(0, 7)
talo.palohälytys()
