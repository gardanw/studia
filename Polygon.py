from Atom import Atom
from Vec2 import Vec2
from copy import deepcopy as dc

def center(nodes):
    if len(nodes) == 0:
        return Vec2(0, 0)
    list_x = []
    list_y = []
    for i in nodes:
        list_x.append(i.x)
        list_y.append(i.y)
    return Vec2(sum(list_x)/len(list_x), sum(list_y)/len(list_y))

def radius(nodes):
    pos = center(nodes)
    lista_r = []
    for i in range(len(nodes)):
        lista_r.append(((nodes[i].x-pos.x)**2 + (nodes[i].x-pos.y)**2)**(0.5))
    return max(lista_r)



class Polygon(Atom):
    def __init__(self, nodes=[]):
        Atom.__init__(self, 0, Vec2(0, 0), center(nodes), radius(nodes))
        self.__nodes = dc(nodes)

    def __str__(self):
        return 'pos = ' + str(self.pos) + ' count nodes = ' + str(len(self.__nodes)) + ' r = ' + str(self.r)

    @property
    def nodes(self):
        return self.__nodes

    def __repr__(self):
        return self.__str__()

if __name__ == '__main__':
    pol = Polygon([Vec2(0, 1), Vec2(1, 0), Vec2(0, 0), Vec2(10, 10)])
    print(pol)
