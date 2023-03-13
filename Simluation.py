import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import norm
from matplotlib.animation import FuncAnimation

class simulation(object):
    def __init__(self, planets_list):
        self.planets = planets_list
        self.timestep = 500
        self.patches = []
        self.KECounter = 0

    def obtain_r(self):
        for k in range(len(self.planets)):
            self.planets[k].calc_r(self.timestep)

    def obtain_a(self):
        for k in range(len(self.planets)):
            self.planets[k].calc_a(self.planets)

    def obtain_v(self):
        for k in range(len(self.planets)):
            self.planets[k].calc_v(self.timestep)

    def obtain_ke(self):
        NetKE = 0
        for k in range(len(self.planets)):
            KE = 0.5*(self.planets[k].massOwn)*(np.linalg.norm(self.planets[k].V))**2
            NetKE += KE
        print("The total Kinetic Energy of the system is " + str(NetKE))

    def forward_move(self):
        i = 0
        while i < 100:
            i += 1
            self.obtain_a()
            self.obtain_v()
            self.obtain_r()

        self.KECounter += 1
        if self.KECounter == 50:
            self.KECounter = 0
            self.obtain_ke()

    def animate(self, i):
        self.forward_move()
        for j in range(len(self.patches)):
            self.patches[j].center = (self.planets[j].Pos[0], self.planets[j].Pos[1])
        return self.patches

    def display(self):
        fig = plt.figure()
        ax = plt.axes()

        ax.axis('square')
        ax.set_xlim(-3.5*10**11, 3.5*10**11)
        ax.set_ylim(-3.5*10**11, 3.5*10**11)

        for k in range(len(self.planets)):
            self.patches.append(plt.Circle((self.planets[k].Pos[0], self.planets[k].Pos[1]), self.planets[k].Radius, color = self.planets[k].colour , animated = True))
            ax.add_patch(self.patches[k])

        anim = FuncAnimation(fig, self.animate, frames = 100000, repeat = False, interval = 20, blit = True)

        plt.show()
