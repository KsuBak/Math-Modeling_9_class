import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.axes3d as p3

fig = plt.figure()
ax = p3.Axes3D(fig)

f = np.linspace(0,  2*np.pi, 100)
A = np.linspace(0, 10*np.pi, 100)

m=10
l=2
n=4

x = np.outer(f, np.cos(A)) + l*np.outer(np.ones(np.size(f)), A)
y = np.outer(f, np.sin(A))+ m*np.outer(np.ones(np.size(f)), A)
z = h*np.outer(np.ones(np.size(f)), A)

ax.plot_surface(x, y, z, color= 'r')
plt.show()