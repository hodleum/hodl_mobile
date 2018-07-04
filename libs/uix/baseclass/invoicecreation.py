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


class Invoicecreation (Screen):

    def printInvoice_amount(self, text):
        invoice_amount=text
        if float(invoice_amount)>0:
            print (invoice_amount)
        else:
            pass
