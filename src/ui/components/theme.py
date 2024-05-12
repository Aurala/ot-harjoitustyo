import pygame_menu
from config import settings


class Theme:
    """Contains visual settings used by other UI components.

    Attributes:
        pygame (pygame): Reference to Pygame.
    """

    def __init__(self, pygame):
        """Constructor that creates the Theme object.

        Most values are read from the configuration file.

        Args:
            pygame (pygame): Reference to Pygame.
        """

        self.logofont = pygame_menu.font.FONT_MUNRO
        self.menufont = pygame.font.SysFont(
            settings.ui.menu_font_name, settings.ui.menu_font_size)

        self.background_color = settings.ui.menu_color_background
        self.background_color_selected = settings.ui.menu_color_background_selected

        self.theme = pygame_menu.Theme(
            widget_font=self.menufont,
            widget_font_color=settings.ui.menu_color_text,
            widget_font_size=settings.ui.menu_font_size,
            title_font_size=settings.ui.menu_font_size,
            background_color=settings.ui.menu_color_background,
            title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE,
        )
        self.theme.widget_selection_effect = pygame_menu.widgets.NoneSelection()

        self.fontawesome = pygame.font.Font(
            settings.resources.file_icons, size=settings.ui.menu_icon_size)

        self.cursor_normal = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW)
        self.cursor_pencil = pygame.cursors.Cursor(
            pygame.SYSTEM_CURSOR_CROSSHAIR)

        self.statusfont = pygame.font.SysFont(
            settings.ui.status_font_name, settings.ui.status_font_size)
        self.statusfont_color = settings.ui.status_color_text

        self.font_inactive = {"color": settings.ui.menu_color_inactive_icon,
                              "selected_color": settings.ui.menu_color_inactive_icon}
        self.font_active = {"color": settings.ui.menu_color_active_icon,
                            "selected_color": settings.ui.menu_color_active_icon}

    def get_theme(self):
        """Returns the pygame_menu theme.

        Returns:
            pygame_menu.themes.Theme: theme settings for pygame_menu components.
        """
        return self.theme
