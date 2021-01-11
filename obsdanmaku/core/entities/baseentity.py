import numpy as np

class BaseEntity:

    def __init__(self, pos=None, v:float=0., angle:float=0., size:float=20.):
        self.pos = pos if pos else np.zeros(2, dtype=float)
        self.v = v
        self.angle = angle
        self.size = size
