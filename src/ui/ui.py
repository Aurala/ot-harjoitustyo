import pygame
import pygame_menu
import numpy as np
from services.outomaatti_service import OutomaattiService


class UI():

    def __init__(self):

        # FIX: Error handling

        # Initialize Pygame
        pygame.init()
        pygame.display.set_caption('Outomaatti')
        self.surface = pygame.display.set_mode((800, 625))
        self.background = pygame.Surface((800, 625))
        self.background.fill((0, 0, 0))

        self.clock = pygame.time.Clock()

        # Initialize Outomaatti
        self.outomaatti = OutomaattiService(200, 200, "rules.life")
        self.generation = 0
        self.cell_surface = pygame.Surface((200, 200))

        # Initialize pygame-menu
        self.theme = pygame_menu.Theme()
        self.theme.background_color = (55, 55, 55)
        self.theme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE
        self.fontawesome = pygame.font.Font(
            "src/ui/resources/Font Awesome 6 Free-Solid-900.otf", size=24)

        self.menu = pygame_menu.Menu(
            position=(100, 0), width=200, height=625, theme=self.theme, title='')

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

    def play_button_pressed(self):
        self.is_simulation_running = True
        print("Play pressed")

    def pause_button_pressed(self):
        self.is_simulation_running = False
        print("Pause pressed")

    # FIX: logic
    def next_frame_button_pressed(self):
        print("Next frame pressed")

    # FIX: logic
    def pencil_button_pressed(self):
        print("Pencil pressed")

    # FIX: logic
    def eraser_button_pressed(self):
        print("Eraser pressed")

    # FIX: logic
    def trash_button_pressed(self):
        print("Trash pressed")

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

        while self.is_application_running:

            self.clock.tick(30)
            start_time = pygame.time.get_ticks()

            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    self.is_running = False

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
                self.cell_surface, (3, 3)), (0, 0))

            font = pygame.font.SysFont("Arial", 18)
            text = font.render("Universumi: " + str(self.outomaatti.get_width()) + "x" + str(self.outomaatti.get_height()) +
                               "   Sukupolvi: " + str(self.generation) + "   Soluja: " + str(self.outomaatti.count_cells()), True, (255, 0, 0))
            self.surface.blit(text, (10, 600))

            self.menu.update(events)
            self.menu.draw(self.surface)

            pygame.display.update()

            end_time = pygame.time.get_ticks()
            print(end_time-start_time)
