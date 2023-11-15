import labyrinths as lb
import numpy as np
import matplotlib.pyplot as plt
import time
import pstats

seed = 1910
rng = np.random.default_rng(seed)


class MazeWalker:
    """
    A class for initilazing random walkers in a maze.
    The class contains methods for moving the walkers,
    removing illegal steps (boundaries of the maze) and property
    methods for assessing the walkers positions.

    Parameters:
    ----------
    M: number of walkers
    maze: numpy array defining the maze
    rng: pseudorandom number generator
    r0: starting positions of all walkers
    """

    def __init__(
        self,
        M: int,
        maze: np.ndarray,
        rng: np.random.Generator,
        r0: tuple[int, int] = np.array([1, 1]),
        endpoints: list[tuple] = [],
    ) -> None:
        self._M = M
        self._maze = maze
        self._rng = rng
        self.r0 = r0
        self.initialize_walkers(r0)
        self.endpoints = endpoints

    @property
    def M(self) -> int:
        return self._M

    @property
    def maze(self) -> np.ndarray:
        return self._maze

    def initialize_walkers(self, r0: tuple[int, int]) -> None:
        """
        Initializing the walkers starting positions.

        Input:
        r0: Starting position, as (x,y) coordinate

        Parameters:
        _positios: numpy array for storing each walkers position.
        """
        if self._maze[(r0[0], r0[1])] == False:
            raise lb.InvalidSquareError("Starting position is inside a wall!")

        self._positions = np.zeros((self._M, 2), dtype=int)
        self._positions[:, 0] = r0[0]
        self._positions[:, 1] = r0[1]

    @property
    def x(self) -> np.ndarray:
        return self._positions[:, 0]

    @property
    def y(self) -> np.ndarray:
        return self._positions[:, 1]

    def move(self) -> None:
        """
        Method for moving each walker by one step.
        Walker stays still if it has reached the end point.
        """
        steps = self._rng.integers(-1, 2, size=(self._M, 2))
        legal_steps = self._remove_illegal(steps)
        is_it_done = self.not_finished()

        self._positions[is_it_done] += legal_steps[is_it_done]

    def _remove_illegal(self, dr: np.ndarray) -> np.ndarray:
        """
        Method for removing illegal steps, and replacing by (0,0),
        making the walker stand still.

        Output:
        dr: numpy array containing the next step for all walkers, with no illegal steps.

        """
        new_positions = self._positions + dr
        valid_indices = self._maze[new_positions[:, 0], new_positions[:, 1]]
        dr[~valid_indices] = 0
        return dr

    def not_finished(self) -> np.ndarray:
        """
        Method for checking if a walker has reached the end point in the maze.

        Output:
        is_it_done: boolean array, value True if the walker has not reached the endpoint.
        False if the walker is at an endpoint.
        """
        position_in_endpoint = np.array(
            [tuple(pos) in self.endpoints for pos in self._positions], dtype=bool
        )
        is_it_done = np.ones(self._M, dtype=bool)
        is_it_done[position_in_endpoint] = False
        return is_it_done


if __name__ == "__main__":
    # 3e
    # maze = lb.circular()
    # walkers = MazeWalker(M=500, maze=maze, rng=rng, r0=(100, 100))
    # animation = lb.Animation(walkers)
    # animation.animate(N=200)

    # 3h
    maze = lb.layered_labyrinth(layers=2)
    line = maze.shape[1] - 2
    start_points = lb.get_legal_line(maze, y=line)
    endpoints = lb.get_legal_line(maze, y=1)

    # walkers = MazeWalker(
    #     M=100_000, maze=maze, rng=rng, r0=start_points[1], endpoints=endpoints
    # )
    # animation = lb.Animation(walkers)
    # animation.animate(N=2000, interval=1, size=5)

    # finished_walkers = 100_000 - np.sum(walkers.not_finished())
    # print(f"{finished_walkers} walkers reached an end point.")

    # plt.hist(
    #     walkers._positions[:, 0],
    #     bins=maze.shape[0],
    #     range=(0, maze.shape[0]),
    #     edgecolor="black",
    # )
    # plt.xlabel("x position")
    # plt.ylabel("nr. walkers")
    # plt.title("Ending positions of 100 000 walkers after 2000 steps")
    # plt.grid()
    # # plt.savefig("3h.png")
    # plt.show()

    # 4a
    M = [1, 10, 100, 1000]
    time_steps = 1000
    avg_elapsed_time = []
    for m in M:
        walkers = MazeWalker(
            M=m, maze=maze, rng=rng, r0=start_points[1], endpoints=endpoints
        )
        start_time = time.perf_counter()
        for i in range(time_steps):
            walkers.move()
        end_time = time.perf_counter()
        avg_elapsed_time.append((end_time - start_time) / time_steps)
    # plt.plot(M, avg_elapsed_time)
    # plt.xlabel("Number of walkers")
    # plt.ylabel("Seconds")
    # plt.title("Average time for M walkers to take 1 step")
    # plt.grid()
    # plt.savefig("4a.png")
    # plt.show()

    # 4b
    stats = pstats.Stats("maze.cprof")
    stats.sort_stats(pstats.SortKey.TIME).print_stats(10)
    stats.sort_stats(pstats.SortKey.TIME).print_stats("maze_walker.py")
