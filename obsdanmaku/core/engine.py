import numpy as np

from .entities.baseentity import BaseEntity
from .entities.player import PlayerEntity
from .entities.bullet import BulletEntity

class Engine:

    def __init__(self):
        self.size = np.array([540, 720], dtype=float)
        self.player = PlayerEntity()
        self.bullets = []

    def add_bullet(self, bullet: BulletEntity):
        self.bullets.append(bullet)


