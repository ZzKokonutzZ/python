import pygame as pg
import numpy as np
from random import randint
import sys
pg.init()
world={}
for x in range(250) :
    for y in range(250) :
        for z in range(250) :
            world[x,y,z]=randint(0,1)

screen=pg.display.set_mode((500,500))
pixels={}
for x in range(125) :
    for y in range(125) :
        pixels[x,y]=(0,0,0)
rd=100
while 1 :
    
    for event in pg.event.get() :
        if event.type==pg.KEYDOWN or event.type==pg.QUIT :
            pg.quit()
            sys.exit()