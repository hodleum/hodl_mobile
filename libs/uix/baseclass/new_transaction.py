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


class New_Transaction (Screen):

    def printTransaction_amount(self, text):
        transaction_amount=text
        if float(transaction_amount)>0:
            print (transaction_amount)
        else:
            pass

    tokens = literal_eval(
        open(
            os.path.join('data', 'tokens.txt')).read()
    )
    text_amount_of_HDL = 'Total amount: ' + str(((tokens['HDL'])['amount'])) + 'HDL'
