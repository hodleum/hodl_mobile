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
import os
from ast import literal_eval


class Buy_More2(Screen):

    def printBuy(self, text):
        buy_amount = text
        if float(buy_amount) > 0:
            print(buy_amount)
        else:
            pass

    tokens = literal_eval(
        open(
            os.path.join('data', 'tokens.txt')).read()
    )
    text_amount_of_HDL = 'Total amount of HDL:' + str(((tokens['HDL'])['amount']))
