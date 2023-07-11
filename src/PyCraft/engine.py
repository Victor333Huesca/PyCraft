from time import time
from typing import Optional as Opt
import glm

from PyQt6.QtCore import QTimer, QObject, pyqtSignal

from .settings import MOUSE_SENSITIVITY, PLAYER_SPEED
from .scene import Scene


class Engine(QObject):
  update = pyqtSignal()

  def __init__(self, parent: Opt[QObject] = None):
    super().__init__(parent)
    # World
    self.scene = Scene()
    self.camera_movement_delta = glm.vec3(0, 0, 0)
    self.camera_movement = QTimer(self)
    self.camera_movement.timeout.connect(self._moveCamera)
    self.camera_movement.start(1000 // 75)

    # Set timer for tick time update
    self._start_time = time()
    self._last_time = time()
    timer = QTimer(self)
    timer.timeout.connect(self.tick)
    timer.start(1000 // 75)

  def load(self):
    self.scene.load()

  def draw(self):
    self.scene.draw()

  def tick(self):
    t = time() - self._start_time
    delta = time() - self._last_time
    self.scene.iTime.set(t)
    self.update.emit()

  def setResolution(self, w: int, h: int):
    self.scene.iResolution.set((w, h))
    self.update.emit()

  def reloadShader(self):
    print('reloading shaders')
    self.scene.shader.load()
    self.update.emit()

  def _moveCamera(self):
    if self.camera_movement_delta == glm.vec3(0):
      return
    dtime = PLAYER_SPEED * 1000 / 75
    self.scene.camera.move(self.camera_movement_delta * dtime)
    self.scene.update()
    self.update.emit()

  def moveCamera(self, d: glm.vec3):
    self.camera_movement_delta = glm.clamp(self.camera_movement_delta + d, -1, 1)

  def rotateCamera(self, d: glm.vec3):
    self.scene.camera.rotate(d.xy * MOUSE_SENSITIVITY)
    self.scene.update()
    self.update.emit()
