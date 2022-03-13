# coding=utf-8
"""
Marcus Vinicius Braga, 2022.
marcus@marvinbraga.com.br
All rights reserved.

Movement Status Module.
"""
from enum import Enum


class BaseMovementStatus(Enum):
    IDLE = 0, "idle"
    UP = 1, "up"
    DOWN = 2, "down"
    RIGHT = 3, "right"
    LEFT = 4, "left"


class BaseMovementStatusManager:

    def __init__(self, player):
        self.player = player
        self.status = []
        self.down()

    @property
    def direction(self):
        return self.value.split("_")[0]

    @property
    def value(self):
        return "_".join([str(status.value[1]) for status in self.status])

    def up(self):
        self.status = []
        self._add(BaseMovementStatus.UP)
        return self

    def down(self):
        self.status = []
        self._add(BaseMovementStatus.DOWN)
        return self

    def right(self):
        self.status = []
        self._add(BaseMovementStatus.RIGHT)
        return self

    def left(self):
        self.status = []
        self._add(BaseMovementStatus.LEFT)
        return self

    def _add(self, status):
        if not self._check(status):
            self.status.append(status)
        return self

    def _check(self, status):
        return status in self.status

    def update(self):
        if self.player.direction.x == 0 and self.player.direction.y == 0:
            if not self._check(BaseMovementStatus.IDLE):
                self._add(BaseMovementStatus.IDLE)

        # if self.player.attacking:
        #     self.player.direction.x = 0
        #     self.player.direction.y = 0
        #     if not self._check(BaseMovementStatus.ATTACKING):
        #         if self._check(BaseMovementStatus.IDLE):
        #             self.status.remove(BaseMovementStatus.IDLE)
        #         self._add(BaseMovementStatus.ATTACKING)
        #
        # else:
        #     if self._check(BaseMovementStatus.ATTACKING):
        #         self.status.remove(BaseMovementStatus.ATTACKING)

        return self
