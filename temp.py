import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.axes3d as p3
from sympy import *

f = Function('f')
x = Function('x')
y = Function('y')
z = Function('z')

t = Symbol('t')
a = Symbol('a')
b = Symbol('b')
c = Symbol('c') 
    
f = x(t)**2/a**2 + y(t)**2/b**2 + z(t)**2/c**2 - 1 

print (diff(f, x(t)))

print (diff(f, y(t)))

print (diff(f, z(t)))

print (diff(f, t))

print (diff(diff(f, t), t))  







