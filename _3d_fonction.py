from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from math import *

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

def f(x,y):
    a = [your function]
    return(a)

X = np.linspace(0, 100, 200)
Y = np.linspace(0, 100, 200)
x, y = np.meshgrid(X, Y)
Z = f(x,y)

ax.plot_surface(x, y, Z, cmap = cm.plasma, linewidth=0, antialiased=True)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.legend()

plt.show()