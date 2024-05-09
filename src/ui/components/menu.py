import pygame_menu
from config import settings


class Menu:

    def __init__(self, pygame, theme):
        self.theme = theme.get_theme()
        self.pygame = pygame

        self.menu = pygame_menu.Menu(position=(
            100, 0), width=200, height=625, center_content=True, theme=self.theme, title='')
        self.menu.add.label("Outomaatti", font_name=theme.logofont)

        self.menu.add.label("Nopeus:")
        speed_controls_frame = self.menu.add.frame_h(200, 50)
        speed_controls_frame.pack(self.menu.add.button(
            "dice-one",
            lambda: self.speed_button_pressed("speed_one", 1),
            font_name=theme.fontawesome,
            button_id="speed_one"))
        speed_controls_frame.pack(self.menu.add.button(
            "dice-two",
            lambda: self.speed_button_pressed("speed_two", 2),
            font_name=theme.fontawesome,
            button_id="speed_two"))
        speed_controls_frame.pack(self.menu.add.button(
            "dice-three",
            lambda: self.speed_button_pressed("speed_three", 3),
            font_name=theme.fontawesome,
            button_id="speed_three"))

        self.menu.add.label("Koko:")
        size_controls_frame = self.menu.add.frame_h(200, 50)
        size_controls_frame.pack(self.menu.add.button(
            "minus",
            lambda: self.size_button_pressed(-5),
            font_name=theme.fontawesome,
            button_id="size_minus"))
        size_controls_frame.pack(self.menu.add.button(
            "plus",
            lambda: self.size_button_pressed(5),
            font_name=theme.fontawesome,
            button_id="size_plus"))

        # When adding buttons, print the name of Font Awesome icon into the widget.
        # Search for icons at https://fontawesome.com/search?q=&o=r&m=free

        flow_controls_frame = self.menu.add.frame_h(200, 50)
        flow_controls_frame.pack(self.menu.add.button(
            "play",
            lambda: self.play_button_pressed(),
            font_name=theme.fontawesome,
            button_id="play"))
        flow_controls_frame.pack(self.menu.add.button(
            "pause",
            lambda: self.play_button_pressed(),
            font_name=theme.fontawesome,
            button_id="pause"))
        self.menu.get_widget("pause").hide()
        flow_controls_frame.pack(self.menu.add.button(
            "forward-step",
            lambda: self.next_button_pressed(),
            font_name=theme.fontawesome,
            button_id="next"))

        edit_controls_frame = self.menu.add.frame_h(200, 50)
        edit_controls_frame.pack(self.menu.add.button(
            "shuffle",
            lambda: self.random_button_pressed(),
            font_name=theme.fontawesome,
            button_id="random"))
        edit_controls_frame.pack(self.menu.add.button(
            "trash",
            lambda: self.trash_button_pressed(),
            font_name=theme.fontawesome,
            button_id="trash"))

        pattern_controls_frame = self.menu.add.frame_h(200, 50)
        pattern_controls_frame.pack(self.menu.add.button(
            "database",
            lambda: self.browse_button_pressed(),
            font_name=theme.fontawesome,
            button_id="browse"))
        pattern_controls_frame.pack(self.menu.add.button(
            "folder-open",
            lambda: self.import_button_pressed(),
            font_name=theme.fontawesome,
            button_id="import"))

        application_controls_frame = self.menu.add.frame_h(200, 50)
        application_controls_frame.pack(self.menu.add.button(
            "gear",
            self.settings_button_pressed(),
            font_name=theme.fontawesome,
            button_id="settings"))
        application_controls_frame.pack(self.menu.add.button(
            "camera-retro",
            lambda: self.snapshot_button_pressed(),
            font_name=theme.fontawesome,
            button_id="snapshot"))
        application_controls_frame.pack(self.menu.add.button(
            "info",
            lambda: self.info_button_pressed(),
            font_name=theme.fontawesome,
            button_id="info"))
        application_controls_frame.pack(self.menu.add.button(
            "right-from-bracket",
            pygame_menu.events.EXIT,
            font_name=theme.fontawesome,
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
        self.speed = speed

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
        self.outomaatti.place_random_pattern()

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