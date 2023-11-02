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
plt.xlabel("Steps")
plt.ylabel("x")
plt.title("Random walk in 1D")
plt.grid()
plt.show()
