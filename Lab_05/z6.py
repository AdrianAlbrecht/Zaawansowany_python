temperatury_fahrenheit = [68.0, 77.0, 86.0, 95.0, 104.0]

temperatury_celsjusza = list(map(lambda c: (c - 32) / (9/5) , temperatury_fahrenheit))

print("Temperatury w stopniach Fahrenheita:", temperatury_fahrenheit)
print("Temperatury w stopniach Celsjusza:", temperatury_celsjusza)
