import pygame
import time
pygame.init()

L=512
A=320
ventana=pygame.display.set_mode((L,A))
correr=True


van_h=pygame.image.load('imagenes_juego/image.png')
van_pos_L=0
van_pos_A=0


jump=pygame.image.load('imagenes_juego/JUMP (3).png')
jump_pos_L=L//2-(jump.get_size()[0]//2)
jump_pos_A=A//2-(jump.get_size()[1]//2)

space=pygame.image.load('imagenes_juego/SPACE (3).png')
space_pos_L=L//2-(space.get_size()[0]//2)
space_pos_A=A//2-(space.get_size()[1]//2)+63


ladrillos=pygame.image.load('imagenes_juego/ladrillos (1).png')

ladrillos_ini_L =200 
ladrillos_ini_A =130 


condicion="off"
conteo=0

def fondo(x,y):
    ventana.blit(van_h,(x,y))

def letra (x,y):
    ventana.blit(jump,(x,y))

def mostrar_instrucciones(x,y):
    ventana.blit(space, (x,y))


#Diseño de ventana
fondo_juego = pygame.image.load("imagenes_juego/fondo_jump (1).png")
pygame.display.set_caption("Mario_Bros")

jugador = pygame.image.load("imagenes_juego/mario_parado(1).jpg")

#Configuraciones personajes
jugador_ini_L =0 
jugador_ini_A =170 

#Movimientos
tasa_cambio_L = 0
tasa_cambio_A = 0
move = 0
saltar = False
altura_salto = 10
clock = pygame.time.Clock()
antilag = 0






while correr:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            correr = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador = pygame.image.load("imagenes_juego/mario_correr.gif")
                tasa_cambio_L = tasa_cambio_L - 3

            if evento.key == pygame.K_RIGHT:
                jugador = pygame.image.load("imagenes_juego/mario_correr.gif")
                tasa_cambio_L = tasa_cambio_L + 3
            if evento.key==pygame.K_SPACE:
                condicion="on"
                L=1900
                A=245
                ventana=pygame.display.set_mode((L,A))
            if evento.key == pygame.K_UP:
                saltar = True

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT:
                jugador = pygame.image.load("imagenes_juego/mario1 (1).jpg")
                tasa_cambio_L = 0
            if evento.key == pygame.K_RIGHT:
                tasa_cambio_L = 0
                jugador = pygame.image.load("imagenes_juego/mario1 (1).jpg")
            if evento.key == pygame.K_SPACE and saltar == False:
                saltar == True

    if saltar == True:
        if altura_salto >= -10:
            dirije = 0.5
            if altura_salto < 0:
                time.sleep(0.020)
                dirije = -0.5
            jugador_ini_A -= (altura_salto**2)//2 * dirije
            altura_salto -= 1
            jugador = pygame.image.load("imagenes_juego/mario_saltando.png")
        else:
            saltar = False
            altura_salto = 10
            jugador = pygame.image.load("imagenes_juego/mario1 (1).jpg")

    #No salir de los límites
    if jugador_ini_L <= 0:
        jugador_ini_L = 0
    elif jugador_ini_L >= L-(jugador.get_size()[1]):
        jugador_ini_L = L-(jugador.get_size()[1])
    
    if condicion=="on":
        ventana.blit(fondo_juego,(0,0))
        jugador_ini_L = jugador_ini_L + tasa_cambio_L
        ventana.blit(jugador,(jugador_ini_L,jugador_ini_A))
        ventana.blit(ladrillos,(ladrillos_ini_L,ladrillos_ini_A))
        clock.tick(60)
        pygame.display.update()
    if condicion=="off":

        fondo(van_pos_L,van_pos_A)
        letra(jump_pos_L,jump_pos_A)
        mostrar_instrucciones(space_pos_L,space_pos_A)
    pygame.display.update()