from math import cos, tan, pi, e
from conctant import gpad, k, h
x=100
b=pi/5
a=pi/3
T=200
z=300
v=((gpad*x*1/tan(b)**2)/(2*cos(a)**2*(1-1/tan(b)*1/tan(a))))**0.5
print(v)
n=(2/pi**0.5)*(h/(k*T)**(1.5))*e**((-z/k*T)*z*(T/2))
print(n)


