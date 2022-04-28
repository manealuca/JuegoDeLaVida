#-*- utf-8 -*- 
import pygame, sys
import numpy as np
import time
from Cola import *
pygame.init()

def save_file(lista):
    f = open('simulacion.txt','a')
    f.write(str(lista))
    f.write('\n\n')
    f.close

def draw_polygon(dimCW,dimCH,x,y,game_state,newGameState):
    poly = [((x)*dimCW, y *dimCH),
        ((x+1)*dimCW, y*dimCH),
        ((x+1)* dimCW, (y+1)*dimCH),
        ((x)*dimCW, (y+1)*dimCH)]
    #actualiza fotograma de las celdas
    if newGameState[x,y] == 0:
        pygame.draw.polygon(screen,(128,128,128),poly,1)
    else:
        pygame.draw.polygon(screen,(255,255,255),poly,0)
    

def tolid_and_conditions(nxC,nyC,game_state,newGameState):
    for y in range(0,nxC):
        for x in range(0,nyC):
            if not pause:
                n_nheight = game_state[(x-1) % nxC, (y-1) % nyC]+\
                            game_state[(x) % nxC, (y-1) % nyC]+\
                            game_state[(x+1) % nxC, (y-1) % nyC]+\
                            game_state[(x-1) % nxC, (y) % nyC]+\
                            game_state[(x+1) % nxC, (y) % nyC]+\
                            game_state[(x-1) % nxC, (y+1) % nyC]+\
                            game_state[(x) % nxC, (y+1) % nyC]+\
                            game_state[(x+1) % nxC, (y+1) % nyC]                                    
                #R1: Celula muerta con 3 vecinas vivas "revive"
                if game_state[x,y] == 0 and n_nheight == 3:
                    newGameState[x,y] = 1
                #R2 Celula viva con menos de 2 o mas de 3 vecinas vivas "Muere"
                elif game_state[x,y] and (n_nheight <2 or n_nheight >3):
                    newGameState[x,y] = 0
            draw_polygon(dimCW,dimCH,x,y,game_state,newGameState)


WIDHT = 800
HEIGHT = 800
##############
screen = pygame.display.set_mode((HEIGHT, WIDHT))
background = (0,0,0)
screen.fill(background)
nxC , nyC = 20,20
dimCW = WIDHT / nxC
dimCH = HEIGHT / nyC
#Estados: Vivas = 1 Muertas = 0
game_state =  np.zeros((nxC,nyC))
pause = True
#Bucle principal
tail = Cola()

if __name__ == '__main__':
    while True:    
        screen.fill(background)    
        newGameState = np.copy(game_state)
        time.sleep(0.2)
        events = pygame.event.get()
        for event in events:
            if event.type  == pygame.KEYDOWN:
                pause = not pause
            #pos donde se encuentra el mouse
            mouse_click = pygame.mouse.get_pressed()
            if sum(mouse_click) > 0:
                posX,posY = pygame.mouse.get_pos()
                celX,celY= int(np.floor(posX  / dimCW)), int(np.floor(posY/dimCH))
                newGameState[celX,celY] = not mouse_click[2]
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        #generando efecto toloide
        tolid_and_conditions(nxC,nyC,game_state,newGameState)


        #copiamos el estado actual del juego y lo guardamos en la variable game_state
        game_state = np.copy(newGameState)
        #dibujamos el estado actual del escenario
        pygame.display.flip()
        #si el juego esta corriendo encolamos el game_state, lo guardamos en un archivo y lo desencolamos
        if not pause:
            tail.encolar(game_state)
            save_file(tail.desencolar())
        




