import pygame_menu


class Confirmation:

    def __init__(self, width, height, parameters, theme):

        self._width = width
        self._height = height
        self._theme = theme

        self._menu = pygame_menu.Menu(
            width=self._width,
            height=self._height,
            theme=self._theme.get_theme(),
            title=""
        )

        self._menu.add.label(parameters["question"])
        self._menu.add.button(parameters[1], lambda: self.on_click(1))
        self._menu.add.button(parameters[2], lambda: self.on_click(2))

        self._return_value = None

    def on_click(self, value):
        self._return_value = value
        self._menu.disable()

    def show(self, surface):
        self._return_value = None
        self._menu.enable()
        self._menu.mainloop(surface)
        return self._return_value
