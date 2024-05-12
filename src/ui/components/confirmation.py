import pygame_menu


class Confirmation:
    """Creates the Confirmation component.

    Lets user choose between two options.

    Used to confirm user choices (such as emptying the Universe),
    but could be used for any decision between two options.

    Attributes:
        width (int): Width of the confirmation dialog.
        height (int): Height of the confirmation dialog.
        parameters (dict): Question and available choices.
        theme (ui.components.Theme): Theme to be used.
    """

    def __init__(self, width, height, parameters, theme):
        """Constructor that creates the confirmation dialog.

        Args:
            width (int): Width of the confirmation dialog.
            height (int): Height of the confirmation dialog.
            parameters (dict): Question and available choices.
            theme (ui.components.Theme): Theme to be used.
        """

        self._menu = pygame_menu.Menu(
            width=width,
            height=height,
            theme=theme.get_theme(),
            title=""
        )

        self._menu.add.label(parameters["question"])
        self._menu.add.label("")
        self._menu.add.button(parameters[1], lambda: self.on_click(1))
        self._menu.add.button(parameters[2], lambda: self.on_click(2))

        self._return_value = None

    def on_click(self, value):
        """Called when the choice is made.

        Stores the choice in the Confirmation object to be retrieved.

        Args:
            value (int): Choice's identifier.
        """
        self._return_value = value
        self._menu.disable()

    def show(self, surface):
        """Shows the dialog and returns the user's choice.

        Args:
            surface (pygame.Surface): Surface to draw the dialog to.

        Returns:
            int: Choice's identifier.
        """
        self._return_value = None
        self._menu.enable()
        self._menu.mainloop(surface)
        return self._return_value
