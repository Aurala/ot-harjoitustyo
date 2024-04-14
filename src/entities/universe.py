import numpy as np


class Universe:

    # FIX: Define the visibility (private, protected)

    def __init__(self, x=5, y=5, padding=5):
        # FIX: Managing bad inputs
        # FIX: Defaults to be read from a configuration file
        self.padding = padding
        self.matrix = np.zeros(
            [y + self.padding * 2, x + self.padding * 2], dtype=np.int8)

    @property
    def width(self):
        _, x = self.matrix.shape
        return x - self.padding * 2

    @property
    def height(self):
        y, _ = self.matrix.shape
        return y - self.padding * 2

    @property
    def true_width(self):
        _, x = self.matrix.shape
        return x

    @property
    def true_height(self):
        y, _ = self.matrix.shape
        return y

    # FIX: Should be internal only
    def get_padding(self):
        return self.padding

    def get_visible_universe(self):
        return self.matrix[self.padding:self.padding+self.height,
                           self.padding:self.padding+self.width]

    def count_cells(self):
        return np.count_nonzero(self.get_visible_universe())

    def add_cell(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.matrix[y + self.padding][x + self.padding] = 1

    def erase_cell(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.matrix[y + self.padding][x + self.padding] = 0

    # FIX: Use Numpy methods for speed
    def add_pattern(self, x, y, pattern):
        for i in range(len(pattern)):
            for j in range(len(pattern[0])):
                if pattern[i][j] == 1:
                    self.add_cell(x + j, y + i)

    def clear_universe(self):
        self.matrix.fill(0)

    def get_entire_universe_as_ndarray(self):
        return self.matrix.copy()

    # FIX: Manage the possible size mismatch
    def set_entire_universe_as_ndarray(self, universe):
        np.copyto(self.matrix, universe)

    def get_universe_as_ndarray(self):
        return self.get_visible_universe().copy()

    def get_universe_as_list(self):
        return self.get_visible_universe().tolist()

    def get_universe_as_text(self):
        universe = self.get_visible_universe()
        presentation = np.where(universe == 0, ".", "*").astype(str)
        return "\n".join("".join(row) for row in presentation) + "\n"
