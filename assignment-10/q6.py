# The bisection method is a technique for finding solutions (roots) to equations with a single
# unknown variable. Given a polynomial function f, try to find an initial interval off by
# random probe. Store all the updates in an Numpy array. Plot the root finding process using
# the matplotlib/pyplot library.

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 - 4*x -9

def init_intervals():
    a,b = np.random.uniform(-10,10,2) #random picking of 2 values between -10 and 10
    while f(a) * f(b) >=0:
        a,b = np.random.uniform(-10,10,2)
    return min(a,b) , max(a,b) #ensuring a <b

def rootApproximator(tol = 1e-6, max_iter = 100):
    a,b = init_intervals()
    approxRoots = []
    iterations = []
    for i in range(max_iter):
        c = (a+b)/2 #finding the approx roots as midpoint
        approxRoots.append(c)
        iterations.append(i)

        if(abs(f(c)) < tol):
            break
        elif f(a)*f(c) <0:
            b =c
        else:
            a =c
    return np.array(iterations),np.array(approxRoots),c


def plotter(iterations,approxRoots):
    plt.plot(iterations,approxRoots, marker= 'o', color ='b' ,linestyle = '-', label = 'Approximated root')
    plt.axhline(y=approxRoots[-1],color = 'r', linestyle =  '--', label = f'Final root:{approxRoots[-1]:.6f}')

    plt.xlabel('iteration')
    plt.ylabel('approximated root value')
    plt.title('Bisection Method Convergence')
    plt.legend()
    plt.grid(True)
    plt.show()


iterations,approxRoots,c = rootApproximator()
plotter(iterations,approxRoots)