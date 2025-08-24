pituus = int(input("Anna kuhan pituus (cm): "))
if pituus < 37:
    puuttuu = 37 - pituus
    print(f"Laske kuha takaisin järveen, puuttuu {puuttuu} cm alimmasta sallitusta pyyntimitasta.")
else:
    print("Kuha on sallitun mittainen.")