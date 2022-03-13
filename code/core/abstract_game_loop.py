# coding=utf-8
"""
Marcus Vinicius Braga, 2022.
marcus@marvinbraga.com.br
https://github.com/marvinbraga/
All rights reserved.

Abstract Game Loop Module.
"""

from abc import ABCMeta, abstractmethod

import pygame

from code.core import settings


class AbstractGameLoop(metaclass=ABCMeta):

    def __init__(self, width, height, title, icon=None, background_color='black'):
        pygame.init()
        self.window = pygame.display.set_mode([width, height])
        self.icon = icon
        self.title = title
        pygame.display.set_caption(self.title)
        self.fps = pygame.time.Clock()
        self.background_color = background_color

        self.loop = True
        self._valid_keys = []

    def add_valid_key(self, keys):
        self._valid_keys.append(keys)
        return self

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def check_keys(self, event):
        pass

    @abstractmethod
    def check_events(self, event):
        pass

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.loop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.loop = False
                if event.key in self._valid_keys:
                    self.check_keys(event)
            elif event.type == pygame.KEYUP:
                if event.key in self._valid_keys:
                    self.check_keys(event)
            else:
                self.check_events(event)

    def update(self):
        pygame.mixer.init()
        try:
            while self.loop:
                self.fps.tick(settings.FPS)
                self.window.fill(self.background_color)
                self.draw()
                self.events()
                pygame.display.update()
        finally:
            # pygame.mixer.music.stop()
            pygame.mixer.quit()
            pygame.quit()
