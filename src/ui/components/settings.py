import pygame_menu


class Settings:

    def __init__(self, width, height, outomaatti, theme):

        self._width = width
        self._height = height
        self._outomaatti = outomaatti
        self._theme = theme

        self._menu = pygame_menu.Menu(
            width=self._width,
            height=self._height,
            theme=self._theme.get_theme(),
            title=""
        )

        rulesets = self._outomaatti.get_rulesets()
        self._menu.add.label("Säännöt:")
        i = 0
        for ruleset in rulesets:
            if i == self._outomaatti.get_ruleset():
                self._menu.add.button(
                    ruleset[0] + " (valittu)", lambda id=i: self.on_click(id))
            else:
                self._menu.add.button(
                    ruleset[0], lambda id=i: self.on_click(id))
            i += 1

        self._menu.add.button("Sulje", lambda: self.on_click(None))

    def on_click(self, value):
        if value is not None:
            self._outomaatti.set_ruleset(value)
        self._menu.disable()

    def show(self, surface):
        self._menu.enable()
        self._menu.mainloop(surface)
