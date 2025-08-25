# tuuma_cm.py
print("Anna tuumamäärä (negatiivinen lopettaa). 1 tuuma = 2.54 cm")
while True:
    s = input("Tuumat: ")
    try:
        tuumat = float(s)
    except ValueError:
        print("Virheellinen syöte, yritä uudelleen.")
        continue

    if tuumat < 0:
        print("Lopetetaan.")
        break

    cm = tuumat * 2.54
    print(f"{tuumat} tuumaa = {cm} cm")
