import pygame as pg
import sys
import math
from random import randint
pg.init()
clock=pg.time.Clock()
screen=pg.display.set_mode((500,500))
g=9.81
def dist(a,b):
    dist=math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)
    return dist
max_dist=dist((50,50),(0,0))
density={}
for i in range(100):
    for j in range(100):
        if 10<=i<=90 and 10<=j<=90 :
            density[i,j]=100
        else :
            density[i,j]=0
velocity={}
for i in range(100):
    for j in range(100):
        velocity[i,j]=pg.Vector2(0,0)
v_grid={}
d={}
for i in range(100):
    for j in range(100) :
        d[i,j]=0
sides={}
for i in range(100):
    for j in range(100) :
        sides[i,j]=0
v=0.5
for i in range(100):
    for j in range(100):
        v_grid[i,j]={}
        for k in range(4):
            v_grid[i,j][k]=0
while 1 :
    screen.fill((0,0,0))
    velocity[0,49]=pg.Vector2(100,0)
    velocity[0,50]=pg.Vector2(100,0)
    
    for i in range(100):
        for j in range(100):
            if i==0 :
                v_grid[i,j][1]=velocity[i,j][0]
            elif i==99 :
                v_grid[i,j][3]=velocity[i,j][0]
            else :
                v_grid[i,j][1]=velocity[i,j][0]/2
                v_grid[i,j][3]=velocity[i,j][0]/2
                
            if j==0 :
                v_grid[i,j][2]=velocity[i,j][1]
            elif j==99 :
                v_grid[i,j][0]=velocity[i,j][1]
            else :
                v_grid[i,j][2]=velocity[i,j][1]/2
                v_grid[i,j][0]=velocity[i,j][1]/2
    
    for n in range(2):            
        for i in range(100):
            for j in range(100):
                if i!=99 :
                    v_grid[i,j][1]=v_grid[i+1,j][3]=(v_grid[i,j][1]+v_grid[i+1,j][3])/2
            
                if j!=99 :
                    v_grid[i,j][2]=v_grid[i,j+1][0]=(v_grid[i,j][2]+v_grid[i,j+1][0])/2
        for i in range(100):
            for j in range(100):
                d=-v_grid[i,j][0]+v_grid[i,j][1]+v_grid[i,j][2]-v_grid[i,j][3]
                s=4
                if i==0 or i==99 :
                    s-=1
                if j==0 or j==99 :
                    s-=1

                if i==0 :
                    v_grid[i,j][1]-=d/s
                elif i==0 :
                    v_grid[i,j][3]+=d/s
                else :
                    v_grid[i,j][1]-=d/s
                    v_grid[i,j][3]+=d/s
                    
                if j==0 :
                    v_grid[i,j][2]-=d/s
                elif j==99 :
                    v_grid[i,j][0]+=d/s
                else :
                    v_grid[i,j][2]-=d/s
                    v_grid[i,j][0]+=d/s
                
    for i in range(100):
        for j in range(100):
            velocity[i,j]=pg.Vector2((v_grid[i,j][1]+v_grid[i,j][3]),(v_grid[i,j][0]+v_grid[i,j][2]))
    v_max=100
    for e in velocity :
        if dist((0,0),velocity[e])>v_max:
            k=1
        else :
            k=dist((0,0),velocity[e])/v_max
    for i in range(100):
        for j in range(100):
            local_color=pg.Vector3(int(255*k))
            pg.draw.rect(screen,(local_color),(i*5,j*5,5,5))
    # for key in v_grid :
    #     if int(key[0])==key[0]:
    #         pg.draw.line(screen,(0,50,255),pg.Vector2(key)*5,pg.Vector2(key)*5+(v_grid[key],0))
    #     else :
    #         pg.draw.line(screen,(0,50,255),pg.Vector2(key)*5,pg.Vector2(key)*5+(0,v_grid[key]))
    # for key in velocity :
    #     pg.draw.line(screen,
    #                  (255,50,0),
    #                  pg.Vector2(key)*5+(2,2),
    #                  pg.Vector2(key)*5+velocity[key]+(2,2))
    for event in pg.event.get():
        if event.type==pg.QUIT :
            pg.quit()
            sys.exit()
        if event.type==pg.KEYDOWN :
            if event.key == pg.K_ESCAPE :
                pg.quit()
                sys.exit()
    pg.display.flip()
    clock.tick(120)