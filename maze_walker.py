import labyrinths
import numpy as np

seed = 1910
rng = np.random.default_rng(seed)


class MazeWalker:
    def __init__(
        self,
        M: int,
        maze: np.ndarray,
        rng: np.random.Generator,
        r0: tuple[int, int] = np.array([1, 1]),
    ) -> None:
        self._M = M
        self._maze = maze
        self._rng = rng
        self.r0 = r0

    @property
    def M(self) -> int:
        return self._M

    @property
    def maze(self) -> np.ndarray:
        return self._maze

    def initialize_walkers(self, r0: tuple[int, int]) -> None:
        ...
