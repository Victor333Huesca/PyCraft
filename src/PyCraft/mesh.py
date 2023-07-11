from abc import ABC
from typing import List
from OpenGL import GL
import numpy as np

from shaders.buffer import Buffer, Buffer2f, Buffer3f, BufferEl3ui
from shaders.numpy_typed import ArrayNx2, ArrayNx3

class Mesh(ABC):
  vbo: Buffer
  vbos: List[Buffer]
  ebo: Buffer

  def __init__(self):
    try:
      self.ebo
    except AttributeError as e:
      raise RuntimeError('classes inherited from Mesh should set the required attributes')

    # Set vbos
    if not hasattr(self, 'vbos'):
      try:
        self.vbos = [self.vbo]
      except AttributeError as e:
        raise RuntimeError('either vbo or vbos are needed')

  def load(self):
    # 1. Attach the Vertex Array Object
    self.vao = GL.glGenVertexArrays(1)
    GL.glBindVertexArray(self.vao)

    # 2. Copy vertices in the Vertex Buffer Object
    for i, vbo in enumerate(self.vbos):
      vbo.load()
      GL.glVertexAttribPointer(i, vbo.ndim, GL.GL_FLOAT, GL.GL_FALSE, 0, None)
      GL.glEnableVertexAttribArray(i)

    # 3. Copy indices in an element buffer object
    self.ebo.load()

  def draw(self):
    # 1. Enable the vao, draw the elements, unbind
    GL.glBindVertexArray(self.vao)
    GL.glDrawElements(GL.GL_TRIANGLES, self.ebo.data.size, GL.GL_UNSIGNED_INT, None)
    GL.glBindVertexArray(0)


class Square(Mesh):
  vbo = Buffer2f(ArrayNx2([(-1, -1), (-1, 1), (1, 1), (1, -1)], dtype=np.float32))
  ebo = BufferEl3ui(ArrayNx3([(0, 1, 2), (2, 3, 0)], dtype=np.uint32))


class ColoredSquare(Mesh):
  vbos = [ # Vertices, Colors
    Buffer2f(.9 * ArrayNx2([(-1, -1),  (-1, 1),   (1, 1),    (1, -1)],   dtype=np.float32)),
    Buffer3f(     ArrayNx3([(1, 0, 0), (0, 1, 0), (0, 1, 0), (0, 0, 1)], dtype=np.float32)),
  ]
  ebo = BufferEl3ui(ArrayNx3([(0, 1, 2), (2, 3, 0)], dtype=np.uint32))


class Cube(Mesh):
  vbo = Buffer3f(.9 * ArrayNx3([(-1, -1,  1),  (-1, 1,  1),   (1, 1,  1),    (1, -1,  1),
                                (-1, -1, -1),  (-1, 1, -1),   (1, 1, -1),    (1, -1, -1)],
                               dtype=np.float32))
  ebo = BufferEl3ui(ArrayNx3([(0, 1, 2),  (2, 3, 0),  (4, 5, 6),  (6, 7, 4),
                              (0, 4, 3),  (0, 3, 4),  (2, 6, 5),  (2, 5, 6)], dtype=np.uint32))
