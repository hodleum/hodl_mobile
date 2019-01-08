# -*- coding: utf-8 -*-
#
# This file created with KivyCreatorProject
# <https://github.com/HeaTTheatR/KivyCreatorProgect
#
# Copyright © 2017 Easy
#
# For suggestions and questions:
# <kivydevelopment@gmail.com>
#
# LICENSE: MIT

from kivy.uix.screenmanager import Screen
from kivymd.theming import ThemeManager


class Set(Screen):
    theme_cls = ThemeManager()

    def printStorage_for_storage_mining(self, text):
        mining_storage = text
        print(mining_storage)
