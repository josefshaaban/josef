# arvo_pi.py
import random

def arvioi_pi(n):
    n = int(n)
    sisalla = 0
    i = 0
    while i < n:
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x*x + y*y < 1.0:
            sisalla += 1
        i += 1
    return 4 * sisalla / n

s = input("Montako pistettä arvotaan (esim. 1000000): ")
try:
    N = int(s)
    if N <= 0:
        print("Pisteiden määrän pitää olla positiivinen kokonaisluku.")
    else:
        pi_arvio = arvioi_pi(N)
        print(f"Piin likiarvo (N={N}): {pi_arvio}")
except ValueError:
    print("Virheellinen syöte, anna kokonaisluku.")
