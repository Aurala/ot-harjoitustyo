import numpy as np
from entities.rule import Rule
from entities.universe import Universe

class GameOfLife(Rule):

    def __init__(self):
        self.name = "Game of Life (B2/S23)"
        self.description = "Game of Life..."

    def calculate(self, universe: Universe):
        
        birth_conditions = [3]
        survive_conditions = [2, 3]

        new_universe = np.zeros([universe.true_height, universe.true_width])
        
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

        universe.set_universe(new_universe)
