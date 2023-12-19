import os
import sys
import time

def main():
    for file_path in sys.argv[1:]:
        stat_info = os.stat(file_path)
        
        print('os.stat({0}):'.format(file_path))
        print('\tRozmiar:', stat_info.st_size)
        print('\tUprawnienia:', oct(stat_info.st_mode))
        print('\tWlasciciel: uzytkownik o numerze uid =', stat_info.st_uid)
        print('\tUrzadzenie:', stat_info.st_dev)
        print('\tOstatnio zmodyfikowany:', time.ctime(stat_info.st_mtime))
    
    
if __name__ == "__main__":
    main()