from math import sqrt
import pygame

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

        return pygame.draw.circle(
            screen,
            (self.colour),
            (self.xcor, self.ycor),
            self.size
        )

def calc_gravitation(location1, location2, mass1, mass2):
    G = 1
    x = location1[0] - location2[0]
    y = location1[1] - location2[1]
    distance = sqrt(x**2 + y**2)

    force = G * ((mass1 * mass2) / distance**2)

    force_x = force * (x / distance)
    force_y = force * (y / distance)

    return force_x, force_y
