import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import norm
from matplotlib.animation import FuncAnimation

class body(object):
    def __init__(self, mass, InitialPosition, InitialVelocity, Radius, colour, name):
        self.massOwn = mass
        self.Pos = InitialPosition
        self.V = InitialVelocity
        self.G = 6.67408*(10**-11)
        self.Radius = Radius
        self.colour = colour
        self.name = name
        self.a_next = np.array([0 , 0])
        self.a_current = np.array([0,0])

    def calc_a(self, the_planets):
        self.a_previous = self.a_current
        self.a_current = self.a_next
        self.a_next = np.array([0 , 0])
        for j in range(len(the_planets)):
            if the_planets[j].name != self.name:
                r_ij = the_planets[j].Pos - self.Pos
                self.a_next = self.a_next + ((self.G) * the_planets[j].massOwn * r_ij)/((np.linalg.norm(r_ij))**3)

    def calc_v(self, timestep):
        self.V = self.V + (0.16667)*((2*self.a_next) + (5*self.a_current) - (self.a_previous))*(timestep)

    def calc_r(self, timestep):
        self.Pos = self.Pos + (self.V * timestep) + (0.166667)*((4*self.a_current)-self.a_previous)*(timestep)**2
