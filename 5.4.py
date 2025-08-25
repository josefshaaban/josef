# kaupungit.py
kaupungit = []

for i in range(5):
    nimi = input(f"Anna {i+1}. kaupungin nimi: ")
    kaupungit.append(nimi)

print("Kaupungit syöttöjärjestyksessä:")
for nimi in kaupungit:
    print(nimi)
