import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (10, 6)  # increase default figure size
np.random.seed(3112163)  # for reproducibility

def Ising(spins_init, Temp, nsteps=None):
    """
    Ising Model.
        spins_init: initial configuration
        Temp: the Temperature
        updates: the number of updates to perform
    """
    spins = spins_init.astype(np.int8)  # copy and save some space :)
    L = spins.shape[0]
    N = L * L
    kernel = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]], dtype=np.int8)
    Temp = Temp
    if nsteps is None:
        nsteps = L * L * 800  # number of updates

    for n in range(nsteps):
        r, c = np.random.randint(0, L, 2)  # select a vertex at random
        C = [(c-1) % L, c % L, (c + 1) % L]
        R = [[(r-1) % L], [r % L], [(r+1) % L]]
        DH = -spins[r, c] * np.sum(kernel * spins[R, C]) / Temp
        if np.log(np.random.rand()) < DH:
            spins[r, c] *= -1  # switch sign
    
    return spins

L = 64 
probOfWhite = .0
Temperature = 0.1
spins = 2 * (np.random.rand(L, L) > probOfWhite) - 1 

plt.imshow(spins, cmap='binary', vmin=-1, vmax=1, interpolation='nearest')
plt.title(r"Grid Size: $%d^2$" % (L))
plt.show()
plt.clf()
plt.cla()


for nsteps in [10,20,50,100,200,400,800 * L * L]:
    spins = Ising(spins,Temperature,nsteps)
    plt.imshow(spins, cmap='binary', vmin=-1, vmax=1, interpolation='nearest')
    plt.title("Temperature: %.1f, Grid Size: %d, Number of Steps: %d" % (Temperature, L, nsteps))
    plt.show()
    plt.cla()
    plt.clf()