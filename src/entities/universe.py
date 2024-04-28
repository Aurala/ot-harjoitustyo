import numpy as np


class Universe:

    # FIX: Managing bad inputs

    def __init__(self, x=5, y=5, padding=5):
        self._padding = padding
        self._matrix = np.zeros(
            [y + self._padding * 2, x + self._padding * 2], dtype=np.int8)

    @property
    def width(self):
        _, x = self._matrix.shape
        return x - self._padding * 2

    @property
    def height(self):
        y, _ = self._matrix.shape
        return y - self._padding * 2

    @property
    def true_width(self):
        _, x = self._matrix.shape
        return x

    @property
    def true_height(self):
        y, _ = self._matrix.shape
        return y

    def get_visible_universe(self):
        return self._matrix[self._padding:self._padding+self.height,
                           self._padding:self._padding+self.width]

    def count_cells(self):
        return np.count_nonzero(self.get_visible_universe())

    def invert_cell(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            if self._matrix[y + self._padding][x + self._padding] == 0:
                self._matrix[y + self._padding][x + self._padding] = 1
            else:
                self._matrix[y + self._padding][x + self._padding] = 0

    def add_cell(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            self._matrix[y + self._padding][x + self._padding] = 1

    def erase_cell(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            self._matrix[y + self._padding][x + self._padding] = 0

    # FIX: Use Numpy methods for speed
    def add_pattern(self, x, y, pattern):
        for i, row in enumerate(pattern):
            for j, value in enumerate(row):
                if value == 1:
                    self.add_cell(x + j, y + i)

    def clear_universe(self):
        self._matrix.fill(0)

    def get_entire_universe_as_ndarray(self):
        return self._matrix.copy()

    # FIX: Manage the possible size mismatch
    def set_entire_universe_as_ndarray(self, universe):
        np.copyto(self._matrix, universe)

    def get_universe_as_ndarray(self):
        return self.get_visible_universe().copy()

    def get_universe_as_list(self):
        return self.get_visible_universe().tolist()

    def get_universe_as_text(self):
        universe = self.get_visible_universe()
        presentation = np.where(universe == 0, ".", "*").astype(str)
        return "\n".join("".join(row) for row in presentation) + "\n"
