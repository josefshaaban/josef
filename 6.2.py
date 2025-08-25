import random

def heita_noppaa(tahkot):
    return random.randint(1, tahkot)

# pääohjelma
tahkojen_maara = int(input("Anna nopan tahkojen määrä: "))

while True:
    silmaluku = heita_noppaa(tahkojen_maara)
    print(f"Heitto: {silmaluku}")
    if silmaluku == tahkojen_maara:  # jatketaan kunnes maksimisilmäluku tulee
        break
