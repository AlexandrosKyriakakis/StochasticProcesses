import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (10, 6)
rd.seed(3112163)

def rand_walk_Z2(start=(0, 0), probs=(0.25, 0.25, 0.25, 0.25)):
    # probs order (left, right, bottom, up)
    x, y = start
    steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while True:
        dx, dy = steps[rd.choice(4, p=probs)]  # choice(4) = choose a number in [0,3]
        x, y = x + dx, y + dy
        yield x, y

r = 20  # radius of circle boundary
escapeTime = []
radius = range(10,110,10)
for r in radius:
    r2 = r**2  # square of radius


    escape_time = []
    for n in range(100):
        walker = rand_walk_Z2()
        x, y = (0, 0)
        t = 0
        while x**2 + y**2 < r2:
            x, y = next(walker)
            t += 1
        escape_time.append(t)
    escapeTime.append(np.mean(escape_time))
line = np.polyfit(np.log10(radius),np.log10(escapeTime),1)
print ("The Slope of this line is", line[0])
plt.subplot()
plt.loglog(radius, escapeTime)

#plt.yscale('log')
plt.xlabel('Radius')
plt.ylabel('Escape Time')
plt.title('Average Escape Time at given radius')
plt.grid()
plt.show()