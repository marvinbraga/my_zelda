import pygame

from code.core.base_artefact import BaseArtefact


class MovementArtefact(BaseArtefact):

    def __init__(self, image, pos, groups):
        super().__init__(image, pos, groups)
        self.direction = pygame.math.Vector2()
        self.speed = 5

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hit_box.x += self.direction.x * speed
        self.hit_box.y += self.direction.y * speed
        self.rect.center += self.direction * speed

        return self

    def up(self):
        super().up()
        self.direction.y = -1
        return self

    def down(self):
        super().down()
        self.direction.y = 1
        return self

    def left(self):
        super().left()
        self.direction.x = -1
        return self

    def right(self):
        super().right()
        self.direction.x = 1
        return self

    def input(self):
        self.update_undo()
        return self

    def update(self):
        super().update()
        self.input().move(self.speed)
