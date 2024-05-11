from ui.components.theme import Theme


class Simulation:

    def __init__(self, pygame, theme, universe_width, universe_height, surface_height, surface_width):
        self._theme = theme
        self._pygame = pygame
        self._surface_height = surface_height
        self._surface_width = surface_width
        self._scaling_factor_x = self._surface_width / universe_width
        self._scaling_factor_y = self._surface_height / universe_height
        self._cell_surface = self._pygame.Surface(
            (universe_width, universe_height))

    def set_size(self, universe_width, universe_height):
        self._scaling_factor_x = self._surface_width / universe_width
        self._scaling_factor_y = self._surface_height / universe_height
        self._cell_surface = self._pygame.Surface(
            (universe_width, universe_height))

    def update(self, surface, universe):
        self._cell_surface = self._pygame.surfarray.make_surface(
            universe * 255)
        surface.blit(self._pygame.transform.scale_by(
            self._cell_surface, (self._scaling_factor_x, self._scaling_factor_y)), (0, 0))

    def get_snapshot(self):
        return self._pygame.transform.scale_by(
            self._cell_surface, (self._scaling_factor_x, self._scaling_factor_y))
