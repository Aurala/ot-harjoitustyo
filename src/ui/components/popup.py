import pygame_menu


class Popup:
    """Creates the Popup component.

    Shows a message to the user.

    Attributes:
        width (int): Width of the popup dialog.
        height (int): Height of the popup dialog.
        message (str): Message to be shown.
        theme (ui.components.Theme): Theme to be used.
    """

    def __init__(self, width, height, message, theme):
        """Constructor that creates the popup dialog.

        Args:
            width (int): Width of the popup dialog.
            height (int): Height of the popup dialog.
            message (str): Message to be shown.
            theme (ui.components.Theme): Theme to be used.
        """

        self._menu = pygame_menu.Menu(
            width=width,
            height=height,
            theme=theme.get_theme(),
            title=""
        )

        self._menu.add.label(message)
        self._menu.add.label("")

        self._menu.add.button("Sulje", lambda: self.on_click())

    def on_click(self):
        """Called when the popup dialog is closed."""
        self._menu.disable()

    def show(self, surface):
        """Shows the popup dialog."""
        self._menu.enable()
        self._menu.mainloop(surface)
