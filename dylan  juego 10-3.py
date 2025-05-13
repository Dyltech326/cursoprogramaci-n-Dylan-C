








import math
import random
import pygame 

from pygame import mixer

#inicio del del juego 
pygame.int()

# se crea el fondo de pantalla 
screen = pygame.display.set_mode((1000,800))

#fondo de pantalla
background = pygame.image.load('/media/pc09/1246-7398/juego 1 Dylan Carvajal/fonfo.png')

#sonid de fondo 
mixer.music.load('/media/pc09/1246-7398/juego 1 Dylan Carvajal/UTF-8background.wav')
mixer.music.load(-1)

#titulo y icono 
pygame.display.set_caption("perdidos en ")
icon= pygame.image.load('/media/pc09/1246-7398/juego 1 Dylan Carvajal/tierra-removebg-preview.png')
pygame.display.set_icon(icon)

#jugador
playerImg=pygame .image.load('/media/pc09/1246-7398/juego 1 Dylan Carvajal/bala-removebg-preview.png')
playerX=370
playery=480
playerX_change=0

#enemigos 
enemyImg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyy_change=[]
num_of_enemies=35

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('/media/pc09/1246-7398/juego 1 Dylan Carvajal/marte-removebg-preview.png'))
    enemyX.append(random.randint(0,736))
    enemyX.append(random.randint(50,150))
    enemyX_change.append(4)
    enemyy_change.append(40)

    # disparo proyectil

    armaImg= pygame.image.load('/home/pc09/Descargas/espada-removebg-preview.png')
    armaX=0
    armaX=480
    armaX_change=0
    armaX_change=10
    arma_estado="ready"

    # puntaje

    score_value=0
    font= pygame.font.Font('freesansbold.ttf'32)


    textX=10
    textX=10

    #juego terminado
    over_font =pygame.font.Font('freesansbold.ttf'64)

def show_puntaje(x,y):
    score=font.render("Score : " +str( score_value),True,(255,255,255))
    screen.blint(score,(x,y))
def gameover_text():
    over_text =over_font.render("game over",True,255,255,255)
    screen.blint( over_text,(200,250))
def player(x,y):
    screen.blint(playerImg,(x,y))
def player(x,y,i):
    screen.blint(enemyImg[i],(x,y))
def iniciar_disparo(x,y):
    global arma_estado
    arma_estado = "fire"
    screen.blit(armaImg,(x+16,y+10))
def iscollission(enemyX,enemyY,armaX,armaY):
    distance = math.sqrt(math.pow(enemyX-armaX)+(math.pow(enemyY-armaY,2)))
    if distance<27:
        return True
    else : return False

# ciclo de juego
Running = True
while Running:
    screen.fill((0,0,0))
    # imagen de fondo
    screen.blit(background,(0,0))
    for event in pygame,event,get():
        if event.type == pygame.quit:
            Running =False



            # si presiona derecha o izquierda
            if event.type==pygame.KEYDOWN:
                 if  playerX_change==pygame.K_LEFT:
                     playerX_change=-5
                 if event.key==pygame.K_RIGHT:
                     playerX_change_= 5
                     while running:
                     screen.fill((0,0,0,))

                     screen.bilt(bachground, (0,0))
                     for event in pygame.event.get():
                         id
                     
    
    


    
