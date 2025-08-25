import math

def yksikkohinta(halkaisija_cm, hinta_euro):
    sade_m = (halkaisija_cm / 2) / 100   # muutetaan metreiksi
    pinta_ala = math.pi * sade_m**2      # m²
    return hinta_euro / pinta_ala        # €/m²

# pääohjelma
halkaisija1 = float(input("Anna ensimmäisen pizzan halkaisija (cm): "))
hinta1 = float(input("Anna ensimmäisen pizzan hinta (€): "))

halkaisija2 = float(input("Anna toisen pizzan halkaisija (cm): "))
hinta2 = float(input("Anna toisen pizzan hinta (€): "))

hinta_m2_1 = yksikkohinta(halkaisija1, hinta1)
hinta_m2_2 = yksikkohinta(halkaisija2, hinta2)

print(f"Pizza 1 yksikköhinta: {hinta_m2_1:.2f} €/m²")
print(f"Pizza 2 yksikköhinta: {hinta_m2_2:.2f} €/m²")

if hinta_m2_1 < hinta_m2_2:
    print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
elif hinta_m2_1 > hinta_m2_2:
    print("Toinen pizza antaa paremman vastineen rahalle.")
else:
    print("Molemmat pizzat ovat yhtä edullisia.")
