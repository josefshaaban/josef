def poista_parittomat(lista):
    return [x for x in lista if x % 2 == 0]

# pääohjelma
luvut = [1, 2, 3, 4, 5, 6, 7]
print("Alkuperäinen lista:", luvut)
print("Parilliset luvut:", poista_parittomat(luvut))
