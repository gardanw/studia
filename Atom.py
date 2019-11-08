from Vec2 import Vec2
from copy import deepcopy as dc

class Atom :
    def __init__(self, m=1, v=Vec2(0, 0), pos=Vec2(0, 0), r=0):
        self.__m = m
        self.__v = dc(v)
        self.__pos = dc(pos)
        self.__r = r

    def __str__(self):
        return 'x: ' + str(self.__pos.x) + ' y: ' + str(self.__pos.y)

    @property
    def m(self):
        return self.__m

    @property
    def v(self):
        return self.__v

    @property
    def pos(self):
        return self.__pos

    @property
    def r(self):
        return self.__r

    # @x.setter
    # def x(self, x):
    #     self.__x = x
    #
    # @y.setter
    # def y(self, y):
    #     self.__y = y


if __name__ == '__main__':
    a = Atom(v=Vec2(1, 2), pos=Vec2(1, 1))
    print(a)