import pygame_menu


class PatternChooser:

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

        self._menu.add.button("Sulje", lambda: self.on_click(None))
        self._menu.add.label("")

        categories = self._outomaatti.get_categories()
        for category in categories:
            self._menu.add.label("--- Kategoria: " + category.name + " ---")
            self._menu.add.label(category.description)
            patterns = self._outomaatti.get_patterns_by_category(category.category_id)
            for pattern in patterns:
                self._menu.add.button("Kuvio: " + pattern.name, lambda id=pattern.pattern_id: self.on_click(id))
            self._menu.add.label("")

        self._menu.add.label("")
        self._menu.add.button("Sulje", lambda: self.on_click(None))

        self._return_value = None

    def on_click(self, value):
        self._return_value = value
        self._menu.disable()

    def show(self, surface):
        self._return_value = None
        self._menu.enable()
        self._menu.mainloop(surface)
        return self._return_value
