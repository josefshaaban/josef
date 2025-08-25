# alkuluku.py
n = int(input("Anna kokonaisluku: "))

if n < 2:
    print(f"{n} ei ole alkuluku.")
else:
    on_alku = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            on_alku = False
            break

    if on_alku:
        print(f"{n} on alkuluku.")
    else:
        print(f"{n} ei ole alkuluku.")
