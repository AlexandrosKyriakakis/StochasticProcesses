import numpy as np
from joblib import Parallel, delayed
import matplotlib.pyplot as plt
np.random.seed(3112163)
def random_walk_next(state):
    if np.random.uniform() < 0.5:
        return 0
    return state + 1
def pi(k): return k/2**(k+1)

NA = 10**4
Sim = []
Real = []
Error = []
for N in range(1,NA,10):
    running_state = 0
    sum_result = 0
    
    for i in range(N):
        running_state = random_walk_next(running_state)
        sum_result += running_state

    realMath = sum([pi(k) for k in range(N)])
    Sim.append(sum_result/N)
    Real.append(realMath)
    Error.append(abs( sum_result/N - realMath ) )


plt.figure(figsize=(12, 7))
plt.subplot()
plt.plot(Sim, color = 'b', label = 'Simulated')
plt.plot(Real, color = 'g', label = 'Actual')
plt.plot(Error, color = 'r', label = 'Error')
plt.xlabel(r'Number of simulations')
plt.ylabel(r'Probability')
plt.title(r'$\sum^\infty_{k=0}k\pi (k)$')
plt.legend()
plt.grid()
plt.show()
plt.cla()
plt.clf()



### Ergodic Limit Theorem
print("The simulated ergodic average [X1+X2+X3+...+XN]/N is: %.4f" % (sum_result / N))
print("The real ergodic average is: %.4f" % (realMath))