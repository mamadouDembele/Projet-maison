from pyibex import*
import numpy as np
from vibes import *
from pyibex.geometry import SepPolarXY

Marks=[[6,12],[-2,-5],[-3,10]]
D=[Interval(10,13),Interval(8,10),Interval(5,7)]
Alpha=[Interval(0.5,1),Interval(-3,-1.5),Interval(1,2)]

m=Marks[0]
vibes.beginDrawing()
seps=[]
for m,d,alpha in zip(Marks,D,Alpha):
    sep1=SepPolarXY(d,alpha)
    f1=Function("v1","v2","(%f-v1;%f-v2)"%(m[0],m[1]))
    f2=Function("p1","p2","(%f-p1;%f-p2)"%(m[0],m[1]))
    sep=SepTransform(sep1,f1,f2)
    seps.append(sep)

sep=SepQInterProjF(seps)
sep.q=0

vibes.newFigure('P')
vibes.setFigureProperties({'x':100, 'y': 100, 'width': 800, 'height': 500})
P=IntervalVector([[-20,20],[-20,20]])
pySIVIA(P,sep,0.1)
for m in Marks:
    vibes.drawCircle(m[0],m[1],1,'yellow[black]')