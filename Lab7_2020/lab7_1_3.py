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
result = []
j = 0
while True:
    j+=1
    for _ in range(50):
        N = j*10**4
        running_state = 0
        sum_result = 0

        for i in range(N):
            running_state = random_walk_next(running_state)
            sum_result += running_state
        result.append(sum_result / N)
    if (np.var(result) <= firstVar/2): break

print("For half variance we need {} times N samples".format(j))