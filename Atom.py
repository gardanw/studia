from Vec2 import Vec2

class Atom :
    def __init__(self, m=1, v=Vec2(0, 0), pos=Vec2(0, 0), r=0):
        self.__m = m
        self.__v = v
        self.__pos = pos
        self.__r = r

    def __str__(self):
        return 'x: ' + str(self.__pos.x) + ' y: ' + str(self.__pos.y)


if __name__ == '__main__':
    a = Atom(v=Vec2(1, 2), pos=Vec2(1, 1))
    print(a)