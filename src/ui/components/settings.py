import pygame_menu


class Settings:
    """Creates the Settings component.

    Currently implements only one setting: ruleset used for the simulation.

    Attributes:
        width (int): Width of the settings dialog.
        height (int): Height of the settings dialog.
        outomaatti (services.OutomaattiService): Reference to OutomaattiService.
        theme (ui.components.Theme): Theme to be used.
    """

    def __init__(self, width, height, outomaatti, theme):
        """Constructor that creates the settings dialog.

        Args:
            width (int): Width of the settings dialog.
            height (int): Height of the settings dialog.
            outomaatti (services.OutomaattiService): Reference to OutomaattiService.
            theme (ui.components.Theme): Theme to be used.
        """

        self._menu = pygame_menu.Menu(
            width=width,
            height=height,
            theme=theme.get_theme(),
            title=""
        )

        rulesets = outomaatti.get_rulesets()
        self._menu.add.label("Säännöt:")
        i = 0
        for ruleset in rulesets:
            if i == outomaatti.get_ruleset():
                self._menu.add.button(
                    ruleset[0] + " (valittu)", lambda id=i: self.on_click(id))
            else:
                self._menu.add.button(
                    ruleset[0], lambda id=i: self.on_click(id))
            i += 1

        self._menu.add.button("Sulje", lambda: self.on_click(None))

    def on_click(self, value):
        """Called when the choice is made.

        Stores the choice in the Settings object to be retrieved.

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
