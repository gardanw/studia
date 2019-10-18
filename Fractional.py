from Polynomial import Polynomial as pl

class Fractional :
    __slots__ = ['__mianownik', '__licznik']
    def __init__(self, licznik, mianownik):
        self.__mianownik = mianownik
        self.__licznik = licznik
    
    def add(self, other):
        if type(other) == Fractional:
            if self.__mianownik == other.__mianownik:
                self.__licznik += other,__licznik
            else:
                temp_dod_licznik = other.__licznik * self.__mianownik
                temp_self_licznik = other.__mianownik * self.__licznik
                self.__licznik = temp_self_licznik + temp_dod_licznik
                self.__mianownik = self.__mianownik * other.__mianownik
        else:
            self.__licznik += other * self.__mianownik
        return self

    def __add__(self, other):
        if type(other) == Fractional:
            if self.__mianownik == other.__mianownik:
                self.__licznik += other,__licznik
            else:
                temp_dod_licznik = other.__licznik * self.__mianownik
                temp_self_licznik = other.__mianownik * self.__licznik
                self.__licznik = temp_self_licznik + temp_dod_licznik
                self.__mianownik = self.__mianownik * other.__mianownik
        else:
            self.__licznik += other * self.__mianownik
        return self

    def __iadd__(self, other):
        if type(other) == Fractional:
            if self.__mianownik == other.__mianownik:
                self.__licznik += other,__licznik
            else:
                temp_dod_licznik = other.__licznik * self.__mianownik
                temp_self_licznik = other.__mianownik * self.__licznik
                self.__licznik = temp_self_licznik + temp_dod_licznik
                self.__mianownik = self.__mianownik * other.__mianownik
        else:
            self.__licznik += other * self.__mianownik
        return self

    def sub(self, other):
        if type(other) == Fractional:
            if self.__mianownik == other.__mianownik:
                self.__licznik -= other,__licznik
            else:
                temp_dod_licznik = other.__licznik * self.__mianownik
                temp_self_licznik = other.__mianownik * self.__licznik
                self.__licznik = temp_self_licznik - temp_dod_licznik
                self.__mianownik = self.__mianownik * other.__mianownik
        else:
            self.__licznik -= other * self.__mianownik
        return self

    def __sub__(self, other):
        if type(other) == Fractional:
            if self.__mianownik == other.__mianownik:
                self.__licznik -= other,__licznik
            else:
                temp_dod_licznik = other.__licznik * self.__mianownik
                temp_self_licznik = other.__mianownik * self.__licznik
                self.__licznik = temp_self_licznik - temp_dod_licznik
                self.__mianownik = self.__mianownik * other.__mianownik
        else:
            self.__licznik -= other * self.__mianownik
        return self

    def __isub__(self, other):
        if type(other) == Fractional:
            if self.__mianownik == other.__mianownik:
                self.__licznik -= other,__licznik
            else:
                temp_dod_licznik = other.__licznik * self.__mianownik
                temp_self_licznik = other.__mianownik * self.__licznik
                self.__licznik = temp_self_licznik - temp_dod_licznik
                self.__mianownik = self.__mianownik * other.__mianownik
        else:
            self.__licznik -= other * self.__mianownik
        return self

    def mul(self, other):
        if type(other) == Fractional:
            self.__mianownik *= other.__mianownik
            self.__licznik *= other.__licznik
        else:
            self.__licznik *= other
        return self

    def __mul__(self, other):
        if type(other) == Fractional:
            self.__mianownik *= other.__mianownik
            self.__licznik *= other.__licznik
        else:
            self.__licznik *= other
        return self

    def __imul__(self, other):
        if type(other) == Fractional:
            self.__mianownik *= other.__mianownik
            self.__licznik *= other.__licznik
        else:
            self.__licznik *= other
        return self

    def __str__(self):
        string = str(self.__licznik) + "/" + str(self.__mianownik)
        return string


if __name__ == "__main__":
    x = Fractional(pl(1,2),pl(2,1))
    y = Fractional(pl(2,3),pl(2,1))
    print(type(x))
    x += y
    print(x)
