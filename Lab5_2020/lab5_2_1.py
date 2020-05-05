from numpy import random, pi
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

Ntrials, Nhits = 1_000_000, 0
for n in range(Ntrials):
    x, y, z = random.uniform(-1, 1, 3) # draw 2 samples, each uniformly distributed over (-1,1)
    if x**2 + y**2 + z**2 < 1:
        Nhits += 1

print("Monte Carlo estimator of V(3): %.5f" % ((2**3)*(Nhits / Ntrials)))
print("Actual value of V(3) up to 5 decimal digits: %.5f" % (4*pi/3))
print("The relative error is %.5f%%" % (100 * abs((2**3)*(Nhits / Ntrials) - (4*pi/3))))
