import pygame as pg
from math import *
import sys
import randsin
pg.init()
noise=randsin.randsin(50,50,3)
screen=pg.display.set_mode((400,400))
blue=pg.Vector3(255,255,255)
heat_map={}
for i in range(400) :
    for j in range(400) :
        k=(noise.dim2(0.1*i,0.1*j,True)+1)/2
        heat_map[i,j]=pg.Vector3((1-k)*255,0,k*255)

while 1 :
    screen.fill((0,0,0))  
    for i in range(400) :
        for j in range(400) :
            pg.draw.rect(screen,heat_map[i,j],(i,j,1,1))
    pg.display.update()
    for event in pg.event.get():
        if event.type==pg.QUIT :
            pg.quit()
            sys.exit()
        if event.type==pg.KEYDOWN :
            if event.key == pg.K_ESCAPE :
                pg.quit()
                sys.exit()
    
