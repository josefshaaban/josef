def gallonat_litroiksi(gallonat):
    return gallonat * 3.785

# pääohjelma
while True:
    s = input("Anna määrä nestegallonoina (negatiivinen lopettaa): ")
    try:
        gall = float(s)
    except ValueError:
        print("Virheellinen syöte.")
        continue

    if gall < 0:
        print("Lopetetaan.")
        break

    litrat = gallonat_litroiksi(gall)
    print(f"{gall} gallonaa = {litrat:.2f} litraa")
