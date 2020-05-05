from numpy import random, pi, mean

Ntrials, Nhits = 1_000_000, 0
absXPlusY = []
for n in range(Ntrials):
    x, y = random.uniform(-1, 1, 2) # draw 2 samples, each uniformly distributed over (-1,1)
    if (x**2 + y**2)**2 <= 2*abs(x*y):
        absXPlusY.append(abs(x+y))
        Nhits += 1
VL = 4 * Nhits / Ntrials
print("Monte Carlo estimator of V(L): %.5f" % (VL))
print("Monte Carlo estimator of I: %.5f" % (VL * mean(absXPlusY)))