import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


fig, ax = plt.subplots()

acok, = plt.plot([], [], 'r-')
xdata, ydata = [], []

# =============================================================================
ax.set_xlim(-10, 10)
ax.set_ylim(10, -10)
# =============================================================================
R = 5

def icok(t):
    xdata.append(R *np.cos(t)**3)
    ydata.append(R *np.sin(t)**3)
    acok.set_data(xdata, ydata)
    
ani = FuncAnimation(fig,
                    icok,
                    frames=np.arange(0, 15*np.pi, 0.1),
                    interval=10)
                  
ani.save('ani.gif')
