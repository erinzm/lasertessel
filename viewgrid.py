import sys
import pygame
import numpy as np
import math

import trigrid as tri
from trigrid import TriTile, LAYOUT

import colors as clrs

pygame.init()
size = width, height = 640, 480
screen = pygame.display.set_mode(size)

layout = LAYOUT.copy(); layout['scale'] = 50
tiles = tri.grid_rect(10, 10)

verts = [t.world_vertices(layout) for t in tiles]
origin = [50, 50]

while True:
    # -- handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # -- draw
    screen.fill(clrs.black)

    # draw origin crosshairs
    pygame.draw.line(screen, clrs.gray, [origin[0], 0], [origin[0], height])
    pygame.draw.line(screen, clrs.gray, [0, origin[1]], [width, origin[1]])

    for i, poly in enumerate(verts):
        pygame.draw.lines(screen, clrs.maroon, True, poly+origin, 1)

    # -- flip display
    pygame.display.flip()
