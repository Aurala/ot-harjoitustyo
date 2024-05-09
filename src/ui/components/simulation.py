from ui.components.theme import Theme


class Simulation:

    def __init__(self, pygame, theme, scaling_factor_x, scaling_factor_y):
        self._theme = theme
        self._pygame = pygame
        self._scaling_factor_x = scaling_factor_x
        self._scaling_factor_y = scaling_factor_y
        self._cell_surface = self._pygame.Surface((100, 100)) # FIX

    def update(self, surface, universe):
        self._cell_surface = self._pygame.surfarray.make_surface(universe * 255)
        surface.blit(self._pygame.transform.scale_by(
            self._cell_surface, (self._scaling_factor_x, self._scaling_factor_y)), (0, 0))

    def get_surface(self):
        return self._cell_surface
