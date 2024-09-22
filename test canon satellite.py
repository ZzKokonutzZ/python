import pygame as pg
from math import *
import sys
pg.init()
screen=pg.display.set_mode((500,500))
sat=pg.Vector2(250,150)
r=100
r_o=150
m=10
g=5
a=atan(sqrt((r_o-r)/(1.5*r_o)))
v_0=sqrt(r_o*m*g)/cos(a)
v_sat=pg.Vector2(v_0*cos(a),v_0*sin(a))
while 1 :
    screen.fill((0,0,0))
    v_sat+=g*pg.math.Vector2.normalize(pg.Vector2(250,250)-sat)
    sat+=0.001*v_sat
    pg.draw.circle(screen,(100,200,200),sat,5)
    pg.display.update()
    for event in pg.event.get():
        if event.type==pg.QUIT :
            pg.quit()
            sys.exit()
        if event.type==pg.KEYDOWN :
            if event.key == pg.K_ESCAPE :
                pg.quit()
                sys.exit()