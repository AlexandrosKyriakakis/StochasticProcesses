import numpy as np

np.random.seed(3112163)
def random_walk_next(state):
    if np.random.uniform() < 0.5:
        return 0
    return state + 1

N = 10000
running_state = 0
sum_result = 0

for i in range(N):
    running_state = random_walk_next(running_state)
    sum_result += 2*np.cos(running_state + np.cos(running_state) )

real = sum([np.cos(k + np.cos(k))/(2**k) if k<=1000 else 0 for k in range(N)])
### Ergodic Limit Theorem
print("The simulated ergodic average [F(X1)+F(X2)+F(X3)+...+F(XN)]/N is: %.4f" % (sum_result / N))
print("The Real ergodic average is: {}".format(real))