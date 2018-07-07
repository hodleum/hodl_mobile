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
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.properties import BooleanProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.metrics import dp
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout

contacts_list= [{'name': 'Вася', 'wallet':'vasyapupkin'},
                {'name':'Коля', 'wallet':'nalogoplotelshik'}
                                                             ]

class SelectableLabel(RecycleDataViewBehavior, Label):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

class Contacts(RecycleView,Screen):
    def __init__(self, **kwargs):
        super(Contacts, self).__init__(**kwargs)
        self.data = [{'text': (str(contact['name'] + '\n' + '('+'wallet: '  +str(contact['wallet'])+ ')'))} for contact in contacts_list*50]
