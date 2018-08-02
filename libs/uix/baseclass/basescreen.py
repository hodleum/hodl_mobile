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
#:import MDList kivymd.list.MDList

class BaseScreen(Screen):

    tokens={ 'HDL':{'amount':10.5 , 'price':1},
             'DVT':{'amount':6, 'price':0.2},
             'BTK':{'amount':10, 'price':3},
             'HDQ': {'amount': 10.5, 'price': 1},
             'DVW': {'amount': 6, 'price': 0.2},
             'BTE': {'amount': 10, 'price': 3},
             'HDR': {'amount': 10.5, 'price': 1},
             'DVY': {'amount': 6, 'price': 0.2},
             'BTU': {'amount': 10, 'price': 3},
             'HDU': {'amount': 10.5, 'price': 1},
             'DVO': {'amount': 6, 'price': 0.2},
             'BTP': {'amount': 10, 'price': 3},
           }

    amount_of_HDL=((tokens['HDL'])['amount'])

    sum = 0
    for token in tokens:
        sum += tokens[token]['amount'] * tokens[token]['price']
    sum=round(sum)

    list_of_tokens=''
    for token in tokens:
        list_of_tokens += ( str(token) + ': '  + str(tokens[token]['amount'])+ '\n')


    balance='Balance: ' + str(amount_of_HDL) + ' HDL'
    total_amount='Total: ' + str(sum) + ' HDL'

    print(list_of_tokens)

