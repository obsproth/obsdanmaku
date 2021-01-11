import math

from OpenGL.GL import *
import glfw

_INSTANCE = None

class Window:

    def __init__(self, x: int, y: int):
        if not glfw.init():
            raise Exception()

        window = glfw.create_window(x, y, 'obsdanmaku', None, None)
        if not window:
            glfw.terminate()
            raise Exception()

        glfw.make_context_current(window)

        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 4)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 0)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

        self._window = window

    def start(self):
        t = 0
        while not glfw.window_should_close(self._window):
            glClearColor(1, 1, 1, 1)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            tt = t*2*math.pi / 60 / 60
            td = 2*math.pi/3
            glBegin(GL_TRIANGLES)
            glColor3d(1, 0, 0)
            glVertex2d(math.cos(tt), math.sin(tt))
            glColor3d(0, 1, 0)
            glVertex2d(math.cos(tt+td), math.sin(tt+td))
            glColor3d(0, 0, 1)
            glVertex2d(math.cos(tt+td*2), math.sin(tt+td*2))
            glEnd()

            glfw.swap_buffers(self._window)

            glfw.poll_events()
            t += 1

        glfw.destroy_window(self._window)
        glfw.terminate()

def get_window(x: int, y: int):
    global _INSTANCE
    if not _INSTANCE:
        _INSTANCE = Window(x, y)
    return _INSTANCE


