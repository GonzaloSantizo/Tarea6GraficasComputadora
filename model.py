from OpenGL.GL import *
import glm
from OpenGL.GL import *
from numpy import array, float32

class Model(object):
    def __init__(self, data):
        self.vertBuffer = array(data, dtype = float32)
        
        #Vertex buffer object
        self.VBO = glGenBuffers(1)

        #Vertex array object
        self.VAO = glGenVertexArrays(1)

        self.position = glm.vec3(0,0,0)
        self.rotation = glm.vec3(0,0,0)
        self.scale = glm.vec3(1,1,1)

    def getModelMatrix(self):
        identity = glm.mat4(1)

        translateMat = glm.translate(identity, self.position)

        pitch = glm.rotate(identity, glm.radians(self.rotation.x), glm.vec3(1,0,0)) #Rotation X - Pitch
        yaw = glm.rotate(identity, glm.radians(self.rotation.y), glm.vec3(0,1,0)) #Rotation Y - Yaw
        roll = glm.rotate(identity, glm.radians(self.rotation.z), glm.vec3(0,0,1)) #Rotation Z - Roll 

        rotationMat = pitch * yaw * roll

        scaleMat = glm.scale(identity, self.scale)

        return  translateMat * rotationMat * scaleMat


    def render(self):
        
        #Bind objects to the GPU
        glBindBuffer(GL_ARRAY_BUFFER, self.VBO)
        glBindVertexArray(self.VAO)

        #Especificar la informacion de vertices
        #1. BufferID
        #2. Buffer size en bytes
        #3. Buffer data
        #4. Usage
        glBufferData(GL_ARRAY_BUFFER,
                     self.vertBuffer.nbytes,
                     self.vertBuffer,
                     GL_STATIC_DRAW)
        
        #Atributos posiciones: especificar contenidos del vertice
        #1. Att number
        #2. Size
        #3. Type
        #4. Is it normalized?
        #5. Stride (deslizamiento)
        #6. Offset
        glVertexAttribPointer(0,
                              3,
                              GL_FLOAT,
                              GL_FALSE,
                              4 * 6,
                              ctypes.c_void_p(0))
        
        glEnableVertexAttribArray(0)
        

        #Atributos colores: especificar contenidos del vertice
        #1. Att number
        #2. Size
        #3. Type
        #4. Is it normalized?
        #5. Stride (deslizamiento)
        #6. Offset
        glVertexAttribPointer(1,
                              3,
                              GL_FLOAT,
                              GL_FALSE,
                              4 * 6,
                              ctypes.c_void_p(4*3))
        

        
        glEnableVertexAttribArray(1)

        glDrawArrays(GL_TRIANGLES, 0, int(len(self.vertBuffer) / 6))