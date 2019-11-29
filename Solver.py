from Atom import Atom
from Vec2 import Vec2, point_on_segment_projection
from Polygon import Polygon
from System import System
from copy import deepcopy as dc

def collision_w(atom, d):
    v_n = dc(atom.v)
    n = dc(d)
    u = n.mul(n.dp(v_n)/n.dp(n))
    w = v_n - u
    v_n = w - u
    return v_n

def collision_a(atom1, atom2):
    a1 = dc(atom1)
    a2 = dc(atom2)
    m_n = a1.m + a2.m
    v_n = a1.v - a2.v
    pos_n = a1.pos - a2.pos
    f = 2*v_n.dp(pos_n)/(m_n * pos_n.length()**2)
    return f
    


class Solver :
    def __init__(self, system, dt=0.001):
        self.__system = system
        self.__dt = dt

    def update_pos(self):
        for atom in self.__system.get_atoms:
            atom.pos = atom.pos + atom.v.mul(self.__dt)
    
    def collision_wall(self):
        for atom in self.__system.get_atoms:
#            print(atom)
            for p in self.__system.get_scena:
                if type(p) == Polygon:
                    for i in range(len(p.nodes)):
                        d, t = point_on_segment_projection(atom.pos, p.nodes[i-1], p.nodes[i])
#                        print(d, d.length(), t, atom.pos, atom.r, p.nodes[i-1], p.nodes[i])
                        if t > 0 and t < 1:
                            if d.length() <= atom.r:
                                print(atom.v)
                                atom.v = collision_w(atom, d)
                                print(atom.v)
                                
    
    def collision_atom(self):
        for i in range(len(self.__system.get_atoms)):
#            print(self.__system.get_atoms[i])
            for j in range(i+1,len(self.__system.get_atoms)):
#                if self.__system.get_atoms[i] != self.__system.get_atoms[j]:
                print(self.__system.get_atoms[j])
                odl = dc(self.__system.get_atoms[i].pos) - self.__system.get_atoms[j].pos
                if odl.length() <= self.__system.get_atoms[i].r + self.__system.get_atoms[j].r:
                    f = collision_a(self.__system.get_atoms[i], self.__system.get_atoms[j])
                    x = dc(self.__system.get_atoms[i].pos) - self.__system.get_atoms[j].pos
                    self.__system.get_atoms[i].v = self.__system.get_atoms[i].v - x.mul(self.__system.get_atoms[i].m*f)
                    self.__system.get_atoms[j].v = self.__system.get_atoms[j].v + x.mul(self.__system.get_atoms[j].m*f)
                    
    def run(self, time):
        for i in range(time):
            self.collision_atom()
            self.collision_wall()
            self.update_pos()



if __name__ == '__main__':
    atomy = [Atom(v=Vec2(1, 1), pos=Vec2(1, 1), r=1), Atom(v=Vec2(1, 1), pos=Vec2(2, 2), r=1), Atom(v=Vec2(1, 1), pos=Vec2(1, 9), r=2), Atom(v=Vec2(1, 1), pos=Vec2(9, 1), r=2)]
    scena = [Polygon([Vec2(0, 0), Vec2(0, 10), Vec2(10, 10), Vec2(10, 0)])]
    s = System(atomy, scena)
    for atom in s.get_atoms:
        print(atom.pos)

    sym = Solver(s)
    # for i in range(3):
#    sym.update_pos()

    for atom in s.get_atoms:
        print(atom.pos)
    print(type(scena[0]), type(atomy[0]))
    sym.run(1000)