from math import *
from myInterval import *

class Box:

    def __init__(self,a,b):
        self.x=a
        self.y=b

    def __str__(self):
        return "[%f,%f] X [%f,%f]" % (self.x.borne_inf,self.y.borne_sup,self.y.borne_inf,self.y.borne_sup)

    def width(self):
        if self.x.empty or self.y.empty:
            return -float('inf')

        else:
            return max(self.x.width(),self.y.width())

    def left(self):
        if self.x.width()>self.y.width():
            return Box(self.x.left(),self.y)
        else:
            return Box(self.x,self.y.left())

    def right(self):
        if self.x.width()>self.y.width():
            return Box(self.x.right(),self.y)
        else:
            return Box(self.x,self.y.right())

