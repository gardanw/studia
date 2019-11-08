# import math
from copy import deepcopy as dc

class Vec2 :

    def __init__(self, *args):
        if type(args[0]) == list:
            self.__x = args[0][0]
            self.__y = args[0][1]
        else:
            self.__x = args[0]
            self.__y = args[1]

    def __str__(self):
        string = str()
        string += str(self.__x) + ', ' + str(self.__y)
        return string

    def add(self, other):
        self.__x += other.__x
        self.__y += other.__y
        return self

    def __add__(self, other):
        return self.add(other)

    def __iadd__(self, other):
        return self.add(other)

    def sub(self, other): 
        self.__x -= other.__x
        self.__y -= other.__y
        return self

    def __sub__(self, other): 
        return self.sub(other)

    def __isub__(self, other): 
        return self.sub(other)
    
    def dp(self, other):
        return (self.__x * other.__x) + (self.__y * other.__y)
    
    def length(self):
        return (self.__x**2 + self.__y**2)**(0.5)
    
    def normalize(self):
        new = dc(self)
        new.__x = new.__x/self.length()
        new.__y = new.__y/self.length()
        return new

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, x):
        self.__x = x

    @y.setter
    def y(self, y):
        self.__y = y


if __name__ == "__main__":
    w1 = Vec2(5,1)
    w2 = Vec2(-2,4)
    print(w1.length(), w2.length())
    print(w1.dp(w2))
    print(w1.normalize().length())