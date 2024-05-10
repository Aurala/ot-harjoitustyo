import pygame
import numpy as np
from config import settings
from services.outomaatti_service import OutomaattiService
from ui.components.menu import Menu
from ui.components.status import Status
from ui.components.simulation import Simulation
from ui.components.theme import Theme


class UI:

    def __init__(self):

        # FIX: Error handling

        self.surface_size_x = 600
        self.surface_size_y = 600
        self.universe_size_x = settings.ui.default_universe_width
        self.universe_size_y = settings.ui.default_universe_height
        self.scaling_factor_x = self.surface_size_x / self.universe_size_x
        self.scaling_factor_y = self.surface_size_y / self.universe_size_y

        pygame.init()
        self.pygame_global = pygame

        pygame.display.set_caption(settings.ui.window_name)
        self.surface = pygame.display.set_mode((800, 625))
        self.clock = pygame.time.Clock()

        self.outomaatti = OutomaattiService(
            100, 100, settings.rules.enabled[0])

        self.theme = Theme(self.pygame_global)
        self.menu = Menu(self.pygame_global, self.outomaatti, self.surface, self.theme)
        self.status = Status(self.pygame_global, self.theme)
        self.simulation = Simulation(self.pygame_global, self.theme, self.scaling_factor_x, self.scaling_factor_y)

    def update_mouse_cursor(self):
        mouse_position_x, mouse_position_y = pygame.mouse.get_pos()
        if mouse_position_x <= self.surface_size_x and mouse_position_y <= self.surface_size_y:
            pygame.mouse.set_cursor(self.theme.cursor_pencil)
        else:
            pygame.mouse.set_cursor(self.theme.cursor_normal)

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
                    if not self.outomaatti.is_running:
                        self.outomaatti.invert_cell(
                            mouse_position_x_scaled, mouse_position_y_scaled)

    def mainloop(self):

        medusa = self.outomaatti.get_pattern_by_name("Medusa").pattern
        self.outomaatti.add_pattern(10, 1, medusa)

        # FIX: optimize, optimize, optimize
        # - framerate
        # - define what to redraw and when
        # - move the Outomaatti calculation to an async thread if needed

        ticks = 0
        last_ticks = -10

        while 1:

            if self.outomaatti.is_redraw_needed():
                self.simulation.update(self.surface, self.outomaatti.get_universe_as_rgb_ndarray())

            self.update_mouse_cursor()

            # FIX: Should process both Outomaatti and menu events at once
            events = pygame.event.get()
            self.process_events(events)

            if self.outomaatti.is_running():
                ticks += 1
                if ticks > last_ticks + (10 * (self.outomaatti.get_speed()-1)):
                    self.outomaatti.next_generation()
                    self.simulation.update(self.surface, self.outomaatti.get_universe_as_rgb_ndarray())
                    last_ticks = ticks

            parameters = {"running": self.outomaatti.is_running(),
                          "width": self.outomaatti.get_width(),
                          "height": self.outomaatti.get_height(),
                          "generation": self.outomaatti.get_generation(),
                          "cells": self.outomaatti.count_cells(),
                          "frames": self.clock.get_fps()}
            self.status.update(self.surface, parameters)

            self.menu.menu.update(events)
            self.menu.menu.draw(self.surface)

            pygame.display.update()

            self.clock.tick(60)
