import pygame as pg
import sys
from random import randint
pg.init()
screen=pg.display.set_mode((500,500),pg.RESIZABLE)
class Sand() :
    def __init__(self):
        self.display={}
    def update(self,x,y) :
        buffer={}
        for i in self.display :
            check = True
            if i[1]+1<=y :    
                try :
                    self.display[i[0],i[1]+1]
                except KeyError :
                    buffer[i[0],i[1]+1]=i[0],i[1]+1
                    check = False 
                if check :
                    if i[0]-1>=0 :
                            try :
                                self.display[i[0]-1,i[1]+1]
                            except KeyError :
                                buffer[i[0]-1,i[1]+1]=i[0]-1,i[1]+1
                                check = False
                if check :
                    if i[0]+1<=x :
                        try :
                            self.display[i[0]+1,i[1]+1]
                        except KeyError :
                            buffer[i[0]+1,i[1]+1]=i[0]+1,i[1]+1
                            check = False
            else :
                if check :
                    if i[0]+1<=x :
                        try :
                            self.display[i[0]+1,i[1]]
                        except KeyError :
                            buffer[i[0]+1,i[1]]=i[0]+1,i[1]
                            check = False
                if check :
                    if i[0]-1>=0 :
                            try :
                                self.display[i[0]-1,i[1]]
                            except KeyError :
                                buffer[i[0]-1,i[1]]=i[0]-1,i[1]
                                check = False
                if check :    
                    buffer[i]=i          
        self.display=buffer
        for i in self.display:
            pg.draw.rect(screen,(240,255,170),(i[0]*4,i[1]*4,4,4))
    def add(self,pos,size):
        for i in range(size) :
            for j in range(size):
                self.display[pos[0]/4+i,pos[1]/4+j]=pos[0]/4+i,pos[1]/4+j
sand=Sand()
while 1 :
    x=int(screen.get_width()/4)
    y=int(screen.get_height()/4)
    screen.fill ((50,50,50))
    for event in pg.event.get():
        if event.type == pg.QUIT :
            pg.quit()
            sys.exit()
        if pg.mouse.get_pressed()[0]:
            sand.add((4*int(pg.mouse.get_pos()[0]/4),4*int(pg.mouse.get_pos()[1]/4)),5)
    sand.update(x,y)
    pg.display.flip()