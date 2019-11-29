# import math
from copy import deepcopy as dc

def point_on_segment_projection(point, w1, w2):
    p = dc(point)
    b = dc(w1)
    e = dc(w2)
    odc = dc(e) - b
    t = ((p.x - b.x)*(e.x - b.x) + (p.y - b.y)*(e.y - b.y))/odc.length()**2
    n_point = odc.mul(t) + b
    d = n_point - p

    return d, t

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
        string += '(' + str(self.__x) + ', ' + str(self.__y) + ')'
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

    def mul(self, other):
        self.__x *= other
        self.__y *= other
        return self
    
    def dp(self, other):
        return (self.__x * other.__x) + (self.__y * other.__y)
    
    def length(self):
        return (self.__x**2 + self.__y**2)**(0.5)
    
    def normalize(self):
        new = dc(self)
        new.__x = new.__x/self.length()
        new.__y = new.__y/self.length()
        return new

    def distance(self, other):
        pass

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

    def __repr__(self):
        return self.__str__()


if __name__ == "__main__":
    point = Vec2(3, 3)
    w1 = Vec2(0, 0)
    w2 = Vec2(5, 5)
    print(w1)
    print(point_on_segment_projection(point, w1, w2)[0])
    # print((w1 - w2).length()**2)