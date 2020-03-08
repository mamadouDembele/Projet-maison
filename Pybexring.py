from vibes import *
from pyibex import *
from mycontractor import *

# class myCtr(Ctc):
#     def __init__(C):
#         Ctc.__init__(C,2)
#
#     def contract(C,X):
#         x,y=X[0],X[1]
#         cx,cy,r=Interval(1,3),Interval(2,4),Interval(4,5)
#         a,b=x-cx,y-cy
#         a2 = sqr(a)
#         b2 = sqr(b)
#         r2=sqr(r)
#         bwd_add(r2,a2,b2)
#         bwd_sqr(a2,a)
#         bwd_sqr(b2,b)
#         bwd_sub(a,x,cx)
#         bwd_sub(b,y,cy)





if __name__=="__main__":
    vibes.beginDrawing()
    vibes.newFigure('one ringe with Pyibex')
    vibes.setFigureProperties({'x': 200, 'y': 100, 'width': 800, 'heigt': 800})
    X = IntervalVector(2,[-10, 10])
    r = Interval(4,5)
    f1 = Function('x[2]', '(x[0]-1)^2+(x[1]-2)^2')
    f2 = Function('x[2]', '(x[0]-2)^2+(x[1]-5)^2')
    sep1=SepFwdBwd(f1,sqr(r))
    sep2 = SepFwdBwd(f2, sqr(Interval(4,5)))
    sep=sep1|sep2
    pySIVIA(X,sep,0.1)
    vibes.axisEqual()