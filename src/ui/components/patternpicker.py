import pygame_menu


class PatternPicker:
    """Creates the PatternPicker component.

    PatternPicker is used to choose a pattern to be added to the Universe.

    Attributes:
        width (int): Width of the dialog.
        height (int): Height of the dialog.
        outomaatti (services.OutomaattiService): Reference to OutomaattiService.
        theme (ui.components.Theme): Theme to be used.
    """

    def __init__(self, width, height, outomaatti, theme):
        """Constructor that creates the dialog for picking a pattern.

        Args:
            width (int): Width of the dialog.
            height (int): Height of the dialog.
            outomaatti (services.OutomaattiService): Reference to OutomaattiService.
            theme (ui.components.Theme): Theme to be used.
        """

        self._menu = pygame_menu.Menu(
            width=width,
            height=height,
            theme=theme.get_theme(),
            title=""
        )

        self._menu.add.button("Sulje", lambda: self.on_click(None))
        self._menu.add.label("")
        self._menu.add.label(
            "Valikon sulkeuduttua, klikkaa hiirellä kohtaa mihin haluat asettaa kuvion.")
        self._menu.add.label("")

        categories = outomaatti.get_categories()
        for category in categories:
            self._menu.add.label("--- Kategoria: " + category.name + " ---")
            self._menu.add.label(category.description)
            patterns = outomaatti.get_patterns_by_category(
                category.category_id)
            for pattern in patterns:
                self._menu.add.button(
                    "Valitse kuvio: " + pattern.name, lambda id=pattern.pattern_id: self.on_click(id))
            self._menu.add.label("")

        self._menu.add.label("")
        self._menu.add.button("Sulje", lambda: self.on_click(None))

        self._return_value = None

    def on_click(self, value):
        """Called when the choice is made.

        Stores the choice in the PatternPicker object to be retrieved.

        Args:
            value (int): Pattern's identifier.
        """
        self._return_value = value
        self._menu.disable()

    def show(self, surface):
        """Shows the dialog and returns the user's choice.

        Args:
            surface (pygame.Surface): Surface to draw the dialog to.

        Returns:
            int: Pattern's identifier.
        """
        self._return_value = None
        self._menu.enable()
        self._menu.mainloop(surface)
        return self._return_value
