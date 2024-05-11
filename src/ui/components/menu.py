import pygame_menu
from ui.components.confirmation import Confirmation
from ui.components.info import Info
from ui.components.patternpicker import PatternPicker
from ui.components.settings import Settings


class Menu:

    def __init__(self, pygame, outomaatti, simulation, surface, theme):
        self.theme = theme
        self.outomaatti = outomaatti
        self.pygame = pygame
        self.simulation = simulation
        self.surface = surface

        self.menu = pygame_menu.Menu(position=(
            100, 0), width=200, height=625, center_content=True, theme=self.theme.get_theme(), title='')
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
        self.speed_button_pressed("speed_one", 1)

        self.menu.add.label("Koko:")
        size_controls_frame = self.menu.add.frame_h(200, 50)
        size_controls_frame.pack(self.menu.add.button(
            "minus",
            lambda: self.size_button_pressed(-1),
            font_name=theme.fontawesome,
            button_id="size_minus"))
        size_controls_frame.pack(self.menu.add.button(
            "plus",
            lambda: self.size_button_pressed(1),
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

        application_controls_frame = self.menu.add.frame_h(200, 50)
        application_controls_frame.pack(self.menu.add.button(
            "gear",
            lambda: self.settings_button_pressed(),
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
            lambda: self.exit_button_pressed(),
            font_name=theme.fontawesome,
            button_id="exit"))

    def change_button_states(self, playing):
        ids = ["speed_one", "speed_two", "speed_three", "size_minus",
               "size_plus", "next", "random", "trash", "browse",
               "settings", "snapshot", "info", "exit"]
        for id in ids:
            button = self.menu.get_widget(id, True)
            if playing:
                button.update_font(self.theme.font_inactive.copy())
            else:
                button.update_font(self.theme.font_active.copy())
        if playing:
            self.menu.get_widget("play", True).hide()
            self.menu.get_widget("pause", True).show()
        else:
            self.menu.get_widget("pause", True).hide()
            self.menu.get_widget("play", True).show()

    def speed_button_pressed(self, widget, speed):
        if not self.outomaatti.is_running():
            ids = ["speed_one", "speed_two", "speed_three"]
            for id in ids:
                button = self.menu.get_widget(id, True)
                if button.get_id() == widget:
                    button.set_background_color(
                        self.theme.background_color_selected)
                else:
                    button.set_background_color(
                        self.theme.background_color)
        self.outomaatti.set_speed(speed)

    def size_button_pressed(self, change):
        if not self.outomaatti.is_running():
            self.outomaatti.change_size(change)

    def play_button_pressed(self):
        if self.outomaatti.is_running():
            self.outomaatti.pause()
            self.change_button_states(False)
        else:
            self.outomaatti.play()
            self.change_button_states(True)

    def next_button_pressed(self):
        if not self.outomaatti.is_running():
            self.outomaatti.next_generation()
            self.outomaatti.force_redraw()

    def random_button_pressed(self):
        if not self.outomaatti.is_running():
            self.outomaatti.place_random_pattern()

    def trash_button_pressed(self):
        if not self.outomaatti.is_running():
            self.outomaatti.menu_open()
            parameters = {
                "question": "Tyhjennetäänkö Universumi?",
                1: "Kyllä",
                2: "Ei"
            }
            empty_confirmation = Confirmation(400, 150, parameters, self.theme)
            if empty_confirmation.show(self.surface) == 1:
                self.outomaatti.clear_universe()
            empty_confirmation = None
            self.outomaatti.menu_closed()

    # FIX: finalize
    def browse_button_pressed(self):
        if not self.outomaatti.is_running():
            self.outomaatti.menu_open()
            pattern_chooser = PatternPicker(
                700, 550, self.outomaatti, self.theme)
            pattern_id = pattern_chooser.show(self.surface)
            pattern_chooser = None
            self.outomaatti.menu_closed()

    def settings_button_pressed(self):
        if not self.outomaatti.is_running():
            self.outomaatti.menu_open()
            settings = Settings(400, 150, self.outomaatti, self.theme)
            settings.show(self.surface)
            self.outomaatti.menu_closed()

    def info_button_pressed(self):
        if not self.outomaatti.is_running():
            self.outomaatti.menu_open()
            info = Info(700, 550, self.theme)
            info.show(self.surface)
            self.outomaatti.menu_closed()

    def snapshot_button_pressed(self):
        if not self.outomaatti.is_running():
            print("snapshot")
            self.outomaatti.save_snapshot(self.simulation.get_snapshot())

    def exit_button_pressed(self):
        if not self.outomaatti.is_running():
            self.outomaatti.menu_open()
            parameters = {
                "question": "Suljetaanko Outomaatti",
                1: "Kyllä",
                2: "Ei"
            }
            exit_confirmation = Confirmation(400, 150, parameters, self.theme)
            if exit_confirmation.show(self.surface) == 1:
                self.outomaatti.close()
            exit_confirmation = None
            self.outomaatti.menu_closed()
