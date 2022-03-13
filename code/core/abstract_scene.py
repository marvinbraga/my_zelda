# coding=utf-8
"""
Marcus Vinicius Braga, 2022.
marcus@marvinbraga.com.br
https://github.com/marvinbraga/
All rights reserved.

Abstract Scene Module.
"""

from abc import ABCMeta, abstractmethod

import pygame


class AbstractScene(metaclass=ABCMeta):

    def __init__(self):
        self.all_sprites = pygame.sprite.Group()
        self.change_scene = False
        self.valid_keys = []

    def draw(self, windows):
        self.all_sprites.draw(windows)

    def update(self, *args, **kwargs):
        self.all_sprites.update(*args, **kwargs)

    @abstractmethod
    def check_keys(self, event):
        pass

    @abstractmethod
    def check_events(self, event):
        pass
