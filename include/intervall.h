#ifndef __INTERVALL_H__
#define __INTERVALL_H__

#include <iostream>

class Intervall

{
	public:
		Intervall();
		Intervall(double x);
		Intervall(double a,double b);
		Intervall prod_by_cst(float a);
		Intervall inverse();
		Intervall prive_inter(const Intervall& I) const;
		Intervall expo() const;
		Intervall sqr() const;
		Intervall sqrt() const;
		double borne_sup() const;
		double borne_inf() const;
		bool empty() const;


	private:
		double m_sup;
		double m_inf;
		bool m_empty;
};

#endif
std::ostream& operator<<(std::ostream& os,const Intervall& x);

Intervall operator+(const Intervall& x, const Intervall& y);
Intervall operator*(const Intervall&,const Intervall& y);
Intervall operator/(const Intervall&, const Intervall& y);
Intervall operator&(const Intervall&, const Intervall& y);
Intervall operator|(const Intervall&, const Intervall& y);
Intervall operator-(const Intervall& x, const Intervall& y);
double width(const Intervall& x);
Intervall left(const Intervall& x);
Intervall right(const Intervall& x);
Intervall maxi(const Intervall& x, const Intervall& y);
Intervall mini(const Intervall& x, const Intervall& y);