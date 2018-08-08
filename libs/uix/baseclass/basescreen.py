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
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class BaseScreen(Screen):

    tokens=literal_eval(
        open(
            os.path.join( 'data', 'tokens.txt')).read()
    )
    amount_of_HDL=((tokens['HDL'])['amount'])

    my_invoices = literal_eval(
        open(
            os.path.join('data', 'my_invoices.txt')).read()
    )
    my_invoices_text=''
    for invoice in my_invoices:
        my_invoices_text += (str(my_invoices[invoice]) + ' HDL to  '+ str(invoice)+'\n')


    sum = 0
    for token in tokens:
        sum += tokens[token]['amount'] * tokens[token]['price']
    sum=round(sum, 7)

    list_of_tokens=''
    for token in tokens:
        list_of_tokens += ( str(token) + ': '  + str(tokens[token]['amount'])+ '\n')


    balance='Balance: ' + str(amount_of_HDL) + ' HDL'
    total_amount='Total: ' + str(sum) + ' HDL'

    print(list_of_tokens)





