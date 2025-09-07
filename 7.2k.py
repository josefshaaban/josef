nimet = set()  # Joukkotietorakenne

while True:
    nimi = input("Anna nimi (tyhjä lopettaa): ")
    if nimi == "":
        break
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        nimet.add(nimi)
        print("Uusi nimi")

print("\nSyötetyt nimet:")
for n in nimet:
    print(n)
