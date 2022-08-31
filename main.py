import pygame
from planet import Planet, calc_gravity

pygame.init()

RESOLUTION = (1280, 720)

# colours
YELLOW = (255, 255, 0)
NEBULA_BLUE = (84, 104, 255)
MAGENTA = (255,0,255)

# planets
SUN = Planet(500, 640, 360, 25, YELLOW, fix=True)
EARTH = Planet(100, 640, 130, 10, (0, 0, 255), velx=1)
PLUTO = Planet(100, 320, 360, 10, MAGENTA, vely=1)

galaxy = [SUN, EARTH, PLUTO]

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

    calc_gravity(galaxy)

    # TODO: make planet spawn on click location
    SUN.draw_planet(screen)
    EARTH.draw_planet(screen)
    PLUTO.draw_planet(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()