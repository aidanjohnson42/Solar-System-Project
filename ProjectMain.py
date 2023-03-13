import numpy as np

from Bodies import body
from Simluation import simulation

def main():
    planets = []
    file = open("planets.sol", "r")
    fileread = file.readlines()
    for line in fileread:
        if line.startswith("#") == False:
            split = line.split(",")
            name = str(split[0])
            mass = float(split[1])
            radius = float(split[2])
            x_pos = float(split[3])
            y_pos = float(split[4])
            pos = np.array([x_pos,y_pos])
            x_vel = float(split[5])
            y_vel = float(split[6])
            vel = np.array([x_vel,y_vel])
            colour = str(split[7])
            planet = body(mass, pos, vel, radius, colour, name)
            planets.append(planet)

    OrbitSim = simulation(planets)
    OrbitSim.display()

main()
