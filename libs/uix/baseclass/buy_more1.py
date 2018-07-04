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


class Buy_More1 (Screen):

    def printBuy(self, text):
        buy_amount=text
        if float(buy_amount)>0:
            print (buy_amount)
        else:
            pass
