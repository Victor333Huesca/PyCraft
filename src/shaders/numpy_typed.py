from typing import TYPE_CHECKING, Any, Iterable, Literal, Tuple, Type, TypeVar
from typing_extensions import TypeVarTuple, Unpack
import sys
import numpy as np

# Main trickery
if TYPE_CHECKING or sys.version_info >= (3, 9):
  _Scalar = TypeVar('_Scalar', bound=np.generic, covariant=True)
  _Shape = TypeVarTuple('_Shape')
  _DType = np.dtype[_Scalar]
  NDArray = np.ndarray[Unpack[_Shape], np.dtype[_Scalar]] # type: ignore
else:
  _Scalar = TypeVar('_Scalar', bound=np.generic, covariant=True)
  _DType = _GenericAlias(np.dtype, (_Scalar,))
  NDArray = _GenericAlias(np.ndarray, (Any, _DType))

DType = TypeVar('DType', bound=np.generic)
Scalar = TypeVar('Scalar', int, float)

# Literals for easy numbers access
_0 = Literal[0]
_1 = Literal[1]
_2 = Literal[2]
_3 = Literal[3]
_4 = Literal[4]
_5 = Literal[5]
_6 = Literal[6]
_7 = Literal[7]
_8 = Literal[8]
_9 = Literal[9]



T  = TypeVar('T')
T1 = TypeVar('T1', bound=int)
T2 = TypeVar('T2', bound=int)
T3 = TypeVar('T3', bound=int)
T4 = TypeVar('T4', bound=int)


V1 = Tuple[T]
V2 = Tuple[T, T]
V3 = Tuple[T, T, T]
V4 = Tuple[T, T, T, T]
V5 = Tuple[T, T, T, T, T]
V6 = Tuple[T, T, T, T, T, T]
V7 = Tuple[T, T, T, T, T, T, T]
V8 = Tuple[T, T, T, T, T, T, T, T]
V9 = Tuple[T, T, T, T, T, T, T, T, T]
VN = Tuple[T, ...] | Iterable[T]


# ---------------------------------------------------------------------------- #
#                               Standard 1D array                              #
# ---------------------------------------------------------------------------- #

def ArrayN(data: VN[   Scalar ], dtype: Type[DType]) -> 'NDArray[Tuple[int], DType]':
  return np.array(data, dtype=dtype)


# ---------------------------------------------------------------------------- #
#                              Standards 2D array                              #
# ---------------------------------------------------------------------------- #

def ArrayNx2(data: VN[V2[Scalar]], dtype: Type[DType]) -> 'NDArray[Tuple[int, _2], DType]':
  return np.array(data, dtype=dtype)

def ArrayNx3(data: VN[V3[Scalar]], dtype: Type[DType]) -> 'NDArray[Tuple[int, _3], DType]':
  return np.array(data, dtype=dtype)

def ArrayNx4(data: VN[V4[Scalar]], dtype: Type[DType]) -> 'NDArray[Tuple[int, _4], DType]':
  return np.array(data, dtype=dtype)

def ArrayNxM(data: VN[VN[Scalar]], dtype: Type[DType]) -> 'NDArray[Tuple[int, int], DType]':
  return np.array(data, dtype=dtype)


# ---------------------------------------------------------------------------- #
#                              Standards 3D array                              #
# ---------------------------------------------------------------------------- #

def ArrayNxMx2(data: VN[VN[V2[Scalar]]], dtype: Type[DType]) -> 'NDArray[Tuple[int, int, _2], DType]':
  return np.array(data, dtype=dtype)

def ArrayNxMx3(data: VN[VN[V3[Scalar]]], dtype: Type[DType]) -> 'NDArray[Tuple[int, int, _3], DType]':
  return np.array(data, dtype=dtype)

def ArrayNxMx4(data: VN[VN[V4[Scalar]]], dtype: Type[DType]) -> 'NDArray[Tuple[int, int, _4], DType]':
  return np.array(data, dtype=dtype)

def ArrayNxMxO(data: VN[VN[VN[Scalar]]], dtype: Type[DType]) -> 'NDArray[Tuple[int, int, int], DType]':
  return np.array(data, dtype=dtype)


def test():
  ArrayN([1, 2, 3, 4, 5, 6], dtype=np.float32)
  ArrayNx2([(1, 2), (3, 4), (5, 6)], dtype=np.float32)
  ArrayNx3([(1, 2, 3), (4, 5, 6)], dtype=np.float32)
  ArrayNx4([(1, 2, 3, 4), (5, 6, 7, 8)], dtype=np.float32)
  ArrayNxM([[1, 2, 3], [4, 5], [6], [7, 8]], dtype=np.float32)
