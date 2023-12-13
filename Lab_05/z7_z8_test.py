from fibbo import generuj_fibonacci

fibbo = list(filter(lambda x: x % 2 != 0, generuj_fibonacci(50))) + list(filter(lambda x: x % 2 == 0, generuj_fibonacci(50)))
fibbo.sort()

print(fibbo == generuj_fibonacci(50))