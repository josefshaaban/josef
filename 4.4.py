# arvauspeli.py
import random

numero = random.randint(1, 10)  # tietokone ei vaihda numeroa arvauskertojen välillä
print("Arvaa luku väliltä 1 - 10. Arvaa, kunnes saat oikein.")

while True:
    s = input("Arvaus: ")
    try:
        arvaus = int(s)
    except ValueError:
        print("Anna kokonaisluku 1..10.")
        continue

    if arvaus < numero:
        print("Liian pieni arvaus")
    elif arvaus > numero:
        print("Liian suuri arvaus")
    else:
        print("Oikein")
        break
