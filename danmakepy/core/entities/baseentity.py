import math

import numpy as np

class BaseEntity:

    def __init__(self, pos=None, v:float=0., angle:float=0., size:float=20.):
        self.pos = pos if pos else np.zeros(2, dtype=float)
        self.v = v
        self.angle = angle
        self.size = size

    def tick(self):
        self.pos[0] += self.v * math.cos(self.angle)
        self.pos[1] += self.v * math.sin(self.angle)
