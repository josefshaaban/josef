import random

def heita_noppaa():
    return random.randint(1, 6)

# pääohjelma
while True:
    silmaluku = heita_noppaa()
    print(f"Heitto: {silmaluku}")
    if silmaluku == 6:
        break
