from Polynomial import Polynomial as pl
from copy import deepcopy as dc


class Fractional:
    __slots__ = ['__mianownik', '__licznik']

    def __init__(self, licznik, mianownik):
        self.__mianownik = dc(mianownik)
        self.__licznik = dc(licznik)

    def add(self, other):
        if type(other) == Fractional:
            if self.__mianownik == other.__mianownik:
                self.__licznik += other.__licznik
            else:
                temp_dod_licznik = other.__licznik * self.__mianownik
                temp_self_licznik = self.__licznik * other.__mianownik
                self.__licznik = temp_self_licznik + temp_dod_licznik
                self.__mianownik = self.__mianownik * other.__mianownik
        else:
            self.__licznik += other * self.__mianownik
        return self

    def __add__(self, other):
        return self.add(other)

    def __iadd__(self, other):
        return self.add(other)

    def sub(self, other):
        if type(other) == Fractional:
            if self.__mianownik == other.__mianownik:
                self.__licznik -= other.__licznik
            else:
                temp_dod_licznik = other.__licznik * self.__mianownik
                temp_self_licznik = self.__licznik * other.__mianownik
                self.__licznik = temp_self_licznik - temp_dod_licznik
                self.__mianownik = self.__mianownik * other.__mianownik
        else:
            self.__licznik -= other * self.__mianownik
        return self

    def __sub__(self, other):
        return self.sub(other)

    def __isub__(self, other):
        return self.sub(other)

    def mul(self, other):
        if type(other) == Fractional:
            self.__mianownik *= other.__mianownik
            self.__licznik *= other.__licznik
        else:
            self.__licznik *= other
        return self

    def __mul__(self, other):
        return self.mul(other)

    def __imul__(self, other):
        return self.mul(other)

    def __str__(self):
        string = str(self.__licznik) + "/" + str(self.__mianownik)
        return string


if __name__ == "__main__":
    w1 = pl(1, 2)
    w2 = pl(2, 1)
    w3 = pl(2, 3)
    print(w1, w2, w3)
    x = Fractional(w1, w2)
    y = Fractional(w3, w2)
    print(x)
    print(y)
    x *= y
    print(x)
    print(y)
    print(w1, w2, w3)
