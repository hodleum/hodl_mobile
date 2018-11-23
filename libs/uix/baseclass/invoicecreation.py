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
from kivy.properties import ObjectProperty


class Invoicecreation(Screen):

    def printInvoice_amount(self, text):
        invoice_amount = text
        if float(invoice_amount) > 0:
            print(invoice_amount)
        else:
            pass

    checkbox_is_active = ObjectProperty(False)

    def checkbox_qr_clicked(self, instance, value):
        if value is True:
            print("QR")
        else:
            pass

    def checkbox_nfc_clicked(self, instance, value):
        if value is True:
            print("NFC")
        else:
            pass

    def checkbox_by_adress_clicked(self, instance, value):
        if value is True:
            print("By Adress")
        else:
            pass
