import pygame as pg
from random import randint, random
from copy import deepcopy
pg.init()
screen=pg.display.set_mode((640,640))
blocks={
    "full_wall.png":[1,1,1,1],
    
    "b_l_angle.png":["r","t",0,0],
    "b_r_angle.png":["l",0,0,"t"],
    "t_r_angle.png":[0,0,"l","b"],
    "t_l_angle.png":[0,"b","r",0],
    
    "b_l_corner.png":["l","b",1,1],
    "b_r_corner.png":["r",1,1,"b"],
    "t_r_corner.png":[1,1,"r","t"],
    "t_l_corner.png":[1,"t","l",1],
    
    "l_wall.png":["l",0,"l",1],
    "r_wall.png":["r",1,"r",0],
    "floor.png":[0,"b",1,"b"],
    "ceiling.png":[1,"t",0,"t"],
    
    "l_platform.png":[0,"p",0,0],
    "platform.png":[0,"p",0,"p"],
    "r_platform.png":[0,0,0,"p"],
    
    "empty.png":[0,0,0,0]
}

sprites={}
for n in blocks :
    sprites[n]=[pg.transform.scale(pg.image.load(n),(64,64))]

grid={}
for i in range(10) :
    for j in range(10) :
        grid[i,j]=[]
        for n in blocks :
            grid[i,j]+=[blocks[n]]

a,b=randint(3,6),randint(3,6)
grid[a,b]=[[0,"p",0,"p"]]
for i in range(10) :
    for e in grid[i,0] :
        if e[0]!=1 :
            grid[i,0].remove(e)
    
    for e in grid[i,9] :
        if e[2]!=1 :
            grid[i,9].remove(e)
    
    for e in grid[0,i] :
        if e[3]!=1 :
            grid[0,i].remove(e)
    
    for e in grid[9,i] :
        if e[1]!=1 :
            grid[9,i].remove(e)

ref_grid=deepcopy(grid)

def collapse(i,j) :
    e=randint(0,len(grid[i,j])-1)
    grid[i,j]=[grid[i,j][e]]
    def update_cell(i,j,side,keys) :
        changed=0
        for e in grid[i,j] :
            if not e[side] in keys :
                grid[i,j].remove(e)
                changed=1
        if changed :
            up=[]
            down=[]
            left=[]
            right=[] 
            for e in grid[i,j] :
                up+=[e[0]]
                right+=[e[1]]
                down+=[e[2]]
                left+=[e[3]]
            if i+1<=9 :
                update_cell(i+1,j,3,right)
            if i-1>=0 :
                update_cell(i-1,j,1,left)
                
            if j+1<=9 :
                update_cell(i,j+1,0,down)
            if j-1>=0 :
                update_cell(i,j-1,2,up)
                
    up=[]
    down=[]
    left=[]
    right=[] 
    for e in grid[i,j] :
        up+=[e[0]]
        right+=[e[1]]
        down+=[e[2]]
        left+=[e[3]]
    if i+1<=9 :
        update_cell(i+1,j,3,right)
    if i-1>=0 :
        update_cell(i-1,j,1,left)
        
    if j+1<=9 :
        update_cell(i,j+1,0,down)
    if j-1>=0 :
        update_cell(i,j-1,2,up)
done=0
while not done :
    collapse(i,j)
    r=0
    check=1
    min_entropy=len(blocks)
    low_entropy_cells=[]
    for i in range(10) :
        for j in range(10):
            if len(grid[i,j])>1  :
                check=0
                if len(grid[i,j])<min_entropy :
                    min_entropy=len(grid[i,j])
                    low_entropy_cells=[(i,j)]
                if len(grid[i,j])==min_entropy :
                    low_entropy_cells+=[(i,j)]
            if len(grid[i,j])==0 :
                r=1
    if len(low_entropy_cells)>0 :
        i,j=low_entropy_cells[randint(0,len(low_entropy_cells)-1)]
    if r :
        check=0
        grid=deepcopy(ref_grid)
    done=check

print(grid)