#création d'une fonction continue et pseudo-aléatoire, pouvant s'apparenter au bruit de Perlin
from random import randint, random
from math import sin, cos
class randsin() :
    def __init__(self,nb_waves=1,max_magnitude=1,max_wavelength=1):
        self.magnitude_a=[]
        self.wavelength_a=[]
        self.offset_a=[]
        self.magnitude_b=[]
        self.wavelength_b=[]
        self.offset_b=[]
        self.angle_b=[]
        for i in range(nb_waves):
            self.magnitude_a.append((2*random()-1)*max_magnitude)
            self.wavelength_a.append(max_wavelength*random())
            self.offset_a.append(max_wavelength*random())
            self.magnitude_b.append((2*random()-1)*max_magnitude)
            self.wavelength_b.append(max_wavelength*random())
            self.offset_b.append(max_wavelength*random())
            self.angle_b.append(3*random())
    def dim1(self,x,normalized=False):
        r=0
        for i in range(len(self.magnitude_a)) :
            r+=self.magnitude_a[i]*sin(self.wavelength_a[i]*x+self.offset_a[i])
        k=0
        if normalized :
            for i in range(len(self.magnitude_a)) :
                k+=abs(self.magnitude_a[i])
            r=r/k
        return r
    def dim2(self,x,y,normalized=False):
        r=0 
        for i in range(len(self.magnitude_a)) :
            r+=self.magnitude_a[i]*sin((self.wavelength_a[i]*(cos(self.angle_b[i])*x-sin(self.angle_b[i])*y)+self.offset_a[i]))+self.magnitude_b[i]*sin((self.wavelength_b[i]*(cos(self.angle_b[i])*y+sin(self.angle_b[i])*x)+self.offset_b[i]))
        k=0
        if normalized :
            for i in range(len(self.magnitude_a)) :
                k+=abs(self.magnitude_a[i])+abs(self.magnitude_b[i])
            r=r/k
        return r