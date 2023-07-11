from typing import Generic, Optional as Opt, Protocol, TypeVar

from OpenGL import GL
from OpenGL.GL.shaders import ShaderProgram
import glm
import numpy as np

from .numpy_typed import V2, V4


class glDeclareFn(Protocol):
  def __call__(self, location: int, init_value) -> None: ...


T = TypeVar('T')
class Uniform(Generic[T]):
  def __init__(self, name: str, default: T):
    self.name = name
    self.value = default
    self.shader: Opt[ShaderProgram] = None

  def attach(self, shader: ShaderProgram):
    self.shader = shader

  def set(self, value: T):
    self.value = value

  def findUniformLocation(self):
    if self.shader is None:
      raise ValueError(f'error: uniform "{self.name}" was never initialized')
    loc = GL.glGetUniformLocation(self.shader, self.name)
    if loc < 0:
      pass
      # raise ValueError(f'error ({loc}): couldn\'t find uniform "{self.name}"')
    return loc

  def update(self) -> None: ...


class Uniform2uiv(Uniform[V2[int]]):
  def update(self):
    GL.glUniform2uiv(self.findUniformLocation(), 1, np.array(self.value, dtype=np.uint32))
    # GL.glUniform2ui(self.findUniformLocation(), *self.value) # Is it converted properly ?

class Uniform1f(Uniform[float]):
  def update(self):
    GL.glUniform1f(self.findUniformLocation(), np.array((self.value,), dtype=np.float32))

class Uniform4f(Uniform[V4[float]]):
  def update(self):
    GL.glUniform2uiv(self.findUniformLocation(), 1, np.array(self.value, dtype=np.float32))
    # GL.glUniform2ui(self.findUniformLocation(), *self.value) # Is it converted properly ?

class Uniform4x4f(Uniform[glm.mat4x4]):
  def update(self):
    GL.glUniformMatrix4fv(self.findUniformLocation(), 1, False, np.array(self.value.to_list(), dtype=np.float32))
