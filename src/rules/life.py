import numpy as np
from rules.ruleset import Ruleset
from entities.universe import Universe


class CustomRuleset(Ruleset):

    def __init__(self):
        self.name = "Game of Life (B2/S23)"
        self.description = "Alkuperäiset John Conway'n kehittämät säännöt"

    # FIX: use of decorator, Pylint does not like
    # FIX: this routine can be made faster, not sure how exactly but needs to be done
    @classmethod
    def calculate(self, universe: Universe):

        birth_conditions = [3]
        survive_conditions = [2, 3]

        # FIX: To be fetched via a method, not accessed directly
        old_universe = universe.matrix.copy()
        new_universe = np.zeros_like(old_universe)

        height, width = old_universe.shape

        kernel = np.array([[1, 1, 1],
                           [1, 0, 1],
                           [1, 1, 1]])

        for row in range(1, height-1):
            for col in range(1, width-1):
                neighborhood = old_universe[row - 1:row + 2, col - 1:col + 2]
                # FIX: Test if it faster to np.sum and deduct own value
                neighborhood_sum = np.sum(neighborhood * kernel)

                if old_universe[row, col] == 0 and neighborhood_sum in birth_conditions:
                    new_universe[row, col] = 1
                elif old_universe[row, col] == 1 and neighborhood_sum in survive_conditions:
                    new_universe[row, col] = 1

        universe.set_entire_universe_as_ndarray(new_universe)
