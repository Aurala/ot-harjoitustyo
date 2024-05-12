import numpy as np
from entities.universe import Universe


class Ruleset:
    """Class containing a cellular automata ruleset.

    Ruleset class has a method for performing computation
    for LifeLike cellular automata based on parameters
    defined in the inheriting classes.
    """

    def __init__(self):
        """Constructor for creating new Ruleset.

        Does currently nothing.
        """

    @classmethod
    def lifelike_calculate(cls, universe: Universe, birth_conditions, survive_conditions):
        """Performs computations for a LifeLike cellular automata.

        Both birth and survive conditions are number lists.

        A birthlist of [3, 6] means a dead cell is brought to life if it has
        3 or 6 alive neighbors.

        Args:
            universe (Universe): Object holding the data.
            birth_conditions (list): Birth conditions for cells.
            survive_conditions (list): Survive conditions for cells.
        """

        old_universe = universe.get_entire_universe_as_ndarray()
        new_universe = np.zeros_like(old_universe)

        height, width = old_universe.shape

        kernel = np.array([[1, 1, 1],
                           [1, 0, 1],
                           [1, 1, 1]])

        for row in range(1, height-1):
            for col in range(1, width-1):
                neighborhood = old_universe[row - 1:row + 2, col - 1:col + 2]
                neighborhood_sum = np.sum(neighborhood * kernel)

                if old_universe[row, col] == 0 and neighborhood_sum in birth_conditions:
                    new_universe[row, col] = 1
                elif old_universe[row, col] == 1 and neighborhood_sum in survive_conditions:
                    new_universe[row, col] = 1

        universe.set_entire_universe_as_ndarray(new_universe)
