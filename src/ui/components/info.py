import pygame_menu
from config import settings


class Info:
    """Creates the Info component.

    The contents of the Info dialog consist of images defined in
    the configuration file.

    Attributes:
        width (int): Width of the information menu.
        height (int): Height of the information menu.
        theme (ui.components..Theme): Theme to be used.
    """

    def __init__(self, width, height, theme):
        """Constructor that creates the information menu.

        Args:
            width (int): Width of the information menu.
            height (int): Height of the information menu.
            theme (ui.components.Theme): Theme to be used.
        """

        self._menu = pygame_menu.Menu(
            width=width,
            height=height,
            theme=theme.get_theme(),
            title=""
        )

        self._menu.add.button("Sulje", lambda: self.on_click())
        self._menu.add.label("")

        for info in settings.resources.file_help:
            self._menu.add.image(info)

        self._menu.add.label("")
        self._menu.add.button("Sulje", lambda: self.on_click())

    def on_click(self):
        """Called when the menu is closed."""
        self._menu.disable()

    def show(self, surface):
        """Shows the menu."""
        self._menu.enable()
        self._menu.mainloop(surface)
