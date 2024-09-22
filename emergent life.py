import pygame as pg
import sys
from random import randint, random
from math import *
pg.init()
screen=pg.display.set_mode((600,600))
colors={}
colors[1]=(255,50,50)
colors[2]=(50,255,50)
colors[3]=(50,50,255)
colors[4]=(255,255,50)
colors[5]=(255,50,255)
colors[6]=(50,255,255)
size=5
influence=70
grid={}
x=screen.get_width()
y=screen.get_height()
for  i in range(x//(influence)+1) :
    for  j in range(y//(influence)+1) :
        grid[i,j]=[]
particles=[]
attraction={}
for i in range(1,7):
    for j in range(1,7):
        if i==j :
            attraction[i,j]=0.75
        elif i+1==j or i+1-6==j :
            attraction[i,j]=0.5
        elif i-1==j or i-1+6==j :
            attraction[i,j]=-0.5
        else :
            attraction[i,j]=0
        
print(attraction)
nb_particles=400
for i in range(nb_particles):
    particles.append([pg.Vector2(randint(0,x),randint(0,y)),pg.Vector2(0,0),randint(1,6)])
while 1 :
    x=screen.get_width()
    y=screen.get_height()
    screen.fill((25,25,25))
    for  i in range(x//(influence)+1) :
        for  j in range(y//(influence)+1) :
            grid[i,j]=[]
    for i in range(nb_particles):
        grid[particles[i][0][0]//(influence),particles[i][0][1]//(influence)].append(i)
    for i in range(nb_particles) :
        tile_x=particles[i][0][0]//influence
        tile_y=particles[i][0][1]//influence
        near_particles=[]
        for j in range(3) :
            for k in range(3) :
                if tile_x+j-1<0 :
                    tile_x=tile_x+j-1+x//influence
                elif tile_x+j-1>x//influence :
                    tile_x=tile_x+j-1-x//influence
                if tile_y+k-1<0 :
                    tile_y=tile_y+k-1+y//influence
                elif tile_y+k-1>y//influence :
                    tile_y=tile_y+k-1-y//influence
                near_particles+=grid[tile_x+j-1,tile_y+k-1]
                    
        for j in near_particles :
            p1=pg.Vector2(particles[i][0])
            p2=pg.Vector2(particles[j][0])
            dx=0
            dy=0
            if abs(p1[0]-p2[0])>2*influence :
                dx=min(p1[0],p2[0])-(max(p1[0],p2[0])-x)
            else :
                dx=abs(p1[0]-p2[0])
            
            if abs(p1[1]-p2[1])>2*influence :
                dy=min(p1[1],p2[1])-(max(p1[1],p2[1])-y)
            else :
                dy=abs(p1[1]-p2[1])
            
                
            
            d=sqrt(dx**2+dy**2)
            if 0!=d<=influence :
                particles[i][1]+=(particles[j][0]-particles[i][0])/d*attraction[particles[i][2],particles[j][2]]*2
                particles[i][1]+=(((particles[i][0]-particles[j][0])/d)*9/d)*4
        if dist((0,0),particles[i][1])>1 :
            particles[i][1]/=dist((0,0),particles[i][1])
    for i in range(nb_particles) :
        particles[i][0]+=particles[i][1]
        
        if particles[i][0][0]<0 :
            particles[i][0][0]+=x
        if particles[i][0][0]>x :
            particles[i][0][0]-=x
            
        if particles[i][0][1]<0 :
            particles[i][0][1]+=y
        if particles[i][0][1]>y :
            particles[i][0][1]-=y
        
            
        
        pg.draw.circle(screen,colors[particles[i][2]],particles[i][0],size)
        
        
    for event in pg.event.get():
        if event.type==pg.QUIT :
            pg.quit()
            sys.exit()
        if event.type==pg.KEYDOWN :
            if event.key == pg.K_ESCAPE :
                pg.quit()
                sys.exit()
    pg.display.flip()