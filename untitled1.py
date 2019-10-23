from conctant import gpad
from numpy import ndarray, arange
import numpy as np
x0=0
v0x=2
y0=0

t= arange(0, 5, 0.1)
print(t)
n=len(t)
txy= np.ndarray(shape=(n,3))
for i in range (0, n, 1):
    x=x0+v0x*t[i]
    y=y0+v0x*t[i]-(gpad*t[i]**2)/2
    txy[i,0]=x
    txy[i,1]=y
    txy[i,2]=t[i]
print(txy)