from ui.components.theme import Theme


class Status:

    def __init__(self, pygame, theme):
        self.pygame = pygame
        self.theme = theme

    def update(self, surface, parameters):
        self.pygame.draw.rect(surface, (0, 0, 0), self.pygame.Rect(0, 601, 600, 625))
        status = ""
        if parameters["running"]:
            status = "Käynnissä..."
        else:
            status = "Pysäytetty"
        text = self.theme.statusfont.render(f"{status}   " +
                                            f"Universumi: {parameters['width']}x{parameters['height']}   " +
                                            f"Sukupolvi: {parameters['generation']}   " +
                                            f"Soluja: {parameters['cells']}   " +
                                            f"FPS: {parameters['frames']:.1f}",
                                            True, self.theme.statusfont_color)
        surface.blit(text, (10, 600))
