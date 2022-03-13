# coding=utf-8
"""
Marcus Vinicius Braga, 2022.
marcus@marvinbraga.com.br
All rights reserved.

Game Module.
"""
from code.core.abstract_scene import AbstractScene
from code.player import Player


class Game(AbstractScene):

    def __init__(self):
        super().__init__()
        self.player = Player(groups=(self.all_sprites, ))

    def update(self):
        self.player.update()
        super().update()

    def check_keys(self, event):
        pass

    def check_events(self, event):
        pass
