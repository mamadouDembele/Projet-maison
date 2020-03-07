from vibes import *
from mybox import *


def test(P):
    b = Intervall(0, 0)
    for i in range(len(Y)):
        yi =Y[i]
        amix=x[i]
        amiy=y[i]
        Fi = ((P.x-Intervall(amix,amix)).sqr()+(P.y-Intervall(amiy,amiy)).sqr()).sqrt()
        if Fi.subset(yi):
            b.borne_inf = b.borne_inf + 1
        if not (yi.disjoint(Fi)):
            b.borne_sup = b.borne_sup + 1
    return b


def sivia(P):
    # vibes.selectFigure('P')
    b = test(P)
    q = 0
    if b.borne_sup < len(Y) - q:
        vibes.drawBox(P.x.borne_inf, P.x.borne_sup, P.y.borne_inf, P.y.borne_sup, '[cyan]')
    elif b.borne_inf >= len(Y) - q:
        vibes.drawBox(P.x.borne_inf, P.x.borne_sup, P.y.borne_inf, P.y.borne_sup, '[red]')
    elif P.width() < 0.01:
        vibes.drawBox(P.x.borne_inf, P.x.borne_sup, P.y.borne_inf, P.y.borne_sup, 'yellow[yellow]')
        # DrawOuput(P)
    else:
        sivia(P.left())
        sivia(P.right())


# def DrawOuput(P):
#     t, dt = 0, 0.05
#     vibes.selectFigure('Y')
#     while t < 5:
#         T = Intervall(t, t + dt)
#         y = P.x * (T * P.y).exp()
#         vibes.drawBox(T.borne_inf, T.borne_sup, y.borne_inf, y.borne_sup, 'green[green]')
#         t += dt


if __name__ == "__main__":

    vibes.beginDrawing()
    vibes.newFigure('minimiser')
    vibes.setFigureProperties({'x': 0, 'y': 0, 'width': 1600, 'heigt': 1000})
    x=[4,-1,1]#,5]
    y=[7,4,2]#-2]
    M=Intervall(0,1)
    N=Intervall(0,1)
    Y = [Intervall(8, 9), Intervall(7, 12), Intervall(3, 5)]# Intervall(7, 11)]
    P = Box(Intervall(-100, 100), Intervall(-100, 100))
    sivia(P)

    # vibes.newFigure('minimiser')
    x = [4, -1,5]
    y = [7, 4,-2]
    # P = Box(Intervall(-100, 100), Intervall(-100, 100))
    Y = [Intervall(8, 9), Intervall(7, 12),Intervall(7, 11)]
    vibes.newFigure('minimiser')
    sivia(P)

    vibes.endDrawing()