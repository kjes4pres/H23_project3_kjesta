import labyrinths as lb
import numpy as np

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
        for i in range(self._M):
            dx = self._positions[i, 0] + dr[i, 0]
            dy = self._positions[i, 1] + dr[i, 1]
            if self._maze[dx, dy] == False:
                dr[i, 0] = 0
                dr[i, 1] = 0
        return dr

    def not_finished(self) -> np.ndarray:
        """
        Method for checking if a walker has reached the end point in the maze.

        Output:
        is_it_done: boolean array, value True if the walker has not reached the endpoint.
        False if the walker is at an endpoint.
        """
        is_it_done = np.ones(self._M, dtype=bool)
        for i in range(self._M):
            if tuple(self._positions[i]) in self.endpoints:
                is_it_done[i] = False
        return is_it_done


if __name__ == "__main__":
    maze = lb.circular()
    walkers = MazeWalker(M=500, maze=maze, rng=rng, r0=(100, 100))
    animation = lb.Animation(walkers)
    animation.animate(N=200)
