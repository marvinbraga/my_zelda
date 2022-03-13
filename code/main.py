# coding=utf-8
"""
Marcus Vinicius Braga, 2022.
marcus@marvinbraga.com.br
All rights reserved.

Main Game Module.
"""
from code.core.settings import SCREEN_SIZE
from code.game_loop import GameLoop

if __name__ == '__main__':
    GameLoop(*SCREEN_SIZE, "Marvin Zelda").update()
