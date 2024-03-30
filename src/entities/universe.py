import numpy as np

class Universe:
    
    def __init__(self, x=5, y=5, padding=5):
        # FIX: negatiiviset luvut, nollat, muut kuin numerot
        self.padding = padding
        self.matrix = np.zeros([y + self.padding * 2, x + self.padding * 2], dtype=np.int8)

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
        _ ,x = self.matrix.shape
        return x

    @property
    def true_height(self):
        y, _ = self.matrix.shape
        return y

    def get_padding(self):
        return self.padding

    def get_visible_universe(self):
        return self.matrix[self.padding:self.padding+self.height, self.padding:self.padding+self.width]

    def count_cells(self):
        return np.count_nonzero(self.get_visible_universe())

    def add_cell(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.matrix[y + self.padding][x + self.padding] = 1

    def erase_cell(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.matrix[y + self.padding][x + self.padding] = 0

    def add_pattern(self, x, y, pattern):
        for i in range(len(pattern)):
            for j in range(len(pattern[0])):
                if pattern[i][j] == 1:
                    self.add_cell(x + j, y + i)

    def clear_universe(self):
        self.matrix.fill(0)

    def get_universe_as_ndarray(self):
        return self.matrix.copy()
    
    def set_universe_as_ndarray(self, universe):
        np.copyto(self.matrix, universe)

    def get_universe_as_list(self):
        return self.get_visible_universe().tolist()

    def __str__(self):
        presentation = ""
        for row in self.matrix[self.padding:-self.padding, self.padding:-self.padding]:
            for col in row:
                if col == 0:
                    presentation += "."
                else:
                    presentation += "*"
            presentation += "\n"
        return presentation
