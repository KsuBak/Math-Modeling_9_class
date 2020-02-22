import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import animation

fig = plt.figure()
ax = p3.Axes3D(fig)

N=100
f = np.linspace(0,  2*np.pi, 100)
A = np.linspace(0, np.pi, 100)

a=2
b=3
c=4

x = a *np.sinh(A)*np.cos(f)
y = b *np.sinh(A)*np.sin(f)
z = c * np.sinh(A)

ball, = ax.plot(x, y, z, 'o')

def animation_func(i):
    ball.set_data(x[i],y[i])
    ball.set_3d_properties(z[i])
    
#ax.set_xlim3d([-1.0, 1.0])    
#ax.set_xlabel('X')
#
#ax.set_ylim3d([-1.0, 1.0])    
#ax.set_ylabel('Y')
#
#ax.set_zlim3d([-1.0, 1.0])    
#ax.set_zlabel('Z')

a=2
b=3
c=4

x1 =a * np.outer(np.cos(f), np.sinh(A))
y1 = b * np.outer(np.sin(f), np.sinh(A))
z1 =c * np.outer(np.ones(np.size(f)), np.sinh(A))

ax.plot_surface(x1, y1, z1, color= 'r')


ani= animation.FuncAnimation(fig, animation_func, N, interval=50)

ani.save('gh.gif')







