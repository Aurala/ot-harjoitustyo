import random
from entities.universe import Universe
from importlib import import_module

class UniverseService:

    # FIX default-arvot
    def __init__(self, x=5, y=5, ruleset="rules.highlife"):
        self.universe = Universe(x, y)
        self.ruleset = import_module(ruleset).CustomRuleset

    def get_textual_presentation(self):
        return str(self.universe)

    def get_width(self):
        return self.universe.width
    
    def get_height(self):
        return self.universe.height

    def count_cells(self):
        return self.universe.count_cells()

    def add_cell(self, x, y):
        self.universe.add_cell(x, y)

    def add_pattern(self, x, y, pattern):
        self.universe.add_pattern(x, y, pattern)

    def erase_cell(self, x, y):
        self.universe.erase_cell(x, y)

    def clear_universe(self):
        self.universe.clear_universe()

    def get_universe_as_list(self):
        return self.universe.get_universe_as_list()

    def next_generation(self):
        self.ruleset.calculate(self.universe)
