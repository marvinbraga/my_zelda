# coding=utf-8
"""
Marcus Vinicius Braga, 2022.
marcus@marvinbraga.com.br
https://github.com/marvinbraga/
All rights reserved.

Game Module.
"""

from code.core.abstract_scene import AbstractScene
from code.core.text_input import TextInput
from code.player import Player


class Game(AbstractScene):

    def __init__(self):
        super().__init__()
        self.player = Player(groups=(self.all_sprites,))
        self.textinput = TextInput()

    def update(self):
        self.player.update()
        super().update()

    def check_keys(self, event):
        pass

    def check_events(self, event):
        self.textinput.check_events(event)
        pass

    def draw(self, windows):
        self.textinput.draw(windows)
        super().draw(windows)
