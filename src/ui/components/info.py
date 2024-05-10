import pygame_menu
from config import settings


class Info:

    def __init__(self, width, height, theme):

        self._width = width
        self._height = height
        self._theme = theme

        self._menu = pygame_menu.Menu(
            width=self._width,
            height=self._height,
            theme=self._theme.get_theme(),
            title=""
        )

        self._menu.add.button("Sulje", lambda: self.on_click())

        for info in settings.resources.file_help:
            self._menu.add.image(info)

        self._menu.add.button("Sulje", lambda: self.on_click())

    def on_click(self):
        self._menu.disable()

    def show(self, surface):
        self._menu.enable()
        self._menu.mainloop(surface)
