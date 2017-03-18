import math
import numpy as np
from numpy import cos, sin, pi, sqrt


LAYOUT_POINTY = dict(f_trans=np.array([[sqrt(3), sqrt(3)/2.0],
                                        [0, 3.0/2.0]]),
                     theta_0=pi/6, scale=1)
LAYOUT_FLAT = dict(f_trans=np.array([[3.0/2.0, 0],
                                      [sqrt(3)/2.0, sqrt(3)]]),
                   theta_0=0, scale=1)

class Hex(object):
    """A wrapper object for cube-space hex grids."""

    def __init__(self, q, r, s=None):
        s = -q-r if s==None else s
        self.coords = np.array([q, r, s])
        assert np.sum(self.coords) == 0 # cubic coords should sum to zero

    def __eq__(self, other):
        return np.all(self.coords == other.coords)

    def __neq__(self, other):
        return not self.__eq__(other)

    @property
    def q(self): return self.coords[0]
    @property
    def r(self): return self.coords[1]
    @property
    def s(self): return self.coords[2]

    def to_pixel(self, layout=None):
        return (layout['f_trans'] @ self.coords[0:2]) * layout['scale']

    def corner_offset(self, i, layout=None):
        angle = i*pi/3 + layout['theta_0']
        return np.array([cos(angle), sin(angle)]) * layout['scale']

    def corners(self, layout=None):
        center = self.to_pixel(layout)
        return np.array([center+self.corner_offset(i, layout) for i in range(6)])

def grid_rhomboid(q1, q2, r1, r2):
    return [Hex(q, r) for q in range(q1, q2+1) for r in range(r1, r2+1)]

def grid_triangular(s):
    return [Hex(q, r) for q in range(0, s+1) for r in range(s-q, s+1)]

def grid_rectangular(h, w):
    hexes = []
    for r in range(0, h):
        r_offset = math.floor(r/2)
        for q in range(-r_offset, w - r_offset):
            hexes.append(Hex(q, r))
    return hexes
