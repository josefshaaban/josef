# min_max_input.py
print("Syötä numeroita yksi kerrallaan. Jätä tyhjä merkki lopetusmerkiksi.")
min_val = None
max_val = None

while True:
    s = input("Anna luku (tyhjä lopettaa): ")
    if s == "":
        break
    try:
        num = float(s)
    except ValueError:
        print("Virheellinen luku, yritä uudelleen.")
        continue

    if min_val is None or num < min_val:
        min_val = num
    if max_val is None or num > max_val:
        max_val = num

if min_val is None:
    print("Ei annettu yhtään lukua.")
else:
    print(f"Pienin: {min_val}")
    print(f"Suurin: {max_val}")
