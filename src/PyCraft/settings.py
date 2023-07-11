import glm

# TODO: on resolution change
RESOLUTION = glm.vec2(800, 800)
ASPECT_RATIO = RESOLUTION.x / RESOLUTION.y

FOV_DEG = 50
_FOV_V = glm.radians(FOV_DEG)
_FOV_H = 2 * glm.atan(glm.tan(_FOV_V / 2) * ASPECT_RATIO)
FOV = glm.vec2(_FOV_H, _FOV_V)
NEAR = .1
FAR = 2000

PITCH_MAX = glm.radians(89)


PLAYER_SPEED = .005
PLAYER_ROT_SPEED = .003
PLAYER_POS = glm.vec3(0, 0, 1)
MOUSE_SENSITIVITY = .002