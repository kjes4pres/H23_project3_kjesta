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

# plt.savefig("random_walk_2D.png")
# plt.show()


def many_random_walks_2D(M=5, N=500) -> np.ndarray:
    """
    Simulation of many random walkers in 2D-

    Input:
    M : number of walkers (int)

    N : number of steps each walker takes (int)

    Output:
    r: numpy array, storing the positions of each walker.
    """

    r = np.zeros((N + 1, 2, M))
    dr = [(1, 0), (0, 0), (-1, 0), (0, 1), (0, 0), (0, -1)]

    for i in range(M):
        for j in range(1, N + 1):
            step = dr[np.random.randint(6)]
            r[j, 0, i] = r[j - 1, 0, i] + step[0]
            r[j, 1, i] = r[j - 1, 1, i] + step[1]

    return r


R = many_random_walks_2D()
X = R[:, 0, :]
Y = R[:, 1, :]

fig, ax = plt.subplots()
ax.plot(X, Y)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("Random Walk in 2D")
ax.grid()
ax.axis("equal")

plt.savefig("many_random_2D.png")
plt.show()
