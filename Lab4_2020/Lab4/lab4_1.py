import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (10, 6)
#rd.seed(3112163)
def randomWalkZ (start, probs):
    x = start
    steps = [1, -1]  # probs order should be (left, right)
    while True:  # continue for ever in needed
        x += rd.choice(steps, p=probs)
        yield x  #

upperB = 100
lowerB = -70

fig, ax = plt.subplots()
comTime = []
impTime = []
N = 500
for i in  range(N):
    communist = randomWalkZ(0,(1/5,4/5))
    imperialist = randomWalkZ(0,(4/5,1/5))
    com = []
    imp = []
    iterator = 0
    time = 0
    while (lowerB <= iterator <= upperB):
        time += 1
        iterator = next(communist)
        com.append(iterator)
    comTime.append(time)
    ax.plot(com, color = 'r', alpha = 0.5)
    iterator = 0
    time = 0
    while (lowerB <= iterator <= upperB):
        time += 1
        iterator = next(imperialist)
        imp.append(iterator)
    impTime.append(time)
    ax.plot(imp, color = 'b', alpha = 0.5)
ax.grid()
plt.axhspan(lowerB, upperB, color = '#cccccc', alpha = 0.8)
plt.xlabel("Time")
plt.ylabel("Position")
plt.title("Random Walks on Z")
plt.show()

#fig, ax = plt.subplots()
plt.hist(comTime, bins=30,alpha = 0.5, color = 'r', edgecolor='black', density=True)
plt.hist(impTime, bins=30,alpha = 0.5, color = 'b', edgecolor='black', density=True)
plt.xlabel('Time')
plt.ylabel('Density')
plt.title('Escape Times')
plt.show()