temperatury_celsjusza = [20, 25, 30, 35, 40]

temperatury_fahrenheit = list(map(lambda c: c * 9/5 + 32, temperatury_celsjusza))

print("Temperatury w stopniach Celsjusza:", temperatury_celsjusza)
print("Temperatury w stopniach Fahrenheita:", temperatury_fahrenheit)
