from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from math import *

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

def f(x,y):
    a = ((np.sin((np.sqrt(x**2 + y**2))/3.2))/2) * (1.0385**(-1*(np.sqrt(x**2 + y**2))))
    return(a)

X = np.linspace(-80, 80, 400)
Y = np.linspace(-80, 80, 400)
x, y = np.meshgrid(X, Y)
Z = f(x,y)

ax.plot_surface(x, y, Z, cmap = cm.plasma, linewidth=0, antialiased=True)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.legend()

plt.show()
