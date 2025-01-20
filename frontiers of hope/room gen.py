import pygame as pg
import sys
import wfcgrid as w
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
    
    "full_wall.png":[1,1,1,1]
    

}
fill=3
distribution={
    
    "empty.png":1,
    
    "l_platform.png":0.5,
    "platform.png":0.5,
    "r_platform.png":0.5,
    
    
    "b_l_corner.png":fill,
    "b_r_corner.png":fill,
    "t_r_corner.png":fill,
    "t_l_corner.png":fill,
    
    "l_wall.png":fill,
    "r_wall.png":fill,
    "floor.png":fill,
    "ceiling.png":fill,
    
    "b_l_angle.png":fill,
    "b_r_angle.png":fill,
    "t_r_angle.png":fill,
    "t_l_angle.png":fill,
    
    "full_wall.png":fill
    
}

indexes=[]
sprites={}
for e in blocks :
    sprites[e]=pg.transform.scale(pg.image.load(e),(32,32))
    indexes.append(e)



dependencies={"up":{},"down":{},"right":{},"left":{}}

for ref in dependencies :
    for e in indexes :
        dependencies[ref][e]=[]

for ref in indexes :
    for e in indexes :
        if blocks[ref][0]==blocks[e][2] :
            dependencies["down"][ref].append(e)
        
        if blocks[ref][1]==blocks[e][3] :
            dependencies["right"][ref].append(e)
        
        if blocks[ref][2]==blocks[e][0] :
            dependencies["up"][ref].append(e)
        
        if blocks[ref][3]==blocks[e][1] :
            dependencies["left"][ref].append(e)

tilemap=w.Grid(20,20,indexes,dependencies,distribution)

tilemap.global_collapse()

while 1 :
    screen.fill((0,0,0))
    for e in tilemap.keys :
        screen.blit(sprites[tilemap.grid[e].tiles],(e[0]*32,e[1]*32))
    pg.display.flip()
    for event in pg.event.get() :
        if event.type==pg.QUIT :
            pg.quit()
            sys.exit()