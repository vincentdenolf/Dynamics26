import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

## TO RUN
## python .\HW4_problem2.py

# paramaters
alpha = 1
beta = 0.5

# dynamical system defined here
def system(t,X,epsilon):
    x,y,z = X
    
    xdot = y
    ydot = np.sin(x) * (z**2*np.cos(x) - 1) - epsilon*y
    zdot = alpha * (np.cos(x) - beta)

    return [xdot, ydot, zdot]

# define epsilon_0, the equilibirum, and the IC
epsilon_0 = (2 * alpha * np.sqrt(beta) * (1-beta**2))/(-(beta - 1/beta))
X_star = [np.arccos(beta),0,1/np.sqrt(beta)]
X0 = [X_star[0] + 0.5, X_star[1] + 0.5, X_star[2] + 0.5]

# two different values of epsilon to test
epsilon_val_unstable = 0.5 * epsilon_0
epsilon_val_stable = 1.5 * epsilon_0

# times we are plotting
tvals = (0,1000)
tvals_eval = np.linspace(*tvals, 20000)

# solution to system for given epsilon
sol_unstable = solve_ivp(system, tvals, X0, args=(epsilon_val_unstable,), t_eval=tvals_eval, dense_output=True)
sol_stable = solve_ivp(system, tvals, X0, args=(epsilon_val_stable,), t_eval=tvals_eval, dense_output=True)

# plotting code here
fig = plt.figure()
ax = fig.add_subplot(111,projection = "3d")

x,y,z = sol_unstable.y
x2,y2,z2 = sol_stable.y

ax.plot(x,y,z, lw = 0.5, label = fr"$\varepsilon = {epsilon_val_unstable}$")
ax.plot(x2,y2,z2, lw = 0.5, label = fr"$\varepsilon = {epsilon_val_stable}$")
ax.scatter(X_star[0], X_star[1], X_star[2], label = r"$x^*$", color = "red", s = 10)
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$y$")
ax.set_zlabel(r"$z$")
ax.set_title(fr"Trajectories for $\alpha = {alpha}, \beta = {beta}$, and $\varepsilon_0 = {epsilon_0}$")
plt.legend()
plt.tight_layout()
plt.show()

