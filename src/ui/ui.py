import pygame
import pygame_menu
import numpy as np
from config import settings
from services.outomaatti_service import OutomaattiService


class UI():

    def __init__(self):

        # FIX: Error handling
        # FIX: Refactor the code to functions/classes

        self.surface_size_x = 600
        self.surface_size_y = 600
        self.universe_size_x = settings.ui.default_universe_width
        self.universe_size_y = settings.ui.default_universe_height
        self.scaling_factor_x = self.surface_size_x / self.universe_size_x
        self.scaling_factor_y = self.surface_size_y / self.universe_size_y

        # Initialize Pygame
        pygame.init()
        pygame.display.set_caption(settings.ui.window_name)
        self.surface = pygame.display.set_mode((800, 625))
        self.background = pygame.Surface((800, 625))
        self.background.fill((0, 0, 0))
        self.clock = pygame.time.Clock()

        # Initialize Outomaatti
        self.outomaatti = OutomaattiService(100, 100, settings.rules.enabled[0])
        self.generation = 0
        self.cell_surface = pygame.Surface((100, 100))

        # Define stuff
        self.cursor_normal = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW)
        self.cursor_pencil = pygame.cursors.Cursor(
            pygame.SYSTEM_CURSOR_CROSSHAIR)

        self.logofont = pygame_menu.font.FONT_MUNRO
        self.menufont = pygame.font.SysFont(
            settings.ui.menu_font_name, settings.ui.menu_font_size)
        self.statusfont = pygame.font.SysFont(
            settings.ui.status_font_name, settings.ui.status_font_size)
        self.fontawesome = pygame.font.Font(
            settings.resources.file_icons, size=settings.ui.menu_icon_font_size)

        self.font_inactive = {"color": settings.ui.menu_color_inactive_icon,
                              "selected_color": settings.ui.menu_color_inactive_icon}
        self.font_active = {"color": settings.ui.menu_color_active_icon,
                            "selected_color": settings.ui.menu_color_active_icon}

        # Construct the menu
        self.setup_menu()

        # Set simulation paused when starting the app
        self.is_simulation_running = False

    # FIX: refactor the code to a separate class
    def setup_menu(self):

        # Theme
        self.theme = pygame_menu.Theme(
            widget_font=self.menufont, widget_font_color=settings.ui.menu_color_text, widget_font_size=16)
        self.theme.background_color = settings.ui.menu_color_background
        self.theme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE
        self.theme.widget_selection_effect = pygame_menu.widgets.NoneSelection()
    
        # Init pygame-menu
        self.menu = pygame_menu.Menu(position=(
            100, 0), width=200, height=625, center_content=True, theme=self.theme, title='')
        self.menu.add.label("Outomaatti", font_name=self.logofont)

        # Set the layout, controls
        self.menu.add.label("Nopeus:")
        speed_controls_frame = self.menu.add.frame_h(200, 50)
        speed_controls_frame.pack(self.menu.add.button(
            "dice-one",
            lambda: self.speed_button_pressed("speed_one", 1),
            font_name=self.fontawesome,
            button_id="speed_one"))
        speed_controls_frame.pack(self.menu.add.button(
            "dice-two",
            lambda: self.speed_button_pressed("speed_two", 2),
            font_name=self.fontawesome,
            button_id="speed_two"))
        speed_controls_frame.pack(self.menu.add.button(
            "dice-three",
            lambda: self.speed_button_pressed("speed_three", 3),
            font_name=self.fontawesome,
            button_id="speed_three"))

        self.menu.add.label("Koko:")
        size_controls_frame = self.menu.add.frame_h(200, 50)
        size_controls_frame.pack(self.menu.add.button(
            "minus",
            lambda: self.size_button_pressed(-5),
            font_name=self.fontawesome,
            button_id="size_minus"))
        size_controls_frame.pack(self.menu.add.button(
            "plus",
            lambda: self.size_button_pressed(5),
            font_name=self.fontawesome,
            button_id="size_plus"))

        # When adding buttons, print the name of Font Awesome icon into the widget.
        # Search for icons at https://fontawesome.com/search?q=&o=r&m=free

        flow_controls_frame = self.menu.add.frame_h(200, 50)
        flow_controls_frame.pack(self.menu.add.button(
            "play",
            lambda: self.play_button_pressed(),
            font_name=self.fontawesome,
            button_id="play"))
        flow_controls_frame.pack(self.menu.add.button(
            "pause",
            lambda: self.play_button_pressed(),
            font_name=self.fontawesome,
            button_id="pause"))
        self.menu.get_widget("pause").hide()
        flow_controls_frame.pack(self.menu.add.button(
            "forward-step",
            lambda: self.next_button_pressed(),
            font_name=self.fontawesome,
            button_id="next"))

        edit_controls_frame = self.menu.add.frame_h(200, 50)
        edit_controls_frame.pack(self.menu.add.button(
            "shuffle",
            lambda: self.random_button_pressed(),
            font_name=self.fontawesome,
            button_id="random"))
        edit_controls_frame.pack(self.menu.add.button(
            "trash",
            lambda: self.trash_button_pressed(),
            font_name=self.fontawesome,
            button_id="trash"))

        pattern_controls_frame = self.menu.add.frame_h(200, 50)
        pattern_controls_frame.pack(self.menu.add.button(
            "database",
            lambda: self.browse_button_pressed(),
            font_name=self.fontawesome,
            button_id="browse"))
        pattern_controls_frame.pack(self.menu.add.button(
            "folder-open",
            lambda: self.import_button_pressed(),
            font_name=self.fontawesome,
            button_id="import"))

        application_controls_frame = self.menu.add.frame_h(200, 50)
        application_controls_frame.pack(self.menu.add.button(
            "gear",
            self.settings_button_pressed(),
            font_name=self.fontawesome,
            button_id="settings"))
        application_controls_frame.pack(self.menu.add.button(
            "camera-retro",
            lambda: self.snapshot_button_pressed(),
            font_name=self.fontawesome,
            button_id="snapshot"))
        application_controls_frame.pack(self.menu.add.button(
            "info",
            lambda: self.info_button_pressed(),
            font_name=self.fontawesome,
            button_id="info"))
        application_controls_frame.pack(self.menu.add.button(
            "right-from-bracket",
            pygame_menu.events.EXIT,
            font_name=self.fontawesome,
            button_id="exit"))

    # FIX: actually changing speed
    def change_button_states(self, playing):
        ids = ["speed_one", "speed_two", "speed_three", "size_minus",
               "size_plus", "next", "random", "trash", "browse",
               "import", "settings", "snapshot", "info", "exit"]
        for id in ids:
            button = self.menu.get_widget(id, True)
            if playing:
                button.update_font(self.font_inactive.copy())
            else:
                button.update_font(self.font_active.copy())
        if playing:
            self.menu.get_widget("play", True).hide()
            self.menu.get_widget("pause", True).show()
        else:
            self.menu.get_widget("pause", True).hide()
            self.menu.get_widget("play", True).show()

    # FIX: logic
    def speed_button_pressed(self, widget, speed):
        if not self.is_simulation_running:
            ids = ["speed_one", "speed_two", "speed_three"]
            for id in ids:
                button = self.menu.get_widget(id, True)
                if button.get_id() == widget:
                    button.set_background_color(
                        settings.ui.menu_color_background_speed)
                else:
                    button.set_background_color(
                        settings.ui.menu_color_background)

   # FIX: logic
    def size_button_pressed(self, size):
        pass

    # FIX: change the state of buttons
    def play_button_pressed(self):
        if self.is_simulation_running:
            self.is_simulation_running = False
            self.change_button_states(False)
        else:
            self.is_simulation_running = True
            self.change_button_states(True)

    # FIX: logic, change the state of buttons
    def next_button_pressed(self):
        pass

    # FIX: logic
    def random_button_pressed(self):
        pass

    # FIX: add a confirmation dialog
    def trash_button_pressed(self):
        if not self.is_simulation_running:
            self.outomaatti.clear_universe()

    # FIX: logic
    def browse_button_pressed(self):
        pass

    # FIX: logic
    def import_button_pressed(self):
        pass

    # FIX: logic
    def settings_button_pressed(self):
        pass

    # FIX: logic
    def snapshot_button_pressed(self):
        pass

    # FIX: logic
    def info_button_pressed(self):
        pass

    # FIX: confirmation dialog
    def exit_button_pressed(self):
        pass

    # FIX: save name, type and location from settings; save the scaled version
    def snapshot_button_pressed(self):
        if not self.is_simulation_running:
            pygame.image.save(self.cell_surface, "universe.png")

    def update_status(self):
        running = ""
        if self.is_simulation_running:
            running = "Käynnissä... "
        text = self.statusfont.render(running +
                                      "Universumi: " +
                                      str(self.outomaatti.get_width()) +
                                      "x" +
                                      str(self.outomaatti.get_height()) +
                                      "   Sukupolvi: " +
                                      str(self.generation) +
                                      "   Soluja: " +
                                      str(self.outomaatti.count_cells()), True, settings.ui.status_color_text)
        self.surface.blit(text, (10, 600))

    def update_simulation(self):
        # FIX: Move the array operations to the Universe class
        universe = self.outomaatti.get_universe_as_ndarray().transpose()
        expanded_array = np.expand_dims(universe, axis=2)
        rgb_array = np.repeat(expanded_array, 3, axis=2)
        self.cell_surface = pygame.surfarray.make_surface(rgb_array * 255)

        self.surface.blit(pygame.transform.scale_by(
            self.cell_surface, (self.scaling_factor_x, self.scaling_factor_y)), (0, 0))

    def update_mouse_cursor(self):
        mouse_position_x, mouse_position_y = pygame.mouse.get_pos()
        if mouse_position_x <= self.surface_size_x and mouse_position_y <= self.surface_size_y:
            pygame.mouse.set_cursor(self.cursor_pencil)
        else:
            pygame.mouse.set_cursor(self.cursor_normal)

    # FIX: Draw only what needs to be drawn, not the whole screen --> speed
    def update_background(self):
        self.surface.blit(self.background, (0, 0))

    # FIX: Less nested code
    def process_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.is_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position_x, mouse_position_y = pygame.mouse.get_pos()
                mouse_position_x_scaled = int(
                    mouse_position_x / self.scaling_factor_x)
                mouse_position_y_scaled = int(
                    mouse_position_y / self.scaling_factor_y)
                if mouse_position_x <= self.surface_size_x and mouse_position_y <= self.surface_size_y:
                    if not self.is_simulation_running:
                        self.outomaatti.invert_cell(
                            mouse_position_x_scaled, mouse_position_y_scaled)

    def mainloop(self):

        # FIX: Patterns to come from the repository

        # Gliders
        glider = [[1, 0, 0], [0, 1, 1], [1, 1, 0]]
        self.outomaatti.add_pattern(0, 0, glider)
        self.outomaatti.add_pattern(10, 10, glider)
        self.outomaatti.add_pattern(20, 20, glider)
        self.outomaatti.add_pattern(30, 30, glider)
        self.outomaatti.add_pattern(40, 40, glider)

        # Blinkers
        blinker = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
        self.outomaatti.add_pattern(5, 50, blinker)
        self.outomaatti.add_pattern(5, 60, blinker)
        self.outomaatti.add_pattern(5, 70, blinker)

        # Glider gun
        glider_gun = \
            [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0,
                 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0,
                 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
             [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0,
                 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0,
                 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0,
                 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.outomaatti.add_pattern(40, 10, glider_gun)

        # FIX: optimize, optimize, optimize
        # - framerate
        # - define what to redraw and when
        # - move the Outomaatti calculation to a thread if needed

        while 1:

            self.clock.tick(30)

            self.update_mouse_cursor()

            # FIX: Should process both Outomaatti and menu events at once
            events = pygame.event.get()
            self.process_events(events)

            self.update_background()

            # self.cell_surface.fill((255, 0, 0))

            if self.is_simulation_running:
                self.outomaatti.next_generation()
                self.generation += 1

            self.update_simulation()
            self.update_status()

            self.menu.update(events)
            self.menu.draw(self.surface)

            pygame.display.update()
