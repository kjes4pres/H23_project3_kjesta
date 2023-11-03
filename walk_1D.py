import numpy as np
import matplotlib.pyplot as plt

seed = 1910

rng = np.random.default_rng(seed)


def random_walk_1D(N=50):
    """
    A random walker in 1D

    Input:
    N : number of steps for the walker

    Output:
    x: numpy array, storing the positions of the walker.

    """
    x = np.zeros(N + 1)

    for i in range(N):
        x[i + 1] = x[i] + rng.choice([-1, 0, 1])

    return x


plt.plot(random_walk_1D())
plt.xlabel("Nr. of steps")
plt.ylabel("Displacement")
plt.title("Random walk in 1D")
plt.grid()
plt.show()


def many_random_walks_1D(M=1000, N=500):
    """
    Simulation of many random walkers in 1D-

    Input:
    M : number of walkers

    N : number of steps each walker takes

    Output:
    x: numpy array, storing the positions of each walker.
    """
    x = np.zeros((N + 1, M))
    x[0, :] = 0
    steps = rng.choice(([-1, 0, 1]), size=(N, M))
    x[1:, :] = np.cumsum(steps, axis=0)

    return x


plt.plot(many_random_walks_1D(), linewidth=0.5)
plt.xlabel("Nr. of steps")
plt.ylabel("Displacement")
plt.title(f"1000 random walkers in 1D")
plt.grid()
plt.show()
