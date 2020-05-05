from numpy import random, pi

Ntrials, Nhits = 1_000_000, 0
for n in range(Ntrials):
    x, y = random.uniform(-1, 1, 2) # draw 2 samples, each uniformly distributed over (-1,1)
    if (x**2 + y**2)**2 <= 2*abs(x*y):
        Nhits += 1
print("Monte Carlo estimator of Pi: %.5f" % (4 * Nhits / Ntrials))
