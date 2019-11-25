from Atom import Atom
from Vec2 import Vec2
from Polygon import Polygon

class System :
    def __init__(self, atoms=list(), scene=list()):
        self.__atoms = atoms
        self.__scena = scene

    def __str__(self):
        return 'liczba atomow w systemie = ' + str(len(self.__atoms)) + ' obiekty w scenie = ' + str(len(self.__scena))

    @property
    def get_atoms(self):
        return self.__atoms

    @property
    def get_scena(self):
        return self.__scena

    def __repr__(self):
        return self.__str__()

if __name__ == '__main__':
    atomy = [Atom(v=Vec2(1, 2), pos=Vec2(1, 1)), Atom(v=Vec2(1, 2), pos=Vec2(2, 1))]
    scena = [Polygon([Vec2(0, 0), Vec2(0, 10), Vec2(10, 10), Vec2(10, 0)])]
    s = System(atomy, scena)
    print(s.get_atoms)
