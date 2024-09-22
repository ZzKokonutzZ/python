import pygame
import numpy as np
import sys
from random import randint


pygame.init() 
clock=pygame.time.Clock()
size=300
screen=pygame.display.set_mode((size,size))
screen.fill((0,0,0))
speed=1
class agents() :
    def __init__(self,number=1):
        self.orientations = np.array([])
        self.x = np.array([])
        self.y = np.array([])
        for i in range (number) :
            self.orientations = np.append(self.orientations,(randint(0,360)))
            self.x = np.append(self.x,(randint(0,300)))
            self.y = np.append(self.y,(randint(0,300)))
    def update(self):
        
        for i in range (len(self.orientations)):
            self.orientations[i]+=randint (-1,1)
            try :
                screen.get_at((int(self.x[i]+np.sin(self.orientations[i]*np.pi/180)*2),int(self.y[i]+np.cos(self.orientations[i])*np.pi/180)*2))
            except IndexError :
                mid_sensor = (0,0,0)
            else :
                mid_sensor = screen.get_at((int(self.x[i]+np.sin(self.orientations[i]*np.pi/180)*2),int(self.y[i]+np.cos(self.orientations[i])*np.pi/180)*2))
            try :
                screen.get_at((int(self.x[i]+np.sin((self.orientations[i]+45)*np.pi/180)*2),int(self.y[i]+np.cos((self.orientations[i]+45)*np.pi/180)*2)))
            except IndexError:
                right_sensor = (0,0,0)
            else : 
                right_sensor = screen.get_at((int(self.x[i]+np.sin((self.orientations[i]+45)*np.pi/180)*2),int(self.y[i]+np.cos((self.orientations[i]+45)*np.pi/180)*2)))
            try :
                screen.get_at((int(self.x[i]+np.sin((self.orientations[i]-45)*np.pi/180)*2),int(self.y[i]+np.cos((self.orientations[i]-45)*np.pi/180)*2)))
            except IndexError :
                left_sensor = (0,0,0)
            else :
                left_sensor = screen.get_at((int(self.x[i]+np.sin((self.orientations[i]-45)*np.pi/180)*2),int(self.y[i]+np.cos((self.orientations[i]-45)*np.pi/180)*2)))
            self.orientations[i]+= ((right_sensor[0]*45/255)/(1+mid_sensor[0]/255))
            self.orientations[i]-= ((left_sensor[0]*45/255)/(1+mid_sensor[0]/255))
            self.x[i]+=np.sin(self.orientations[i]*np.pi/180)*speed
            self.y[i]+=np.cos(self.orientations[i]*np.pi/180)*speed
            if self.x[i]>= size :
                self.x[i]= 1
            if self.y[i]>= size :
                self.y[i]=1
            if self.x[i]<= 0 :
                self.x[i]=size
            if self.y[i]<= 0 :
                self.y[i]=size
            x_int=int(self.x[i])
            y_int=int(self.y[i])
            pygame.draw.rect(screen,(255,255,255), pygame.Rect(x_int,y_int,1,1))
            pygame.display.update()
            
            
agents_holder=agents(100)             
a=0 
while 1 :
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit()
            sys.exit()
    a+=1
    if a==10 :
        screen.blit(pygame.transform.box_blur(screen,1),(0,0))
        a=0
    
    agents_holder.update()
    pygame.display.update()
    clock.tick(2048)