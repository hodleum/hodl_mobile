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
import sys
from ast import literal_eval
from kivy.uix.popup import Popup

from kivy.app import App
from kivy.uix.modalview import ModalView
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.config import ConfigParser
from kivy.clock import Clock
from kivy.utils import get_color_from_hex, get_hex_from_color
from kivy.metrics import dp
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.gridlayout import GridLayout

from main import __version__
from libs.translation import Translation
from libs.uix.baseclass.startscreen import StartScreen
from libs.uix.lists import Lists
from kivy.uix.textinput import TextInput
from libs.utils.showplugins import ShowPlugins

from kivymd.theming import ThemeManager

from toast import toast
from dialogs import card

kv = """
<Theme_Popup>:
    size_hint: .8, .6
    auto_dismiss: False
    title: 'Choose theme'
    title_color:0,0,0,1
    separator_color:app.theme_cls.primary_color
    background: ''
    FloatLayout:
        GridLayout:
            rows:4
            cols:5
            pos_hint: {'x':0.05,'y':0.15}
            size_hint:0.9,0.8
            spacing:'18dp'
            Button:
                color:0,0,0,1
                background_normal: ''
                background_color:(0.404, 0.227, 0.718, 1.0) 
                on_press:
                    app.change_theme('DeepPurple')
            Button:
                color:0,0,0,1
                background_normal: ''
                background_color:(0.012, 0.663, 0.957, 1.0) 
                on_press:
                    app.change_theme('LightBlue')
            Button:
                color:0,0,0,1
                background_normal: ''
                background_color:(0.545, 0.765, 0.290, 1.0) 
                on_press:
                    app.change_theme('LightGreen')                
            Button:
                color:0,0,0,1
                background_normal: ''
                background_color:(0.957, 0.263, 0.212, 1.0)
                on_press:
                    app.change_theme('Red')
            Button:
                color:0,0,0,1
                background_normal: ''
                background_color:(1.000, 0.757, 0.027, 1.0)
                on_press:
                    app.change_theme('Amber')
            Button:
                color:0,0,0,1
                background_normal: ''
                background_color:(1.000, 0.341, 0.133, 1.0) 
                on_press:
                    app.change_theme('DeepOrange')    
            Button:
                color:0,0,0,1
                background_normal: ''
                background_color:(0.376, 0.490, 0.545, 1.0) 
                on_press:
                    app.change_theme('BlueGrey')                
            Button:
                color:0,0,0,1
                background_normal: ''
                background_color:(0.129, 0.588, 0.953, 1.0)  
                on_press:
                    app.change_theme('Blue')
            Button:
                color:0,0,0,1
                background_normal: ''
                background_color:(0.298, 0.686, 0.314, 1.0)
                on_press:
                    app.change_theme('Green')
            Button:
                color:0,0,0,1      
                background_normal: ''
                background_color:(1.000, 0.922, 0.231, 1.0)
                on_press:
                    app.change_theme('Yellow')
            Button:
                color:0,0,0,1
                background_normal: ''
                background_color:(0.914, 0.118, 0.388, 1.0)
                on_press:
                    app.change_theme('Pink')
            Button:
                color:0,0,0,1
                background_normal: ''
                background_color:(0.612, 0.153, 0.690, 1.0)    
                on_press:
                    app.change_theme('Purple')
            Button:
                color:0,0,0,1
                background_normal: ''
                background_color:(0.247, 0.318, 0.710, 1.0)
                on_press:
                    app.change_theme('Indigo')
            Button:
                color:0,0,0,1      
                background_normal: ''
                background_color:(0.000, 0.737, 0.831, 1.0)
                on_press:
                    app.change_theme('Cyan')
            Button:
                color:0,0,0,1
                background_normal: ''
                background_color:(0.475, 0.333, 0.282, 1.0)
                on_press:
                    app.change_theme('Brown')
            Button:
                color:0,0,0,1
                background_normal: ''
                background_color:(0.620, 0.620, 0.620, 1.0)   
                on_press:
                    app.change_theme('Grey')
            Button:
                color:0,0,0,1
                background_normal: ''
                background_color:(1.000, 0.596, 0.000, 1.0)
                on_press:
                    app.change_theme('Orange')
            Button:
                color:0,0,0,1      
                background_normal: ''
                background_color:(0.000, 0.588, 0.533, 1.0)
                on_press:
                    app.change_theme('Teal')
            Button:
                color:0,0,0,1
                background_normal: ''
                background_color:(0.804, 0.863, 0.224, 1.0)
                on_press:
                    app.change_theme('Lime')                    
        Button:
            background_normal: ''
            color:0,0,0,1
            pos_hint: {'x':0.8,'y':0.05}
            size_hint:0.2,0.1
            text:'Close'
            on_press:
                root.dismiss()  
"""
Builder.load_string(kv)


class Theme_Popup(Popup):
    pass


class hodl_mobile(App):
    def show_popup(self):
        p = Theme_Popup()
        p.open()

    '''Функционал программы.'''

    title = 'hodl_mobile'
    icon = 'icon.png'
    nav_drawer = ObjectProperty()
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Blue'
    lang = StringProperty('en')
    cont = StringProperty()

    def __init__(self, **kvargs):
        super(hodl_mobile, self).__init__(**kvargs)
        Window.bind(on_keyboard=self.events_program)
        Window.soft_input_mode = 'below_target'

        self.list_previous_screens = ['base']
        self.window = Window
        self.plugin = ShowPlugins(self)
        self.config = ConfigParser()
        self.manager = None
        self.window_language = None
        self.window_contacts = None
        self.exit_interval = False
        self.dict_language = literal_eval(
            open(
                os.path.join(self.directory, 'data', 'locales', 'locales.txt')).read()
        )
        self.dict_contacts = literal_eval(
            open(
                os.path.join(self.directory, 'data', 'contacts.txt')).read()
        )
        self.translation = Translation(
            self.lang, 'Ttest', os.path.join(self.directory, 'data', 'locales')
        )

    def get_application_config(self):
        return super(hodl_mobile, self).get_application_config(
            '{}/%(appname)s.ini'.format(self.directory))

    def build_config(self, config):
        '''Создаёт файл настроек приложения hodl_mobile.ini.'''

        config.adddefaultsection('General')
        config.setdefault('General', 'language', 'en')

    def set_value_from_config(self):
        '''Устанавливает значения переменных из файла настроек hodl_mobile.ini.'''

        self.config.read(os.path.join(self.directory, 'hodl_mobile.ini'))
        self.lang = self.config.get('General', 'language')

    def build(self):
        self.set_value_from_config()
        self.load_all_kv_files(os.path.join(self.directory, 'libs', 'uix', 'kv'))
        self.screen = StartScreen()  # main screen
        self.manager = self.screen.ids.manager
        self.nav_drawer = self.screen.ids.nav_drawer

        return self.screen

    def load_all_kv_files(self, directory_kv_files):
        for kv_file in os.listdir(directory_kv_files):
            kv_file = os.path.join(directory_kv_files, kv_file)
            if os.path.isfile(kv_file):
                with open(kv_file, encoding='utf-8') as kv:
                    Builder.load_string(kv.read())

    def events_program(self, instance, keyboard, keycode, text, modifiers):
        '''On menu button press.'''

        if keyboard in (1001, 27):
            if self.nav_drawer.state == 'open':
                self.nav_drawer.toggle_nav_drawer()
            self.back_screen(event=keyboard)
        elif keyboard in (282, 319):
            pass

        return True

    def back_screen(self):
        '''Менеджер экранов. Вызывается при нажатии Back Key
        и шеврона "Назад" в ToolBar.'''

        # Нажата BackKey.
        if self.manager.current == 'base':
            self.dialog_exit()
            return
        try:
            self.manager.current = self.list_previous_screens.pop()
        except:
            self.manager.current = 'base'
        self.screen.ids.action_bar.title = self.title
        self.screen.ids.action_bar.left_action_items = \
            [['menu', lambda x: self.nav_drawer._toggle()]]

    def select_locale(self, *args):
        '''Выводит окно со списком имеющихся языковых локализаций для
        установки языка приложения.'''

        def select_locale(name_locale):
            '''Устанавливает выбранную локализацию.'''

            for locale in self.dict_language.keys():
                if name_locale == self.dict_language[locale]:
                    self.lang = locale
                    self.config.set('General', 'language', self.lang)
                    self.config.write()

        dict_info_locales = {}
        for locale in self.dict_language.keys():
            dict_info_locales[self.dict_language[locale]] = \
                ['locale', locale == self.lang]

        if not self.window_language:
            self.window_language = card(
                Lists(
                    dict_items=dict_info_locales,
                    events_callback=select_locale, flag='one_select_check'
                ),
                size=(.85, .55)
            )
        self.window_language.open()

    def show_plugins(self, *args):
        '''Выводит на экран список плагинов.'''
        self.plugin.show_plugins()

    def show_about(self, *args):
        self.nav_drawer.toggle_nav_drawer()
        self.screen.ids.about.ids.label.text = \
            self.translation._(
                u'[size=20][b]hodl_mobile[/b][/size]\n\n'
                u'[b]Version:[/b] {version}\n'
                u'[b]License:[/b] MIT\n\n'
                u'[size=20][b]Developer[/b][/size]\n\n'
                u'HODL is a cryptocurrency with smart contracts.\n\n'
                u'[ref=SITE_PROJECT]'
                u'[color={link_color}]NAME_AUTHOR[/color][/ref]\n\n'
                u'[b]Source code:[/b] '
                u'[ref=https://github.com/hodleum/hodl_mobile.git]'
                u'[color={link_color}]GitHub[/color][/ref]').format(
                version=__version__,
                link_color=get_hex_from_color(self.theme_cls.primary_color)
            )
        self.manager.current = 'about'
        self.screen.ids.action_bar.title = \
            self.translation._('About')

    def show_buy_new_tokens(self, *args):
        self.manager.current = 'buy_new_tokens'
        self.screen.ids.action_bar.title = \
            self.translation._('Buy tokens')
        self.screen.ids.action_bar.left_action_items = \
            [['arrow-left', lambda x: self.show_back_trade()]]

    def show_scan(self, *args):
        self.manager.current = 'scan'
        self.screen.ids.action_bar.title = \
            self.translation._('Scan')
        self.screen.ids.action_bar.left_action_items = \
            [['arrow-left', lambda x: self.show_back_main()]]

    def show_find_new_contact(self, *args):
        self.manager.current = 'find_new_contact'
        self.screen.ids.action_bar.title = \
            self.translation._('Find new contact')
        self.screen.ids.action_bar.left_action_items = \
            [['arrow-left', lambda x: self.show_back_contacts()]]

    def show_new_transaction(self, *args):
        self.manager.current = 'new_transaction'
        self.screen.ids.action_bar.title = \
            self.translation._('New transaction')
        self.screen.ids.action_bar.left_action_items = \
            [['arrow-left', lambda x: self.show_back_main()]]

    def show_tokens_info(self, *args):
        self.manager.current = 'tokens_info'
        self.screen.ids.action_bar.title = \
            self.translation._('DVT')
        self.screen.ids.action_bar.left_action_items = \
            [['arrow-left', lambda x: self.show_back_trade()]]

    def show_back_tokens_info(self, *args):
        self.manager.current = 'tokens_info'
        self.screen.ids.action_bar.title = \
            self.translation._('DVT')
        self.screen.ids.action_bar.left_action_items = \
            [['arrow-left', lambda x: self.show_back_trade()]]

    def show_choose_from_contacts(self, *args):

        def select_contact(name_contact):
            for contact in self.dict_contacts.keys():
                if name_contact == self.dict_contacts[contact]:
                    self.window_contacts.dismiss()
                    self.cont = name_contact
                    text_cont = name_contact
                    print(text_cont)
                    self.window_contacts.dismiss()

        dict_info_contacts = {}
        for contact in self.dict_contacts.keys():
            dict_info_contacts[self.dict_contacts[contact]] = \
                ['contact', contact == self.cont]

        if not self.window_contacts:
            self.window_contacts = card(
                Lists(
                    dict_items=dict_info_contacts,
                    events_callback=select_contact, flag='one_select_check'
                ),
                size=(.85, .55)
            )
        self.window_contacts.open()

    def show_invoicecreation(self, *args):
        self.manager.current = 'invoicecreation'
        self.screen.ids.action_bar.title = \
            self.translation._('Invoice creation')
        self.screen.ids.action_bar.left_action_items = \
            [['arrow-left', lambda x: self.show_back_main()]]

    def show_set(self, *args):
        self.manager.current = 'set'
        self.nav_drawer._toggle()
        self.screen.ids.action_bar.title = \
            self.translation._('Settings')

    def show_trade(self, *args):
        self.manager.current = 'trade'
        self.nav_drawer._toggle()
        self.screen.ids.action_bar.title = \
            self.translation._('Trade')

    def show_profile(self, *args):
        self.manager.current = 'profile'
        self.nav_drawer._toggle()
        self.screen.ids.action_bar.title = \
            self.translation._('Profile')

    def show_back_trade(self, *args):
        self.manager.current = 'trade'
        self.screen.ids.action_bar.title = \
            self.translation._('Trade')
        self.screen.ids.action_bar.left_action_items = \
            [['menu', lambda x: self.nav_drawer._toggle()]]

    def show_buy_more1(self, *args):
        self.manager.current = 'buy_more1'
        self.screen.ids.action_bar.title = \
            self.translation._('Buy')
        self.screen.ids.action_bar.left_action_items = \
            [['arrow-left', lambda x: self.show_back_trade()]]

    def show_sell1(self, *args):
        self.manager.current = 'sell1'
        self.screen.ids.action_bar.title = \
            self.translation._('Sell')
        self.screen.ids.action_bar.left_action_items = \
            [['arrow-left', lambda x: self.show_back_trade()]]

    def show_contacts(self, *args):
        self.manager.current = 'contacts'
        self.nav_drawer._toggle()
        self.screen.ids.action_bar.title = \
            self.translation._('Contacts')

    def show_back_contacts(self, *args):
        self.manager.current = 'contacts'
        self.screen.ids.action_bar.title = \
            self.translation._('Contacts')
        self.screen.ids.action_bar.left_action_items = \
            [['menu', lambda x: self.nav_drawer._toggle()]]

    def show_main(self, *args):
        self.manager.current = 'base'
        self.nav_drawer._toggle()
        self.screen.ids.action_bar.title = \
            self.translation._('Home screen')

    def show_back_main(self, *args):
        self.manager.current = 'base'
        self.screen.ids.action_bar.title = \
            self.translation._('Home screen')
        self.screen.ids.action_bar.left_action_items = \
            [['menu', lambda x: self.nav_drawer._toggle()]]

    def show_network(self, *args):
        self.manager.current = 'network'
        self.nav_drawer._toggle()
        self.screen.ids.action_bar.title = \
            self.translation._('Network')

    def show_license(self, *args):
        self.screen.ids.license.ids.text_license.text = \
            self.translation._('%s') % open(
                os.path.join(self.directory, 'LICENSE'), encoding='utf-8').read()
        self.nav_drawer._toggle()
        self.manager.current = 'license'
        self.screen.ids.action_bar.title = \
            self.translation._('MIT LICENSE')

    def dialog_exit(self):
        def check_interval_press(interval):
            self.exit_interval += interval
            if self.exit_interval > 5:
                self.exit_interval = False
                Clock.unschedule(check_interval_press)

        if self.exit_interval:
            sys.exit(0)

        Clock.schedule_interval(check_interval_press, 1)
        toast(self.translation._('Press Back to Exit'))

    def change_theme(self, value):
        self.theme_cls.primary_palette = value
        return value

    def on_lang(self, instance, lang):
        self.translation.switch_lang(lang)

    def to_start(self):

        self.screen = StartScreen()
        return self.screen
