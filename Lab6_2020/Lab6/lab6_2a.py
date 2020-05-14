import random as r
import matplotlib.pyplot as plt
delta = 1.0
for delta in [1.0,0.01,20.0]:
    N = 100 # number of steps to approach equilibrium
    samples = 1000 
    point_x = []
    point_y = []

    for _ in range(samples):
        x = [0,0]  ## start at the centre of th disc. This variable will keep the position of the chain
        R_sq = 0.0  ## this variable keeps the squared distance from 0. It saves some computations to keep it

        for _ in range(N):
            k = r.choice([0,1])  ## choose a jump direction at random
            z = r.uniform(-delta,delta) ## choose a jump size uniformly in (-delta,delta)
            x_prop_k = x[k] + z   ## propose a jump by z in the direction k
            R_sqprop = R_sq - x[k]**2+ x_prop_k**2 ## compute the squared distance from 0 after the proposed jump 
            if R_sqprop < 1.0: 
                R_sq = R_sqprop
                x[k]= x_prop_k   ## if the proposed jump leads to a point in the disc, then jump
    
        point_x.append(x[0])
        point_y.append(x[1])
    plt.subplot()
    plt.scatter(point_x,point_y)
    plt.show()
    plt.cla()
    plt.clf()