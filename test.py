from Lagrange import *
import numpy as np
import matplotlib.pyplot as plt


N = 3
a = 0
b = np.pi


X = np.linspace(a,b,N)
x = np.linspace(a,b,1000)

f = lambda x : np.sin(x)

plt.plot(x,f(x),label='original function')


divided_diff = divided_differences(f,X)
plt.plot(x,evaluate_lagrange_polynomial(X,divided_diff,x),label="Approximated function")
plt.legend()
plt.show()