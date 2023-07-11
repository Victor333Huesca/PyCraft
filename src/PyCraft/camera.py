from typing import ClassVar, cast
import glm

from .settings import ASPECT_RATIO, FAR, FOV, NEAR, PITCH_MAX


class Camera:
  # Vectors
  WORLD_UP: ClassVar = glm.vec3(0, 1, 0)
  WORLD_RIGHT: ClassVar = glm.vec3(1, 0, 0)
  WORLD_FORWARD: ClassVar = glm.vec3(0, 0, 1)

  def __init__(self, pos: glm.vec3, yaw: float, pitch: float):
    # "Points"
    self.pos = pos

    # Scalars
    self.yaw = glm.radians(yaw)
    self.pitch = glm.radians(pitch)

    # Vectors
    self.up = self.WORLD_UP
    self.right = self.WORLD_RIGHT
    self.forward = self.WORLD_FORWARD

    # Matrices
    self.m_proj  = glm.perspective(FOV.y, ASPECT_RATIO, NEAR, FAR)
    self.m_view  = glm.mat4x4()
    self.m_model = glm.mat4x4()

    self.update()

  def update(self):
    self.forward = glm.normalize(glm.vec3(
      x = glm.cos(self.pitch) * glm.cos(self.yaw),
      y = glm.sin(self.pitch),
      z = glm.cos(self.pitch) * glm.sin(self.yaw)
    ))
    self.right  = glm.normalize(glm.cross(self.forward, self.WORLD_UP))
    self.up     = glm.normalize(glm.cross(self.right, self.forward))
    self.m_view = glm.lookAt(self.pos, self.pos + self.forward, self.up)

  def rotate(self, d: glm.vec2):
    self.pitch = cast(float, glm.clamp(self.pitch - d.y, -PITCH_MAX, PITCH_MAX))
    self.yaw += d.x

  def rotate_pitch(self, dy: float):
    self.pitch = cast(float, glm.clamp(self.pitch - dy, -PITCH_MAX, PITCH_MAX))

  def rotate_yaw(self, dx: float):
    self.yaw += dx

  def move(self, d: glm.vec3) -> None:
    # Can probably be one lined with matmul / dot prod
    self.pos += d.x * self.right
    self.pos += d.y * self.up
    self.pos += d.z * self.forward

  def move_left(self, d: float):
    self.pos -= d * self.right

  def move_right(self, d: float):
    self.pos += d * self.right

  def move_backward(self, d: float):
    self.pos -= d * self.forward

  def move_forward(self, d: float):
    self.pos += d * self.forward

  def move_down(self, d: float):
    self.pos -= d * self.up

  def move_up(self, d: float):
    self.pos += d * self.up
