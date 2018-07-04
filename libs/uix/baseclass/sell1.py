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


class Sell1 (Screen):

    def printSell(self, text):
        sell_amount=text
        if float(sell_amount)>0:
            print (sell_amount)
        else:
            pass
