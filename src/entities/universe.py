import numpy as np


class Universe:
    """Class holding information about Universe.

    Universe holds the cell data in a 2D array, and methods for manipulation.

    It is not clear how to apply cellular automata rules for cells next
    to edges. Therefore the Universe has some padding around it and all
    calculations are applied to the extended area.

    Attributes:
        width (int, optional): Width of the visible universe.
        height (int, optional): Height of the visible universe.
        padding (int, optional): Padding applied to the universe.
     """

    def __init__(self, width=5, height=5, padding=5):
        """Class constructor for creating a new Universe.

        Args:
            width (int, optional): Width of visible Universe (default: 5)
            height (int, optional): Height of visible Universe (default: 5)
            padding (int, optional): Padding applied to the Universe (default: 5)
        """
        self._padding = padding
        self._matrix = np.zeros(
            [height + self._padding * 2, width + self._padding * 2], dtype=np.int8)

    def change_size(self, change):
        """Changes the Universe's size.

        Negative values decrease the size.
        Positive values increase the size.

        Only even values should be used to avoid rounding errors.

        Does not do anything if the new vertical or horizontal size
        would be 1 (or less).

        Args:
            change (int): Amount to be increased/decreased by.
        """
        if self.width + change >= 1 and self.height + change >= 1:
            delta = change // 2
            if change < 0:
                self._matrix = self._matrix[abs(delta):delta, abs(delta):delta]
            elif change > 0:
                self._matrix = np.pad(self._matrix, delta)

    @property
    def width(self):
        """Returns the width of the visible Universe.

        Returns:
            int: Width of the visible Universe.
        """
        _, x = self._matrix.shape
        return x - self._padding * 2

    @property
    def height(self):
        """Returns the height of the visible Universe.

        Returns:
            int: Height of the visible Universe.
        """
        y, _ = self._matrix.shape
        return y - self._padding * 2

    @property
    def true_width(self):
        """Returns the width of the entire Universe.

        Includes padding.

        Returns:
            int: Width of the entire Universe.
        """
        _, x = self._matrix.shape
        return x

    @property
    def true_height(self):
        """Returns the height of the entire Universe.

        Includes padding.

        Returns:
            int: Height of the entire Universe.
        """
        y, _ = self._matrix.shape
        return y

    def get_visible_universe(self):
        """Returns the array containing the visible Universe.

        Returns:
            numpy.ndarray: 2D array containing the visible Universe.
        """
        return self._matrix[self._padding:self._padding+self.height,
                            self._padding:self._padding+self.width]

    def count_cells(self):
        """Returns the number of living cells in the visible Universe.

        Living cells are cells with non-zero values.

        Returns:
            int: Number of living cells in the visible Universe.
        """
        return np.count_nonzero(self.get_visible_universe())

    def invert_cell(self, x, y):
        """Inverts a cell in the visible Universe.

        A living cell becomes dead, and vice versa.

        Args:
            x (int): X coordinate of the cell to be inverted
            y (int): Y coordinate of the cell to be inverted
        """
        if 0 <= x < self.width and 0 <= y < self.height:
            if self._matrix[y + self._padding][x + self._padding] == 0:
                self._matrix[y + self._padding][x + self._padding] = 1
            else:
                self._matrix[y + self._padding][x + self._padding] = 0

    def add_cell(self, x, y):
        """Adds a living cell in the visible Universe.

        Args:
            x (int): X coordinate.
            y (int): Y coordinate.
        """
        if 0 <= x < self.width and 0 <= y < self.height:
            self._matrix[y + self._padding][x + self._padding] = 1

    def add_pattern(self, x, y, pattern):
        """Adds a predefined pattern to the Universe.

        The coordinates mark the pattern's upper left corner.

        Args:
            x (int): X coordinate.
            y (int): Y coordinate.
            pattern (list): 2D array of cells.
        """
        for i, row in enumerate(pattern):
            for j, value in enumerate(row):
                if value == 1:
                    self.add_cell(x + j, y + i)

    def clear_universe(self):
        """Empties the Universe.

        All cells are marked dead.
        """
        self._matrix.fill(0)

    def get_entire_universe_as_ndarray(self):
        """Returns a copy of the entire Universe.

        Used mainly by the classes that perform the computations.

        Returns:
            numpy.ndarray: Entire Universe.
        """
        return self._matrix.copy()

    def set_entire_universe_as_ndarray(self, universe):
        """Sets the entire Universe.

        The classes performing the computations use this function
        instead of setting cells individually.

        The array must have the same shape.

        Args:
            universe (numpy.ndarray): 2D array of cells.
        """
        np.copyto(self._matrix, universe)

    def get_universe_as_rgb_ndarray(self):
        """Returns a copy of the visible Universe.

        Used by the UI to render cells efficiently to a
        Pygame surface.

        Returns:
            numpy.ndarray: 2D array of cells.
        """
        rgb_ndarray = self.get_visible_universe().copy().transpose()
        rgb_ndarray = np.tile(np.expand_dims(rgb_ndarray, axis=2), (1, 1, 3))
        return rgb_ndarray

    def get_universe_as_list(self):
        """Returns the visible Universe.

        Used mainly by unit tests.

        Returns:
            list: 2D array of cells.
        """
        return self.get_visible_universe().tolist()

    def get_universe_as_text(self):
        """Returns the visible Universe.

        Used mainly by unit tests.

        Returns:
            str: 2D array of cells.
        """
        universe = self.get_visible_universe()
        presentation = np.where(universe == 0, ".", "*").astype(str)
        return "\n".join("".join(row) for row in presentation) + "\n"
