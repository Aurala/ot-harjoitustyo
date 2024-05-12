import random
import sys
from importlib import import_module
from entities.universe import Universe
from config import settings
from repositories.library_repository import LibraryRepository


class OutomaattiService:
    """Class contains the Outomaatti application logic.

    Attributes:
        width (int, optional): Width of the universe.
        height (int, optional): Height of the universe.
        ruleset (int, optional): The ruleset used.
    """

    def __init__(self, width=5, height=5, ruleset=0):
        """Class constructor for creating a new OutomaattiService.

        Args:
            width (int, optional): Width of the universe. Defaults to 5.
            height (int, optional): Height of the universe. Defaults to 5.
            ruleset (int, optional): The ruleset used. Defaults to 0.
        """
        self._universe = Universe(width, height)
        self._ruleset_number = ruleset
        self.set_ruleset(self._ruleset_number)
        self._library_repository = LibraryRepository()
        self._running = False
        self._speed = 1
        self._generation = 0
        self._redraw_needed = True
        self._menu_open = False
        self._pattern_queue = None

    def save_snapshot(self, surface):
        """Saves a snapshot of the simulation to a file.

        Args:
            surface (pygame.Surface): Surface containing the image.
        """
        self._library_repository.save_snapshot(surface)

    def menu_open(self):
        """Tells the application that a menu has been opened.

        Certain functionalities are disabled while a menu is open.
        """
        self._menu_open = True

    def menu_closed(self):
        """Tells the application that a menu has been closed.

        Certain functionalities are disabled while a menu is open.
        """
        self._menu_open = False
        self.force_redraw()

    def is_menu_open(self):
        """Returns whether the menu is open.

        Returns:
            bool: True = Open. False = Not open.
        """
        return self._menu_open

    def change_size(self, change):
        """Changes the Universe's size.

        -1 means the size is to be decreased and +1 means the size is to be
        decreased. The value is multiplied by a number configured in the 
        settings (e.g. 10).

        Does not do anything if the new vertical or horizontal size
        would be 10 (or less).

        Args:
            change (int): -1 (decrease) or +1 (increase).
        """
        change = change * settings.general.size_change
        if self.get_width() + change >= 10 and self.get_height() + change >= 10:
            self._universe.change_size(change)
            self.force_redraw()

    def import_pattern(self, filename):
        """Imports a pattern into the database.

        Args:
            filename (str): File containing the pattern.

        Returns:
            str: Message to be shown in the UI.
        """
        if self._library_repository.import_pattern(filename):
            return "Tiedoston lisäys tietokantaan onnistui!"
        return "Tiedoston lisäys tietokantaan epäonnistui!"

    def get_ruleset(self):
        """Return the ruleset currently used for simulation.

        Returns:
            int: Ruleset used.
        """
        return self._ruleset_number

    def get_rulesets(self):
        """Returns all rulesets available.

        Returns:
            list: Rulesets available.
        """
        return settings.rules.enabled

    def set_ruleset(self, ruleset_id):
        """Sets the ruleset to be used for simulation.

        Args:
            ruleset_id (int): Ruleset to be used.
        """
        self._ruleset_number = ruleset_id
        self._ruleset = import_module(
            settings.rules.enabled[ruleset_id][1]).CustomRuleset

    def is_running(self):
        """Returns Whether the simulation is running.

        Returns:
            _bool: True = Running. False = Not running.
        """
        return self._running

    def is_redraw_needed(self):
        """Returns whether the UI should redraw the screen.

        UI will periodically redraw the screen, but the redraw
        can be forced. Should be used especially when the service
        manipulates Universe.

        Returns:
            bool: True = Should redraw. False = Shouldn't redraw.
        """
        redraw_needed = self._redraw_needed
        if redraw_needed:
            self._redraw_needed = False
        return redraw_needed

    def force_redraw(self):
        """Sets the flag that tells th UI should redraw the screen.

        UI will periodically redraw the screen, but the redraw
        can be forced. Should be used especially when the service
        manipulates the universe.
        """
        self._redraw_needed = True

    def play(self):
        """Starts the simulation.
        """
        self._running = True

    def pause(self):
        """Pauses the simulation.
        """
        self._running = False

    def close(self):
        """Terminates the application.
        """
        sys.exit()

    def set_speed(self, speed):
        """Sets the simulation speed.

        1-3 (fastest-slowest)

        Does not do anything if the speed is not within range.

        Args:
            speed (int): Specified speed.
        """
        if 1 <= speed <= 3:
            self._speed = speed

    def get_speed(self):
        """Gets the simulation speed.

        1-3 (fastest-slowest)

        Returns:
            int: Current speed.
        """
        return self._speed

    def get_generation(self):
        """Returns the count of generations in the simulation.

        Returns:
            int: Count of generations.
        """
        return self._generation

    def reset_generation(self):
        """Resets the count of generations if the simulation.
        """
        self._generation = 0

    def get_width(self):
        """Returns the width of the universe.

        Returns:
            int: Width of the universe.
        """
        return self._universe.width

    def get_height(self):
        """Returns the height of the universe.

        Returns:
            int: Height of the universe.
        """
        return self._universe.height

    def count_cells(self):
        """Returns the number of alive cells in the universe.

        Returns:
            int: Number of alive cells.
        """
        return self._universe.count_cells()

    def invert_cell(self, x, y):
        """Inverts a cell in the visible Universe.

        A living cell becomes dead, and vice versa.

        Args:
            x (int): X coordinate of the cell to be inverted
            y (int): Y coordinate of the cell to be inverted
        """
        self._universe.invert_cell(x, y)
        self.force_redraw()

    def add_cell(self, x, y):
        """Adds a living cell in the visible Universe.

        Args:
            x (int): X coordinate.
            y (int): Y coordinate.
        """
        self._universe.add_cell(x, y)
        self.force_redraw()

    def add_pattern(self, x, y, pattern):
        """Adds a predefined pattern to the Universe.

        The coordinates mark the pattern's upper left corner.

        Args:
            x (int): X coordinate.
            y (int): Y coordinate.
            pattern (list): 2D array of cells.
        """
        self._universe.add_pattern(x, y, pattern)
        self.force_redraw()

    def clear_universe(self):
        """Empties the Universe.

        The generation count is reset.

        All cells are marked dead.
        """
        self._universe.clear_universe()
        self.reset_generation()
        self.force_redraw()

    def get_universe_as_rgb_ndarray(self):
        """Returns a copy of the visible Universe.

        Used by the UI to render cells efficiently to a
        Pygame surface.

        Returns:
            numpy.ndarray: 2D array of cells.
        """
        return self._universe.get_universe_as_rgb_ndarray()

    def get_universe_as_list(self):
        """Returns the visible Universe.

        Used mainly by unit tests.

        Returns:
            list: 2D array of cells.
        """
        return self._universe.get_universe_as_list()

    def get_universe_as_text(self):
        """Returns the visible Universe.

        Used mainly by unit tests.

        Returns:
            str: 2D array of cells.
        """
        return self._universe.get_universe_as_text()

    def next_generation(self):
        """Advances the simulation by one generation.
        """
        self._ruleset.calculate(self._universe)
        self._generation += 1

    def get_categories(self):
        """Returns all pattern categories.

        Returns:
            list: All categories as Category objects.
        """
        return self._library_repository.get_categories()

    def place_random_pattern(self):
        """Places a random pattern to a random place in the Universe.
        """
        patterns = self._library_repository.get_patterns()
        if len(patterns) > 0:
            self._universe.add_pattern(random.randint(1, self._universe.width), random.randint(
                1, self._universe.height), random.choice(patterns).pattern)
        self.force_redraw()

    def get_patterns_by_category(self, category_id):
        """Returns patterns in a specified category.

        Args:
            category_id (int): Category identifier.

        Returns:
            list: Patterns as Pattern objects.
        """
        return self._library_repository.get_patterns_by_category(category_id)

    def get_pattern_by_id(self, pattern_id):
        """Returns a pattern based on its identifier.

        Args:
            pattern_id (int): Pattern identifier.

        Returns:
            Pattern: Specified pattern as a Pattern object. (None if not found.)
        """
        return self._library_repository.get_pattern_by_id(pattern_id)

    def get_pattern_by_name(self, name):
        """Returns a pattern based on its name.

        Args:
            pattern_name (str): Pattern name.

        Returns:
            Pattern: Specified pattern as a Pattern object. (None if not found.)
        """
        return self._library_repository.get_pattern_by_name(name)

    def set_pattern_queue(self, pattern_id):
        """Sets a pattern in a "queue" to be added in the Universe on the next click.

        Args:
            pattern_id (int): Pattern's identifier.
        """
        self._pattern_queue = pattern_id

    def get_pattern_queue(self):
        """Gets a pattern from the queue (if any).

        Returns:
            int: Pattern's identifier.
        """
        pattern_id = self._pattern_queue
        self._pattern_queue = None
        return pattern_id
