import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
from scipy.integrate import simpson

# function to evaluate operator on function f
def T(f,lambd,x):
    integral = np.zeros_like(x)
    for i,xi in enumerate(x):
        integrand = f/(1+(xi-x)**2)
        integral[i] = simpson(integrand, x=x)
    return np.sin(2*np.pi*x) + lambd * integral


# TEST HERE
x = np.linspace(-1,1,100)
y = np.linspace(-1,1,100)

# change g to the initial guess you want
g = lambda x: x**2
f = g(y)

# change lambda here
lambd = 0.8

applications = []
Tk = f.copy()
applications.append(Tk.copy())
for k in range(1,21):
    print("starting evaluation", k)
    Tk = T(Tk,lambd,x)
    applications.append(Tk.copy())

plt.figure()
# enumterate through functions and keep track of index
for k,func in enumerate(applications, start = 0):
    print("plotting eval ", k)
    plt.plot(x,func, alpha = 0.8, label = f"T^{k}(f)")

plt.legend(fontsize = 10)
plt.ylabel("T(f)", fontsize = 18)
plt.xlabel("x",fontsize = 18)
plt.title(r"$\text{Fixed Point Iterations for } f_0 = x^2, \lambda = 0.8$",fontsize = 20)
plt.tick_params(axis = "both", which = "major", labelsize = 12)
plt.grid(True)

plt.show()