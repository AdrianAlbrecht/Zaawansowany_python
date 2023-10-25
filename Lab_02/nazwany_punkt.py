from punkt import Punkt

class NazwanyPunkt(Punkt):
    __slots__ = ('_x', '_y', '_name')

    def __init__(self, x, y, name):
        super().__init__(x, y)
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name

    def __repr__(self):
        return f'NazwanyPunkt({self._x}, {self._y}, "{self._name}")'

    def __str__(self):
        return f'({self._x}, {self._y}, "{self._name}")'
