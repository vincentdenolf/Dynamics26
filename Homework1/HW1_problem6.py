
## TO RUN
## python .\HW1_problem6.py

import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.integrate import solve_ivp

# define given system 
xDot = lambda x,y: -y+x * (1 - x**2 - y**2)
yDot = lambda x,y: x+y * (1 - x**2 - y**2)

# create grid to plot on
x = np.linspace(-10,10,1000)
y = np.linspace(-10,10,1000)
X,Y = np.meshgrid(x,y)

# evaluate system at grid points 
DX = xDot(X,Y)
DY = yDot(X,Y)

# create system to plot phase space trajectories
# takes in time and v = (x,y) vector
# time needed for solveivp function
def ODE_system(t, v):
    x, y = v
    return [xDot(x,y), yDot(x,y)]

# create some initial conditions to plot, v0 = (x0,y0)
v0 = []
for i in range (0,60):
    v0.append([random.uniform(-5,5),random.uniform(-5,5)])

# times to plot
times = [0,100]

# solve ivp with scipy, for all ICs
# solutions.y[0] = x(t) and solutions.y[1] = y(t)
for i in range(len(v0)):
    solutions = solve_ivp(ODE_system, times, v0[i])
    plt.plot(solutions.y[0], solutions.y[1], color = "teal")
    x = solutions.y[0]
    y = solutions.y[1]
    #arrIndicies = np.linspace(1, len(x)-2, 100, dtype = int)
    # for adding arrows
    arrowIndex= 1
    dx = x[arrowIndex+1] - x[arrowIndex]
    dy = y[arrowIndex+1] - y[arrowIndex]
    plt.quiver(x[arrowIndex], y[arrowIndex], dx, dy, color = "teal", scale = 30, headwidth = 2, headlength = 5, headaxislength = 5)
    
# use plt.contour for level curves at 0
# this plots nullclines
plt.contour(X, Y, DX, levels = [0], colors = "yellowgreen",linewidth =2)
plt.contour(X, Y, DY, levels = [0], colors = "coral", linewidth = 2)
# for nullcline legends
plt.plot([],[], color = "yellowgreen", label = "x-Nullcline")
plt.plot([],[], color = "coral", label = "y-Nullcline")
plt.plot([],[], color = "teal", label = "Trajectories")
plt.xlabel("x", fontsize = 16)
plt.ylabel("y", fontsize = 16)
plt.title("Nullclines and Phase Space Trajectories", fontsize = 18)
plt.grid()
plt.axis("equal")
plt.xlim(-5.5,5.5)
plt.ylim(-5.5,5.5)
plt.legend(fontsize = 12)
plt.show()