import random as rd
import matplotlib.pyplot as plt
import numpy as np

a = [False for x in range(1000)]
track = []
N = 100000
for i in range(N):
    b = rd.choice(range(1000))
    a[b] = not a[b]
    track.append(sum(a))
    #print (rd.choice(a))
kapa = np.mean(track)
b = [kapa for x in range(N)]
lapa = np.std(track)
c = [lapa + kapa for x in range(N)]
d = [-lapa + kapa for x in range(N)]
plt.plot(track)
plt.plot(b, color = "red")
plt.plot(c, color = "green")
plt.plot(d, color = "green")
plt.grid()
plt.show()
print (np.std(track))