import os

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        
def save_number_to_file(number, folder_path):
    if number % 2 == 0:
        file_path = os.path.join(folder_path, 'even.txt')
    else:
        file_path = os.path.join(folder_path, 'odd.txt')

    with open(file_path, 'a') as file:
        file.write(str(number) + '\n')

        
folder_name = 'number_files'
create_directory('Lab_07/'+folder_name)

while True:
    try:
        user_input = int(input("Podaj liczbę naturalną (0 kończy program): "))
        if user_input < 0:
            raise ValueError("To nie jest liczba naturalna. Spróbuj ponownie.")
    except ValueError:
        print("To nie jest liczba naturalna. Spróbuj ponownie.")
        continue

    if user_input == 0:
        print("Koniec programu.")
        break

    save_number_to_file(user_input, 'Lab_07/'+folder_name)