from Atom import Atom
from Vec2 import Vec2, point_on_segment_projection
from Polygon import Polygon
from System import System
from copy import deepcopy as dc
import numpy as np
import pygame, sys


def collision_w(atom, d):
    v_n = dc(atom.v)
    n = dc(d)
    u = n.mul(n.dp(v_n) / n.dp(n))
    w = v_n - u
    v_n = w - u
    return v_n


def collision_a(atom1, atom2):
    a1 = dc(atom1)
    a2 = dc(atom2)
    m_n = a1.m + a2.m
    v_n = a1.v - a2.v
    pos_n = a1.pos - a2.pos
    f = 2 * v_n.dp(pos_n) / (m_n * pos_n.length() ** 2)
    return f


class Solver:
    def __init__(self, system, dt=0.001):
        self.__system = system
        self.__dt = dt
        self.__list_pos = []
        for i in range(len(self.__system.get_atoms)):
            #            print(self.__system.get_atoms[i].pos)
            self.__list_pos.append([np.array([self.__system.get_atoms[i].pos.x, self.__system.get_atoms[i].pos.y])])

        self.kolory_atom = []
        for i in range(len(self.__system.get_atoms)):
            k1, k2, k3 = np.random.randint(255), np.random.randint(255), np.random.randint(255)
            self.kolory_atom.append(pygame.Color(k1, k2, k3, 255))

        self.kolory_scena = []
        for i in range(len(self.__system.get_scena)):
            k1, k2, k3 = np.random.randint(255), np.random.randint(255), np.random.randint(255)
            self.kolory_atom.append(pygame.Color(k1, k2, k3, 255))

    def update_pos(self):
        for atom in self.__system.get_atoms:
            atom.pos = atom.pos + dc(atom.v).mul(self.__dt)

    def collision_wall(self):
        for atom in self.__system.get_atoms:
            #            print(atom)
            for p in self.__system.get_scena:
                if type(p) == Polygon:
                    for i in range(len(p.nodes)):
                        d, t = point_on_segment_projection(atom.pos, p.nodes[i - 1], p.nodes[i])
                        #                        print(d, d.length(), t, atom.pos, atom.r, p.nodes[i-1], p.nodes[i])
                        if t > 0 and t < 1:
                            if d.length() <= atom.r:
                                #                                print('v1',atom.v)
                                atom.v = collision_w(atom, d)

    #                                print('v2', atom.v)

    def collision_atom(self):
        for i in range(len(self.__system.get_atoms)):
            #            print(self.__system.get_atoms[i])
            for j in range(i + 1, len(self.__system.get_atoms)):
                #                if self.__system.get_atoms[i] != self.__system.get_atoms[j]:
                #                print(self.__system.get_atoms[j])
                odl = dc(self.__system.get_atoms[i].pos) - self.__system.get_atoms[j].pos
                if odl.length() <= self.__system.get_atoms[i].r + self.__system.get_atoms[j].r:
                    f = collision_a(self.__system.get_atoms[i], self.__system.get_atoms[j])
                    x = dc(self.__system.get_atoms[i].pos) - self.__system.get_atoms[j].pos
                    self.__system.get_atoms[i].v = self.__system.get_atoms[i].v - dc(x).mul(
                        self.__system.get_atoms[i].m * f)
                    self.__system.get_atoms[j].v = self.__system.get_atoms[j].v + x.mul(
                        self.__system.get_atoms[j].m * f)

    def run(self, time):
        for i in range(time):
            self.collision_atom()
            self.collision_wall()
            self.update_pos()
            for i in range(len(self.__system.get_atoms)):
                self.__list_pos[i].append(
                    np.array([self.__system.get_atoms[i].pos.x, self.__system.get_atoms[i].pos.y]))
        return self.__list_pos

    def drawrun(self):

        # config
        self.tps_max = 100.0

        # initalisation
        pygame.init()

        self.window = pygame.display.set_mode((500, 500))  # tworzy okno

        self.tps_clock = pygame.time.Clock()  # zegar
        self.tps_delta = 0.0
        while True:
            # sprawdza nowe zdarzania
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)

            # ticking
            self.tps_delta += self.tps_clock.tick() / 1000.0

            # rendering
            self.window.fill((0, 0, 0))
            self.draw(self.window)
            pygame.display.flip()
            self.run(1)

    def draw(self, window):
        # rysuje
        for scen, kolor in zip(self.__system.get_scena, self.kolory_scena):
            point = []
            for i in scen:
                point.append([i[0], i[1]])
            pygame.draw.polygon(self.window, pygame.Color(k1, k2, k3, 255), point)
        for atom, kolor in zip(self.__system.get_atoms, self.kolory_atom):
            #            print(atom.pos_get[0]+odl_pom/2, atom.pos_get[1]+odl_pom/2, 3.5, 3.5)
            center = (int(atom.pos[0]), int(atom.pos[1]))
            rad = dc(atom.r)
            pygame.draw.circle(self.window, kolor, [int((center[0]) * 10), int((center[1]) * 10)], rad * 10, 3)


if __name__ == '__main__':
    # atomy = [Atom(v=Vec2(25, 25), pos=Vec2(20, 22), r=1), Atom(v=Vec2(-25, -25), pos=Vec2(30, 20), r=1),
    #          Atom(v=Vec2(25, 25), pos=Vec2(41, 23), r=1), Atom(v=Vec2(-25, -25), pos=Vec2(15, 20), r=1),
    #          Atom(v=Vec2(25, 25), pos=Vec2(37, 22), r=1), Atom(v=Vec2(-25, -25), pos=Vec2(16, 4), r=1)]
    atomy = []
    n = 5
    for i in range(n):
        atomy.append(Atom(v=Vec2(np.random.randint(25), np.random.randint(25)),
                          pos=Vec2(np.random.randint(5, 40), np.random.randint(5, 40)), r=np.random.randint(1, 5)))
    scena = [Polygon([Vec2(0, 0), Vec2(0, 50), Vec2(50, 50), Vec2(50, 0)])]
    s = System(atomy, scena)
    #    for atom in s.get_atoms:
    #        print(atom.pos)

    sym = Solver(s)
    sym.drawrun()
#    print(sym.run(100))
