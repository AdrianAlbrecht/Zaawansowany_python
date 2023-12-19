import os
import sys

def main():
    for file_path in sys.argv[1:]:
        print('Testowanie pliku', file_path)
        print('Plik istnieje:', os.access(file_path, os.F_OK))
        print('Plik mozna odczytac:', os.access(file_path, os.R_OK))
        print('Plik jest zapisywalny:', os.access(file_path, os.W_OK))
        print('Plik jest wykonywalny:', os.access(file_path, os.X_OK))
    
    
if __name__ == "__main__":
    main()