from random import randint
def D(n) :
    return randint(1,n)

def test(n,d) :
    t=D(d)
    if t==20 :
        t = 40-2*n
    elif t==1 :
        t=2*(n-1)
    else :
        t=n-t
    return t