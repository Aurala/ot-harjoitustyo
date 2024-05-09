import random
from importlib import import_module
from entities.universe import Universe
from config import settings
from repositories.library_repository import LibraryRepository


class OutomaattiService:

    # FIX: Read defaults from a configuration file
    def __init__(self, x=5, y=5, ruleset=settings.rules.enabled[0]):
        self._universe = Universe(x, y)
        self._ruleset = import_module(ruleset).CustomRuleset
        self._library_repository = LibraryRepository()
        self._running = False
        self._speed = 1
        self._generation = 0
        self._redraw_needed = True

    def is_running(self):
        return self._running

    def is_redraw_needed(self):
        redraw_needed = self._redraw_needed
        if redraw_needed:
            self._redraw_needed = False
        return redraw_needed
    
    def force_redraw(self):
        self._redraw_needed = True

    def play(self):
        self._running = True

    def pause(self):
        self._running = False

    def close(self):
        exit()

    def set_speed(self, speed):
        if 1 <= speed <= 3:
            self._speed = speed

    def get_speed(self):
        return self._speed

    def get_generation(self):
        return self._generation

    def reset_generation(self):
        self._generation = 0

    def get_width(self):
        return self._universe.width

    def get_height(self):
        return self._universe.height

    def count_cells(self):
        return self._universe.count_cells()

    def invert_cell(self, x, y):
        self._universe.invert_cell(x, y)
        self.force_redraw()

    def add_cell(self, x, y):
        self._universe.add_cell(x, y)
        self.force_redraw()

    def add_pattern(self, x, y, pattern):
        self._universe.add_pattern(x, y, pattern)
        self.force_redraw()

    def erase_cell(self, x, y):
        self._universe.erase_cell(x, y)
        self.force_redraw()

    def clear_universe(self):
        self._universe.clear_universe()
        self.force_redraw()

    def get_universe_as_rgb_ndarray(self):
        return self._universe.get_universe_as_rgb_ndarray()

    def get_universe_as_list(self):
        return self._universe.get_universe_as_list()

    def get_universe_as_text(self):
        return self._universe.get_universe_as_text()

    # FIX: Should there be a lock of some kind until this operation finishes?
    # FIX: Should pass Universe or just the methods to get/set?
    def next_generation(self):
        self._ruleset.calculate(self._universe)
        self._generation += 1

    def get_categories(self):
        return self._library_repository.get_categories()

    def place_random_pattern(self):
        patterns = self._library_repository.get_patterns()
        if len(patterns) > 0:
            self._universe.add_pattern(random.randint(1, self._universe.width), random.randint(
                1, self._universe.height), random.choice(patterns).pattern)
        self.force_redraw()

    def get_patterns_by_category(self, category_id):
        return self._library_repository.get_patterns_by_category(category_id)

    def get_pattern_by_id(self, pattern_id):
        return self._library_repository.get_pattern_by_id(pattern_id)

    def get_pattern_by_name(self, name):
        return self._library_repository.get_pattern_by_name(name)
