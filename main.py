import pygame
from planet import Planet, calc_gravitation

pygame.init()

RESOLUTION = (1280, 720)

# colours
YELLOW = (255, 255, 0)
NEBULA_BLUE = (84, 104, 255)

# planets
SUN = Planet(1000, 640, 360, 25, YELLOW, fix=True)
EARTH = Planet(100, 640, 130, 10, (0, 0, 255), velx=1)

screen = pygame.display.set_mode(RESOLUTION)
clock = pygame.time.Clock()

pygame.display.set_caption("First Window")

game = True

x = 0
y = 0

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            print("Spieler hat Quit-Button angeklickt")

    screen.fill(NEBULA_BLUE)


    # TODO: make a funktion for this
    # find all "zweipärchen" use itertools
    force_x, force_y = calc_gravitation((SUN.xcor, SUN.ycor), (EARTH.xcor, EARTH.ycor), SUN.mass, EARTH.mass)
    ax_sun = -force_x / SUN.mass
    ay_sun = -force_y / SUN.mass
    ax_earth = force_x / EARTH.mass
    ay_earth = force_y / EARTH.mass
    SUN.velx += ax_sun
    SUN.vely += ay_sun
    EARTH.velx += ax_earth
    EARTH.vely += ay_earth

    # TODO: make planet spawn on click location
    SUN.draw_planet(screen)
    EARTH.draw_planet(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()