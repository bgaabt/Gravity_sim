from math import sqrt
from pygame import draw
from itertools import combinations


class Planet:

    def __init__(self, mass, xcor, ycor, size, colour, velx = 0, vely = 0, fix = False) -> None:
        self.mass = mass
        self.xcor = xcor
        self.ycor = ycor
        self.size = size
        self.colour = colour
        self.velx = velx
        self.vely = vely
        self.fix = fix

    def draw_planet(self, screen):
        if not self.fix:
            self.xcor = self.xcor + self.velx
            self.ycor = self.ycor + self.vely

        return draw.circle(
            screen,
            (self.colour),
            (self.xcor, self.ycor),
            self.size
        )

def calc_force(location1, location2, mass1, mass2):
    G = 1
    x = location1[0] - location2[0]
    y = location1[1] - location2[1]
    distance = sqrt(x**2 + y**2)

    force = G * ((mass1 * mass2) / distance**2)

    force_x = force * (x / distance)
    force_y = force * (y / distance)

    return force_x, force_y

def calc_gravity(galaxy):
    counter_a = 0
    counter_b = 1
    num_planets = len(galaxy)

    for i in range(len(list(combinations(galaxy, 2)))):

        force_x, force_y = calc_force(
            (galaxy[counter_a].xcor, galaxy[counter_a].ycor),
            (galaxy[counter_b].xcor, galaxy[counter_b].ycor),
            galaxy[counter_a].mass, galaxy[counter_b].mass)
        
        ax_p1 = -force_x / galaxy[counter_a].mass
        ay_p1 = -force_y / galaxy[counter_a].mass
        ax_p2 = force_x / galaxy[counter_b].mass
        ay_p2 = force_y / galaxy[counter_b].mass

        galaxy[counter_a].velx += ax_p1
        galaxy[counter_b].vely += ay_p1
        galaxy[counter_b].velx += ax_p2
        galaxy[counter_b].vely += ay_p2

        counter_b += 1
        if num_planets == counter_b:
            counter_a += 1
            counter_b = counter_a + 1
    
