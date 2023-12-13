from fibbo import generuj_fibonacci

print(f"Lista nieparzystych liczb Fibonacciego:", list(filter(lambda x: x % 2 == 0, generuj_fibonacci(50))))