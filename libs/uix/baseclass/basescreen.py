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

class BaseScreen(Screen):

    tokens={ 'HDL':{'amount':10.5 , 'price':1},
             'DVT':{'amount':6, 'price':0.2}
                                                            }

    amount_of_HDL=((tokens['HDL'])['amount'])

    sum = 0
    for token in tokens:
        sum += tokens[token]['amount'] * tokens[token]['price']

    balance='Balance: ' + str(amount_of_HDL) + ' HDL'
    total_amount='Total: ' + str(sum) + ' HDL'
