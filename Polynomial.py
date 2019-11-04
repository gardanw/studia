class Polynomial :
    __slots__ = ['__wspolczynniki']
    
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
    
    def add(self, other):
        if type(other) == Polynomial:
            wsp = other.__wspolczynniki
            dlu = len(wsp) - len(self.__wspolczynniki)
            for i in range(dlu):
                self.__wspolczynniki.append(0)
            for i in range(len(wsp)):
                self.__wspolczynniki[i] += wsp[i]
        else:
            self.__wspolczynniki[0] += other
        return self
    
    def __add__(self, other):
        return self.add(other)

    def __iadd__(self, other):
        return self.add(other)
    
    def sub(self, other):
        if type(other) == Polynomial:
            wsp = other.__wspolczynniki
            dlu = len(wsp) - len(self.__wspolczynniki)
            for i in range(dlu):
                self.__wspolczynniki.append(0)
            for i in range(len(wsp)):
                self.__wspolczynniki[i] -= wsp[i]
        else:
            self.__wspolczynniki[0] -= other
        return self
    
    def __sub__(self, other):
        return self.sub(other)
    
    def __isub__(self, other):
        return self.sub(other)
    
    def mul(self, other):
        if type(other) == Polynomial:
            dl = len(self.__wspolczynniki) + len(other.__wspolczynniki) - 1
            wyniki = list()
            for i in range(dl):
                wyniki.append(0)
            for i in range(len(self.__wspolczynniki)):
                for j in range(len(other.__wspolczynniki)):
                    wyniki[j+i] += self.__wspolczynniki[i] * other.__wspolczynniki[j]
            self.__wspolczynniki = wyniki
        else:
            for i in range(len(self.__wspolczynniki)):
                self.__wspolczynniki[i] *= other
        return self
    
    def __mul__(self, other):
        return self.mul(other)
    
    def __imul__(self, other):
        return self.mul(other)

    def differentiate(self):
        dl = len(self.__wspolczynniki) - 1
        wyniki = list()
        for i in range(dl):
            wyniki.append(0)
        for i in range(len(wyniki)):
            wyniki[i] = self.__wspolczynniki[i+1]*(i+1)
        self.__wspolczynniki = wyniki
        return self
    
    def integrate(self):
        dl = len(self.__wspolczynniki) + 1
        wyniki = list()
        for i in range(dl):
            wyniki.append(0)
        for i in range(len(wyniki)-1):
            wyniki[i+1] = self.__wspolczynniki[i]/(i+1)
        self.__wspolczynniki = wyniki
        return self
    
    def __call__(self, x):
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
    
    def __eq__(self, other):
        if self.__wspolczynniki == other.__wspolczynniki:
            return True
        else:
            return False

if __name__ == "__main__":
    t0 = Polynomial(1)
    t1 = Polynomial(1,0)
    k = 128
    for i in range(k-1):
        pom = Polynomial(2,0)
        tk = pom * t1 - t0
        t0 = t1
        t1 = tk
    print(tk)
    x = Polynomial(1,2)
    print(x)
    x.mul(2)
    print(x)
    
    w1 = Polynomial(2,1)
    w2 = Polynomial(2,1)
    print(w1, "*", w1, "=")
    w1 *= w2
    
    print(w1)
