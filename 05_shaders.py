import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders as gls
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
shaderId = 0

# Função para configurações iniciais da minha aplicação
def init():
    global vertices, vaoId, shaderId
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

    # Codigo fonte dos shaders
    with open('06_vertexShader.glsl', 'r') as file:
        vsSource = file.read()
    with open('06_fragmentShader.glsl', 'r') as file:
        fsSource = file.read()

    vsId = gls.compileShader(vsSource, GL_VERTEX_SHADER)
    fsId = gls.compileShader(fsSource, GL_FRAGMENT_SHADER)
    shaderId = gls.compileProgram(vsId, fsId)

    # vsId = glCreateShader(GL_VERTEX_SHADER)         # Criar o objeto vertex shader
    # glShaderSource(vsId, vsSource)                  # Enviar o codigo-fonte do vertex shader para esse objeto
    # glCompileShader(vsId)                           # Compilar o vertex shader
    # if not glGetShaderiv(vsId, GL_COMPILE_STATUS):  # Verificar por erros no vertex shader
    #     info = glGetShaderInfoLog(vsId)
    #     print('Erro de compilacao no vertex shader... \n', info)

    # fsId = glCreateShader(GL_FRAGMENT_SHADER)       # Criar o objeto vertex shader
    # glShaderSource(fsId, fsSource)                  # Enviar o codigo-fonte do vertex shader para esse objeto
    # glCompileShader(fsId)                           # Compilar o vertex shader
    # if not glGetShaderiv(fsId, GL_COMPILE_STATUS):  # Verificar por erros no vertex shader
    #     info = glGetShaderInfoLog(fsId)
    #     print('Erro de compilacao no fragment shader... \n', info)

    # shaderId = glCreateProgram()    # Criar um shader program
    # glAttachShader(shaderId, vsId)
    # glAttachShader(shaderId, fsId)
    # glLinkProgram(shaderId)

# Função para atualizar a renderização da cena
def render():
    glClear(GL_COLOR_BUFFER_BIT)

    glUseProgram(shaderId)
    glBindVertexArray(vaoId)
    glDrawArrays(GL_TRIANGLES, 0, qtd_vertices)
    glBindVertexArray(0)
    glUseProgram(0)

# Função Principal
def main():
    glfw.init()                                                          # Inicializa a API GLFW
    window = glfw.create_window(500, 500, '05 - shaders', None, None)    # Criando a janela
    glfw.make_context_current(window)                                    # Contexto OpenGL na janela
    init()
    while not glfw.window_should_close(window):                          # Enquanto a janela não é fechada
        glfw.poll_events()                                               # Tratamento de eventos 
        render() 
        glfw.swap_buffers(window)                                        # Troca de frame buffers
    glfw.terminate()                                                     # Finalizando a API GLFW

if __name__ == '__main__':
    main()