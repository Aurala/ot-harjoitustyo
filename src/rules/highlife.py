import numpy as np
from rules.ruleset import Ruleset
from entities.universe import Universe


class CustomRuleset(Ruleset):

    def __init__(self):
        self.name = "HighLife (B36/S23)"
        self.description = "HighLife on Game of Life -variaatio ..."

    # FIX: use of decorator, Pylint does not like
    @classmethod
    def calculate(self, universe: Universe):

        birth_conditions = [3, 6]
        survive_conditions = [2, 3]

        # FIX: Get universe data as a ndarray, process using Numpy functions --> speed
        new_universe = np.zeros(
            [universe.true_height, universe.true_width], dtype=np.int8)

        for row in range(1, universe.true_height-1):
            for col in range(1, universe.true_width-1):
                current_state = universe.matrix[row][col]
                window = universe.matrix[row-1:row+2, col-1:col+2]
                neighbors = window.sum() - current_state
                if current_state == 0:
                    if neighbors in birth_conditions:
                        new_universe[row][col] = 1
                if current_state == 1:
                    if neighbors in survive_conditions:
                        new_universe[row][col] = 1

        universe.set_entire_universe_as_ndarray(new_universe)
