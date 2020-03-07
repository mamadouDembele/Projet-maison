from vibes import *
from mybox import *
from mycontractor import *
from myrang import CinRing

def SinRing(x,y,cx,cy,r,outer):
    if outer:
        x,y=CinRing(x,y,cx,cy,r)
    else:
        xa,ya=x,y
        xb,yb=x,y
        xa,ya=CinRing(xa,ya,cx,cy,Intervall(0,r.borne_sup))
        xb, yb = CinRing(xb, yb, cx, cy, Intervall(r.borne_inf,+float('inf')))
        x,y=xa.union(xb),ya.union(yb)
    return x,y

def Sep(x,y,outer):
    cx1,cy1,r1=Intervall(1,1),Intervall(2,2),Intervall(4,5)
    cx2, cy2, r2 = Intervall(2, 2), Intervall(5, 5), Intervall(5, 6)
    x1,y1=x,y
    x2,y2=x,y
    x1,y1=SinRing(x1,y1,cx1,cy1,r1,outer)
    x2, y2= SinRing(x2, y2, cx2, cy2, r2, outer)
    if outer:
        x, y = x1.union(x2), y1.union(y2)
    else:
        x, y = x1.intersect(x2), y1.intersect(y2)
    return x,y

def sivia(X):
    if X.width()<0.01:
        return
    vibes.drawBox(X.x.borne_inf, X.x.borne_sup, X.y.borne_inf, X.y.borne_sup, 'black[cyan]')
    X.x,X.y=Sep(X.x,X.y,True)
    # print(X.x,X.y)
    vibes.drawBox(X.x.borne_inf, X.x.borne_sup, X.y.borne_inf, X.y.borne_sup, 'red[magenta]')
    X.x, X.y = Sep(X.x, X.y, False)
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
