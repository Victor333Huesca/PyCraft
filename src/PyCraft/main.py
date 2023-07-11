from typing import cast
from OpenGL import GL
import sys
import glm

from PyQt6.QtGui import QKeyEvent, QMouseEvent, QSurfaceFormat, QResizeEvent, QMoveEvent
from PyQt6.QtOpenGL import QOpenGLVersionProfile
from PyQt6.QtWidgets import QApplication
from PyQt6.QtOpenGLWidgets import QOpenGLWidget
from PyQt6.QtCore import QSize, Qt

from .engine import Engine


class OpenGLWidget(QOpenGLWidget):
  def __init__(self, debug: bool = False):
    super().__init__()
    self.debug = debug

  def initializeGL(self):
    prof = QOpenGLVersionProfile()
    prof.setVersion(3, 3)
    prof.setProfile(QSurfaceFormat.OpenGLContextProfile.CoreProfile)
    # self.ctx = self.context()
    # self.fmt = self.format()
    # self.fmt.setSwapBehavior(QSurfaceFormat.SwapBehavior.DoubleBuffer)
    print(f'Open GL version: {cast(bytes, GL.glGetString(GL.GL_VERSION)).decode()}')

    # Debug
    if self.debug:
      GL.glPolygonMode(GL.GL_FRONT_AND_BACK, GL.GL_LINE)

    # Set mesh
    self.setMesh()

  def paintGL(self):
    GL.glClear(GL.GL_COLOR_BUFFER_BIT)
    self.drawMesh()

  def setMesh(self) -> None:
    raise NotImplementedError

  def drawMesh(self) -> None:
    raise NotImplementedError


class PyCraft(OpenGLWidget):
  def __init__(self, debug: bool = False):
    super().__init__(debug=debug)
    # Disable mouse
    self.center = glm.ivec2(0, 0)
    self.setMouseTracking(True)
    self.setCursor(Qt.CursorShape.BlankCursor)

    # World
    self.engine = Engine(self)
    self.engine.update.connect(self.update)

    self.setMesh = self.engine.load
    self.drawMesh = self.engine.draw

  def resizeEvent(self, event: QResizeEvent):
    super().resizeEvent(event)
    self.engine.setResolution(event.size().width(), event.size().height())

  @staticmethod
  def keyToVec(key: Qt.Key):
    return {
      Qt.Key.Key_W:      glm.vec3( 0,  0,  1),
      Qt.Key.Key_A:      glm.vec3(-1,  0,  0),
      Qt.Key.Key_S:      glm.vec3( 0,  0, -1),
      Qt.Key.Key_D:      glm.vec3( 1,  0,  0),
      Qt.Key.Key_Space:  glm.vec3( 0,  1,  0),
      Qt.Key.Key_Shift:  glm.vec3( 0, -1,  0),
    }.get(key, glm.vec3())

  def keyPressEvent(self, event: QKeyEvent):
    super().keyPressEvent(event)
    key = cast(Qt.Key, event.key())
    if key == Qt.Key.Key_F3:
      self.engine.reloadShader()
    else:
      self.engine.moveCamera(self.keyToVec(key))
      self.keyToVec(key)

  def keyReleaseEvent(self, event: QKeyEvent):
    super().keyReleaseEvent(event)
    key = cast(Qt.Key, event.key())
    self.engine.moveCamera(-self.keyToVec(key))

  def mouseMoveEvent(self, event: QMouseEvent):
    super().mouseMoveEvent(event)
    # Get movement delta, and recenter cursor
    p = glm.ivec2(event.pos().x(), event.pos().y())
    d = p - self.rcenter
    self.cursor().setPos(*self.center)
    # Inform engine
    self.engine.rotateCamera(glm.vec3(d.x, d.y, 0))

  def moveEvent(self, event: QMoveEvent):
    super().moveEvent(event)
    # Get new center and re-center the cursor
    self.rcenter = glm.ivec2(self.width(), self.height()) // 2
    self.center = glm.ivec2(self.pos().x(), self.pos().y()) + self.rcenter + glm.ivec2(0, 32) # 32 is title bar... TODO: remove this hack
    self.cursor().setPos(*self.center)



def main():
  app = QApplication(sys.argv)
  GLwindow = PyCraft(debug=False)
  GLwindow.resize(QSize(800, 800))
  GLwindow.show()
  app.exec()


if __name__ == '__main__':
  main()
