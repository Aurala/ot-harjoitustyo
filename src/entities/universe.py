import numpy as np

class Universe:

    X_PADDING = 1
    Y_PADDING = 1

    def __init__(self, x=5, y=5):
        # FIX: negatiiviset luvut, nollat, muut kuin numerot
        x += self.X_PADDING * 2
        y += self.Y_PADDING * 2
        self.matrix = np.zeros([y, x])

    # FIX, np-metodit
    @property
    def width(self):
        return len(self.matrix[0]) - self.X_PADDING * 2

    # FIX, np-metodit
    @property
    def height(self):
        return len(self.matrix) - self.Y_PADDING * 2
    
    # FIX, np-metodit
    @property
    def true_width(self):
        return len(self.matrix[0])

    # FIX, np-metodit
    @property
    def true_height(self):
        return len(self.matrix)

    def add_cell(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.matrix[y + self.Y_PADDING][x + self.X_PADDING] = 1

    def erase_cell(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.matrix[y + self.Y_PADDING][x + self.X_PADDING] = 0

    def clear_universe(self):
        self.matrix.fill(0)

    def get_universe(self):
        return self.matrix.copy()
    
    def set_universe(self, universe):
        np.copyto(self.matrix, universe)

    def __str__(self):
        presentation = ""
        for row in self.matrix[self.Y_PADDING:-self.Y_PADDING, self.X_PADDING:-self.X_PADDING]:
            for col in row:
                if col == 0:
                    presentation += "."
                else:
                    presentation += "*"
            presentation += "\n"
        return presentation
