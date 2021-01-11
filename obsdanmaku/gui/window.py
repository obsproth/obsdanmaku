import math

import glfw
import numpy as np
from OpenGL.GL import *

from ..core.engine import Engine
from ..core.entities.baseentity import BaseEntity

_INSTANCE = None

class Window:

    def __init__(self, window_size: np.ndarray, engine: Engine):
        # create window
        if not glfw.init():
            raise Exception()

        window = glfw.create_window(*window_size, 'obsdanmaku', None, None)
        if not window:
            glfw.terminate()
            raise Exception()

        glfw.make_context_current(window)

        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 4)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 0)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

        self._window = window
        #
        self.window_size = window_size
        self.engine = engine

    def start(self):
        t = 0
        while not glfw.window_should_close(self._window):
            glClearColor(1, 1, 1, 1)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            self._render_all()

            glfw.swap_buffers(self._window)

            glfw.poll_events()
            t += 1

        glfw.destroy_window(self._window)
        glfw.terminate()

    def _render_all(self):
        self._render_entity(self.engine.player)
        for bullet in self.engine.bullets:
            self._render_entity(bullet)

    def _render_entity(self, entity: BaseEntity):
        center_pos = entity.pos
        glBegin(GL_TRIANGLES)
        glColor3d(1, 0, 0)
        glVertex2d(*self._convert_to_gl_pos(center_pos + entity.size*np.array((math.cos(0), math.sin(0)), dtype=float)))
        glColor3d(0, 1, 0)
        glVertex2d(*self._convert_to_gl_pos(center_pos + entity.size*np.array((math.cos(2*math.pi/3), math.sin(2*math.pi/3)), dtype=float)))
        glColor3d(0, 0, 1)
        glVertex2d(*self._convert_to_gl_pos(center_pos + entity.size*np.array((math.cos(2*math.pi/3*2), math.sin(2*math.pi/3*2)), dtype=float)))
        glEnd()

    def _convert_to_gl_pos(self, pos: np.ndarray):
        return pos / (self.window_size / 2)


def get_window(x: int, y: int, engine: Engine):
    global _INSTANCE
    if not _INSTANCE:
        _INSTANCE = Window(np.array((x, y), dtype=int), engine)
    return _INSTANCE


