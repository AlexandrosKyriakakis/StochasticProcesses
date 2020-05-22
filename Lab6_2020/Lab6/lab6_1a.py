import numpy as np
from numpy import random as rd
from joblib import Parallel, delayed
from math import gamma, pi 
import matplotlib.pyplot as plt
rd.seed(12163)
def vol_Aux(d):
    x = rd.uniform(-1,1,d)
    return (sum(x ** 2) < 1)

def vol(N,d):
    # Parallel prossesing for more speed!!!
    results = Parallel(n_jobs=-1, backend="multiprocessing")(
             map(delayed(vol_Aux), [d for i in range(N)]))
    nhits = sum(results)
    return (2 ** d * nhits / N)


def Vol1(d):
    x = d/2
    return pi ** x / gamma(x + 1)

d = 2
N = 1_000_000
MonteCarlo = []
Actual = []
Error = []
while True:
    current = vol(N,d)
    if current == 0: break
    actual = Vol1(d)
    MonteCarlo.append(current)
    Actual.append(actual)
    Error.append(abs(actual - current))
    d += 1

plt.subplot()
plt.plot(MonteCarlo, color = 'b', label = 'Monte Carlo Est')
plt.plot(Actual, color = 'g', label = 'Actual')
plt.plot(Error, color = 'r', label = 'Error')
plt.xlabel(r'Dimensions d')
plt.ylabel(r'V($Sphere$)')
plt.title(r'$p(d) = \frac{\omega (d)}{2^d}$')
plt.legend()
plt.grid()
plt.show()
print( "Monte Carlo: ", np.array(MonteCarlo) )
print("Actual: ", np.array(Actual))
print("Error: ", np.array(Error))