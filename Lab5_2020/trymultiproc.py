from joblib import Parallel, delayed
from numpy import random, pi, mean

Ntrials, Nhits = 1_000_000, 0
def myproc(i):
    global Nhits, absXPlusY
    x, y = random.uniform(-1, 1, 2) # draw 2 samples, each uniformly distributed over (-1,1)
    if (x**2 + y**2)**2 <= 2*abs(x*y):
        return (True,abs(x+y))
    return (False,0)

results = Parallel(n_jobs=-1, backend="multiprocessing")(
             map(delayed(myproc), range(Ntrials)))
Nhits = []
absXPlusY = []
for i,j in results:
    Nhits.append(i) 
    if j != 0:
        absXPlusY.append(j) 

Nhits = sum(Nhits)
VL = 4 * Nhits / Ntrials
print("Monte Carlo estimator of V(L): %.5f" % (VL))
print("Monte Carlo estimator of I: %.5f" % (VL * mean(absXPlusY)))


     
 
     
