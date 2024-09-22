import pygame as pg
from math import cos, dist, sqrt,pi, sin
import sys
from random import random
pg.init()
screen=pg.display.set_mode((600,600))
x=600
y=600
class planet() :
    def __init__(self,origin,r,white={}) :
        self.origin=origin
        self.r=r
        self.white=white
        self.pixels={}
        self.pixels_buffer={}
        for i in range(r) :
            for j in range(r) :
                self.pixels[i,j]=pg.Vector3(0)
        for i in range(r) :
            for j in range(r) :
                self.pixels_buffer[i,j]=[pg.Vector3(0),0]
        if len(self.white)<r**2 :
            for i in range(r) :
                for j in range(r): 
                    self.white[i,j]=pg.Vector3(250,100,50)
    def update(self,light_pos) :
        light_pos[2]=1.5*self.r
        for i in range(self.r) :
            for j in range (self.r) :
                d=dist((i*4+1+self.origin[0]-self.r,j*4+1+self.origin[1]-self.r),(self.origin[0],self.origin[1]))/self.r
                pixel=pg.Vector3(i*4+1-self.r,j*4+1-self.r,0)
                if d<=1 :  
                    pixel[2]+=sqrt(1-d**2)*self.r
                    normal=cos(-(light_pos-self.origin-pixel).angle_to(pg.math.Vector3.normalize(pixel))*pi/180)
                    if normal>=0.92 :
                        self.pixels[i,j]=self.pixels_buffer[i,j][0]=self.white[i,j]*0.6
                    elif normal>= 0.6  :
                        local_normal=0.6
                        if normal==self.pixels_buffer[i,j][1] :
                            self.pixels[i,j]=self.pixels_buffer[i,j][0]
                            self.pixels_buffer[i,j][0]=self.pixels[i,j]
                        else :
                            self.pixels_buffer[i,j][1]=normal
                            if random()<((normal-local_normal)/0.32)**2 :
                                self.pixels[i,j]=self.pixels_buffer[i,j][0]=self.white[i,j]*0.6
                            else :
                                self.pixels[i,j]=self.pixels_buffer[i,j][0]=self.white[i,j]*0.5
                    elif normal >=0.28 :
                        self.pixels[i,j]=self.white[i,j]*0.5
                        self.pixels_buffer[i,j]=[self.pixels[i,j],1]
                    elif normal>=-0.04 :
                        local_normal=-0.04
                        if normal==self.pixels_buffer[i,j][1] :
                            self.pixels[i,j]=self.pixels_buffer[i,j][0]
                            self.pixels_buffer[i,j][0]=self.pixels[i,j]
                        else :
                            self.pixels_buffer[i,j][1]=normal
                            if random()<((normal-local_normal)/0.32)**3 :
                                self.pixels[i,j]=self.pixels_buffer[i,j][0]=self.white[i,j]*0.5
                            else :
                                self.pixels[i,j]=self.pixels_buffer[i,j][0]=self.white[i,j]*0.4
                    elif normal >=-0.36 :
                        self.pixels[i,j]=self.white[i,j]*0.4
                        self.pixels_buffer[i,j]=[self.pixels[i,j],normal]
                    elif normal >=-0.68 :
                        local_normal=-0.68
                        if normal==self.pixels_buffer[i,j][1] :
                            self.pixels[i,j]=self.pixels_buffer[i,j][0]
                            self.pixels_buffer[i,j][0]=self.pixels[i,j]
                        else :
                            self.pixels_buffer[i,j][1]=normal
                            if random()<((normal-local_normal)/0.32)**4 :
                                self.pixels[i,j]=self.pixels_buffer[i,j][0]=self.white[i,j]*0.4
                            else :
                                self.pixels[i,j]=self.pixels_buffer[i,j][0]=self.white[i,j]*0.1
                    else :
                        self.pixels[i,j]=self.white[i,j]*0.1
                        self.pixels_buffer[i,j]=[self.pixels[i,j],normal]
                else :
                    self.pixels[i,j]=self.white[i,j]*0
                    self.pixels_buffer[i,j]=[self.pixels[i,j],0]
                pg.draw.rect(screen,self.pixels[i,j],(i*4+self.origin[0]-self.r,j*4+self.origin[1]-self.r,4,4))
test=planet(pg.Vector3(x/2,y/2,0),150)
t=0
while 1 :
    screen.fill((0,0,0))
    test.origin[0]=x/2+150*cos(t*pi/180)
    test.origin[1]=y/2+150*sin(t*pi/180)
    test.update(pg.Vector3(pg.mouse.get_pos()[0],pg.mouse.get_pos()[1],0))
    t+=1
    for event in pg.event.get():
        if event.type==pg.QUIT :
            pg.quit()
            sys.exit()
        if event.type==pg.KEYDOWN :
            if event.key==pg.K_ESCAPE :
                pg.quit()
                sys.exit()
    pg.display.flip()
    