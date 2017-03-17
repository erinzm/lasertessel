import numpy as np

def translate(point, v):
    return np.array(point) + np.array(v)

def scale(point, s):
    return np.array(point) * s
