'''
Wrapper around OpenGL constants to allow to use them as literal
'''
from enum import Enum
from OpenGL import GL

class GLC(Enum):
    '''OpenGL Constants'''

    '''OpenGL 1.5 Constants'''
    GL_ARRAY_BUFFER                          = GL.GL_ARRAY_BUFFER
    GL_ARRAY_BUFFER_BINDING                  = GL.GL_ARRAY_BUFFER_BINDING
    GL_BUFFER_ACCESS                         = GL.GL_BUFFER_ACCESS
    GL_BUFFER_MAPPED                         = GL.GL_BUFFER_MAPPED
    GL_BUFFER_MAP_POINTER                    = GL.GL_BUFFER_MAP_POINTER
    GL_BUFFER_SIZE                           = GL.GL_BUFFER_SIZE
    GL_BUFFER_USAGE                          = GL.GL_BUFFER_USAGE
    GL_COLOR_ARRAY_BUFFER_BINDING            = GL.GL_COLOR_ARRAY_BUFFER_BINDING
    GL_CURRENT_FOG_COORD                     = GL.GL_CURRENT_FOG_COORD
    GL_CURRENT_QUERY                         = GL.GL_CURRENT_QUERY
    GL_DYNAMIC_COPY                          = GL.GL_DYNAMIC_COPY
    GL_DYNAMIC_DRAW                          = GL.GL_DYNAMIC_DRAW
    GL_DYNAMIC_READ                          = GL.GL_DYNAMIC_READ
    GL_EDGE_FLAG_ARRAY_BUFFER_BINDING        = GL.GL_EDGE_FLAG_ARRAY_BUFFER_BINDING
    GL_ELEMENT_ARRAY_BUFFER                  = GL.GL_ELEMENT_ARRAY_BUFFER
    GL_FOG_COORD                             = GL.GL_FOG_COORD
    GL_ELEMENT_ARRAY_BUFFER_BINDING          = GL.GL_ELEMENT_ARRAY_BUFFER_BINDING
    GL_FOG_COORDINATE_ARRAY_BUFFER_BINDING   = GL.GL_FOG_COORDINATE_ARRAY_BUFFER_BINDING
    GL_FOG_COORD_ARRAY                       = GL.GL_FOG_COORD_ARRAY
    GL_FOG_COORD_ARRAY_BUFFER_BINDING        = GL.GL_FOG_COORD_ARRAY_BUFFER_BINDING
    GL_FOG_COORD_ARRAY_POINTER               = GL.GL_FOG_COORD_ARRAY_POINTER
    GL_FOG_COORD_ARRAY_STRIDE                = GL.GL_FOG_COORD_ARRAY_STRIDE
    GL_FOG_COORD_ARRAY_TYPE                  = GL.GL_FOG_COORD_ARRAY_TYPE
    GL_FOG_COORD_SRC                         = GL.GL_FOG_COORD_SRC
    GL_INDEX_ARRAY_BUFFER_BINDING            = GL.GL_INDEX_ARRAY_BUFFER_BINDING
    GL_NORMAL_ARRAY_BUFFER_BINDING           = GL.GL_NORMAL_ARRAY_BUFFER_BINDING
    GL_QUERY_COUNTER_BITS                    = GL.GL_QUERY_COUNTER_BITS
    GL_QUERY_RESULT                          = GL.GL_QUERY_RESULT
    GL_QUERY_RESULT_AVAILABLE                = GL.GL_QUERY_RESULT_AVAILABLE
    GL_READ_ONLY                             = GL.GL_READ_ONLY
    GL_READ_WRITE                            = GL.GL_READ_WRITE
    GL_SAMPLES_PASSED                        = GL.GL_SAMPLES_PASSED
    GL_SECONDARY_COLOR_ARRAY_BUFFER_BINDING  = GL.GL_SECONDARY_COLOR_ARRAY_BUFFER_BINDING
    GL_SRC0_ALPHA                            = GL.GL_SRC0_ALPHA
    GL_SRC0_RGB                              = GL.GL_SRC0_RGB
    GL_SRC1_ALPHA                            = GL.GL_SRC1_ALPHA
    GL_SRC1_RGB                              = GL.GL_SRC1_RGB
    GL_SRC2_ALPHA                            = GL.GL_SRC2_ALPHA
    GL_SRC2_RGB                              = GL.GL_SRC2_RGB
    GL_STATIC_COPY                           = GL.GL_STATIC_COPY
    GL_STATIC_DRAW                           = GL.GL_STATIC_DRAW
    GL_STATIC_READ                           = GL.GL_STATIC_READ
    GL_STREAM_COPY                           = GL.GL_STREAM_COPY
    GL_STREAM_DRAW                           = GL.GL_STREAM_DRAW
    GL_STREAM_READ                           = GL.GL_STREAM_READ
    GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING    = GL.GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING
    GL_VERTEX_ARRAY_BUFFER_BINDING           = GL.GL_VERTEX_ARRAY_BUFFER_BINDING
    GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING    = GL.GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING
    GL_WEIGHT_ARRAY_BUFFER_BINDING           = GL.GL_WEIGHT_ARRAY_BUFFER_BINDING
    GL_WRITE_ONLY                            = GL.GL_WRITE_ONLY

    '''OpenGL 2.0 Constants'''
    GL_ACTIVE_ATTRIBUTES                     = GL.GL_ACTIVE_ATTRIBUTES
    GL_ACTIVE_ATTRIBUTE_MAX_LENGTH           = GL.GL_ACTIVE_ATTRIBUTE_MAX_LENGTH
    GL_ACTIVE_UNIFORMS                       = GL.GL_ACTIVE_UNIFORMS
    GL_ACTIVE_UNIFORM_MAX_LENGTH             = GL.GL_ACTIVE_UNIFORM_MAX_LENGTH
    GL_ATTACHED_SHADERS                      = GL.GL_ATTACHED_SHADERS
    GL_BLEND_EQUATION_ALPHA                  = GL.GL_BLEND_EQUATION_ALPHA
    GL_BLEND_EQUATION_RGB                    = GL.GL_BLEND_EQUATION_RGB
    GL_BOOL                                  = GL.GL_BOOL
    GL_BOOL_VEC2                             = GL.GL_BOOL_VEC2
    GL_BOOL_VEC3                             = GL.GL_BOOL_VEC3
    GL_BOOL_VEC4                             = GL.GL_BOOL_VEC4
    GL_COMPILE_STATUS                        = GL.GL_COMPILE_STATUS
    GL_COORD_REPLACE                         = GL.GL_COORD_REPLACE
    GL_CURRENT_PROGRAM                       = GL.GL_CURRENT_PROGRAM
    GL_CURRENT_VERTEX_ATTRIB                 = GL.GL_CURRENT_VERTEX_ATTRIB
    GL_DELETE_STATUS                         = GL.GL_DELETE_STATUS
    GL_DRAW_BUFFER0                          = GL.GL_DRAW_BUFFER0
    GL_DRAW_BUFFER1                          = GL.GL_DRAW_BUFFER1
    GL_DRAW_BUFFER10                         = GL.GL_DRAW_BUFFER10
    GL_DRAW_BUFFER11                         = GL.GL_DRAW_BUFFER11
    GL_DRAW_BUFFER12                         = GL.GL_DRAW_BUFFER12
    GL_DRAW_BUFFER13                         = GL.GL_DRAW_BUFFER13
    GL_DRAW_BUFFER14                         = GL.GL_DRAW_BUFFER14
    GL_DRAW_BUFFER15                         = GL.GL_DRAW_BUFFER15
    GL_DRAW_BUFFER2                          = GL.GL_DRAW_BUFFER2
    GL_DRAW_BUFFER3                          = GL.GL_DRAW_BUFFER3
    GL_DRAW_BUFFER4                          = GL.GL_DRAW_BUFFER4
    GL_DRAW_BUFFER5                          = GL.GL_DRAW_BUFFER5
    GL_DRAW_BUFFER6                          = GL.GL_DRAW_BUFFER6
    GL_DRAW_BUFFER7                          = GL.GL_DRAW_BUFFER7
    GL_DRAW_BUFFER8                          = GL.GL_DRAW_BUFFER8
    GL_DRAW_BUFFER9                          = GL.GL_DRAW_BUFFER9
    GL_FLOAT_MAT2                            = GL.GL_FLOAT_MAT2
    GL_FLOAT_MAT3                            = GL.GL_FLOAT_MAT3
    GL_FLOAT_MAT4                            = GL.GL_FLOAT_MAT4
    GL_FLOAT_VEC2                            = GL.GL_FLOAT_VEC2
    GL_FLOAT_VEC3                            = GL.GL_FLOAT_VEC3
    GL_FLOAT_VEC4                            = GL.GL_FLOAT_VEC4
    GL_FRAGMENT_SHADER                       = GL.GL_FRAGMENT_SHADER
    GL_FRAGMENT_SHADER_DERIVATIVE_HINT       = GL.GL_FRAGMENT_SHADER_DERIVATIVE_HINT
    GL_INFO_LOG_LENGTH                       = GL.GL_INFO_LOG_LENGTH
    GL_INT_VEC2                              = GL.GL_INT_VEC2
    GL_INT_VEC3                              = GL.GL_INT_VEC3
    GL_INT_VEC4                              = GL.GL_INT_VEC4
    GL_LINK_STATUS                           = GL.GL_LINK_STATUS
    GL_LOWER_LEFT                            = GL.GL_LOWER_LEFT
    GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS      = GL.GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS
    GL_MAX_DRAW_BUFFERS                      = GL.GL_MAX_DRAW_BUFFERS
    GL_MAX_FRAGMENT_UNIFORM_COMPONENTS       = GL.GL_MAX_FRAGMENT_UNIFORM_COMPONENTS
    GL_MAX_TEXTURE_COORDS                    = GL.GL_MAX_TEXTURE_COORDS
    GL_MAX_TEXTURE_IMAGE_UNITS               = GL.GL_MAX_TEXTURE_IMAGE_UNITS
    GL_MAX_VARYING_FLOATS                    = GL.GL_MAX_VARYING_FLOATS
    GL_MAX_VERTEX_ATTRIBS                    = GL.GL_MAX_VERTEX_ATTRIBS
    GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS        = GL.GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS
    GL_MAX_VERTEX_UNIFORM_COMPONENTS         = GL.GL_MAX_VERTEX_UNIFORM_COMPONENTS
    GL_POINT_SPRITE                          = GL.GL_POINT_SPRITE
    GL_POINT_SPRITE_COORD_ORIGIN             = GL.GL_POINT_SPRITE_COORD_ORIGIN
    GL_SAMPLER_1D                            = GL.GL_SAMPLER_1D
    GL_SAMPLER_1D_SHADOW                     = GL.GL_SAMPLER_1D_SHADOW
    GL_SAMPLER_2D                            = GL.GL_SAMPLER_2D
    GL_SAMPLER_2D_SHADOW                     = GL.GL_SAMPLER_2D_SHADOW
    GL_SAMPLER_3D                            = GL.GL_SAMPLER_3D
    GL_SAMPLER_CUBE                          = GL.GL_SAMPLER_CUBE
    GL_SHADER_SOURCE_LENGTH                  = GL.GL_SHADER_SOURCE_LENGTH
    GL_SHADER_TYPE                           = GL.GL_SHADER_TYPE
    GL_SHADING_LANGUAGE_VERSION              = GL.GL_SHADING_LANGUAGE_VERSION
    GL_STENCIL_BACK_FAIL                     = GL.GL_STENCIL_BACK_FAIL
    GL_STENCIL_BACK_FUNC                     = GL.GL_STENCIL_BACK_FUNC
    GL_STENCIL_BACK_PASS_DEPTH_FAIL          = GL.GL_STENCIL_BACK_PASS_DEPTH_FAIL
    GL_STENCIL_BACK_PASS_DEPTH_PASS          = GL.GL_STENCIL_BACK_PASS_DEPTH_PASS
    GL_STENCIL_BACK_REF                      = GL.GL_STENCIL_BACK_REF
    GL_STENCIL_BACK_VALUE_MASK               = GL.GL_STENCIL_BACK_VALUE_MASK
    GL_STENCIL_BACK_WRITEMASK                = GL.GL_STENCIL_BACK_WRITEMASK
    GL_UPPER_LEFT                            = GL.GL_UPPER_LEFT
    GL_VALIDATE_STATUS                       = GL.GL_VALIDATE_STATUS
    GL_VERTEX_ATTRIB_ARRAY_ENABLED           = GL.GL_VERTEX_ATTRIB_ARRAY_ENABLED
    GL_VERTEX_ATTRIB_ARRAY_NORMALIZED        = GL.GL_VERTEX_ATTRIB_ARRAY_NORMALIZED
    GL_VERTEX_ATTRIB_ARRAY_POINTER           = GL.GL_VERTEX_ATTRIB_ARRAY_POINTER
    GL_VERTEX_ATTRIB_ARRAY_SIZE              = GL.GL_VERTEX_ATTRIB_ARRAY_SIZE
    GL_VERTEX_ATTRIB_ARRAY_STRIDE            = GL.GL_VERTEX_ATTRIB_ARRAY_STRIDE
    GL_VERTEX_ATTRIB_ARRAY_TYPE              = GL.GL_VERTEX_ATTRIB_ARRAY_TYPE
    GL_VERTEX_PROGRAM_POINT_SIZE             = GL.GL_VERTEX_PROGRAM_POINT_SIZE
    GL_VERTEX_PROGRAM_TWO_SIDE               = GL.GL_VERTEX_PROGRAM_TWO_SIDE
    GL_VERTEX_SHADER                         = GL.GL_VERTEX_SHADER
