import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

## TO RUN
## python .\HW4_problem5.py

# paramaters
a = 0.2
b = 0.2
c = 5.7

# define driver system
def driver(t,x):
    xD,yD,zD = x
    x_Ddot = -yD - zD
    y_Ddot = xD + a*yD
    z_Ddot =  b + zD*(xD-c)

    return [x_Ddot,y_Ddot,z_Ddot]

# define response system
def response(t,x):
    xR,yR,zR = x
    xD,yD,zD = sol.sol(t)

    x_Rdot = -yR-zD -xR + xD
    y_Rdot = xR + (a+1)*yD - yR
    z_Rdot = b - c*zR + zD*xD

    return [x_Rdot,y_Rdot,z_Rdot]

# define times and IC
tvals = (0,300)
tvals_eval = np.linspace(*tvals, 20000)
tval_transient = 0
d0 = [0.5,1,-1]
#r0 = [-2,-1,0.25]
r0 = [20,-20,10]

# solve IVP
sol = solve_ivp(driver, tvals, d0, t_eval=tvals_eval, dense_output=True)
solR = solve_ivp(response, tvals, r0, t_eval=tvals_eval)

# discard transients
# i kept these for the last part
times_to_keep = sol.t >= tval_transient

xD = sol.y[0,times_to_keep]
yD = sol.y[1,times_to_keep]
zD = sol.y[2,times_to_keep]

times_to_keep_R = solR.t >= tval_transient
xR = solR.y[0,times_to_keep]
yR = solR.y[1,times_to_keep]
zR = solR.y[2,times_to_keep]

# plot attractors
fig = plt.figure()
ax = fig.add_subplot(111,projection = "3d")
ax.plot(xD, yD, zD, lw = 0.5, label = f"Driver System : IC = {d0}")
ax.plot(xR,yR,zR, lw = 0.5, label = f"Response System : IC = {r0}", linestyle = "--")
ax.set_xlabel(r"$x_D$")
ax.set_ylabel(r"$y_D$")
ax.set_zlabel(r"$z_D$")
#ax.set_title(f"Driver System with Time Horizon of T = {300}", fontsize = 18)
ax.set_title(f"Driver and Response System with Time Horizon of T = {300}", fontsize = 18)
ax.legend(fontsize = 12)
plt.tight_layout()
plt.show()