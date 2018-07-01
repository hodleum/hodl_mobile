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
from kivy.properties import ObjectProperty, StringProperty

class Network (Screen):

    text = StringProperty()

    def save_searching(self):
         text= self._form_network.ids.network_search.text