class MiastaIterator:
    def __init__(self, miasta):
        self.miasta = miasta
        self.indeks = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.indeks < len(self.miasta):
            aktualne_miasto = self.miasta[self.indeks]
            self.indeks += 1
            return aktualne_miasto
        else:
            raise StopIteration

def wypisz_miasta(miasta):
    iterator_miasta = MiastaIterator(miasta)
    
    try:
        while True:
            aktualne_miasto = next(iterator_miasta)
            print(aktualne_miasto)
    except StopIteration:
        pass