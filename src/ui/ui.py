import pygame
import pygame_menu
import numpy as np
from config import settings
from services.outomaatti_service import OutomaattiService


class UI():

    def __init__(self):

        # FIX: Error handling
        # FIX: Move code to functions/classes
        # FIX: Read defaults

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
        self.outomaatti = OutomaattiService(100, 100, "rules.life")
        self.generation = 0
        self.cell_surface = pygame.Surface((100, 100))

        self.cursor_normal = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW)
        self.cursor_pencil = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)

        self.logofont = pygame_menu.font.FONT_MUNRO
        self.menufont = pygame.font.SysFont("Arial", 16)
        self.statusfont = pygame.font.SysFont("Arial", 18)
        self.fontawesome = pygame.font.Font(
            "src/ui/resources/Font Awesome 6 Free-Solid-900.otf", size=24)
        
        self.font_inactive = {"color": settings.ui.menu_color_inactive_icon, "selected_color": settings.ui.menu_color_inactive_icon}
        self.font_inactive = {"color": settings.ui.menu_color_active_icon, "selected_color": settings.ui.menu_color_active_icon}

        # Initialize pygame-menu
        self.theme = pygame_menu.Theme(widget_font=self.menufont, widget_font_color=settings.ui.menu_color_text, widget_font_size=16)
        self.theme.background_color = settings.ui.menu_color_background
        self.theme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE

        self.menu = pygame_menu.Menu(position=(100, 0), width=200, height=625, theme=self.theme, title='')
        self.menu.add.label("Outomaatti", font_name=self.logofont)

        # FIX: Read values from database
        self.menu.add.label("Säännöt:")
        self.menu.add.dropselect(title="", items=[('Life', 1), ('HighLife', 2), ('zzz', 3)])

        self.menu.add.label("Nopeus:")
        self.menu.add.selector("", [('hidas', 1), ('keskinopea', 2), ('nopea', 3)], onchange=self.set_speed())

        # When adding buttons, simply print the name of Font Awesome icon and it will render
        # Search for icons at https://fontawesome.com/search?q=&o=r&m=free

        flow_controls_frame = self.menu.add.frame_h(200, 50)
        flow_controls_frame.pack(self.menu.add.button(
            "play",
            lambda: self.play_button_pressed(),
            font_name=self.fontawesome)
        )
        flow_controls_frame.pack(self.menu.add.button(
            "pause",
            lambda: self.pause_button_pressed(),
            font_name=self.fontawesome)
        )
        flow_controls_frame.pack(self.menu.add.button(
            "forward-step",
            lambda: self.next_frame_button_pressed(),
            font_name=self.fontawesome))

        edit_controls_frame = self.menu.add.frame_h(200, 50)
        edit_controls_frame.pack(self.menu.add.button(
            "pencil",
            lambda: self.pencil_button_pressed(),
            font_name=self.fontawesome)
        )
        edit_controls_frame.pack(self.menu.add.button(
            "eraser",
            lambda: self.eraser_button_pressed(),
            button_id="eraser",
            font_name=self.fontawesome)
        )
        edit_controls_frame.pack(self.menu.add.button(
            "shuffle",
            lambda: self.random_button_pressed(),
            font_name=self.fontawesome)
        )
        edit_controls_frame.pack(self.menu.add.button(
            "trash",
            lambda: self.trash_button_pressed(),
            font_name=self.fontawesome)
        )

        pattern_controls_frame = self.menu.add.frame_h(200, 50)
        pattern_controls_frame.pack(self.menu.add.button(
            "database",
            lambda: self.browse_button_pressed(),
            font_name=self.fontawesome)
        )
        pattern_controls_frame.pack(self.menu.add.button(
            "folder-open",
            lambda: self.import_button_pressed(),
            font_name=self.fontawesome)
        )

        application_controls_frame = self.menu.add.frame_h(200, 50)
        application_controls_frame.pack(self.menu.add.button(
            "gear",
            self.settings_button_pressed(),
            font_name=self.fontawesome)
        )
        application_controls_frame.pack(self.menu.add.button(
            "camera-retro",
            lambda: self.snapshot_button_pressed(),
            font_name=self.fontawesome)
        )
        application_controls_frame.pack(self.menu.add.button(
            "right-from-bracket",
            pygame_menu.events.EXIT,
            font_name=self.fontawesome)
        )

        self.is_simulation_running = False

    # FIX: logic
    def set_speed(self):
        print("Speed changed")

    # FIX: change the state of buttons
    def play_button_pressed(self):
        print("Play pressed")
        self.is_simulation_running = True

    # FIX: change the state of buttons
    def pause_button_pressed(self):
        print("Pause pressed")
        self.is_simulation_running = False

    # FIX: logic, change the state of buttons
    def next_frame_button_pressed(self):
        print("Next frame pressed")

    # FIX: logic, change the state of buttons
    def pencil_button_pressed(self):
        print("Pencil pressed")

    # FIX: logic
    def eraser_button_pressed(self):
        print("Eraser pressed")
        self.menu.get_widget("eraser").update_font(self.font_inactive)

    # FIX: logic
    def random_button_pressed(self):
        print("Random pressed")

    # FIX: add a confirmation dialog, pause simulation
    def trash_button_pressed(self):
        print("Trash pressed")
        self.outomaatti.clear_universe()

    # FIX: logic
    def browse_button_pressed(self):
        print("Browse pressed")

    # FIX: logic
    def import_button_pressed(self):
        print("Import pressed")

    # FIX: logic
    def settings_button_pressed(self):
        print("Settings pressed")

    # FIX: logic
    def snapshot_button_pressed(self):
        print("Snapshot pressed")
        pygame.image.save(self.cell_surface, "universe.png")

    def update_status(self):
        text = self.statusfont.render("Universumi: " + 
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
        #self.cell_surface.set_colorkey((0, 0, 0))

        self.surface.blit(pygame.transform.scale_by(
            self.cell_surface, (self.scaling_factor_x, self.scaling_factor_y)), (0, 0))

    def update_mouse_cursor(self):
        mouse_position_x, mouse_position_y = pygame.mouse.get_pos()
        if mouse_position_x <= self.surface_size_x and mouse_position_y <= self.surface_size_y:
            pygame.mouse.set_cursor(self.cursor_pencil)
        else:
            pygame.mouse.set_cursor(self.cursor_normal)

    # FIX: For speed, no need to redraw the whole screen
    def update_background(self):
        self.surface.blit(self.background, (0, 0))

    def process_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.is_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position_x, mouse_position_y = pygame.mouse.get_pos()
                if mouse_position_x <= self.surface_size_x and mouse_position_y <= self.surface_size_y:
                    print("Mouse clicked (scaled): x = " + str(mouse_position_x/self.scaling_factor_x) + ", y = " + str(mouse_position_y/self.scaling_factor_y))
                    if not self.is_simulation_running:
                        self.outomaatti.invert_cell(int(mouse_position_x/self.scaling_factor_x), int(mouse_position_y/self.scaling_factor_y))

    def mainloop(self):

        # FIX: Patterns come from the repository

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

        self.is_simulation_running = False

        # FIX: optimize
        # - framerate
        # - define what to redraw and when
        # - move the Outomaatti calculation to a thread if needed
        # FIX: move code to functions

        while 1:

            self.clock.tick(30)
            start_time = pygame.time.get_ticks()

            self.update_mouse_cursor()

            # FIX: Should process both Outomaatti and menu events at once
            events = pygame.event.get()
            self.process_events(events)

            self.update_background()

            #self.cell_surface.fill((255, 0, 0))

            if self.is_simulation_running:
                self.outomaatti.next_generation()
                self.generation += 1

            self.update_simulation()
            self.update_status()

            self.menu.update(events)
            self.menu.draw(self.surface)

            pygame.display.update()

            end_time = pygame.time.get_ticks()
            # print(end_time-start_time)
