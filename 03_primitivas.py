import glfw
from OpenGL.GL import *

vertices = [
    [-0.8,-0.4],
    [-0.8, 0.4],
    [-0.4,-0.8],
    [-0.4, 0.8],
    [ 0.4,-0.8],
    [ 0.4, 0.8],
    [ 0.8,-0.4],
    [ 0.8, 0.4],
]

# Função para configurações iniciais da minha aplicação
def init():
    glClearColor(1,1,1,1)
    glPointSize(10)
    glLineWidth(3)

# Função para atualizar a renderização da cena
def render():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1,0,0)

    glBegin(GL_POINTS)
    for v in vertices:
        glVertex2fv(v)
    glEnd()

    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    glBegin(GL_TRIANGLE_STRIP)
    for v in vertices:
        glVertex2fv(v)
    glEnd()

    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)                            # Wireframe
    glColor3f(0,0,0)
    glBegin(GL_TRIANGLE_STRIP)
    for v in vertices:
        glVertex2fv(v)
    glEnd()

# Função Principal
def main():
    glfw.init()                                                          # Inicializa a API GLFW
    window = glfw.create_window(500, 500, '03 - Primitivas', None, None) # Criando a janela
    glfw.make_context_current(window)                                    # Contexto OpenGL na janela
    init()
    while not glfw.window_should_close(window):                          # Enquanto a janela não é fechada
        glfw.poll_events()                                               # Tratamento de eventos 
        render() 
        glfw.swap_buffers(window)                                        # Troca de frame buffers
    glfw.terminate()                                                     # Finalizando a API GLFW

if __name__ == '__main__':
    main()