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
        while not glfw.window_should_close(self._window):
            glClearColor(1, 1, 1, 1)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            glfw.swap_buffers(self._window)

            glfw.poll_events()

        glfw.destroy_window(self._window)
        glfw.terminate()

def get_window(x: int, y: int):
    global _INSTANCE
    if not _INSTANCE:
        _INSTANCE = Window(x, y)
    return _INSTANCE


