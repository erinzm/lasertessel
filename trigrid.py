import math
import numpy as np
from numpy import sqrt, pi

LAYOUT = dict(f_trans=np.array([[1,   0.5],
                                [0, sqrt(3)/2]]),
              scale=1)

class TriTile:
    def __init__(self, m, n, s):
        s=s.lower(); assert s=='l' or s=='r'
        s = 0 if s=='l' else 1

        self.coords = np.array([m, n, s])

    def __eq__(self, other):
        return np.all(self.coords == other.coords)

    def __neq__(self, other):
        return not self.__eq__(other)

    @property
    def m(self): return self.coords[0]
    @property
    def n(self): return self.coords[1]
    @property
    def s(self): return 'l' if self.coords[2] == 0 else 'r'

    def __repr__(self):
        return '<TriTile m={} n={} s={}>'.format(self.m, self.n, self.s)

    def vertices(self, layout=None):
        layout = layout or LAYOUT

        m, n = self.m, self.n; side = self.s
        return {'l': [(m, n+1), (m+1, n), (m, n)],
                'r': [(m+1, n+1), (m+1, n), (m, n+1)]}[side]

    def world_vertices(self, layout=None):
        return np.array([vert_to_world(v, layout) for v in self.vertices()])

def vert_to_world(vert, layout=None):
    layout = layout or LAYOUT # short circuit default to LAYOUT

    return (layout['f_trans'] @ vert) * layout['scale']


def faces(m, n):
    return [TriTile(m, n, 'l'), TriTile(m, n, 'r')]

def conj_s(s):
    return 'l' if s=='r' else 'r'

def grid_rect(w, h):
    tiles = []
    for i in range(h):
        # offset each row
        offs = math.ceil(i/2)
        # we should start with l on even columns and r on odd ones
        s = 'l' if i%2==0 else 'r'
        for j in range(-offs, w-offs):
            tiles.append(TriTile(j, i, s))
            if (j>-offs or i%2==0) and (i%2!=0 or j<w-offs-1):
                tiles.append(TriTile(j, i, conj_s(s)))

    return tiles
