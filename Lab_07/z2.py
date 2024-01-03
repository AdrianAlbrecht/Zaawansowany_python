import os

def process_file(file_path):
    try:
        with open(file_path, 'r') as file:
            numbers = [float(line.strip()) for line in file.readlines()]
            file_sum = sum(numbers)
            file_average = file_sum / len(numbers) if len(numbers) > 0 else 0

            print(f"File: {file_path}")
            print(f"Sum: {file_sum}")
            print(f"Average: {file_average}\n")

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")


folder_name = 'number_files'
folder_path = 'Lab_07/' + folder_name        
file_paths = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))]

for file_path in file_paths:
    process_file(file_path)