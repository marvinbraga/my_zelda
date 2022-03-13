# coding=utf-8
"""
Marcus Vinicius Braga, 2022.
marcus@marvinbraga.com.br
https://github.com/marvinbraga/
All rights reserved.

Movement Status Module.
"""
import os

from code.core.base_artefact import BaseArtefact
from code.core.base_movement import BasicMovement
from code.core.support import ImportFolder


class SpritesArtefact(BaseArtefact, BasicMovement):

    def __init__(self, image, pos, groups):
        super().__init__(image, pos, groups)
        self.status = None
        self.animations = {}
        self.sprites_path = ''
        self.index = 0
        self.animation_speed = 0.15

    def import_assets(self):
        for animation in self.animations.keys():
            full_path = os.path.normpath(os.path.join(self.sprites_path, animation))
            self.animations[animation] = ImportFolder.load(full_path)
        return self

    def animate(self):
        animation = self.animations[self.status.value]
        self.index = (self.index + self.animation_speed) % len(animation)
        self.image = animation[int(self.index)]
        self.rect = self.image.get_rect(center=self.hit_box.center)
        return self

    def up(self):
        super().up()
        self.status.up()
        return self

    def down(self):
        super().down()
        self.status.down()
        return self

    def left(self):
        super().left()
        self.status.left()
        return self

    def right(self):
        super().right()
        self.status.right()
        return self

    def update_status(self):
        self.status.update()
        return self

    def update(self):
        super().update()
        self.update_status().animate()
