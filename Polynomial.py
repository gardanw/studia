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
        return self

    def sub(self, wielomian):
        wsp = wielomian.__wspolczynniki
        dlu = len(wsp) - len(self.__wspolczynniki)
        for i in range(dlu):
            self.__wspolczynniki.append(0)
        for i in range(len(wsp)):
            self.__wspolczynniki[i] -= wsp[i]
        return self
    
    def mul(self, wielomian):
        dl = len(self.__wspolczynniki) + len(wielomian.__wspolczynniki) - 1
        wyniki = list()
        for i in range(dl):
            wyniki.append(0)
        for i in range(len(self.__wspolczynniki)):
            for j in range(len(wielomian.__wspolczynniki)):
                wyniki[j+i] += self.__wspolczynniki[i] * wielomian.__wspolczynniki[j]
        self.__wspolczynniki = wyniki
#        return Polynomial(wyniki[::-1])
        return self
    
    def differentiate(self):
        dl = len(self.__wspolczynniki) - 1
        wyniki = list()
        for i in range(dl):
            wyniki.append(0)
        for i in range(len(wyniki)):
            wyniki[i] = self.__wspolczynniki[i+1]*(i+1)
        self.__wspolczynniki = wyniki
#        return Polynomial(wyniki[::-1])
        return self
    
    def integrate(self):
        dl = len(self.__wspolczynniki) + 1
        wyniki = list()
        for i in range(dl):
            wyniki.append(0)
        for i in range(len(wyniki)-1):
            wyniki[i+1] = self.__wspolczynniki[i]/(i+1)
        self.__wspolczynniki = wyniki
#        return Polynomial(wyniki[::-1])
        return self
    
    def eval(self, x):
        wartosc = int()
        for i in range(len(self.__wspolczynniki)):
            wartosc += self.__wspolczynniki[i]*x**i
        return wartosc

    def __str__(self):
        string = str()
        for i in range(len(self.__wspolczynniki)):
            if self.__wspolczynniki[len(self.__wspolczynniki)-1-i] == 0:
                continue
            if self.__wspolczynniki[len(self.__wspolczynniki)-1-i] < 0:    
                string += str(self.__wspolczynniki[len(self.__wspolczynniki)-1-i])\
                + 'x^' + str(len(self.__wspolczynniki)-1-i)
            else:
                string += '+' + str(self.__wspolczynniki[len(self.__wspolczynniki)-1-i])\
                + 'x^' + str(len(self.__wspolczynniki)-1-i)
        return string
    
if __name__ == "__main__":
    t0 = Polynomial(1)
    t1 = Polynomial(1,0)
    k = 128
    for i in range(k-1):
        pom = Polynomial(2,0)
        tk = pom.mul(t1).sub(t0)
        t0 = t1
        t1 = tk
    print(tk)