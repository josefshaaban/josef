# Monikko, jossa vuodenajat
vuodenajat = ("talvi", "talvi", "talvi",  # joulukuu, tammikuu, helmikuu
              "kevät", "kevät", "kevät",  # maaliskuu, huhtikuu, toukokuu
              "kesä", "kesä", "kesä",    # kesäkuu, heinäkuu, elokuu
              "syksy", "syksy", "syksy")  # syyskuu, lokakuu, marraskuu

kuukausi = int(input("Anna kuukauden numero (1-12): "))

# Koska joulukuu on ensimmäinen talvikuukausi, indeksin lasku:
indeksi = (kuukausi + 8) % 12
print("Vuodenaika:", vuodenajat[indeksi])
