import random
from importlib import import_module
from entities.universe import Universe
from config import settings
from repositories.library_repository import LibraryRepository


class OutomaattiService:

    # FIX: Read defaults from a configuration file
    def __init__(self, x=5, y=5, ruleset=settings.rules.enabled[0]):
        self.universe = Universe(x, y)
        self.ruleset = import_module(ruleset).CustomRuleset
        self.library_repository = LibraryRepository()
        self._is_simulation_running = False

    def is_simulation_running(self):
        return self._is_simulation_running

    def play(self):
        self._is_simulation_running = True

    def pause(self):
        self._is_simulation_running = False

    def get_width(self):
        return self.universe.width

    def get_height(self):
        return self.universe.height

    def count_cells(self):
        return self.universe.count_cells()

    def invert_cell(self, x, y):
        self.universe.invert_cell(x, y)

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

    def get_categories(self):
        return self.library_repository.get_categories()

    def place_random_pattern(self):
        patterns = self.library_repository.get_patterns()
        if len(patterns) > 0:
            self.universe.add_pattern(random.randint(1, self.universe.width), random.randint(
                1, self.universe.height), random.choice(patterns).pattern)

    def get_patterns_by_category(self, category_id):
        return self.library_repository.get_patterns_by_category(category_id)

    def get_pattern_by_id(self, pattern_id):
        return self.library_repository.get_pattern_by_id(pattern_id)

    def get_pattern_by_name(self, name):
        return self.library_repository.get_pattern_by_name(name)
