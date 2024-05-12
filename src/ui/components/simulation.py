class Simulation:
    """Creates the Simulation component.

    Simulation renders the cell data.

    Attributes:
        pygame (pygame): Reference to Pygame.
        universe_width (int): Width of the Universe.
        universe_height (int): Height of the Universe.
        surface_width (int): Width of the Pygame surface.
        surface_height (int): Height of the Pygame surface.
    """

    def __init__(self, pygame, universe_width, universe_height, surface_height, surface_width):
        """Constructor that creates the Simulation component.

        In most cases the Universe and surface have different dimensions
        so scaling factors are calculated and stored.

        Args:
            pygame (pygame): Reference to Pygame.
            universe_width (int): Width of the Universe.
            universe_height (int): Height of the Universe.
            surface_width (int): Width of the Pygame surface.
            surface_height (int): Height of the Pygame surface.
        """
        self._pygame = pygame
        self._surface_height = surface_height
        self._surface_width = surface_width
        self._scaling_factor_x = self._surface_width / universe_width
        self._scaling_factor_y = self._surface_height / universe_height
        self._cell_surface = self._pygame.Surface(
            (universe_width, universe_height))

    def set_size(self, universe_width, universe_height):
        """Sets the size of Universe.

        New scaling factors are calculated and drawing surface is resized.

        Args:
            universe_width (_type_): _description_
            universe_height (_type_): _description_
        """
        self._scaling_factor_x = self._surface_width / universe_width
        self._scaling_factor_y = self._surface_height / universe_height
        self._cell_surface = self._pygame.Surface(
            (universe_width, universe_height))

    def update(self, surface, universe):
        """Draws the Universe to the Pygame surface.

        Args:
            surface (pygame.Surface): Pygame surface to draw to.
            universe (entities.Universe): Object holding the cell data.
        """
        self._cell_surface = self._pygame.surfarray.make_surface(
            universe * 255)
        surface.blit(self._pygame.transform.scale_by(
            self._cell_surface, (self._scaling_factor_x, self._scaling_factor_y)), (0, 0))

    def get_snapshot(self):
        """Returns the drawing surface to be saved in a file.

        Returns:
            pygame.Surface: Surface containing the image.
        """
        return self._pygame.transform.scale_by(
            self._cell_surface, (self._scaling_factor_x, self._scaling_factor_y))
