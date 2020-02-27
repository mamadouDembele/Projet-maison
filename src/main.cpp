#include "intervall.h"
#include <iostream>

int main(){
	Intervall I1,I2,I3,I4,I5,I6,I7,I8,I9;
	Intervall I=Intervall();
	I1=Intervall(-1,4)+Intervall(2,3);
	I2=Intervall(-1,4)-Intervall(2,3);
	I3=Intervall(-1,4)*Intervall(2,3);
	I4=Intervall(-1,4)/Intervall(2,3);
	//I5=Intervall(3,7)/Intervall(2,9);
	//I6=Intervall(-3,7)/Intervall(-2,6);
	I7=Intervall(-1,3)&Intervall(2,4);
	I8=Intervall(-1,2)|Intervall(3,4);
	I9=I1&I2;
	std::cout<<I<<std::endl;
	std::cout<<I1<<std::endl;
	std::cout<<I2<<std::endl;
	std::cout<<I3<<std::endl;
	std::cout<<I4<<std::endl;
	//std::cout<<I5<<std::endl;
	std::cout<<I1.inverse()<<std::endl;
	std::cout<<I9<<std::endl;
	std::cout<<I7<<std::endl;
	std::cout<<I8<<std::endl;
	std::cout<<Intervall(1,2).prod_by_cst(2)<<std::endl;
	std::cout<<Intervall(-1,4).prive_inter(Intervall(2,3))<<std::endl;

}