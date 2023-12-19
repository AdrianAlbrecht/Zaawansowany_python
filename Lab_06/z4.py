import os

def main():
    print()
    print("Głowa i ogon bieżącego katalogu:")
    print(os.path.split(os.getcwd()))
    print()
    
    print("Korzeń oraz rozszerzenie ścieżki ../app-2022-w10.tar.xz")
    print(os.path.splitext("app-2022-w10.tar.xz"))
    print()
    
    print("Ścieżka bezwględna dla katalogu bieżącego:")
    print(os.path.abspath('.'))
    
    print("Ścieżka bezwględna dla katalogu nadrzędnego:")
    print(os.path.abspath('..'))
    print()
 
    
if __name__ == '__main__':
    main()