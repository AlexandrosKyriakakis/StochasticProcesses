import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (10, 6)
rd.seed(3112163)
def randomWalk (start = 0, probs = [1/3,2/3]):
    x = start
    stepsFromZero = [1, 0]
    stepsFromNotZero = [1,-1]
    while True:  
        if (x == start):
            x += rd.choice(stepsFromZero, p=probs)
        else:
            x += rd.choice(stepsFromNotZero, p=probs)
        yield x  #

x100 = []

for i in range(1000):
    jonny = randomWalk()
    j = 0
    x = 0
    while(j<101):
        j+=1
        x = next(jonny)
    x100.append(x)
plt.hist(x100, bins=30, edgecolor='black', density=True)
plt.xlabel('Position')
plt.ylabel('Density')
plt.title('Position at $x_{100}$')
plt.show()

maxX_1000 = []

for i in range(1000):
    jonny = randomWalk()
    j = 0
    x = 0
    maxX = 0
    while(j<1001):
        j+=1
        x = next(jonny)
        if (x >= maxX): maxX = x
    maxX_1000.append(maxX)

print ("Mean of max(x_i), i <= 1000:", np.mean(maxX_1000) )
print ("Variance of max(x_i), i <= 1000:", np.var(maxX_1000) )

plt.hist(maxX_1000, bins=30, edgecolor='black', density=True)
plt.xlabel('Position')
plt.ylabel('Density')
plt.title('Position at $\max(x_i),\ 0 \leq i \leq 1000$')
plt.show()
