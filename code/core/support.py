# coding=utf-8
"""
Marcus Vinicius Braga, 2022.
marcus@marvinbraga.com.br
https://github.com/marvinbraga/
All rights reserved.

Support Functions Module.
"""

import os
from csv import reader
from os import walk

import pygame


class ImportCsvLayout:

    @staticmethod
    def load(path):
        with open(path) as level_map:
            layout = reader(level_map, delimiter=",")
            terrain_map = [list(row) for row in layout]
        return terrain_map


class ImportFolder:

    @staticmethod
    def load(path):
        surface_list = []
        for _, _, img_files in walk(path):
            surface_list = [
                pygame.image.load(os.path.normpath(os.path.join(path, image))).convert_alpha()
                for image in img_files
            ]
        return surface_list
