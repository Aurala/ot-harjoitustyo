import numpy as np


class Universe:
    """
    Class holds information about Universe.

    Universe holds the cell data in a 2D array, and methods to manipulate it.

    It is not clear how to apply cellular automata rules for cells next to edges.
    Therefore the Universe has some padding around it and all calculations are
    applied to the extended area.

    Attributes:
        pattern_id: integer, used to query the pattern from the database
        category_id: integer, links the pattern to a category
        name: string, the pattern's name
        rules: string, the rules the pattern was designed for
        pattern: list, the represented as a 2D array
        metadata: string, arbitrary information about the pattern
    """

    def __init__(self, x=5, y=5, padding=5):
        """
        Class constructor that creates a new Universe.

        Args:
            x (int, optional): horizontal size of visible Universe (default: 5)
            y (int, optional): vertical size of visible Universe (default: 5)
            padding (int, optional): padding applied to the Universe (default: 5)
        """
        # FIX: Managing bad inputs
        self._padding = padding
        self._matrix = np.zeros(
            [y + self._padding * 2, x + self._padding * 2], dtype=np.int8)

    @property
    def width(self):
        """
        Returns the width of the visible Universe.

        Returns:
            int: the width of the visible Universe
        """
        _, x = self._matrix.shape
        return x - self._padding * 2

    @property
    def height(self):
        """
        Returns the height of the visible Universe.

        Returns:
            int: the height of the visible Universe
        """
        y, _ = self._matrix.shape
        return y - self._padding * 2

    @property
    def true_width(self):
        """
        Returns the width of the entire Universe.

        Returns:
            int: the width of the entire Universe
        """
        _, x = self._matrix.shape
        return x

    @property
    def true_height(self):
        """
        Returns the height of the entire Universe.

        Returns:
            int: the height of the entire Universe
        """
        y, _ = self._matrix.shape
        return y

    def get_visible_universe(self):
        """
        Returns the array containing the visible Universe.

        Returns:
            numpy.ndarray: a 2D array containing the visible Universe
        """
        return self._matrix[self._padding:self._padding+self.height,
                            self._padding:self._padding+self.width]

    def count_cells(self):
        """
        Returns the number of alive cells in the visible Universe.

        Returns:
            int: the number of alive cells in the visible Universe
        """
        return np.count_nonzero(self.get_visible_universe())

    def invert_cell(self, x, y):
        """
        Inverts a cell in the visible Universe. A living one
        becomes dead, and vice versa.

        Args:
            x (int): the x coordinate of the cell to be inverted
            y (int): the y coordinate of the cell to be inverted
        """
        if 0 <= x < self.width and 0 <= y < self.height:
            if self._matrix[y + self._padding][x + self._padding] == 0:
                self._matrix[y + self._padding][x + self._padding] = 1
            else:
                self._matrix[y + self._padding][x + self._padding] = 0

    def add_cell(self, x, y):
        """
        Adds a living cell in the visible Universe.

        Args:
            x (int): the x coordinate of the cell to be added
            y (int): the y coordinate of the cell to be added
        """
        if 0 <= x < self.width and 0 <= y < self.height:
            self._matrix[y + self._padding][x + self._padding] = 1

    def erase_cell(self, x, y):
        """
        Sets a cell dead in the visible Universe.

        Args:
            x (int): the x coordinate of the cell to be added
            y (int): the y coordinate of the cell to be added
        """
        if 0 <= x < self.width and 0 <= y < self.height:
            self._matrix[y + self._padding][x + self._padding] = 0

    # FIX: Use Numpy methods for speed
    def add_pattern(self, x, y, pattern):
        """
        Adds a predefined pattern to the Universe.

        Args:
            x (int): the coordinate of the cell to be added
            y (int): the coordinate of the cell to be added
            pattern (list): a 2D array of cells
        """
        for i, row in enumerate(pattern):
            for j, value in enumerate(row):
                if value == 1:
                    self.add_cell(x + j, y + i)

    def clear_universe(self):
        """
        Empties the Universe.
        """
        self._matrix.fill(0)

    def get_entire_universe_as_ndarray(self):
        """
        Returns a copy of the entire Universe.

        Returns:
            numpy.ndarray: the entire Universe
        """
        return self._matrix.copy()

    # FIX: Manage the possible size mismatch
    def set_entire_universe_as_ndarray(self, universe):
        """
        Sets the entire Universe.
        
        For example, after calculating the next generation.

        Args:
            universe (numpy.ndarray): the new Universe
        """
        np.copyto(self._matrix, universe)

    def get_universe_as_ndarray(self):
        """
        Returns a copy of the visible Universe.

        Returns:
            numpy.ndarray: the visible Universe
        """
        return self.get_visible_universe().copy()

    def get_universe_as_list(self):
        """
        Returns the visible Universe.

        Returns:
            list: the visible Universe
        """
        return self.get_visible_universe().tolist()

    def get_universe_as_text(self):
        """
        Returns the visible Universe.

        Returns:
            str: the entire Universe
        """
        universe = self.get_visible_universe()
        presentation = np.where(universe == 0, ".", "*").astype(str)
        return "\n".join("".join(row) for row in presentation) + "\n"
