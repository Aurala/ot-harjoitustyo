from ui.components.theme import Theme


class Status:
    """Creates the Statusbar component.

    Attributes:
        pygame (pygame): Reference to Pygame.
        theme (ui.components.Theme): Theme to be used.
    """

    def __init__(self, pygame, theme):
        """Constructor that creates the Statusbar component.

        Args:
            pygame (pygame): Reference to Pygame.
            theme (ui.components.Theme): Theme to be used.
        """
        self._pygame = pygame
        self._theme = theme

    def update(self, surface, parameters):
        """Draws the Universe to the Pygame surface.

        Args:
            surface (pygame.Surface): Pygame surface to draw to.
            parameters (dict): Metrics used in the statusbar.
        """
        self._pygame.draw.rect(surface, (0, 0, 0),
                               self._pygame.Rect(0, 600, 600, 625))
        status = ""
        if parameters["running"]:
            status = "Käynnissä"
        else:
            status = "Pysäytetty"
        text = self._theme.statusfont.render(f"{status}   " +
                                             f"Säännöt: {parameters['ruleset']}   " +
                                             f"Universumi: {parameters['width']}x{parameters['height']}   " +
                                             f"Sukupolvi: {parameters['generation']}   " +
                                             f"Soluja: {parameters['cells']}   " +
                                             f"FPS: {parameters['frames']:.0f}",
                                             True, self._theme.statusfont_color)
        surface.blit(text, (10, 600))
