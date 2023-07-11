from typing import Generic, List, Optional as Opt, Tuple, TypeVar, cast
import numpy as np
from OpenGL import GL

from .numpy_typed import ArrayN, ArrayNx2, ArrayNx3, DType, NDArray, _2, _3
from .constant import GLC


T = TypeVar('T')

class Buffer(Generic[T, DType]):
  btype: GLC

  def __init__(self, data: 'NDArray[T, DType]'):
    if data.ndim == 1:
      self.ndim = 1
    elif data.ndim == 2:
      self.ndim = data.shape[1]
    else:
      raise ValueError('3D vector are not supported yet')
    self.data = data
    self.buffer: Opt[int] = None

  def load(self):
    self.buffer = cast(int, GL.glGenBuffers(1))
    data = self.data.flatten()
    GL.glBindBuffer(self.btype.value, self.buffer)
    GL.glBufferData(self.btype.value, data.nbytes, data, GL.GL_STATIC_DRAW)



class BufferEl1ui(Buffer[Tuple[int], np.uint32]):
  btype = GLC.GL_ELEMENT_ARRAY_BUFFER
  cst = ArrayN

class BufferEl2ui(Buffer[Tuple[int, _2], np.uint32]):
  btype = GLC.GL_ELEMENT_ARRAY_BUFFER
  cst = ArrayNx2

class BufferEl3ui(Buffer[Tuple[int, _3], np.uint32]):
  btype = GLC.GL_ELEMENT_ARRAY_BUFFER
  cst = ArrayNx3



class Buffer1f(Buffer[int, np.float32]):
  btype = GLC.GL_ARRAY_BUFFER
  cst = ArrayN

class Buffer2f(Buffer[Tuple[int, _2], np.float32]):
  btype = GLC.GL_ARRAY_BUFFER
  cst = ArrayNx2

class Buffer3f(Buffer[Tuple[int, _3], np.float32]):
  btype = GLC.GL_ARRAY_BUFFER
  cst = ArrayNx3
