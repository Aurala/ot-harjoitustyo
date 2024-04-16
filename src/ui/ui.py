import pygame
import pygame_menu
import numpy as np
from services.outomaatti_service import OutomaattiService


class UI():

    def __init__(self):

        # FIX: Error handling
        # FIX: Move code to functions/classes

        self.surface_size_x = 600
        self.surface_size_y = 600
        self.universe_size_x = 100
        self.universe_size_y = 100
        self.scaling_factor_x = self.surface_size_x / self.universe_size_x
        self.scaling_factor_y = self.surface_size_y / self.universe_size_y

        # Initialize Pygame
        pygame.init()
        pygame.display.set_caption('Outomaatti')
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

        self.menufont = pygame_menu.font.FONT_MUNRO
        self.fontawesome = pygame.font.Font(
            "src/ui/resources/Font Awesome 6 Free-Solid-900.otf", size=24)
        
        # Initialize pygame-menu
        self.theme = pygame_menu.Theme(widget_font=self.menufont, widget_font_color=(255, 255, 255), widget_font_size=16)
        self.theme.background_color = (55, 55, 55)
        self.theme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE

        self.menu = pygame_menu.Menu(
            position=(100, 0), width=200, height=625, theme=self.theme, title='')

        self.menu.add.label("Outomaatti")

        self.menu.add.selector('Nopeus: ', [('hidas', 1), ('keskinopea', 2), ('nopea', 3)], onchange=self.set_speed())

        flow_controls_frame = self.menu.add.frame_h(200, 50)
        flow_controls_frame.pack(self.menu.add.button(
            "play", lambda: self.play_button_pressed(), font_name=self.fontawesome))
        flow_controls_frame.pack(self.menu.add.button(
            "pause", lambda: self.pause_button_pressed(), font_name=self.fontawesome))
        flow_controls_frame.pack(self.menu.add.button(
            "forward-step", lambda: self.next_frame_button_pressed(), font_name=self.fontawesome))

        edit_controls_frame = self.menu.add.frame_h(200, 50)
        edit_controls_frame.pack(self.menu.add.button(
            "pencil", lambda: self.pencil_button_pressed(), font_name=self.fontawesome))
        edit_controls_frame.pack(self.menu.add.button(
            "eraser", lambda: self.erase_button_pressed(), font_name=self.fontawesome))
        edit_controls_frame.pack(self.menu.add.button(
            "trash", lambda: self.trash_button_pressed(), font_name=self.fontawesome))

        pattern_controls_frame = self.menu.add.frame_h(200, 50)
        pattern_controls_frame.pack(self.menu.add.button(
            "database", lambda: self.browse_button_pressed(), font_name=self.fontawesome))
        pattern_controls_frame.pack(self.menu.add.button(
            "folder-open", lambda: self.import_button_pressed(), font_name=self.fontawesome))

        application_controls_frame = self.menu.add.frame_h(200, 50)
        application_controls_frame.pack(self.menu.add.button(
            "gear", self.settings_button_pressed(), font_name=self.fontawesome))
        application_controls_frame.pack(self.menu.add.button(
            "right-from-bracket", pygame_menu.events.EXIT, font_name=self.fontawesome))

        self.is_application_running = False
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

    def mainloop(self):

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

        self.is_application_running = True
        self.is_simulation_running = False

        # FIX: optimize
        # - framerate
        # - define what to redraw and when
        # - move the Outomaatti calculation to a thread if needed
        # FIX: move code to functions

        while self.is_application_running:

            self.clock.tick(30)
            start_time = pygame.time.get_ticks()

            mouse_position_x, mouse_position_y = pygame.mouse.get_pos()
            if mouse_position_x <= self.surface_size_x and mouse_position_y <= self.surface_size_y:
                pygame.mouse.set_cursor(self.cursor_pencil)
            else:
                pygame.mouse.set_cursor(self.cursor_normal)

            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    self.is_running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_position_x, mouse_position_y = pygame.mouse.get_pos()
                    if mouse_position_x <= self.surface_size_x and mouse_position_y <= self.surface_size_y:
                        print("Mouse clicked (scaled): x = " + str(mouse_position_x/self.scaling_factor_x) + ", y = " + str(mouse_position_y/self.scaling_factor_y))
                        if not self.is_simulation_running:
                            self.outomaatti.invert_cell(int(mouse_position_x/self.scaling_factor_x), int(mouse_position_y/self.scaling_factor_y))

            self.surface.blit(self.background, (0, 0))

            self.cell_surface.fill((255, 0, 0))

            if self.is_simulation_running:
                self.outomaatti.next_generation()
                self.generation += 1

            universe = self.outomaatti.get_universe_as_ndarray().transpose()
            expanded_array = np.expand_dims(universe, axis=2)
            rgb_array = np.repeat(expanded_array, 3, axis=2)
            self.cell_surface = pygame.surfarray.make_surface(rgb_array * 255)
            self.cell_surface.set_colorkey((0, 0, 0))

            self.surface.blit(pygame.transform.scale_by(
                self.cell_surface, (self.scaling_factor_x, self.scaling_factor_y)), (0, 0))

            font = pygame.font.SysFont("Arial", 18)
            text = font.render("Universumi: " + 
                               str(self.outomaatti.get_width()) + 
                               "x" + 
                               str(self.outomaatti.get_height()) +
                               "   Sukupolvi: " + 
                               str(self.generation) + 
                               "   Soluja: " + 
                               str(self.outomaatti.count_cells()), True, (255, 0, 0))
            self.surface.blit(text, (10, 600))

            self.menu.update(events)
            self.menu.draw(self.surface)

            pygame.display.update()

            end_time = pygame.time.get_ticks()
            # print(end_time-start_time)
