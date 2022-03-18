# coding=utf-8
"""
Marcus Vinicius Braga, 2022.
marcus@marvinbraga.com.br
https://github.com/marvinbraga/
All rights reserved.

Game Module.
"""
import pygame
from pygame_textinput import TextInputManager, TextInputVisualizer

from code.core.abstract_scene import AbstractScene
from code.player import Player


class Game(AbstractScene):

    def __init__(self):
        super().__init__()
        self.player = Player(groups=(self.all_sprites,))
        self.textinput_custom = None
        self.init_input()

    def init_input(self):
        # But more customization possible: Pass your own font object
        font = pygame.font.SysFont("Consolas", 55)
        # Create own manager with custom input validator
        manager = TextInputManager(validator=lambda i: len(i) <= 15)
        # Pass these to constructor
        self.textinput_custom = TextInputVisualizer(manager=manager, font_object=font)
        # Customize much more
        self.textinput_custom.cursor_width = 4
        self.textinput_custom.cursor_blink_interval = 400  # blinking interval in ms
        self.textinput_custom.antialias = True
        self.textinput_custom.cursor_width = 4

    def update(self):
        self.player.update()
        super().update()

    def check_keys(self, event):
        pass

    def check_events(self, event):
        self.textinput_custom.update([event])

    def draw(self, windows):
        windows.blit(self.textinput_custom.surface, (10, 50))
        self.textinput_custom.font_color = [(c + 10) % 255 for c in self.textinput_custom.font_color]
        super().draw(windows)
