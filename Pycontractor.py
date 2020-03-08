from pyibex import *
from vibes import *

T=[0.2,1,2,4,5,6,7]
Y=[Interval(1.5,2),Interval(0.7,0.8),Interval(0.1,0.3),Interval(-0.1,0.03),
   Interval(0,1),Interval(1,2),Interval(1,2)]
seps=[]
for t,y in zip(T,Y):
    f = Function("p1", "p2", "p1*exp(p2*%f)" % t)
    sep = SepFwdBwd(f, y)
    seps.append(sep)
sep=SepQInterProjF(seps)
sep.q=2

t=0.2
f=Function("p1", "p2", "p1*exp(p2*%f)" % t)
sepj = SepFwdBwd(f, Interval(1.5,2))

vibes.beginDrawing()
vibes.newFigure('P')
vibes.setFigureProperties({'x':200, 'y': 100, 'width': 800, 'height': 500})
P=IntervalVector([[-3,3],[-3,3]])
pySIVIA(P,sep&sepj,0.02)

vibes.axisEqual()