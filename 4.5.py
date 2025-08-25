# kirjautuminen.py
oikea_tunnus = "python"
oikea_salasana = "rules"
yritykset = 0
max_yritykset = 5

while yritykset < max_yritykset:
    tunnus = input("Käyttäjätunnus: ")
    salasana = input("Salasana: ")
    yritykset += 1

    if tunnus == oikea_tunnus and salasana == oikea_salasana:
        print("Tervetuloa")
        break
    else:
        if yritykset < max_yritykset:
            print(f"Väärä tunnus tai salasana. Yrityksiä jäljellä: {max_yritykset - yritykset}")
        else:
            print("Pääsy evätty")
