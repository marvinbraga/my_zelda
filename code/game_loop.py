# coding=utf-8
"""
Marcus Vinicius Braga, 2022.
marcus@marvinbraga.com.br
https://github.com/marvinbraga/
All rights reserved.

Game Loop Module.
"""

import os

import pygame

from code.game import Game
from core.abstract_game_loop import AbstractGameLoop


class GameLoop(AbstractGameLoop):

    def __init__(self, width, height, title, background_color='black'):
        icon_file = os.path.normpath("../resources/graphics/test/player.png")
        super().__init__(width, height, title, pygame.image.load(icon_file), background_color)
        self.game = Game()

    def draw(self):
        pygame.display.set_icon(self.icon)
        self.game.draw(self.window)
        self.game.update()

    def check_keys(self, event):
        self.game.check_keys(event)

    def check_events(self, event):
        self.game.check_events(event)
