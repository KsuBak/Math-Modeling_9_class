import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


fig, ax = plt.subplots()

cik, = plt.plot([], [], 'o')
xdata, ydata = [], []

# =============================================================================
# ax.set_xlim(0, 10)
# ax.set_ylim(-10, 10)
# =============================================================================
R = 5

def cok(t):
    xdata.append(5 * (t - np.sin(t)))
    ydata.append(5 * (1 - np.cos(t)))
    cik.set_data(xdata, ydata)
    
ani = FuncAnimation(fig,
                    cok,
                    frames=np.arange(0, 6*np.pi, 0.1),
                    interval=100)
                  
ani.save('ani.gif')
