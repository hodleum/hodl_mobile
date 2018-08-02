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
import sys
from ast import literal_eval

from kivy.app import App
from kivy.uix.modalview import ModalView
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.config import ConfigParser
from kivy.clock import Clock
from kivy.utils import get_color_from_hex, get_hex_from_color
from kivy.metrics import dp
from kivy.properties import ObjectProperty, StringProperty

from main import __version__
from libs.translation import Translation
from libs.uix.baseclass.startscreen import StartScreen
from libs.uix.lists import Lists
from kivy.uix.textinput import TextInput
from libs.utils.showplugins import ShowPlugins

from kivy.uix.screenmanager import Screen

class Contacts(Screen):

    contacts = literal_eval(
        open(
            os.path.join( 'data', 'contacts.txt')).read()
    )
    cont_text = ''
    for contact in contacts:
        cont_text += (str(contacts[contact])  + '\n')
        cont_text=cont_text*2
