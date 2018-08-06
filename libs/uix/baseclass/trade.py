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
from kivy.uix.spinner import Spinner

class Trade (Screen):

    tokens = literal_eval(
        open(
            os.path.join('data', 'tokens.txt')).read()
    )
    text_amount_of_HDL = str(((tokens['HDL'])['amount'])) + 'HDL'

    sum = 0
    for token in tokens:
        sum += tokens[token]['amount'] * tokens[token]['price']
    sum = round(sum, 7)

    total_amount = 'Total: ' + str(sum) + ' HDL'

    list_of_tokens = []
    for token in tokens:
        list_of_tokens.append(str(token) + ': '  +'\n'+ str(tokens[token]['amount']))

    def spinner_clicked(self, value):

        index = (value.index (':'))
        token_inf_name=(value[0:index])
        print (token_inf_name)
