import numpy as np

from .entities.baseentity import BaseEntity
from .entities.player import PlayerEntity
from .entities.bullet import BulletEntity

class Engine:

    def __init__(self):
        self.size = np.array([540, 720], dtype=float)
        self.player = PlayerEntity(v=1)
        self.entities = [self.player]
        self.tick_counter = 0

    def tick(self):
        for entity in self.entities:
            entity.tick()
        self.tick_counter += 1

