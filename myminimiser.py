from vibes import *
from myInterval import*

def drawtube(tmin,tmax,dt,color):
    t=tmin
    M=Intervall(+float('inf'),+float('inf'))
    while t<tmax:
        x=Intervall(t,t+dt)
        y=x.sqr()+Intervall(2,2)*x-x.exp()
        vibes.drawBox(x.borne_inf,x.borne_sup,y.borne_inf,y.borne_sup,color)
        t=t+dt
        M=y.mini(M)
    return M


if __name__=="__main__":
    vibes.beginDrawing()
    vibes.newFigure('minimiser')
    vibes.setFigureProperties({'x':0,'y':0,'width':1600,'heigt':1000})
    print(drawtube(-2,2,0.5,'[blue]'))
    print(drawtube(-2, 2, 0.05, '[yellow]'))
    print(drawtube(-2, 2, 0.005, '[red]'))
    print(drawtube(-2, 2, 0.0005, '[green]'))
    vibes.endDrawing()