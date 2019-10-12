class Polynomial :
    def __init__(self, *args):
        self.__wspolczynniki = list()
        if len(args) == 1 and type(args[0]) == list:
            for i in args[0]:
                self.__wspolczynniki.append(i)
            self.__wspolczynniki = self.__wspolczynniki[::-1]
        else:
            for i in args:
                self.__wspolczynniki.append(i)
            self.__wspolczynniki = self.__wspolczynniki[::-1]
    
    def add(self, wielomian):
        wsp = wielomian.__wspolczynniki
        dlu = len(wsp) - len(self.__wspolczynniki)
        for i in range(dlu):
            self.__wspolczynniki.append(0)
        for i in range(len(wsp)):
            self.__wspolczynniki[i] += wsp[i]

    def eval(self):
        pass

    def __str__(self):
        string = str()
        for i in range(len(self.__wspolczynniki)):
            if self.__wspolczynniki[i] == 0:
                continue
            string += str(self.__wspolczynniki[len(self.__wspolczynniki)-1-i]) + 'x^' + str(len(self.__wspolczynniki)-1-i) + '+'
        return string[:-1]
    

c = [1,0,3]
y = Polynomial(2,3,5)
x = Polynomial(c)
print(x, '+', y, ' = ')
x.add(y)
print(x)