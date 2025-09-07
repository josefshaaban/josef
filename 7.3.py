lentoasemat = {}  # Sanakirja ICAO-koodille

while True:
    toiminto = input("\nValitse toiminto (uusi/haku/lopeta): ").lower()

    if toiminto == "uusi":
        icao = input("Anna lentoaseman ICAO-koodi: ").upper()
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi
        print("Lentoasema tallennettu.")

    elif toiminto == "haku":
        icao = input("Anna haettavan lentoaseman ICAO-koodi: ").upper()
        if icao in lentoasemat:
            print("Lentoaseman nimi:", lentoasemat[icao])
        else:
            print("Lentoasemaa ei löytynyt.")

    elif toiminto == "lopeta":
        print("Ohjelma lopetettu.")
        break

    else:
        print("Virheellinen valinta. Valitse 'uusi', 'haku' tai 'lopeta'.")
