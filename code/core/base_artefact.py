# coding=utf-8
"""
Marcus Vinicius Braga, 2022.
marcus@marvinbraga.com.br
All rights reserved.

Base Artefact Module.
"""
from math import sin

import pygame

from code.core.settings import TILE_SIZE, DEFAULT_HIT_BOX


class BaseArtefact(pygame.sprite.Sprite):

    def __init__(self, image, pos, groups):
        super().__init__(*groups)
        self.pos = pos
        self.rect_undo = None
        self.hit_box = None
        self.hit_box_undo = None
        self.load_image(image).get_rect().set_hit_box(*DEFAULT_HIT_BOX)

    def load_image(self, image):
        if image:
            self.image = pygame.image.load(image).convert_alpha()
        else:
            self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        return self

    def get_rect(self):
        self.rect = self.image.get_rect(topleft=self.pos)
        self.rect_undo = self.rect.copy()
        return self

    def set_hit_box(self, x, y):
        self.hit_box = self.rect.inflate(x, y)
        self.hit_box_undo = self.hit_box.copy()
        return self

    def update_undo(self):
        self.rect_undo = self.rect.copy()
        self.hit_box_undo = self.hit_box.copy()
        return self

    def undo(self):
        self.rect = self.rect_undo.copy()
        self.hit_box = self.hit_box_undo.copy()
        return self

    def is_collide(self, group):
        return [sprite for sprite in group if sprite.hit_box.colliderect(self.hit_box)]

    def wave_value(self, opaque=False):
        if opaque:
            self.image.set_alpha(255 if sin(pygame.time.get_ticks()) >= 0 else 0)
        else:
            self.image.set_alpha(255)
        return

    def draw(self, window):
        return self

    def up(self):
        return self

    def down(self):
        return self

    def left(self):
        return self

    def right(self):
        return self
