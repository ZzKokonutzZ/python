from dices import test
avgNR=0
success=100
nbtours6=0
nbtours4=0
for i in range(1000) :
    NR=test(15,20)+test(14,20)+test(7,20)+6
    if NR<=0 :
        success-=0.1
        NR=0
    nbtours6+=NR//6
    nbtours4+=NR//4
    avgNR+=NR
    
avgNR/=1000
nbtours4/=1000
nbtours6/=1000
print(avgNR,",",success)
print("NR/6 : ",nbtours6)
print("NR/4 : ",nbtours4)