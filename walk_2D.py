import numpy as np
import matplotlib.pyplot as plt

seed = 1910

rng = np.random.default_rng(seed)


def random_walk_2D(N=50) -> np.ndarray:
    """
    A random walker in 2D

    Input:
    N : number of steps for the walker (int)

    Output:
    r: numpy array, storing the positions of the walker.

    """
    r = np.zeros((N + 1, 2))
    dr = [(1, 0), (0, 0), (-1, 0), (0, 1), (0, 0), (0, -1)]

    for i in range(N):
        step = dr[np.random.randint(6)]
        r[i + 1, :] = r[i, :] + step

    return r


R = random_walk_2D()
X = R[:, 0]
Y = R[:, 1]

fig, ax = plt.subplots()
ax.plot(X, Y)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("Random Walk in 2D")
ax.grid()
ax.axis("equal")

plt.show()
