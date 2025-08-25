# arpakuutiot.py
import random

n = int(input("Kuinka monta arpakuutiota heitetään? "))
summa = 0

for i in range(n):
    silmaluku = random.randint(1, 6)
    summa += silmaluku

print(f"Silmälukujen summa: {summa}")
