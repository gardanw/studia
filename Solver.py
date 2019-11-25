from Atom import Atom
from Vec2 import Vec2
from Polygon import Polygon
from System import System

class Solver :
    def __init__(self, system, dt=1):
        self.__system = system
        self.__dt = dt

    def update_pos(self):
        for atom in self.__system.get_atoms:
            atom.pos = atom.pos + atom.v.mul(self.__dt)



if __name__ == '__main__':
    atomy = [Atom(v=Vec2(1, 1), pos=Vec2(1, 1)), Atom(v=Vec2(0, 1), pos=Vec2(1, 2))]
    scena = [Polygon([Vec2(0, 0), Vec2(0, 10), Vec2(10, 10), Vec2(10, 0)])]
    s = System(atomy, scena)
    for atom in s.get_atoms:
        print(atom.pos)

    sym = Solver(s)
    # for i in range(3):
    sym.update_pos()

    for atom in s.get_atoms:
        print(atom.pos)