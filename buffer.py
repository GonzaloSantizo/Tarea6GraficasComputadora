from OpenGL.GL import *
from numpy import array, float32

class Buffer(object):
    def __init__(self, data):
        self.vertBuffer = array(data, dtype = float32)
        
        #Vertex buffer object
        self.VBO = glGenBuffers(1)

        #Vertex array object
        self.VAO = glGenVertexArrays(1)

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
        
        #Atributos: especificar contenidos del vertice
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
                              4 * 3,
                              ctypes.c_void_p(0))
        
        glEnableVertexAttribArray(0)

        glDrawArrays(GL_TRIANGLES, 0, int(len(self.vertBuffer / 3)))