import pygame as pg
pg.init()
keys=[]
screen=pg.display.set_mode((500,500))
screen.fill((0,0,0))
pg.display.flip()
while 1 :
    for event in pg.event.get() :
        if event.type==pg.KEYDOWN :
            keys+=[event.key]
        if event.type==pg.KEYUP :
            keys.remove(event.key)
    print(keys)