from typing import Any, List, Literal, Optional as Opt, TypeVar, cast
from pathlib import Path
from colorama import Fore, Style
import re

from OpenGL import GL
from OpenGL.GL.shaders import compileProgram as _compileProgram, compileShader as _compileShader, ShaderProgram, ShaderCompilationError as _ShaderCompilationError


from .uniform import Uniform
from .constant import GLC

def colored(color: str, text: str):
  return color + text + Style.RESET_ALL


class ShaderCompilationError(RuntimeError):
  def __init__(self, summary: str, errors: List[str], file: Opt[Path] = None, *args: Any, ) -> None:
    super().__init__(*args)
    self.file = file
    self.summary =  summary
    self.errors = errors

  def fmt_error(self, err: str):
    line_header, errno_header, msg = (s.strip() for s in err.split(':', 2))
    if m := re.match(r'([0-9]+)\(([0-9]+)\)', line_header):
      shader_id, line = m.groups()
    else:
      shader_id, line = '?', '?'
    err_type, errno = errno_header.split(' ')
    err_color = {
      'error':   Fore.RED,
      'warning': Fore.YELLOW,
    }.get(err_type, '')
    if self.file:
      return colored(err_color, err_type + ' ' + errno + ':') + ' File ' + colored(Style.DIM, '"' + str(self.file) + '", line ' + line) + ': ' + msg
    else:
      return colored(err_color, err_type + ' ' + errno + ':') + ' line ' + line + ': ' + msg

  def __str__(self):
    return self.summary + '\n' + '\n'.join(self.fmt_error(err) for err in self.errors)

  def __repr__(self):
    return str(self)


def compileShader(src_or_path: str | Path, shader_type: Literal[GLC.GL_VERTEX_SHADER, GLC.GL_FRAGMENT_SHADER]):
  # Get source code
  if isinstance(src_or_path, Path):
    src = src_or_path.read_text()
  elif isinstance(src_or_path, str):
    src = src_or_path
  else:
    raise TypeError(f'shader type must be source code (str) or a path the source (Path), received {type(src_or_path)}')

  # Compile
  try:
    shader = _compileShader(src, shader_type.value)
  except _ShaderCompilationError as e:
    err, source, shader_t = cast(tuple[str, list[bytes], GLC], e.args)
    err_t, err_msg = err.split(': ', 1)
    errors = cast(bytes, eval(err_msg)).decode().splitlines()
    raise ShaderCompilationError(err_t, errors, isinstance(src_or_path, Path) and src_or_path or None) from e

  return shader


def compileShaderProgram(*, vertex: str | Path, fragment: str | Path):
  shaders = [compileShader(vertex,   GLC.GL_VERTEX_SHADER),
             compileShader(fragment, GLC.GL_FRAGMENT_SHADER)]
  program = _compileProgram(*shaders)
  return program



T = TypeVar('T')
class ShaderPipeline:
  def __init__(self, *, vertex: str | Path, fragment: str | Path):
    self.vertex = vertex
    self.fragment = fragment
    self.uniforms = set[Uniform]()
    self.program: Opt[ShaderProgram] = None
    # self.program: ShaderProgram # compiled on flight

  def addUniform(self, uniform: Uniform[T]) -> Uniform[T]:
    self.uniforms.add(uniform)
    return uniform

  def compile(self):
    self.program = compileShaderProgram(vertex=self.vertex, fragment=self.fragment)
    GL.glUseProgram(self.program)

  def load(self):
    # Compile and use shader
    self.compile()
    # TODO: find a type-guard thing to make so that .compile() ensure the program is not None
    assert self.program

    # Attach shaders
    for uniform in self.uniforms:
      uniform.attach(self.program)

  def draw(self):
    # Use shader and vao
    GL.glUseProgram(self.program)

    # Update uniforms
    for uniform in self.uniforms:
      uniform.update()
