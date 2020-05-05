from numpy import random, pi
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Parameters
N = 10_000  # number of required points
Ntrials, Nhits = 0, 0
acc_x, acc_y, acc_z = [], [], []  # accepted x, y
rej_x, rej_y, rej_z = [], [], []  # rejected x, y

# Rejection Sampling
while Nhits < N:
    Ntrials += 1
    x, y, z = random.uniform(-1, 1, 3)

    if x**2 + y**2 + z**2 < 1:
        acc_x.append(x)
        acc_y.append(y)
        acc_z.append(z)
        Nhits += 1
    else:
        rej_x.append(x)
        rej_y.append(y)
        rej_z.append(z)

print("Total number of samples drawn %d" % Ntrials)
print("Number of samples in the disk %d" % N)


fig = plt.figure()
ax = fig.gca(projection='3d')

ax.scatter(acc_x, acc_y, acc_z, color = 'green', s = 1) # parameter s determines the size of each dot in the scatter plot
ax.scatter(rej_x, rej_y, rej_z, color = 'red', s = 1)

ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])
#ax.set_aspect('equal')  # set aspect ratio 1:1

plt.show()