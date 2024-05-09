import numpy as np
from ui.components.theme import Theme


class Simulation:

    def __init__(self, pygame, theme, scaling_factor_x, scaling_factor_y):
        self.theme = theme
        self.pygame = pygame
        self.scaling_factor_x = scaling_factor_x
        self.scaling_factor_y = scaling_factor_y
        self.cell_surface = self.pygame.Surface((100, 100)) # FIX

    def update(self, surface, universe):
        # FIX: Move the array operations to the Universe class or OutomaattiService
        universe = universe.transpose()
        expanded_array = np.expand_dims(universe, axis=2)
        rgb_array = np.repeat(expanded_array, 3, axis=2)
        self.cell_surface = self.pygame.surfarray.make_surface(rgb_array * 255)

        surface.blit(self.pygame.transform.scale_by(
            self.cell_surface, (self.scaling_factor_x, self.scaling_factor_y)), (0, 0))
