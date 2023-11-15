import maze_walker as mz
import labyrinths
import numpy as np

seed = 1910
rng = np.random.default_rng(seed)


example_labyrinth = labyrinths.example()


def test_remove_illegal():
    """
    Testing that _remove_illegal method in MazeWalker class
    correctly removes illegal steps. No moving across aze boundaries.
    """
    starting_point = [4, 3]
    walker = mz.MazeWalker(M=10, maze=example_labyrinth, rng=rng, r0=starting_point)
    dr = rng.integers(-1, 2, size=(walker._M, 2))
    computed = walker._remove_illegal(dr)
    want_removed = np.array([[0, 1], [0, -1]])
    for step in computed:
        if np.array_equal(step, want_removed[0]):
            assert False, "Failed to remove illegal steps."
        elif np.array_equal(step, want_removed[1]):
            assert False, "Failed to remove illegal steps."
    print("Success, all illegal steps were removed!")


test_remove_illegal()
