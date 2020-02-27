#include "intervall.h"
#include <algorithm>
#include <cmath>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <limits>

Intervall::Intervall()
{
	m_empty=true;
}

Intervall::Intervall(double x):m_sup(x),m_inf(x),m_empty(false)
{

}

Intervall::Intervall(double a, double b)
{
	if (a<b){
		m_inf=a;
		m_sup=b;
		m_empty=false;
	}
	else
	{
		m_empty=true;
	}
}

bool Intervall::empty() const
{
	return m_empty;
}

double Intervall::borne_inf() const
{
	return m_inf;
}

double Intervall::borne_sup() const
{
	return m_sup;
}

Intervall Intervall::expo() const
{
	if (!this->empty()){

		return Intervall(std::exp(this->borne_inf()),std::exp(this->borne_sup()));
	}

	else{
		return Intervall();
	}
}

Intervall Intervall::sqr() const
{
	if (this->empty())
		return Intervall();
	else{


	if (this-> borne_sup()<0)
	{
		return Intervall();
	}
	if (this->borne_sup()>=0 and this->borne_inf()<0)
	{
		return Intervall(0,std::pow(this->borne_sup(),2));
	}
	else{
		return Intervall(std::pow(this->borne_inf(),2),std::pow(this->borne_sup(),2));
	}
}
}

Intervall Intervall::sqrt() const
{
	if (this->empty())
		return Intervall();
	else{


	if (this-> borne_sup()<0)
	{
		return Intervall();
	}
	if (this->borne_sup()>=0 and this->borne_inf()<0)
	{
		return Intervall(0,std::sqrt(this->borne_sup()));
	}
	else{
		return Intervall(std::sqrt(this->borne_inf()),std::sqrt(this->borne_sup()));
	}
}
}

Intervall Intervall::inverse(){
	double inf=900000000000;//l'infini
	if (this-> borne_inf()==0 and this-> borne_sup()==0){
		return Intervall();
	}
	if ((this->borne_sup()<0 and this->borne_inf()<0) or (this->borne_sup()>0 and this->borne_inf()>0)){
		return Intervall(1/(this->borne_sup()),1/(this->borne_inf()));
	}
	if (this->borne_sup()==0 and this->borne_inf()<0){

		return Intervall(-inf,1/this->borne_inf());
	}

	if (this->borne_inf()==0 and this->borne_sup()>0){

		return Intervall(1/this->borne_sup(),inf);
	}

	if (this->borne_sup()>0 and this->borne_inf()<0)
		return Intervall(-inf, +inf);
}

Intervall Intervall::prive_inter(const Intervall& I) const
{
	if (this->borne_sup()<I.borne_inf())
		return Intervall();
	if (this->borne_inf()<I.borne_inf() and this->borne_sup()<=I.borne_sup() and this->borne_sup()>I.borne_inf())
	{
		return Intervall(this->borne_inf(),I.borne_inf());
	}
	if (this->borne_inf()>=I.borne_inf() and this->borne_sup()>I.borne_sup() and this->borne_inf()<I.borne_sup())
	{
		return Intervall(I.borne_sup(),this->borne_sup());
	}

	else{
		return Intervall(this->borne_inf(),this->borne_sup());
	}

}

Intervall Intervall::inter_cst(float a)
{	
	double bor_inf=this-> borne_inf();
	double bor_sup=this-> borne_sup();
	if (a<0)
	{
		return Intervall(a*bor_sup,a*bor_inf);
	}
	else{
		return Intervall(a*bor_inf,a*bor_sup);
	}
}

std::ostream& operator<<(std::ostream& os,const Intervall& x)
{
	if (x.empty()==false)
	{
	
	if (x.borne_inf()==x.borne_sup())
	{
		os << "{" << x.borne_inf() << "}";
	}
	else{
		os << "[" << x.borne_inf() << "," << x.borne_sup() << "]";
	}
	}
	else{
		os<<"{}";
	}
  return os;
}

Intervall operator+(const Intervall& x, const Intervall& y)
{
	return Intervall(x.borne_inf()+y.borne_inf(),x.borne_sup()+y.borne_sup());
}

Intervall operator-(const Intervall& x, const Intervall& y)
{
	return Intervall(x.borne_inf()-y.borne_sup(),x.borne_sup()-y.borne_inf());
}

Intervall operator*(const Intervall& x,const Intervall& y)

{
	
	return Intervall(std::min(std::min(x.borne_inf()*y.borne_inf(),x.borne_inf()*y.borne_sup()),std::min(x.borne_sup()*y.borne_inf(),x.borne_sup()*y.borne_sup())),
		std::max(std::max(x.borne_inf()*y.borne_inf(),x.borne_inf()*y.borne_sup()),std::max(x.borne_sup()*y.borne_inf(),x.borne_sup()*y.borne_sup())));
}

Intervall operator/(const Intervall& x, const Intervall& y)
{
	double inf=900000000000;//l'infini
	if (y.borne_inf()==0 and y.borne_sup()==0){
		return Intervall();
	}
	if ((y.borne_sup()<0 and y.borne_inf()<0) or (y.borne_sup()>0 and y.borne_inf()>0)){
		return x*Intervall(1/(y.borne_sup()),1/(y.borne_inf()));
	}
	if (y.borne_sup()==0 and y.borne_inf()<0){

		return x*Intervall(-inf,1/y.borne_inf());
	}

	if (y.borne_inf()==0 and y.borne_sup()>0){

		return x*Intervall(1/y.borne_sup(),inf);
	}

	if (y.borne_sup()>0 and y.borne_inf()<0)
		return x*Intervall(-inf, +inf);
}

Intervall operator&(const Intervall& x, const Intervall& y)
{
	if (std::max(x.borne_inf(),y.borne_inf())<=std::min(x.borne_sup(),y.borne_sup()))
		return Intervall(std::max(x.borne_inf(),y.borne_inf()),std::min(x.borne_sup(),y.borne_sup()));
	else{
		return Intervall();
	}
}
Intervall operator|(const Intervall& x, const Intervall& y)
{
	
	return Intervall(std::min(x.borne_inf(),y.borne_inf()),std::max(x.borne_sup(),y.borne_sup()));
}