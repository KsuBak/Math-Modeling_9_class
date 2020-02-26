import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.axes3d as p3

N = 100
t = np.linspace(0, 5, N)
A = np.linspace(0, np.pi, 100)
f = np.linspace(0,  2*np.pi, 100)
fig = plt.figure()
ax = p3.Axes3D(fig)

def move_func(s, t):
    x, v_x, y, v_y, z, v_z = s
    dxdt = v_x
    dv_xdt = x/a**2 * ((g - v_x**2/a**2 - v_y**2/b**2 - v_z**2/c**2 )/
    (x**2/a**4 + y**2/b**4 + z**2/c**4))
    
    dydt = v_y
    dv_ydt = y/b**2 *( (g - v_x**2/a**2 - v_y**2/b**2 - v_z**2/c**2 )/
    (x**2/a**4 + y**2/b**4 + z**2/c**4))
    
    dzdt = v_z
    dv_zdt= - g + x/a**2 * ((g - v_x**2/a**2 - v_y**2/b**2 - v_z**2/c**2 )/
    (x**2/a**4 + y**2/b**4 + z**2/c**4))
    
    return dxdt, dv_xdt, dydt, dv_ydt, dzdt, dv_zdt
 
x0 = 9    
v_x0 = 0

y0 = 3
v_y0 = 0

s0 = x0, v_x0, y0, v_y0

g = 9.8

a = 1
b = 1
c = 1

ball, = ax.plot(x, y, z, 'o')

def animation_func(i):
    ball.set_data(x[i],y[i])
    ball.set_3d_properties(z[i])
       
x = sol[:, 0]
y = sol[:, 2]
z = sol[:, 4]


ani= animation.FuncAnimation(fig, animation_func, N, interval=50)

ani.save('gh.gif')








