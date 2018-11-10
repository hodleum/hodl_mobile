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
import os
from ast import literal_eval
from kivy.uix.screenmanager import Screen

class Contacts(Screen):

    def populate(self):
        contacts = literal_eval(
            open(
                os.path.join('data','contacts.txt')).read()
        )
        self.rv.data = [{'value': ''.join(str(contacts[contact]))}
                        for contact in contacts]
