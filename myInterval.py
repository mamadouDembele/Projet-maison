from math import*

class Intervall:

    def __init__(self,a,b):
        if a<=b:
            self.borne_inf=a
            self.borne_sup=b
            self.empty=False
        else:
            self.borne_inf = nan
            self.borne_sup = nan
            self.empty=True

    def intersect(self,other):
        if (self.empty==True or other.empty==True):
            return Intervall(1, 0)
        else:
            return Intervall(max(self.borne_inf, other.borne_inf), min(self.borne_sup, other.borne_sup))

    def union(self,other):
        if self.empty==True:
            return other
        elif other.empty==True:
            return Intervall(self.borne_inf,self.borne_sup)
        else:
            return Intervall(min(self.borne_inf,other.borne_inf),max(self.borne_sup,other.borne_sup))

    def __add__(self, other):
        if self.empty==True or other.empty==True:
            return Intervall(1,0)
        return Intervall(self.borne_inf+other.borne_inf,self.borne_sup+other.borne_sup)

    def __mul__(self, other):
        a=min(self.borne_inf * other.borne_inf, self.borne_inf * other.borne_sup, self.borne_sup * other.borne_sup,
            self.borne_sup * other.borne_inf)
        b=max(self.borne_inf * other.borne_inf, self.borne_inf * other.borne_sup, self.borne_sup * other.borne_sup,
            self.borne_sup * other.borne_inf)
        return Intervall(a,b)

    def __sub__(self, other):
        if self.empty==True or other.empty==True:
            return Intervall(1,0)
        a=min(self.borne_inf-other.borne_inf,self.borne_inf-other.borne_sup)
        b=max(self.borne_sup-other.borne_inf,self.borne_sup-other.borne_sup)
        return Intervall(a,b)

    def __truediv__(self, other):
        if other.borne_inf==0:
            return Intervall(self.borne_sup/other.borne_sup,float('inf'))
        if other.borne_sup==0:
            return Intervall(-float('inf'),self.borne_inf/other.borne_inf)
        if other.borne_inf<0 and other.borne_sup>0:
            return Intervall(-float('inf'),float('inf'))
        else:
            a=min(self.borne_inf / other.borne_inf, self.borne_inf / other.borne_sup, self.borne_sup / other.borne_sup,self.borne_sup / other.borne_inf)
            b=max(self.borne_inf / other.borne_inf, self.borne_inf / other.borne_sup, self.borne_sup / other.borne_sup,self.borne_sup / other.borne_inf)
            return Intervall(a,b)

    def exp(self):
        return Intervall(exp(self.borne_inf),exp(self.borne_sup))

    def mini(self,other):
        return Intervall(min(self.borne_inf,other.borne_inf),min(self.borne_sup,other.borne_sup))


    def maxi(self,other):
        return Intervall(max(self.borne_inf, other.borne_inf), max(self.borne_sup, other.borne_sup))

    def sqr(self):
        if self.empty!=True:
            L=[self.borne_sup**2,self.borne_inf**2]
            if self.borne_inf<=0 and self.borne_sup>=0:
                return Intervall(0,max(L))
            else:
                return Intervall(min(L),max(L))
        else:
            return Intervall(1,0)

    def sqrt(self):
        if self.borne_sup<0:
            return Intervall(1,0)
        if self.borne_sup>=0 and self.borne_inf<0:
            return Intervall(0,sqrt(self.borne_sup))
        else:
            return Intervall(self.borne_inf**0.5,self.borne_sup**0.5)

    def width(self):
        return self.borne_sup-self.borne_inf

    def left(self):
        return Intervall(self.borne_inf,0.5*(self.borne_inf+self.borne_sup))

    def right(self):
        return Intervall(0.5*(self.borne_inf+self.borne_sup),self.borne_sup)

    def subset(self,y):
        if self.empty:
            return True
        else:
            if y.borne_inf<=self.borne_inf<=y.borne_sup:
                a=True
            else:
                a=False
            if y.borne_inf<=self.borne_sup<=y.borne_sup:
                b=True
            else:
                b=False
            return a and b

    def __and__(self, other):
        if (self.empty and other.empty):
            return Intervall(1,0)
        else:
            return Intervall(max(self.borne_inf,other.borne_inf),min(self.borne_sup,other.borne_sup))

    def loga(self):
        if self.borne_sup<=0:
            return Intervall(1,0)
        if self.borne_sup>0 and self.borne_inf<0:
            return Intervall(0,log(self.borne_sup))
        else:
            return Intervall(log(self.borne_inf),log(self.borne_sup))

    def __str__(self):
        if self.empty==False:
            return "[%f,%f]" % (self.borne_inf, self.borne_sup)
        if self.borne_sup==self.borne_inf:
            return "{%d}"%(self.borne_sup)
        else:
            return Intervall(1,0)

    def disjoint(self,other):
        return (self.intersect(other)).empty



if __name__=="__main__":
    I1=Intervall(-1,3)
    I2=Intervall(2,5)
    I3 = Intervall(-10, 4)
    I4 = Intervall(-2, -1)
    print(log(2))
    print("sqr(I1)=",I1.sqr())
    print("sqrt(I3)=", I3.sqrt())
    #print("log(I4)=", I4.loga())
    print("I1 + I2=",I1+I2)
    print("I1 - I2=",I1 - I2)
    print("I1 * I2=",I1*I2)
    print("I1 / I2=",I1/I2)
    print("max(I1,I2)=",I1.maxi(I2))
    print("min(I1,I2)=",I1.mini(I2))

    #question 3

    x=Intervall(-2,2)
    f_x=x.sqr()+Intervall(2,2)*x-x.exp()
    print("f(x)=",f_x)