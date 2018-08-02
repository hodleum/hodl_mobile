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

    contacts = literal_eval(
        open(
            os.path.join( 'data', 'contacts.txt')).read()
    )
    cont_text = ''
    for contact in contacts:
        cont_text += (str(contacts[contact])  + '\n')
    cont_text=cont_text*5