from math import gamma, pi 
import numpy as np
import matplotlib.pyplot as plt

def Vol1(d):
    x = d/2
    return (pi ** x / gamma(x + 1))/2**d

plt.subplot()
plt.plot([d-np.log(Vol1(d)) for d in range(100)] )
plt.xlabel(r'Dimensions d')
plt.ylabel(r'$d - \log{p(d)}$')
plt.grid()
plt.show()
plt.cla()
plt.clf()

plt.subplot()
plt.plot([np.log(Vol1(d)) for d in range(100)] )
plt.xlabel(r'Dimensions d')
plt.ylabel(r'$d - \log{p(d)}$')
plt.grid()
plt.show()

#print (1e11/2.46)