import random as r
import matplotlib.pyplot as plt
from math import pi,gamma
import numpy as np
def Vol1(d):
    x = d/2
    return pi ** x / gamma(x + 1)

delta = 1.0
N = 100 # number of steps to approach equilibrium
samples = 1000 
Omega = 2
Mcmc = []
Actual = []
Error = []
for d in range(1,101):
    nhits = 0
    x = [0 for i in range(d)]  ## start at the centre of th disc. This variable will keep the position of the chain
    R_sq = 0.0  ## this variable keeps the squared distance from 0. It saves some computations to keep it

    for _ in range(N*samples):
        k = r.choice(range(d))  ## choose a jump direction at random
        z = r.uniform(-delta,delta) ## choose a jump size uniformly in (-delta,delta)
        x_prop_k = x[k] + z   ## propose a jump by z in the direction k
        R_sqprop = R_sq - x[k]**2+ x_prop_k**2 ## compute the squared distance from 0 after the proposed jump 
        if R_sqprop < 1.0: 
            R_sq = R_sqprop
            x[k]= x_prop_k   ## if the proposed jump leads to a point in the disc, then jump
        x_d_next = r.uniform(-delta,delta)
        R_sq_new = R_sq + x_d_next**2
        if R_sq_new < 1.0:
            nhits += 1

    result = 2*Omega*(nhits/(N*samples))
    Mcmc.append(result)
    Omega = result
    Actual.append(Vol1(d+1))
    Error.append(abs(result - Vol1(d+1)))


plt.subplot()
plt.plot(Mcmc, color = 'b', label = 'Ergodic MCMC')
plt.plot(Actual, color = 'g', label = 'Actual')
plt.plot(Error, color = 'r', label = 'Error')
plt.legend()
plt.grid()
plt.show()
plt.cla()
plt.clf()
print("MCMC : \n",np.array(Mcmc))
print("Actual : \n",np.array(Actual))
print("Error : \n",np.array(Error))