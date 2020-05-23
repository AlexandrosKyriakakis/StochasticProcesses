import numpy as np
np.random.seed(3112163)
def random_walk_next(state):
    if np.random.uniform() < 0.5:
        return 0
    return state + 1
result = []
for _ in range(50):
    N = 10**4
    running_state = 0
    sum_result = 0

    for i in range(N):
        running_state = random_walk_next(running_state)
        sum_result += running_state
    result.append(sum_result / N)
firstVar = np.var(result)
print("The simulated ergodic variance is: %.6f" % (firstVar))