import pygame as pg
from math import *
from random import randint
import sys
pg.init()
clock=pg.time.Clock()
screen=pg.display.set_mode((500,500),pg.RESIZABLE)
size=10
particles=[]
def scal_len(a):
    return dist((0,0),a)

#calcul de l'alignement de deux vecteurs (égal à 1 lorsque les vecteurs sont colinéaires et 0 lorsqu'ils sont orthogonaux)
def alignment(a,b):
    if a[0]==0 :
        if a[1]>0 :
            angle_a=pi/2
        elif a[1]<0 :
            angle_a=3*pi/2
        else :
            return 1    
    else :
        angle_a=atan(a[1]/a[0])
        
    if b[0]==0 :
        if b[1]>0 :
            angle_b=pi/2
        elif b[1]<0 :
            angle_b=3*pi/2
        else :
            return 1    
    else :
        angle_b=atan(b[1]/b[0])
    t=angle_a-angle_b
    return abs(cos(t))

#création de la liste de particules composant le fluide
for i in range(150):
    particles.append([pg.Vector2(randint(size-1,500-size),randint(size-1,500-size)),pg.Vector2(0,0)])
    
    
ball=[pg.Vector2(0,0),30]
chunks={}
chunk_size=2*size
while 1 :
    x=screen.get_width()
    y=screen.get_height()
    screen.fill((0,0,0))
    ball[0]=pg.Vector2(pg.mouse.get_pos())
    
    #réinitialisation des chunks
    for i in range(x//chunk_size+1):
        for j in range(y//chunk_size+1):
            chunks[i,j]=[]
    
    for i in range(len(particles)) :
        particles[i][1][1]+=1
    
    
    for n in range(5) :
        
        #chaque particule est mise dans un chunk, ainsi nous n'avons qu'à prendre en compte les intéractions entre les particules de chunk voisins plutôt qu'entre toutes les particules de la liste
        for i in range(len(particles)):
            chunks[particles[i][0][0]//chunk_size,particles[i][0][1]//chunk_size].append(i)
        
        
        for i in range(len(particles)) :
            near_particles=[]
            for j in range(3):
                for k in range(3) :
                    if 0<=particles[i][0][0]//chunk_size+j-1<=x//chunk_size and 0<=particles[i][0][1]//chunk_size+k-1<=x//chunk_size :
                        near_particles.extend(chunks[particles[i][0][0]//chunk_size+j-1,particles[i][0][1]//chunk_size+k-1])
            if dist(particles[i][0],ball[0])<size+ball[1] :
                        while dist(particles[i][0],ball[0])==0 :
                            particles[i][0]+=particles[i][1]/100
                        overlap=size+ball[1]-dist(particles[i][0],ball[0])
                        particles[i][1]+=(alignment(particles[i][1],particles[i][0]-ball[0]))*(overlap*(particles[i][0]-ball[0])/(scal_len(particles[i][0]-ball[0])))/2
                        particles[i][0]+=(overlap*(particles[i][0]-ball[0])/(scal_len(particles[i][0]-ball[0])))/2
            for j in near_particles :
                if 0<dist(particles[i][0],particles[j][0])<2*size :   
                    overlap=2*size-dist(particles[i][0],particles[j][0])    
                    particles[i][1]+=(alignment(particles[i][1],particles[i][0]-particles[j][0]))*(overlap*(particles[i][0]-particles[j][0])/(scal_len(particles[i][0]-particles[j][0])))/2
                    particles[i][0]+=(overlap*(particles[i][0]-particles[j][0])/(scal_len(particles[i][0]-particles[j][0])))/2
                        
                    particles[j][1]+=(alignment(particles[j][1],particles[j][0]-particles[i][0]))*(overlap*(particles[j][0]-particles[i][0])/(scal_len(particles[j][0]-particles[i][0])))/2
                    particles[j][0]+=(overlap*(particles[j][0]-particles[i][0])/(scal_len(particles[j][0]-particles[i][0])))/2
        for i in range(len(particles)) :
            particles[i][0]+=particles[i][1]
            if particles[i][0][1]>y-size :
                particles[i][0][1]=y-size
                particles[i][1][1]/=-2
            if particles[i][0][1]<size-1 :
                particles[i][0][1]=size-1
                particles[i][1][1]/=-2
                
            if particles[i][0][0]>x-size :
                particles[i][0][0]=x-size
                particles[i][1][0]/=-2
            if particles[i][0][0]<size-1 :
                particles[i][0][0]=size-1
                particles[i][1][0]/=-2
    pg.draw.circle(screen,(255,50,0),ball[0],ball[1])                
    for i in range(len(particles)) :
        pg.draw.circle(screen,(0,50,255),particles[i][0],size)
    for event in pg.event.get():
        if event.type==pg.QUIT :
            pg.quit()
            sys.exit()
        if event.type==pg.KEYDOWN :
            if event.key == pg.K_ESCAPE :
                pg.quit()
                sys.exit()
    pg.display.flip()
    clock.tick(60)