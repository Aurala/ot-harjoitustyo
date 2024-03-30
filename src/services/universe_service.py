import random
from entities.universe import Universe
from rules.gameoflife import GameOfLife

class UniverseService:

    def __init__(self, x=5, y=5):
        self.universe = Universe(x, y)

    def get_textual_presentation(self):
        return str(self.universe)

    def get_width(self):
        return self.universe.width
    
    def get_height(self):
        return self.universe.height

    def add_cell(self, x, y):
        self.universe.add_cell(x, y)

    def erase_cell(self, x, y):
        self.universe.erase_cell(x, y)

    def clear_universe(self):
        self.universe.clear_universe()

    def next_generation(self):
        gol = GameOfLife()
        gol.calculate(self.universe)
