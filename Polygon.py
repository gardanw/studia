from Atom import Atom

def center(nodes):
    if len(nodes) == 0:
        return Vec2(0, 0)
    list_x = []
    list_y = []
    for i in nodes:
        list_x.append(i.x)
        list_y.append(i.y)
    return Vec2(sum(list_x)/len(list_x), sum(list_y)/len(list_y))


class Polygon(Atom):
    def __init__(self, nodes=[]):
        super.__init__(self,  m=0, v=Vec2(0, 0), pos=center(    ))
        self.__nodes = nodes
