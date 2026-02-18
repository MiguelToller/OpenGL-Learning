import glfw

# Função Principal
def main():
    glfw.init()                                                     # Inicializa a API GLFW
    window = glfw.create_window(500, 500, '01 - Intro', None, None) # Criando a janela
    glfw.make_context_current(window)                               # Contexto OpenGL na janela

    while not glfw.window_should_close(window):                     # Enquanto a janela não é fechada
        glfw.poll_events()                                          # Tratamento de eventos  
        glfw.swap_buffers(window)                                   # Troca de frame buffers
    glfw.terminate()                                                # Finalizando a API GLFW

if __name__ == '__main__':
    main()