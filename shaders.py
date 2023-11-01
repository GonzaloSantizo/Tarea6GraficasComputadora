vertex_shader = '''
#version 450 core

layout (location = 0 ) in vec3 position;
layout (location = 1 ) in vec3 inColor;
layout (location = 2 ) in vec2 texCoords;



uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

uniform float time;


out vec4 outColor;
out vec2 UVs;

void main()
{
    vec4 newPos = vec4(position.x, position.y + sin(time), position.z, 1);
    
    gl_Position = projectionMatrix * viewMatrix * modelMatrix * newPos;
    outColor = vec4(inColor, 1.0);
    UVs = texCoords;

}


'''

fragmet_shader = '''
#version 450 core


layout (binding  = 0) uniform sampler2D tex;


in vec4 outColor;
in vec2 UVs;


out vec4 fragColor;

void main()
{
    fragColor = texture(tex, UVs);
}


'''