import pygame as pg
import numpy as np
import sys
from random import random
pg.init()
screen=pg.display.set_mode((500,500))
points=[]
norm=pg.math.Vector3.length
def normalize(a) :
    return(a/norm(a))
clock=pg.time.Clock()
def fibonacci_sphere(samples=1000):

    points = []
    phi = (np.pi/2) * (np.sqrt(5.) - 1.)  # golden angle in radians

    for i in range(samples):
        y = 1 - (i / float(samples - 1)) * 2  # y goes from 1 to -1
        radius = np.sqrt(1 - y * y)  # radius at y

        theta = phi * i  # golden angle increment

        x = np.cos(theta) * radius
        z = np.sin(theta) * radius

        points.append(200*pg.Vector3(x, y, z))

    return points

points=fibonacci_sphere(18)
colors=[]
for i in range(18):
    colors+=[[random()*255,random()*255,random()*255]]
t=0
while 1 :
    t+=0.005
    screen.fill((0,0,0))
    # temp_vecs=[]
    # for i in range(18) :
    #     temp_vec=pg.Vector3(0)
    #     for ii in range(18) :
    #         if i!=ii and points[i]!=points[ii] and points[i]!=-points[ii]:
    #             temp_vec+=(points[i]-points[ii])*(1/(0.5*min(norm(points[i]-points[ii]),norm(points[i]+points[ii]))))
    #     temp_vecs+=[temp_vec]
    # for i in range(18) :
    #     points[i]+=temp_vecs[i]
    #     points[i]=250*normalize(points[i])
    
    for i in range(18) :
        points[i][0]=np.cos(0.001)*points[i][0]-np.sin(0.001)*points[i][1]
        points[i][1]=np.sin(0.001)*points[i][0]+np.cos(0.001)*points[i][1]
        
        points[i][1]=np.cos(0.001)*points[i][1]-np.sin(0.001)*points[i][2]
        points[i][2]=np.sin(0.001)*points[i][1]+np.cos(0.001)*points[i][2]
        pg.draw.aaline(screen,(200,200,200),(250-points[i][0],250-points[i][1]),(250+points[i][0],250+points[i][1]))
    
    for i in range(18) :
        for ii in range(18):
            
            pg.draw.aaline(screen,(255,255,255),(250-np.sin(t+i)*points[i][0],250-np.sin(t+i)*points[i][1]),(250-np.sin(t+ii)*points[ii][0],250-np.sin(t+ii)*points[ii][1]))
    pg.display.update()
    
    clock.tick(60)
    
    for event in pg.event.get() :
        if event.type==pg.QUIT or (event.type==pg.KEYDOWN and event.key==pg.K_ESCAPE) :
            pg.quit()
            sys.exit