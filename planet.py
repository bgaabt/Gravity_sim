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

    for body_a, body_b in combinations(galaxy, 2):

        force_x, force_y = calc_force(
            (body_a.xcor, body_a.ycor),
            (body_b.xcor, body_b.ycor),
            body_a.mass, body_b.mass)
        
        ax_p1 = -force_x / body_a.mass
        ay_p1 = -force_y / body_a.mass
        ax_p2 = force_x / body_b.mass
        ay_p2 = force_y / body_b.mass

        body_a.velx += ax_p1
        body_a.vely += ay_p1
        body_b.velx += ax_p2
        body_b.vely += ay_p2
