from vibes import *
from mybox import *

def test(P):
    b=Intervall(0,0)
    for i in range(len(Y)):
        ti,yi=T[i],Y[i]
        Fi=P.x*(Intervall(ti,ti)*P.y).exp()
        if Fi.subset(yi):
            b.borne_inf=b.borne_inf+1
        if not(yi.disjoint(Fi)):
            b.borne_sup=b.borne_sup+1
    return b

def sivia(P):
    vibes.selectFigure('P')
    b=test(P)
    q=0
    if b.borne_sup<len(Y)-q:
        vibes.drawBox(P.x.borne_inf,P.x.borne_sup,P.y.borne_inf,P.y.borne_sup,'[cyan]')
    elif b.borne_inf>=len(Y)-q:
        vibes.drawBox(P.x.borne_inf,P.x.borne_sup,P.y.borne_inf,P.y.borne_sup,'[red]')
    elif P.width()<0.01:
        vibes.drawBox(P.x.borne_inf,P.x.borne_sup,P.y.borne_inf,P.y.borne_sup,'yellow[yellow]')
        DrawOuput(P)
    else:
        sivia(P.left())
        sivia(P.right())
        print(P)

def DrawOuput(P):
    t,dt=0,0.05
    vibes.selectFigure('Y')
    while t<5:
        T=Intervall(t,t+dt)
        y=P.x*(T*P.y).exp()
        vibes.drawBox(T.borne_inf, T.borne_sup, y.borne_inf, y.borne_sup, 'green[green]')
        t+=dt
    


if __name__=="__main__":
    vibes.beginDrawing()
    vibes.newFigure('minimiser')
    vibes.setFigureProperties({'x': 0, 'y': 0, 'width': 1600, 'heigt': 1000})
    T=[0.2,1,2,4]
    Y=[Intervall(1.5,2),Intervall(0.7,0.8),Intervall(0.1,0.3),Intervall(-0.1,0.03)]
    P=Box(Intervall(-3,3),Intervall(-3,3))
    sivia(P)
    vibes.selectFigure('Y')
    for i in range(len(Y)):
        vibes.drawBox(T[i]-0.01, T[i]+0.01, Y[i].borne_inf, Y[i].borne_sup, 'red[red]')


    vibes.endDrawing()