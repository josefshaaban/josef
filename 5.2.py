# viisi_suurinta.py
luvut = []

print("Syötä lukuja. Tyhjä syöte lopettaa.")
while True:
    s = input("Anna luku: ")
    if s == "":
        break
    try:
        num = float(s)
        luvut.append(num)
    except ValueError:
        print("Ei ollut kelvollinen luku, yritä uudelleen.")

# järjestetään suurimmasta pienimpään
luvut.sort(reverse=True)

print("Viisi suurinta lukua:")
for luku in luvut[:5]:
    print(luku)
