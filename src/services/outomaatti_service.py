from entities.universe import Universe
from importlib import import_module

class OutomaattiService:

    # FIX: Read defaults from a configuration file
    def __init__(self, x=5, y=5, ruleset="rules.life"):
        self.universe = Universe(x, y)
        self.ruleset = import_module(ruleset).CustomRuleset

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

    def get_universe_as_ndarray(self):
        return self.universe.get_universe_as_ndarray()

    def get_universe_as_list(self):
        return self.universe.get_universe_as_list()
  
    def get_universe_as_text(self):
        return self.universe.get_universe_as_text()

    # FIX: Should there be a lock of some kind until this operation finishes?
    # FIX: Should pass Universe or just the methods to get/set?
    def next_generation(self):
        self.ruleset.calculate(self.universe)
