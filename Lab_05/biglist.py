import sys

if len(sys.argv) != 2:
    print("Uzycie: python biglist.py n")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("Podana wartosc n musi byc liczba calkowita.")
    sys.exit(1)

if n < 1:
    print("Podana liczba n musi byc wieksza niz 0.")
    sys.exit(1)

lista_liczb = list(range(1, n + 1))

suma = sum(lista_liczb)

print('Suma liczb od 1 do '+str(n)+': '+str(suma))