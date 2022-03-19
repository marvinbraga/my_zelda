# coding=utf-8
"""
Marcus Vinicius Braga, 2022.
marcus@marvinbraga.com.br
https://github.com/marvinbraga/
All rights reserved.

Text Input Utils Module.
"""
import pygame
from pygame_textinput import TextInputManager, TextInputVisualizer


class TextInput:

    def __init__(self, max_length=15, fontname="Consolas", fontsize=55, fontcolor='black'):
        font = pygame.font.SysFont(fontname, fontsize)
        manager = TextInputManager(validator=lambda i: len(i) <= max_length)
        self.fontcolor = fontcolor
        # Pass these to constructor
        self.textinput_custom = TextInputVisualizer(manager=manager, font_object=font)
        self.textinput_custom.cursor_width = 4
        self.textinput_custom.antialias = True
        self.textinput_custom.cursor_blink_interval = 400  # blinking interval in ms

    @property
    def value(self):
        return self.textinput_custom.value

    def check_events(self, event):
        self.textinput_custom.update([event])

    def get_font_color(self, effect=False):
        if effect:
            return [(c + 10) % 255 for c in self.textinput_custom.font_color]
        return self.fontcolor

    def draw(self, windows):
        windows.blit(self.textinput_custom.surface, (10, 50))
        self.textinput_custom.font_color = self.get_font_color()
