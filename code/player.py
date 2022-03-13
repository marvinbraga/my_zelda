# coding=utf-8
"""
Marcus Vinicius Braga, 2022.
marcus@marvinbraga.com.br
All rights reserved.

Player Module.
"""
import os

import pygame

from code.core.movement_artefact import MovementArtefact
from code.core.sprites_artefact import SpritesArtefact


class Player(MovementArtefact, SpritesArtefact):

    def __init__(self, groups):
        super().__init__(None, (50, 50), groups)
        self.sprites_path = os.path.normpath('../resources/graphics/player/')
        self.animations = {
            'up': [], 'down': [], 'left': [], 'right': [],
            'right_idle': [], 'left_idle': [], 'up_idle': [], 'down_idle': [],
            'right_attack': [], 'left_attack': [], 'up_attack': [], 'down_attack': []
        }
        self.import_player_assets()

    def input(self):
        super().input()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.up()
        elif keys[pygame.K_DOWN]:
            self.down()
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.right()
        elif keys[pygame.K_LEFT]:
            self.left()
        else:
            self.direction.x = 0

        return self

    def update_status(self):
        self.status.update()
        return self

    def update(self):
        self.input()
        self.update_status()
        self.move(self.speed)
        self.animate()
