import math
from myInterval import *

def cadd(z,x,y):
    return z.intersect(x+y), x.intersect(z-y), y.intersect(z-x)

def cmul(z,x,y):
    return z.intersect(x*y), x.intersect(z/y), y.intersect(z/x)

def cexp(z,x):
    return z.intersect(x), x.intersect(log(z))

def csqr(y,x):
    x1=x.intersect(Intervall(-float('inf'),0))
    x2 = x.intersect(Intervall(0,+float('inf')))
    # print("x2=",x2)
    # print("x1= ",x1)
    y=(y.intersect(x1.sqr())).union(y.intersect(x2.sqr()))
    if y.empty:
        return y,y
    else:
        x1=x1.intersect(Intervall(-1,-1)*(y.sqrt()))
        x2 = x2.intersect(y.sqrt())
        return y,x1.union(x2)

if __name__=="__main__":
    a = Intervall(-1, 2)
    b = Intervall(3, 4)
    c = Intervall(5, 20)
    print("a= ",a,"b= ",b,"c= ",c)
    b,a=csqr(b,a)
    print("a= ", a, "b= ", b, "c= ", c)
    b, a = csqr(b, a)
    print("a= ", a, "b= ", b, "c= ", c)

