import numpy as np
import matplotlib.pyplot as plt

## TO RUN
## python .\HW2_problem5.py

def W(x ,N, alpha): 
    func = 0
    for n in range(0,N):
        func = func + 2**(-n*alpha) * np.cos((2**n)*x)
    return func

Nmax = 1000
alpha = 0.5
x = np.linspace(-np.pi,np.pi, 500)
y = np.zeros_like(x)

for i, xi in enumerate(x):
    y[i] = W(xi,1000, 0.5)

plt.figure()
plt.plot(x,y)
plt.xlabel(r"$x$", fontsize = 18)
plt.ylabel(r"$W(x)$", fontsize = 18)
plt.title(r"Approximaton to $W(x)$ with 1000 Terms and $\alpha = 0.5$", fontsize = 20)
plt.tick_params(axis = "both", which = "major", labelsize = 12)
plt.grid(True)
plt.show()