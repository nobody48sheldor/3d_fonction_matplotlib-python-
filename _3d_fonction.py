#importing packages

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from math import *

#define the graphic

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

#define function

def f(x,y):
    a = #your function
    return(a)

X = np.linspace(0, 100, 200)
Y = np.linspace(0, 100, 200)

#making x and y 2d

x, y = np.meshgrid(X, Y)

#define z as the function you define earlyer

Z = f(x,y)

#define the renders

ax.plot_surface(x, y, Z, cmap = cm.plasma, linewidth=0, antialiased=True)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.legend()

#displaying the plot

plt.show()
