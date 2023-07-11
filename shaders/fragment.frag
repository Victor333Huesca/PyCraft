#version 330 core

uniform uvec2 iResolution;
uniform float iTime;

in  vec4 fragmentColor;
out vec4 finalColor;


void main() {
  finalColor = vec4(fragmentColor);
}
