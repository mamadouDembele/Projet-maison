from mycontractor import *

if __name__=="__main__":
    R1=Intervall(0,+float('inf'))
    R2=Intervall(0,float('inf'))
    R=Intervall(-float('inf'),float('inf'))
    I2=Intervall(-float('inf'),float('inf'))
    E=Intervall(23,26)
    I = Intervall(4, 8)
    U1 = Intervall(10, 11)
    U2 = Intervall(14, 17)
    P = Intervall(124, 130)
    print("R1= ",R1,"R2= ",R1,"I= ",I,"E= ",E,"U1= ",U1,"U2= ",U2)
    for k in range(10):
        R,R1,R2=cadd(R,R1,R2)
        P,E,I=cmul(P,E,I)
        E,R,I=cmul(E,R,I)
        U2,R2,I=cmul(U2,R2,I)
        U1, R1, I = cmul(U1, R1, I)
        E,U1,U2=cadd(E,U1,U2)
        I2,I=csqr(I2,I)
        P,R,I2=cmul(P,R,I2)
    print("R1= ", R1, "R2= ", R1, "I= ", I, "E= ", E, "U1= ", U1, "U2= ", U2)