import glfw
from OpenGL.GL import *
import numpy as np
import ctypes

vertices = [
    [-0.8,-0.8],
    [ 0.0,-0.8],
    [-0.4, 0.0],
    [ 0.0,-0.8],
    [ 0.8,-0.8],
    [ 0.4, 0.0],
    [-0.4, 0.0],
    [ 0.4, 0.0],
    [ 0.0, 0.8],
]
qtd_vertices = len(vertices)

vaoId = 0

# Função para configurações iniciais da minha aplicação
def init():
    global vertices, vaoId
    glClearColor(1,1,1,1)

    vertices = np.array(vertices, np.dtype(np.float32)) # 4 bytes ou 32 bits

    vaoId = glGenVertexArrays(1)         # Criar o VAO
    glBindVertexArray(vaoId)             # Tornando VAO ativo

    vboId = glGenBuffers(1)              # Criar o VBO         
    glBindBuffer(GL_ARRAY_BUFFER, vboId) # Tornar o VBO ativo    

    # Enviar os dados para esse VBO    
    glBufferData(GL_ARRAY_BUFFER,        # Tipo de buffer 
                 vertices.nbytes,        # Tamanho do buffer
                 vertices,               # Dados do buffer
                 GL_STATIC_DRAW)         # Uso do buffer
    
    glVertexAttribPointer(0,             # Codigo do atributo, posicao
                          2,             # Quantidade de valores do atributo (x,y)
                          GL_FLOAT,      # Tipo dos valores do atributo
                          GL_FALSE,      # Desejo normalizar os valores
                          2*4,           # Qtd de bytes entre um atributo e o proximo   
                          ctypes.c_void_p(0))
    glEnableVertexAttribArray(0)

    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)


# Função para atualizar a renderização da cena
def render():
    glClear(GL_COLOR_BUFFER_BIT)

    glBindVertexArray(vaoId)
    glDrawArrays(GL_TRIANGLES, 0, qtd_vertices)
    glBindVertexArray(0)

# Função Principal
def main():
    glfw.init()                                                          # Inicializa a API GLFW
    window = glfw.create_window(500, 500, '04 - vbo-vao', None, None)    # Criando a janela
    glfw.make_context_current(window)                                    # Contexto OpenGL na janela
    init()
    while not glfw.window_should_close(window):                          # Enquanto a janela não é fechada
        glfw.poll_events()                                               # Tratamento de eventos 
        render() 
        glfw.swap_buffers(window)                                        # Troca de frame buffers
    glfw.terminate()                                                     # Finalizando a API GLFW

if __name__ == '__main__':
    main()