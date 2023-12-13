from functools import reduce

lista_liczb = [5, 12, 8, 24, 3, 17, 10]

najwieksza_liczba_max = max(lista_liczb)

najwieksza_liczba_reduce = reduce(lambda x, y: x if x > y else y, lista_liczb)

print("Lista liczb:", lista_liczb)
print("Największa liczba:", najwieksza_liczba_max)
print("Czy obie funkcje działają tak samo:", najwieksza_liczba_max == najwieksza_liczba_reduce)