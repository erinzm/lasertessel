import numpy as np
from numpy import cos, sin, pi
import geom

def corner(i):
    return (cos(i*pi/3), sin(i*pi/3))

def hex():
    return np.array([corner(i) for i in range(6)])

def center(q, r):
    return np.array([3/2*q, np.sqrt(3)*(r+q/2)])

def grid_parallelo(q1, q2, r1, r2):
    return [hex()+center(q, r) for q in range(q1, q2+1) for r in range(r1, r2+1)]

def grid_tri(s):
    return [hex()+center(q, -q-r) for q in range(s) for r in range(s)]

def grid_hex(r):
    raise NotImplementedError

def grid_rect():
    raise NotImplementedError

if __name__ == '__main__':
    print(grid(3, 3))
