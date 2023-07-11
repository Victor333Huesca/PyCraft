from pathlib import Path

from shaders import ShaderPipeline
from shaders.uniform import Uniform1f, Uniform2uiv, Uniform4x4f
from .settings import PLAYER_POS
from .camera import Camera
from .mesh import ColoredSquare


SHADERS_PATH = Path(__file__).parents[2] / 'shaders'
VERTEX_SHADER   = SHADERS_PATH / 'vertex.vert'
FRAGMENT_SHADER = SHADERS_PATH / 'fragment.frag'


class Scene:
  def __init__(self):
    self.shader = ShaderPipeline(vertex=VERTEX_SHADER, fragment=FRAGMENT_SHADER)
    self.mesh   = ColoredSquare()
    self.camera = Camera(pos=PLAYER_POS, yaw=-90, pitch=0)

    # Uniforms
    self.iResolution = self.shader.addUniform(Uniform2uiv('iResolution', (0, 0)))
    self.iTime       = self.shader.addUniform(Uniform1f('iTime', 0))
    self.m_proj      = self.shader.addUniform(Uniform4x4f('m_proj',  self.camera.m_proj))
    self.m_model     = self.shader.addUniform(Uniform4x4f('m_model', self.camera.m_model))
    self.m_view      = self.shader.addUniform(Uniform4x4f('m_view',  self.camera.m_view))

  def load(self):
    self.shader.load()
    self.mesh.load()

  def update(self):
    self.camera.update()
    self.m_view.set(self.camera.m_view)

  def draw(self):
    self.shader.draw()
    self.mesh.draw()
