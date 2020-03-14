import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

#
#L = Function ('L')
#f = Function ('f')
#vf = Function ('vf')
#
#t = Symbol('t')
#
#R = Symbol('R')
#w = Symbol('w')
#l = Symbol ('l')
#m = Symbol('m')
#g = 10
#
#L =((((m * (l**2)) / 2) * vf(t)**2 + m * R * l *( w**2) * cos(f(t)) - w * t ) +
#                 m * g * l * cos(f(t)))
#                 
#print (diff(L, f(t))) 
#
#print() 
#
#print (diff(diff(L, vf(t)), t))

N = 200
t = np.linspace (0, 4.3, N)

def move_func (s, t):
    f, v_f = s
    
    dfdt = v_f
    dv_dfdt = (-R*l*m*w**2*np.sin(f) - 10*l*m*np.sin(f))/(l**2*m)
    
    return dfdt, dv_dfdt

f0 = np.pi / 180 * 90
v_f0 = 5
s0 = f0, v_f0

g = 10
R = 1
l = 0.5
w = 0.1
m = 1
sol = odeint(move_func, s0, t)

x1 = R * np.sin(w * t[:]) 
y1 = -R * np.cos(w * t[:])

x2 = x1 + l * np.sin(sol[:, 0])
y2 = y1 + l * np.cos(sol[:, 0])

fig = plt.figure()
bodys = []


for i in range (0, len(t), 1):
    thisx = [0, x1[i], y1[i]]
    thisy = [0, x2[i], y2[i]]
       
    body_line, = plt.plot(thisx, thisy, '-o', color = 'g')
    bodys.append([body_line])
    
ani = ArtistAnimation(fig, bodys, interval=50)

ani.save('lagr.gif')    
    
    
    
    
    
    
    
    
    
    
    


               
