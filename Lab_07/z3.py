numbers = [x for x in range(1,101)]

with open('Lab_07/99_numbers.txt', 'r') as file:
    for number in file.readlines():
        numbers.remove(int(number))
        
print(f'Brakująca liczba to: {numbers[0]}')