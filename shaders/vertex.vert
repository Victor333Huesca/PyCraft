#version 330 core

layout (location=0) in vec3 vertexPos;
layout (location=1) in vec3 vertexColor;

uniform uvec2 iResolution;
uniform float iTime;

uniform mat4 m_proj;
uniform mat4 m_view;
uniform mat4 m_model;

out vec4 fragmentColor;


void main() {
  gl_Position = m_proj * m_view * m_model * vec4(vertexPos, 1.0);
  fragmentColor = vec4(vertexColor, 1.0);
}
