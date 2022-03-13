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


class Player(MovementArtefact):

    def __init__(self, groups):
        image = os.path.normpath('../resources/graphics/test/player.png')
        super().__init__(image, (50, 50), groups)

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
