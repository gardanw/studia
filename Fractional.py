class Fractional :
    
    def __init__(self, licznik, mianownik):
        self.__mianownik = mianownik
        self.__licznik = licznik
    
    def add(self, dodawany):
        if type(dodawany) == Fractional:
            if self.__mianownik == dodawany.__mianownik:
                self.__licznik += dodawany,__licznik
            else:
                temp_dod_licznik = dodawany.__licznik * self.__mianownik
                temp_self_licznik = dodawany.__mianownik * self.__licznik
                self.__licznik = temp_self_licznik + temp_dod_licznik
                self.__mianownik = self.__mianownik * dodawany.__mianownik
        else:
            self.__licznik += dodawany * self.__mianownik
        return self

    def __add__(self, dodawany):
        if type(dodawany) == Fractional:
            if self.__mianownik == dodawany.__mianownik:
                self.__licznik += dodawany,__licznik
            else:
                temp_dod_licznik = dodawany.__licznik * self.__mianownik
                temp_self_licznik = dodawany.__mianownik * self.__licznik
                self.__licznik = temp_self_licznik + temp_dod_licznik
                self.__mianownik = self.__mianownik * dodawany.__mianownik
        else:
            self.__licznik += dodawany * self.__mianownik
        return self

    def __iadd__(self, dodawany):
        if type(dodawany) == Fractional:
            if self.__mianownik == dodawany.__mianownik:
                self.__licznik += dodawany,__licznik
            else:
                temp_dod_licznik = dodawany.__licznik * self.__mianownik
                temp_self_licznik = dodawany.__mianownik * self.__licznik
                self.__licznik = temp_self_licznik + temp_dod_licznik
                self.__mianownik = self.__mianownik * dodawany.__mianownik
        else:
            self.__licznik += dodawany * self.__mianownik
        return self

    def __str__(self):
        string = str(self.__licznik) + "/" + str(self.__mianownik)
        return string


if __name__ == "__main__":
    x = Fractional(1,2)
    y = Fractional(7,3)
    x += y
    print(x)
