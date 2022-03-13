# coding=utf-8
"""
Marcus Vinicius Braga, 2022.
marcus@marvinbraga.com.br
https://github.com/marvinbraga/
All rights reserved.

Abstract Game Loop Module.
"""

import pygame

pygame.init()
font = pygame.font.Font(None, 30)


class DebugInfo:

    @staticmethod
    def show(info, y=10, x=10, foreground_color='White', background_color='Black'):
        surface = pygame.display.get_surface()
        debug_surf = font.render(str(info), True, foreground_color)
        debug_rect = debug_surf.get_rect(topleft=(x, y))
        pygame.draw.rect(surface, background_color, debug_rect)
        surface.blit(debug_surf, debug_rect)
