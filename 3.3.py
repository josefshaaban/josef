sukupuoli = input("Anna biologinen sukupuolesi (nainen/mies): ").lower()
hb = int(input("Anna hemoglobiiniarvosi (g/l): "))

if sukupuoli == "nainen":
    if hb < 117:
        print("Hemoglobiiniarvo on alhainen.")
    elif hb <= 175:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on korkea.")
elif sukupuoli == "mies":
    if hb < 134:
        print("Hemoglobiiniarvo on alhainen.")
    elif hb <= 195:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on korkea.")
else:
    print("Virheellinen sukupuoli.")