from math import gamma, pi 
from numpy import random


#def vol(N,d):
#    nhits = 0
#    for i in range(N):
#        x = random.uniform(-1,1,d)
#        if sum(x ** 2) < 1: 
#            nhits += 1
#    return 2 ** d * nhits / N
#
#d = 2
#N = 1_000_000       
#print ("The Monte Carlo estimate of ω(", d,") is  : %.5f " % vol (N,d))
#
#
#def Vol1(d):
#    x = d/2
#    return pi ** x / gamma(x + 1)
#
#print("The actual value of ω(", d,") is  : %.5f " % Vol1(d))
print((5*10**4)/60/60)