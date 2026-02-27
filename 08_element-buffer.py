import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders as gls
import numpy as np
import ctypes

vertices = [
    [-0.8,-0.8, 1,0,0], # v0
    [ 0.0,-0.8, 1,0,0], # v1 - vermelho
    [ 0.0,-0.8, 0,1,0], # v2 - verde
    [ 0.0,-0.8, 1,1,0], # v3 - amarelo
    [ 0.8,-0.8, 0,1,0], # v4
    [-0.4, 0.0, 1,0,0], # v5 - vermelho
    [-0.4, 0.0, 1,0,1], # v6 - magenta
    [ 0.4, 0.0, 0,1,0], # v7 - verde
    [ 0.4, 0.0, 0,1,1], # v8 - ciano
    [ 0.0, 0.8, 0,0,1], # v9
]

faces = [
    [0,1,5], # face inferior esquerda
    [2,4,7], # face inferior direita
    [6,8,9], # face superior
    [3,8,6]  # face do meio
]

qtd_vertices = len(vertices)
qtd_faces = len(faces)
vaoId = 0
shaderId = 0

# Função para configurações iniciais da minha aplicação
def init():
    global vertices, faces, vaoId, shaderId
    glClearColor(1,1,1,1)

    vertices = np.array(vertices, dtype=np.float32) # 4 bytes ou 32 bits

    vaoId = glGenVertexArrays(1)         # Criar o VAO
    glBindVertexArray(vaoId)             # Tornando VAO ativo

    vboId = glGenBuffers(1)              # Criar o VBO         
    glBindBuffer(GL_ARRAY_BUFFER, vboId) # Tornar o VBO ativo    

    # Enviar os dados para esse VBO    
    glBufferData(GL_ARRAY_BUFFER,        # Tipo de buffer 
                 vertices.nbytes,        # Tamanho do buffer
                 vertices,               # Dados do buffer
                 GL_STATIC_DRAW)         # Uso do buffer
    
    glVertexAttribPointer(0,             # Codigo do atributo (posicao)
                          2,             # Quantidade de valores do atributo (x,y)
                          GL_FLOAT,      # Tipo dos valores do atributo
                          GL_FALSE,      # Desejo normalizar os valores
                          5*4,           # Qtd de bytes entre um atributo e o proximo   
                          ctypes.c_void_p(0))
    glVertexAttribPointer(1,             # Codigo do atributo (cor)
                          3,             # Quantidade de valores do atributo (RGB)
                          GL_FLOAT,      # Tipo dos valores do atributo
                          GL_FALSE,      # Desejo normalizar os valores
                          5*4,           # Qtd de bytes entre um atributo e o proximo   
                          ctypes.c_void_p(2*4))
    glEnableVertexAttribArray(0)         # Habilitando o atributo posicao (location = 0)
    glEnableVertexAttribArray(1)         # Habilitando o atributo cor (location = 1)

    # Criando EBO
    faces = np.array(faces, dtype=np.uint32)
    eboId = glGenBuffers(1)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER ,eboId)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER,
                 faces.nbytes,
                 faces,
                 GL_STATIC_DRAW)

    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)

    # Codigo fonte dos shaders
    with open('06_vertexShader.glsl', 'r') as file:
        vsSource = file.read()
    with open('06_fragmentShader.glsl', 'r') as file:
        fsSource = file.read()

    vsId = gls.compileShader(vsSource, GL_VERTEX_SHADER)
    fsId = gls.compileShader(fsSource, GL_FRAGMENT_SHADER)
    shaderId = gls.compileProgram(vsId, fsId)

# Função para atualizar a renderização da cena
def render():
    glClear(GL_COLOR_BUFFER_BIT)

    glUseProgram(shaderId)
    glBindVertexArray(vaoId)
    # glDrawArrays(GL_TRIANGLES, 0, qtd_vertices)
    glDrawElements(GL_TRIANGLES,    # Primitiva
                   3*qtd_faces,     # Qtd de indices
                   GL_UNSIGNED_INT, # Tipo de dados (GL_UNSIGNED_BYTE/GL_UNSIGNED_SHORT)
                   None)
    glBindVertexArray(0)
    glUseProgram(0)

# Função Principal
def main():
    glfw.init()                                                          # Inicializa a API GLFW
    window = glfw.create_window(500, 500, '08 - element-buffer', None, None)  # Criando a janela
    glfw.make_context_current(window)                                    # Contexto OpenGL na janela
    init()
    while not glfw.window_should_close(window):                          # Enquanto a janela não é fechada
        glfw.poll_events()                                               # Tratamento de eventos 
        render() 
        glfw.swap_buffers(window)                                        # Troca de frame buffers
    glfw.terminate()                                                     # Finalizando a API GLFW

if __name__ == '__main__':
    main()