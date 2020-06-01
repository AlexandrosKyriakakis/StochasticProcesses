import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import argparse


np.random.seed(2017)


if __name__ == "__main__":

    # Parse arguments from command line
    parser = argparse.ArgumentParser(description="Simulate the Ising model")
    parser.add_argument("-T", "--Temp", type=float, help="Temperature", required=True)
    parser.add_argument("-L", type=int, default=64, help="The size of the lattice side")
    parser.add_argument("-up", type=float, default=0.5,
                        help="The ratio of up-spined particles to the total number of particles")
    parser.add_argument("-i", "--interval", type=int, default=10, help="The size of the lattice side")

    args = parser.parse_args()
    L = args.L
    interval = args.interval
    Temp = args.Temp
    down_rt = 1 - args.up
    if down_rt > 1.0 or down_rt < 0.0:
        raise ValueError("-up should be in the [0,1] interval")
    spins = 2 * (np.random.rand(L, L) > down_rt) - 1  # random table of {1, -1}

    # Parameters
    N = L * L  # number of particles
    kernel = np.array([[0., 0., 0.], [0., 0., 0.], [0., 0., 0.]])

    fig = plt.figure()


    # Plot initial state
    im = plt.imshow(spins, cmap='binary', vmin=-1, vmax=1,
                    interpolation='nearest', animated=True)


    # update lattice
    def updatefig(*args):
        global spins

        ## same as previous loop-iteration
        r, c = np.random.randint(0, L, 2)
        R = np.array([r - 1, r, r + 1]) % L
        R = [[r] for r in R]  # because numpy is weird...
        C = np.array([c - 1, c, c + 1]) % L
        DH = spins[r, c] * np.sum(kernel * spins[R, C])
        if np.random.rand() < np.exp(- DH / Temp):
            spins[r, c] *= -1  # switch sign

        ## redraw and return image
        im.set_array(spins)
        return im,

    # Make animation
    anim = animation.FuncAnimation(fig, updatefig,
                                   repeat = False,
                                   interval=interval, blit=True)

    plt.show()

