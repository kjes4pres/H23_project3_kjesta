import numpy as np
import matplotlib.pyplot as plt

seed = 1910

rng = np.random.default_rng(seed)


def random_walk_1D(N=50) -> np.ndarray:
    """
    A random walker in 1D

    Input:
    N : number of steps for the walker (int)

    Output:
    x: numpy array, storing the positions of the walker.

    """
    x = np.zeros(N + 1)

    for i in range(N):
        x[i + 1] = x[i] + rng.choice([-1, 0, 1])

    return x


X = random_walk_1D()

plt.plot(X)
plt.xlabel("Nr. of steps")
plt.ylabel("Displacement")
plt.title("Random walk in 1D")
plt.grid()
# plt.savefig("random_walk_1D.png")
# plt.show()


def many_random_walks_1D(M=1000, N=500) -> np.ndarray:
    """
    Simulation of many random walkers in 1D-

    Input:
    M : number of walkers (int)

    N : number of steps each walker takes (int)

    Output:
    x: numpy array, storing the positions of each walker.
    """
    x = np.zeros((N + 1, M))
    x[0, :] = 0
    steps = rng.choice(([-1, 0, 1]), size=(N, M))
    x[1:, :] = np.cumsum(steps, axis=0)

    return x


X = many_random_walks_1D()

plt.plot(X, alpha=0.5, linewidth=0.5)
plt.xlabel("Nr. of steps")
plt.ylabel("Displacement")
plt.title(f"1000 random walkers in 1D")
plt.grid()
# plt.savefig("many_random_1D.png")
# plt.show()

ten = X[:, :10]
hundred = X[:, :100]
thousand = X[:, :1000]

time_steps = np.arange(501)
analytical_mean = np.zeros(500)
analytical_RMS = np.sqrt(np.arange(501) * (2 / 3))


fig, ax = plt.subplots(2, 1, figsize=(6, 6))
fig.suptitle("Statistical properties of walkers")

ax[0].set_title("Mean displacement")
ax[0].plot(time_steps, np.mean(ten, axis=1), label="10 walkers")
ax[0].plot(time_steps, np.mean(hundred, axis=1), label="100 walkers")
ax[0].plot(time_steps, np.mean(thousand, axis=1), label="1000 walkers")
ax[0].plot(analytical_mean, "--", label="analytical")
ax[0].set_xlabel("Nr. of steps")
ax[0].set_ylabel("Mean displacement")
ax[0].legend()
ax[0].grid()

ax[1].set_title("RMS")
ax[1].plot(time_steps, np.sqrt(np.mean(ten**2, axis=1)), label="10 walkers")
ax[1].plot(time_steps, np.sqrt(np.mean(hundred**2, axis=1)), label="100 walkers")
ax[1].plot(time_steps, np.sqrt(np.mean(thousand**2, axis=1)), label="1000 walkers")
ax[1].plot(analytical_RMS, "--", label="analytical")
ax[1].set_xlabel("Nr. of steps")
ax[1].set_ylabel("RMS")
ax[1].legend()
ax[1].grid()

plt.subplots_adjust(hspace=0.5)
# plt.savefig("statistical_1D.png")
# plt.show()
