import numpy as np
from scipy.integrate import odeint 
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

year = 365*24*60*60
day = 24*60*60
years = 2
t = np.arange(0, years*year, 5*day)

l = 149 * 10**9

def move_func(s, t):
    (x1, v_x1, y1, v_y1,
     x2, v_x2, y2, v_y2,
     x3, v_x3, y3, v_y3)= s
     
    dxdt1= v_x1
    dv_xdt1 = ( k * q1* q2 / m1 * (x1- x2) / ((x1-x2)**2 + (y1-y2)**2)**1.5
             + k * q1* q3 / m1 * (x1 - x3) / ((x1 - x3)**2 + (y1 - y3)**2)**1.5)
     
    dydt1= v_y1
    dv_ydt1= ( k * q1* q2 / m1 * (y1- y2) / ((x1-x2)**2 + (y1-y2)**2)**1.5
            + k * q1* q3 / m1 * (y1 - y3) / ((x1 - x3)**2 + (y1 - y3)**2)**1.5)
            
    dxdt2= v_x2
    dv_xdt2= ( k * q1* q2 / m2 * (x2- x3) / ((x2-x1)**2 + (y2 - y1)**2)**1.5
            + k * q1* q3 / m2 * (x2- x3) / ((x2 - x3)**2 + (y2 - y3)**2)**1.5)
     
    dydt2= v_y2
    dv_ydt2= ( k * q1* q2 / m2 * (y2- y1) / ((x2-x1)**2 + (y2-y1)**2)**1.5
            + k * q1* q3 / m2 * (y2 - y3) / ((x2 - x3)**2 + (y2 - y3)**2)**1.5)
     
    dxdt3= v_x3
    dv_xdt3= ( k * q1* q2 / m3 * (x3- x1) / ((x3-x2)**2 + (y3-y1)**2)**1.5
            + k * q1* q3 / m3 * (x3 - x2) / ((x3 - x2)**2 + (y3 - y2)**2)**1.5)
     
    dydt3= v_y3
    dv_ydt3= ( k * q1* q2 / m3 * (y3- y1) / ((x3-x1)**2 + (y3-y1)**2)**1.5
            + k * q1* q3 / m3 * (y3 - y2) / ((x3 - x2)**2 + (y3 - y2)**2)**1.5)
     
    return (dxdt1, dv_xdt1, dydt1, dv_ydt1,
             dxdt2, dv_xdt2, dydt2, dv_ydt2, 
             dxdt3, dv_xdt3, dydt3, dv_ydt3 )


x11 = 0
v_x11 = -12000
y11 = (l**2- (l/2)**2)**0.5
v_y11 = 0
     
x22= -l/2
v_x22 = 0
y22 = 0
v_y22 = -20000

x33=l/2
v_x33 = 0
y33 = 0
v_y33 = 15000

s0 = (x11,v_x11, y11, v_y11,
      x22, v_x22, y22, v_y22,
      x33, v_x33, y33, v_y33)

m1 = 1*10**30
q1 = 1*10**20

m2 = 1*10**30
q2 = -1*10**20

m3 = 1*10**30
q3 = 1*10**20

k = 8.98755 * 10**9

sol = odeint(move_func, s0, t)

fig = plt.figure()
body = []

for i in range (0, len(t), 1):
    body1, = plt.plot(sol[:i, 0], sol[:i, 2], '-', color='r')
    body1_line, = plt.plot(sol[i, 0], sol[i, 2], 'o', color='r')

    body2, = plt.plot(sol[:i, 4], sol[:i, 6], '-', color='y')
    body2_line, = plt.plot(sol[i, 4], sol[i, 6], 'o', color='y' )

    body3, = plt.plot(sol[:i, 8], sol[:i, 10], '-', color='b')
    body3_line, = plt.plot(sol[i, 8], sol[i, 10], 'o', color='b')
    
                    
    
    body.append([body1, body1_line, body2, body2_line, body3, body3_line])
    
ani = ArtistAnimation(fig, body, interval= 100)
plt.axis('equal')
































ani.save('body.gif')