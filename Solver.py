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


def random_color():
    k1, k2, k3 = np.random.randint(255), np.random.randint(255), np.random.randint(255)
    return pygame.Color(k1, k2, k3, 255)


class Solver:
    def __init__(self, system, dt=0.001):
        self.__system = system
        self.__dt = dt
        self.__list_pos = []
        for i in range(len(self.__system.get_atoms)):
            self.__list_pos.append([np.array([self.__system.get_atoms[i].pos.x, self.__system.get_atoms[i].pos.y])])

        self.atoms_color = []
        for i in range(len(self.__system.get_atoms)):
            self.atoms_color.append(random_color())

        self.scenes_color = []
        for i in range(len(self.__system.get_scena)):
            self.scenes_color.append(random_color())

    def update_pos(self):
        for atom in self.__system.get_atoms:
            if type(atom) == Atom:
                atom.pos = atom.pos + dc(atom.v).mul(self.__dt)
            elif type(atom) == Polygon:
                for n in atom.nodes:
                    pass

    def collision_atom_wall(self):
        for atom in self.__system.get_atoms:
            for p in self.__system.get_scena:
                if type(p) == Polygon:
                    for i in range(len(p.nodes)):
                        d, t = point_on_segment_projection(atom.pos, p.nodes[i - 1], p.nodes[i])
                        if 0 < t < 1:
                            if d.length() <= atom.r:
                                atom.v = collision_w(atom, d)
                                atom.pos = atom.pos + dc(atom.v).mul(0.001)

    def collision_atom_atom(self):
        for i in range(len(self.__system.get_atoms)):
            for j in range(i + 1, len(self.__system.get_atoms)):
                odl = dc(self.__system.get_atoms[i].pos) - self.__system.get_atoms[j].pos
                if odl.length() <= self.__system.get_atoms[i].r + self.__system.get_atoms[j].r:
                    f = collision_a(self.__system.get_atoms[i], self.__system.get_atoms[j])
                    x = dc(self.__system.get_atoms[i].pos) - self.__system.get_atoms[j].pos
                    self.__system.get_atoms[i].v = self.__system.get_atoms[i].v - dc(x).mul(
                        self.__system.get_atoms[j].m * f)
                    self.__system.get_atoms[j].v = self.__system.get_atoms[j].v + x.mul(
                        self.__system.get_atoms[i].m * f)
                    self.__system.get_atoms[i].pos = self.__system.get_atoms[i].pos + dc(
                        self.__system.get_atoms[i].v).mul(0.001)
                    self.__system.get_atoms[j].pos = self.__system.get_atoms[j].pos + dc(
                        self.__system.get_atoms[j].v).mul(0.001)

    def run(self, time):
        for t in range(time):
            self.collision_atom_atom()
            self.collision_atom_wall()
            self.update_pos()

    def draw_run(self):

        # config
        self.tps_max = 100.0

        # initalisation
        pygame.init()

        self.window = pygame.display.set_mode((510, 510))  # tworzy okno

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
        for scen, kolor in zip(self.__system.get_scena, self.scenes_color):
            point = []
            for i in scen.nodes:
                point.append([i[0] * 10, i[1] * 10])
            pygame.draw.polygon(self.window, pygame.Color(255, 255, 255, 255), point, 1)
        for atom, kolor in zip(self.__system.get_atoms, self.atoms_color):
            if type(atom) == Atom:
                center = (int(atom.pos[0] * 10), int(atom.pos[1] * 10))
                rad = dc(atom.r)
                pygame.draw.circle(self.window, kolor, center, rad * 10, 3)
            elif type(atom) == Polygon:
                point = []
                for i in atom.nodes:
                    point.append([i[0] * 10, i[1] * 10])
                pygame.draw.polygon(self.window, pygame.Color(200, 200, 200, 200), point)


if __name__ == '__main__':
    # atomy = [Atom(v=Vec2(25, 25), pos=Vec2(20, 22), r=2, m=100), Atom(v=Vec2(-25, -25), pos=Vec2(30, 20), r=1),
    #          Atom(v=Vec2(25, 25), pos=Vec2(41, 23), r=1), Atom(v=Vec2(-25, -25), pos=Vec2(15, 20), r=1),
    #          Atom(v=Vec2(25, 25), pos=Vec2(37, 22), r=1), Atom(v=Vec2(-25, -25), pos=Vec2(16, 4), r=1)]
    atomy = [Atom(v=Vec2(np.random.randint(75), np.random.randint(75)),
                  pos=Vec2(np.random.randint(5, 40), np.random.randint(5, 40)), r=np.random.randint(1, 5), m=20)]
    n = 25
    i = 0
    while len(atomy) < n:
        x = np.random.randint(5, 40)
        y = np.random.randint(5, 40)
        p = Vec2(x, y)
        rad = np.random.randint(1, 5)
        flaga = 0
        for atom in atomy:
            odl = dc(atom.pos) - p
            if odl.length() < atom.r + rad:
                flaga += 1
        if flaga == 0:
            mass = rad * 10
            atomy.append(Atom(v=Vec2(np.random.randint(75), np.random.randint(75)),
                              pos=p, r=rad, m=mass))
    scena = [Polygon([Vec2(0, 0), Vec2(0, 50), Vec2(50, 50), Vec2(50, 0)])]
    s = System(atomy, scena)

    sym = Solver(s)
    sym.draw_run()
