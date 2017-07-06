import sys
import math
import numpy as np
import svgwrite

import trigrid as tri
import geom

DEBUG=False

layout = tri.LAYOUT.copy(); layout['scale'] = 7
tiles = tri.grid_rect(10, 10)

# -- create svg drawing
dwg = svgwrite.Drawing()
g_main = dwg.add(dwg.g())

for tile in tiles:
    verts = tile.world_vertices(layout)
    d = 'M {0[0]} {0[1]}'.format(verts[0]) # move to first vertex
    d += ' ' + ' '.join(['L {0[0]} {0[1]}'.format(p) for p in verts[1:]]) # draw lines through the rest of the points
    d += ' z' # close path
    path = g_main.add(dwg.path(d, stroke='black', stroke_width='0.5',
                               fill='white', fill_opacity=0))

    if DEBUG:
        # compute centroid
        c = np.sum(verts, axis=0)/len(verts)
        g_main.add(dwg.text('{},{},{}'.format(tile.m, tile.n, tile.s),
                        insert=c, font_size='1mm', text_anchor='middle', fill='black'))

dwg.write(open('grid.svg', 'w'))
