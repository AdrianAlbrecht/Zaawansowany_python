def generuj_fibonacci(dlugosc):
    fibonacci = [0, 1]

    while len(fibonacci) < dlugosc:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

    return fibonacci