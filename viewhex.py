import sys
import pygame

import hexagongrid as hex
import geom as g

gray = (0xaa, 0xaa, 0xaa)
orange = (0xff, 0x85, 0x1b)

pygame.init()
size = width, height = 640, 480
screen = pygame.display.set_mode(size)

points = [h*100+[150,150] for h in hex.grid_rect(3)]

while True:
    # -- handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # -- draw
    screen.fill(gray)
    for hp in points:
        pygame.draw.lines(screen, orange, True, hp, 2)

    # -- flip display
    pygame.display.flip()
