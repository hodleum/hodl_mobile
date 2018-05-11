'''
VKGroups

Copyright © 2017 HeaTTheatR

Для предложений и вопросов:
<kivydevelopment@gmail.com>

Данный файл распространяется по условиям той же лицензии,
что и фреймворк Kivy.

'''


import os
from ast import literal_eval

from libs.uix.lists import Lists
from dialogs import card, dialog


class ShowPlugins(object):
    '''Выводит на экран список установленных плагинов.'''

    def __init__(self, app):
        self._app = app
        self.window_user_plugins = None

    def _save_status_plugin(self, dialog, name_plugin, result):
        if result == self._app.translation._('Да'):
            self._list_activate_plugins.append(name_plugin)
            with open(os.path.join(self._app.directory, 'libs', 'plugins', 'plugins_list.list'), 'w') as plugin_list:
                plugin_list.write(str(self._list_activate_plugins))
        else:
            for item_list in self._list_plugins.ids.md_list.children:
                if item_list.id == name_plugin:
                    item_list.active = False
        if dialog:
            dialog.dismiss()

    def _action_plugin(self, name_plugin, state_plugin, action_plugin):
        '''Вызывается при манипуляции с пунктом плагина.
        Принимает имя, статус чекбокса ('normal/down')
        и действие ('item/check'), выбранного из списка плагина.'''

        if action_plugin == 'check':  # выбран чекбокс плагина
            if state_plugin == 'down':
                self._save_status_plugin(
                    None, name_plugin, self._app.translation._('Да')
                )
            else:
                try:
                    self._list_activate_plugins.remove(name_plugin)
                    with open(os.path.join(self._app.directory, 'libs', 'plugins', 'plugins_list.list'), 'w') as plugin_list:
                        plugin_list.write(str(self._list_activate_plugins))
                except ValueError:
                    pass
        else:
            self._show_info_plugin(name_plugin)

    def _get_info_plugins(self):
        '''Возвращает словарь вида
        {'Name item': ['Desc item', 'icon_item.png'], ...}.'''

        dict_info_plugins = {}
        self._list_activate_plugins = literal_eval(
            open(os.path.join(self._app.directory, 'libs', 'plugins', 'plugins_list.list'), encoding='utf-8').read()
        )

        for plugin in os.listdir(os.path.join(self._app.directory, 'libs', 'plugins')):
            if not os.path.isdir(os.path.join(self._app.directory, 'libs', f'plugins/{plugin}')):
                continue

            if plugin in self._list_activate_plugins:
                active = True
            else:
                active = False

            plugin_desc = self._app.started_plugins[plugin]['plugin-desc']
            plugin_icon = os.path.join(
                self._app.directory, 'libs', 'plugins',
                self._app.started_plugins[plugin]['plugin-package'], 'plugin_logo.png'
            )

            if not os.path.exists(plugin_icon):
                plugin_icon = os.path.join('data', 'logo', 'kivy-icon-128.png')
            dict_info_plugins[plugin] = [plugin_desc, plugin_icon, active]

        return dict_info_plugins

    def _show_info_plugin(self, name_plugin):
        '''Вызывается при клике на имя плагина из списка.'''

        if not os.path.exists(os.path.join(self._app.directory, 'libs', 'plugins', name_plugin, 'README.rst')):
            dialog(
                text=self._app.translation._('Нет информации о плагине!'),
                title=name_plugin
            )
        else:
            info_plugin = \
                open(os.path.join(self._app.directory, 'libs', 'plugins', name_plugin, 'README.rst'), encoding='utf-8').read()
            info_plugin = info_plugin.format(
                NAME_APP=self._app.title,
                VERSION=self._app.started_plugins[name_plugin]['plugin-version'],
                AUTHOR=self._app.started_plugins[name_plugin]['plugin-author'],
                MAIL=self._app.started_plugins[name_plugin]['plugin-mail'],
                DESC=self._app.started_plugins[name_plugin]['plugin-desc']
            )
            dialog(
                text=info_plugin, title=self._app.title
            )

    def show_plugins(self):
        '''Выводит на экран список установленных плагинов.'''

        if not self.window_user_plugins:
            dict_info_plugins = self._get_info_plugins()
            if not dict_info_plugins.__len__():
                dialog(
                    text=self._app.translation._('Нет установленных плагинов!'),
                    title=self._app.title
                )
                return

            self._list_plugins = Lists(
                dict_items=dict_info_plugins,
                events_callback=self._action_plugin, flag='two_list_icon_check'
            )
            self.window_user_plugins = card(self._list_plugins, size=(.85, .55) )
        self.window_user_plugins.open()
