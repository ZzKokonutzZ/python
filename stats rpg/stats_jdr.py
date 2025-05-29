from random import randint
from matplotlib import pyplot
ch=15
co=13
iu=7
def NR() :
    d1=D(20)
    d2=D(20)
    d3=D(20)
    n=4
    if d1==1 :
        n+=2*(ch-1)
    else :
        n+=ch-d1
    if d2==1 :
        n+=2*(co-1)
    else :
        n+=co-d2
    if d3==1 :
        n+=2*(iu-1)
    else :
        n+=iu-d3
    return n

def D(n) :
    return randint(1,n)

nb=0
atks_p=[]
atks=[]
group_atks=[]
group_atks_D4=[]
group_atks_p=[]
group_atks_p_D4=[]

for i in range(41):
    atks_p.append(0)
    atks.append(0)
    # group_atks.append(0)
    # group_atks_D4.append(0)
    # group_atks_p.append(0)
    # group_atks_p_D4.append(0)
while nb<100000 :
    nr=NR()
    if nr>0:
        for i in range(nr//4):
            test=D(20)
            for malus in range(-20,21,1):
                if test==1 :
                    atks_p[malus+20]+=D(6)+D(6)+D(4)+D(4)+12+nr//2
                    atks[malus+20]+=D(6)+D(6)+D(4)+D(4)+8+nr//2
                elif test==20 :
                    pass
                # for i in range(40) :
                #     group_atks[i]+=D(6)+D(6)+D(4)+D(4)+8+nr//2+2*i*D(4)
                #     group_atks_p[i]+=D(6)+D(6)+D(4)+D(4)+12+nr//2+2*i*D(4)
                #     group_atks_D4[i]+=D(6)+D(6)+D(4)+D(4)+8+nr//2+2*i*D(4)
                #     group_atks_p_D4[i]+=D(6)+D(6)+D(4)+D(4)+12+nr//2+2*i*D(4)
                elif D(20)>10 : 
                    if test-malus==2 :
                        atks_p[malus+20]+=D(6)+D(6)+D(4)+D(4)+12+nr//2
                        atks[malus+20]+=D(6)+D(6)+D(4)+D(4)+8+nr//2
                        # for i in range(40) :
                        #     group_atks[i]+=D(6)+D(6)+D(4)+D(4)+8+nr//2+2*i*D(4)
                        #     group_atks_p[i]+=D(6)+D(6)+D(4)+D(4)+12+nr//2+2*i*D(4)
                        #     group_atks_D4[i]+=D(6)+D(6)+D(4)+D(4)+8+nr//2+2*i*D(4)
                        #     group_atks_p_D4[i]+=D(6)+D(6)+D(4)+D(4)+12+nr//2+2*i*D(4)
                    elif test-malus<=12 :
                        atks_p[malus+20]+=D(6)+6+D(4)+nr//4
                        atks[malus+20]+=D(6)+4+D(4)+nr//4
                        # for i in range(40) :
                        #     group_atks[i]+=D(6)+D(4)+6+nr//4+i*D(4)
                        #     group_atks_p[i]+=D(6)+D(4)+4+nr//4+i*D(4)
                        #     group_atks_D4[i]+=D(6)+D(6)+D(4)+D(4)+8+nr//2+2*i*D(4)
                        #     group_atks_p_D4[i]+=D(6)+D(6)+D(4)+D(4)+12+nr//2+2*i*D(4)
                    elif test-malus==13 :
                        atks[malus+20]+=D(6)+4+D(4)+nr//4
                        # group_atks[i]+=D(6)+D(4)+6+nr//4+i*D(4)
                        # group_atks_D4[i]+=D(6)+D(6)+D(4)+D(4)+8+nr//2+2*i*D(4)
            # else :
            #     for i in range(40) :
                    
            #         group_atks_D4[i]+=i*D(4)
            #         group_atks_p_D4[i]+=i*D(4)
            nb+=1
x=[]
for i in range(41) :
    atks[i]/=nb
    atks_p[i]/=nb
    x.append(i-20)
pyplot.plot(x,atks)
pyplot.plot(x,atks_p)
pyplot.show()