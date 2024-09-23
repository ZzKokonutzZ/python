from random import randint
import numpy as np
n=int(input())

# 3D6
scores=[]
for i in range(n) :
    dices=[]
    for i in range(4):
        dices+=[randint(1,6)]
    dices.sort()
    dices.pop(0)
    s=dices[0]+dices[1]+dices[2]
    scores+=[s]

print("score moyen avec 3D6 :",np.mean(scores))
print("écart-type avec 3D6 :", np.std(scores))

# D20
scores=[]
for i in range(n) :
    scores+=[randint(1,20)]
print("score moyen avec un D20 :",np.mean(scores))
print("écart-type avec un D20 :", np.std(scores))