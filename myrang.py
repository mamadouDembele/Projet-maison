from vibes import *
from mybox import *
from mycontractor import *

def CinRing(x,y,cx,cy,r):
    a=x-cx
    b=y-cy
    a2=a.sqr()
    b2=b.sqr()
    r2=r.sqr()
    r2,a2,b2=cadd(r2,a2,b2)
    a2,a=csqr(a2,a)
    b2,b=csqr(b2,b)
    x,a,cx=cadd(x,a,cx)
    y,b,cy=cadd(y,b,cy)
    return x,y

def f(x,y,cx,cy,d):
    a = x - cx
    b = y - cy
    a2 = a.sqr()
    b2 = b.sqr()
    c=(a2+b2).sqrt()
    d,c=csqr(d,c)
    c,a2,b2=cadd(c,a2,b2)
    a2, a = csqr(a2, a)
    b2, b = csqr(b2, b)
    x, a, cx = cadd(x, a, cx)
    y, b, cy = cadd(y, b, cy)
    return x,y



def sivia(X):
    if X.width()<0.01:
        return
    vibes.drawBox(X.x.borne_inf, X.x.borne_sup, X.y.borne_inf, X.y.borne_sup, '[cyan]')
    X.x,X.y=CinRing(X.x,X.y,Intervall(1,3),Intervall(2,4),Intervall(4,5))
    vibes.drawBox(X.x.borne_inf, X.x.borne_sup, X.y.borne_inf, X.y.borne_sup, '[yellow]')
    sivia(X.left())
    sivia(X.right())


if __name__=="__main__":
    vibes.beginDrawing()
    vibes.newFigure('minimiser')
    vibes.setFigureProperties({'x': 0, 'y': 0, 'width': 1600, 'heigt': 1000})
    X = Box(Intervall(-10, 10), Intervall(-10, 10))
    sivia(X)
    vibes.endDrawing()
