import pygame
import PySimpleGUI as sg
import webbrowser

from botao import Button

pygame.init()

size = width, height = 800, 600

tela = pygame.display.set_mode(size)
pygame.display.set_caption("Smart Car")
imagem_fundo = pygame.image.load('img.png')

janela_aberta = True

texto_ip = ''
font = pygame.font.Font('freesansbold.ttf', 14)

#Definindo os botões da tela
#Button(cor, x, y, width, height, text)
cor_btn = r, g, b = 0, 255, 255
#Direcionais
btn_W = Button(cor_btn, 123, 342, 65, 65, 'W')
btn_S = Button(cor_btn, 123, 524, 65, 65, 'S')
btn_A = Button(cor_btn, 33, 433, 65, 65, 'A')
btn_D = Button(cor_btn, 215, 433, 65, 65, 'D')
#Câmera
btn_UP = Button(cor_btn, 400, 364, 65, 65, '^')
btn_DOWN = Button(cor_btn, 400, 501, 65, 65, 'v')
#Funcionalidades
btn_C = Button(cor_btn, 158, 176, 65, 65, 'C') #Connect camera
btn_P = Button(cor_btn, 427, 24, 65, 65, 'P')  #Print
btn_R = Button(cor_btn, 427, 116, 65, 65, 'R') #Record
btn_V = Button(cor_btn, 427, 206, 65, 65, 'V') #CV On-Off
btn_ESC = Button(cor_btn, 628, 428, 65, 65, 'ESC') #ESC-Sair

while janela_aberta:

    pygame.time.delay(50) #milissegundos

    for event in pygame.event.get():
        #Clicou no botão Fechar
        if event.type == pygame.QUIT:
            janela_aberta = False

        #Lê a tecla pressionada pelo usuário, mas por estar dentro do loop for, lerá apenas um único toque/clique
        #Teclado
        comandos_clique_unico = pygame.key.get_pressed()
        #Mouse
        mouse_pos = pygame.mouse.get_pos()
        #btn_esq, btn_meio, btn_dir = pygame.mouse.get_pressed()

        #Tira print
        if comandos_clique_unico[pygame.K_p] or (btn_P.isOver(mouse_pos) and event.type == pygame.MOUSEBUTTONUP):
            print("Clicou em p")

        #Grava vídeo (play/pause)
        if comandos_clique_unico[pygame.K_r] or (btn_R.isOver(mouse_pos) and event.type == pygame.MOUSEBUTTONUP):
            print("Clicou em r")

        #Ativa/desativa visão computacional
        if comandos_clique_unico[pygame.K_v] or (btn_V.isOver(mouse_pos) and event.type == pygame.MOUSEBUTTONUP):
            print("Clicou em v")
        
        #Abre navegador com a imagem da câmera
        if comandos_clique_unico[pygame.K_c] or (btn_C.isOver(mouse_pos) and event.type == pygame.MOUSEBUTTONUP):
            print("Clicou em c")
            #Captura o IP da Jetson no momento da inicialização
            ip = sg.PopupGetText('Informe o IP da Jetson para acessar sua câmera', 'IP Jetson')

            if not(ip is None) and (ip != ""):
                link_cam = 'http://{}:8000'.format(ip)
                texto_ip = 'Access cam at: {}'.format(link_cam) #Pequeno log na tela
                print("Jetson camera running on IP: {}".format(ip))

                #Delay para dar tempo de soltar o clique do mouse antes de abrir o navegador, senão entra em um loop infinito
                pygame.time.delay(1000)
                #Abre o navegador com o IP informado, desde que ele seja diferente de None/Null e não esteja vazio
                webbrowser.open(link_cam, new=0, autoraise=True)
        
        #Fecha a janela
        if comandos_clique_unico[pygame.K_ESCAPE] or (btn_ESC.isOver(mouse_pos) and event.type == pygame.MOUSEBUTTONUP):
            janela_aberta = False
            print("Clicou em ESC")


    #Lê a tecla pressionada pelo usuário e executa a ação enquanto a tecla estiver pressionada
    #Teclado
    comandos = pygame.key.get_pressed()
    #Mouse
    mouse_position = pygame.mouse.get_pos()
    btn_esq_mouse_press, btn_meio_mouse_press, btn_dir_mouse_press = pygame.mouse.get_pressed()

    #Camera para cima
    if comandos[pygame.K_UP] or (btn_UP.isOver(mouse_position) and btn_esq_mouse_press):
        print("clicou seta para cima")
        
    #Camera para baixo
    if comandos[pygame.K_DOWN] or (btn_DOWN.isOver(mouse_position) and btn_esq_mouse_press):
        print("clicou seta para baixo")
        
    #Carro para frente
    if comandos[pygame.K_w] or (btn_W.isOver(mouse_position) and btn_esq_mouse_press):
        print("clicou w (frente)")
    
    #Carro para trás
    if comandos[pygame.K_s] or (btn_S.isOver(mouse_position) and btn_esq_mouse_press):
        print("clicou s (trás)")

    #Carro para esquerda
    if comandos[pygame.K_a] or (btn_A.isOver(mouse_position) and btn_esq_mouse_press):
        print("clicou a (esquerda)")
        
    #Carro para direita
    if comandos[pygame.K_d] or (btn_D.isOver(mouse_position) and btn_esq_mouse_press):
        print("clicou d (direita)")
    
    #Carrega imagem da variável imagem_fundo na tela
    tela.blit(imagem_fundo,(0,0))

    #Pequeno log para mostrar o IP em que a câmera está rodando
    texto = font.render(texto_ip, True, (0,255,0), (0,0,128))
    text_rect = texto.get_rect() #captura a área escrita do texto
    text_rect.center = (200,270) #posiciona o centro do texto na tela
    tela.blit(texto, text_rect)  #mostra o texto

    #Desenha os botões na tela por cima da imagem carregada
    btn_W.draw(tela)
    btn_S.draw(tela)
    btn_A.draw(tela)
    btn_D.draw(tela)

    #Não são desenhados na tela, para não sobrepor os ícones, mas sua área continua ativa funcionando como botão
    '''btn_UP.draw(tela)
    btn_DOWN.draw(tela)
    btn_C.draw(tela)
    btn_P.draw(tela)
    btn_R.draw(tela)
    btn_V.draw(tela)
    btn_ESC.draw(tela)'''

    pygame.display.update()

pygame.quit()