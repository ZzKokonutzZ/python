import pygame as pg
from random import randint, random
from copy import deepcopy
from math import *
import sys
pg.init()
screen=pg.display.set_mode((640,640))
blocks={
    
    "empty.png":[0,0,0,0],
    "l_platform.png":[0,"p",0,0],
    "platform.png":[0,"p",0,"p"],
    "r_platform.png":[0,0,0,"p"],
    
    
    "b_l_corner.png":["l","b",1,1],
    "b_r_corner.png":["r",1,1,"b"],
    "t_r_corner.png":[1,1,"r","t"],
    "t_l_corner.png":[1,"t","l",1],
    
    "l_wall.png":["l",0,"l",1],
    "r_wall.png":["r",1,"r",0],
    "floor.png":[0,"b",1,"b"],
    "ceiling.png":[1,"t",0,"t"],
    
    "b_l_angle.png":["r","t",0,0],
    "b_r_angle.png":["l",0,0,"t"],
    "t_r_angle.png":[0,0,"l","b"],
    "t_l_angle.png":[0,"b","r",0],
    
    
    
    
    
    
    
    
    
    
    
    
    
    "full_wall.png":[1,1,1,1],
    

}

sprites={}
for n in blocks :
    sprites[n]=pg.transform.scale(pg.image.load(n),(64,64))



grid={}
for i in range(10) :
    for j in range(10) :
        grid[i,j]=[]
        for n in blocks :
            grid[i,j]+=[deepcopy(blocks[n])]



ref_grid=deepcopy(grid)
def update_grid(i,j) :
    t=0
    holder=deepcopy(grid[i,j])
    for e in grid[i,j] :
        try :
            grid[i+1,j]
        except :
            pass
        else :
            if len(grid[i+1,j])==1 :
                if e[1]!=grid[i+1,j][0][3] :
                    if e in holder :
                        holder.remove(e)

        try :
            grid[i-1,j]
        except :
            pass
        else :
            if len(grid[i-1,j])==1 :
                if e[3]!=grid[i-1,j][0][1] :
                    if e in holder :
                        holder.remove(e)
        
        try :
            grid[i,j+1]
        except :
            pass
        else :
            if len(grid[i,j+1])==1 :
                if e[2]!=grid[i,j+1][0][0] :
                    if e in holder :
                        holder.remove(e)
        
        
        try :
            grid[i,j-1]
        except :
            pass
        else :
            if len(grid[i,j-1])==1 :
                if e[0]!=grid[i,j-1][0][2] :
                    if e in holder :
                        holder.remove(e)                                
    if len(holder)==0 :
        t=1

    else :
        grid[i,j]=[holder[floor((random())*(len(holder)))]]
    return t
def reduce_grid(i,j) :
    t=0
    holder=deepcopy(grid[i,j])
    for e in grid[i,j] :
        try :
            grid[i+1,j]
        except :
            pass
        else :
            if len(grid[i+1,j])==1 :
                if e[1]!=grid[i+1,j][0][3] :
                    if e in holder :
                        holder.remove(e)

        try :
            grid[i-1,j]
        except :
            pass
        else :
            if len(grid[i-1,j])==1 :
                if e[3]!=grid[i-1,j][0][1] :
                    if e in holder :
                        holder.remove(e)
        
        try :
            grid[i,j+1]
        except :
            pass
        else :
            if len(grid[i,j+1])==1 :
                if e[2]!=grid[i,j+1][0][0] :
                    if e in holder :
                        holder.remove(e)
        
        
        try :
            grid[i,j-1]
        except :
            pass
        else :
            if len(grid[i,j-1])==1 :
                if e[0]!=grid[i,j-1][0][2] :
                    if e in holder :
                        holder.remove(e)                                
    if len(holder)==0 :
        t=1
    return t
running=1
while running :
    grid=deepcopy(ref_grid)
    for i in range(10) :
        for j in range(10) :
            running=update_grid(i,j)
            if running :
                break
        if running :
            break

for i in range(10) :
    for j in range(10) :
        for e in grid[i,j] :
            for k in blocks :
                if blocks[k]==e :
                    screen.blit(sprites[k],(i*64,j*64))
                    pg.display.flip()

k=0
l=0
while 1 :
    screen.fill((0,0,0))
    gen=[]
    for i in range(10) :
        for j in range(10) :
            new=0
            try :
                grid[i+k,j+l]
            except :
                gen.append([i+k,j+l])
            else :
                for e in blocks :
                    if blocks[e]==grid[i+k,j+l][0] :
                        screen.blit(sprites[e],(i*64,j*64))
    pg.display.flip()
    for e in gen :
        grid[e[0],e[1]]=[]
        for n in blocks :
            grid[e[0],e[1]]+=[deepcopy(blocks[n])]
        reduce_grid(e[0],e[1])
    while len(gen)>0 :
        tracker="min"
        min_l=len(grid[gen[0][0],gen[0][1]])
        ref=gen[0][0],gen[0][1]
        ind=0
        for i in range(len(gen)) :
            try :
                grid[gen[i][0]-1,gen[i][1]]
            except :
                pass
            else :
                if len(grid[gen[i][0]-1,gen[i][1]])==1 :
                    if grid[gen[i][0]-1,gen[i][1]][0][1]=="p" :
                        ref=gen[i][0],gen[i][1]
                        ind=i
                        tracker="p"
            try :
                grid[gen[i][0]+1,gen[i][1]]
            except :
                pass
            else :
                if len(grid[gen[i][0]+1,gen[i][1]])==1 :
                    if grid[gen[i][0]+1,gen[i][1]][0][3]=="p" :
                        ref=gen[i][0],gen[i][1]
                        ind=i
                        tracker="p"

            if tracker=="min":
                try :
                    grid[gen[i][0]-1,gen[i][1]]
                except :
                    pass
                else :
                    if len(grid[gen[i][0]-1,gen[i][1]])==1 :
                        if grid[gen[i][0]-1,gen[i][1]][0][1]!=0 :
                            ref=gen[i][0],gen[i][1]
                            ind=i
                            tracker="b"
                
                try :
                    grid[gen[i][0]+1,gen[i][1]]
                except :
                    pass
                else :
                    if len(grid[gen[i][0]+1,gen[i][1]])==1 :
                        if grid[gen[i][0]+1,gen[i][1]][0][3]!=0 :
                            ref=gen[i][0],gen[i][1]
                            ind=i
                            tracker="b"
                try :
                    grid[gen[i][0],gen[i][1]+1]
                except :
                    pass
                else :
                    if len(grid[gen[i][0],gen[i][1]+1])==1 :
                        if grid[gen[i][0],gen[i][1]+1][0][0]!=0 :
                            ref=gen[i][0],gen[i][1]
                            ind=i
                            tracker="b"
                try :
                    grid[gen[i][0],gen[i][1]-1]
                except :
                    pass
                else :
                    if len(grid[gen[i][0],gen[i][1]-1])==1 :
                        if grid[gen[i][0],gen[i][1]-1][0][2]!=0 :
                            ref=gen[i][0],gen[i][1]
                            ind=i
                            tracker="b"
            
            if len(grid[gen[i][0],gen[i][1]])<min_l and tracker=="min":
                min_l=len(grid[gen[i][0],gen[i][1]])
                ref=gen[i][0],gen[i][1]
                ind=i
        update_grid(ref[0],ref[1])
        gen.pop(ind)
        for e in blocks :
                if blocks[e]==grid[ref][0] :
                    screen.blit(sprites[e],((ref[0]-k)*64,(ref[1]-l)*64))
        pg.display.flip()
        for e in gen :
            reduce_grid(e[0],e[1]) 
            
    pg.display.flip()
    
    for event in pg.event.get() :
        if event.type==pg.KEYDOWN :
            if event.key==pg.K_LEFT :
                k-=1
            if event.key==pg.K_RIGHT :
                k+=1
            if event.key==pg.K_UP :
                l-=1
            if event.key==pg.K_DOWN :
                l+=1
            if event.key==pg.K_ESCAPE :
                pg.quit()
                sys.exit()

        if event.type==pg.QUIT :
            pg.quit()
            sys.exit()