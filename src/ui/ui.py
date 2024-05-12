import pygame
import numpy as np
from config import settings
from services.outomaatti_service import OutomaattiService
from ui.components.menu import Menu
from ui.components.status import Status
from ui.components.simulation import Simulation
from ui.components.theme import Theme
from ui.components.popup import Popup


class UI:
    """This class implements the Outomaatti UI."""

    def __init__(self):
        """Constructor for the Outomaatti UI.
        
        Creates an instance of OutomaattiService and instances of UI components.
        """

        self.simulation_surface_size_x = 600
        self.simulation_surface_size_y = 600
        self.universe_size_x = settings.general.default_universe_width
        self.universe_size_y = settings.general.default_universe_height
        self.scaling_factor_x = self.simulation_surface_size_x / self.universe_size_x
        self.scaling_factor_y = self.simulation_surface_size_y / self.universe_size_y

        self.outomaatti = OutomaattiService(
            self.universe_size_x, self.universe_size_y)

        pygame.init()
        self.pygame_global = pygame

        self.pygame_global.display.set_caption(settings.ui.window_name)
        self.surface = self.pygame_global.display.set_mode((800, 625))
        self.clock = self.pygame_global.time.Clock()

        self.theme = Theme(self.pygame_global)
        self.status = Status(self.pygame_global, self.theme)
        self.simulation = Simulation(
            self.pygame_global, self.universe_size_x, self.universe_size_y, self.simulation_surface_size_x, self.simulation_surface_size_y)
        self.menu = Menu(self.outomaatti, self.simulation,
                         self.surface, self.theme)

    def update_mouse_cursor(self):
        """Updates mouse cursor based on location.

        Mouse cursor changes shape when user can draw.
        """
        mouse_position_x, mouse_position_y = self.pygame_global.mouse.get_pos()
        if not self.outomaatti.is_menu_open() and mouse_position_x <= self.simulation_surface_size_x and mouse_position_y <= self.simulation_surface_size_y:
            self.pygame_global.mouse.set_cursor(self.theme.cursor_pencil)
        else:
            self.pygame_global.mouse.set_cursor(self.theme.cursor_normal)

    def process_events(self, events):
        """Processes Pygame events.

        Args:
            events (list): Pygame events.
        """
        for event in events:
            if event.type == self.pygame_global.QUIT:
                self.is_running = False
            elif event.type == self.pygame_global.MOUSEBUTTONDOWN:
                mouse_position_x, mouse_position_y = self.pygame_global.mouse.get_pos()
                mouse_position_x_scaled = int(
                    mouse_position_x / self.scaling_factor_x)
                mouse_position_y_scaled = int(
                    mouse_position_y / self.scaling_factor_y)
                if not self.outomaatti.is_running() and mouse_position_x <= self.simulation_surface_size_x and mouse_position_y <= self.simulation_surface_size_y:
                    pattern_id = self.outomaatti.get_pattern_queue()
                    if pattern_id is not None:
                        pattern = self.outomaatti.get_pattern_by_id(pattern_id)
                        self.outomaatti.add_pattern(
                            mouse_position_x_scaled, mouse_position_y_scaled, pattern.pattern)
                    else:
                        self.outomaatti.invert_cell(
                            mouse_position_x_scaled, mouse_position_y_scaled)
            elif event.type == self.pygame_global.DROPFILE:
                status = self.outomaatti.import_pattern(event.file)
                self.outomaatti.menu_open()
                popup = Popup(500, 200, status, self.theme)
                popup.show(self.surface)
                self.outomaatti.menu_closed()

    def mainloop(self):
        """UI mainloop.
        
        Keeps reading inputs, processing them, refreshing components, etc.
        """

        medusa = self.outomaatti.get_pattern_by_name("Medusa").pattern
        self.outomaatti.add_pattern(10, 1, medusa)

        ticks = 0
        last_ticks = -10

        while 1:

            if self.outomaatti.is_redraw_needed():
                self.universe_size_x = self.outomaatti.get_width()
                self.universe_size_y = self.outomaatti.get_height()
                self.scaling_factor_x = self.simulation_surface_size_x / self.universe_size_x
                self.scaling_factor_y = self.simulation_surface_size_y / self.universe_size_y
                self.simulation.set_size(
                    self.universe_size_x, self.universe_size_y)
                self.simulation.update(
                    self.surface, self.outomaatti.get_universe_as_rgb_ndarray())

            if not self.outomaatti.is_running():
                self.update_mouse_cursor()

            events = self.pygame_global.event.get()
            self.process_events(events)
            self.menu.menu.update(events)

            self.menu.menu.draw(self.surface)

            if self.outomaatti.is_running():
                ticks += 1
                if ticks > last_ticks + (10 * (self.outomaatti.get_speed()-1)):
                    self.outomaatti.next_generation()
                    self.simulation.update(
                        self.surface, self.outomaatti.get_universe_as_rgb_ndarray())
                    last_ticks = ticks

            parameters = {"running": self.outomaatti.is_running(),
                          "ruleset": settings.rules.enabled[self.outomaatti.get_ruleset()][0],
                          "width": self.outomaatti.get_width(),
                          "height": self.outomaatti.get_height(),
                          "generation": self.outomaatti.get_generation(),
                          "cells": self.outomaatti.count_cells(),
                          "frames": self.clock.get_fps()}
            self.status.update(self.surface, parameters)

            self.pygame_global.display.update()

            self.clock.tick(60)
