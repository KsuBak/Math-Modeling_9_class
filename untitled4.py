import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.axes3d as p3

fig = plt.figure()
ax = p3.Axes3D(fig)

f = np.linspace(0,  2*np.pi, 100)
A = np.linspace(0, 2*np.pi, 100)

a=2
b=3
c=4

x =a * np.outer(np.cos(f), np.sinh(A))
y = b * np.outer(np.sin(f), np.sinh(A))
z =c * np.outer(np.ones(np.size(f)), np.sinh(A))

ax.plot_surface(x, y, z, color= 'r')
plt.show()







