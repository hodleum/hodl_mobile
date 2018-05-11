# This file created with KivyCreatorProject
# <https://github.com/HeaTTheatR/KivyCreatorProgect
#
# Copyright © 2017 Easy
#
# For suggestions and questions:
# <kivydevelopment@gmail.com>
# 
# LICENSE: MIT

# Точка входа в приложение. Запускает основной программный код program.py.
# В случае ошибки, выводит на экран окно с её текстом.

import os
import sys
import traceback

# Никнейм и имя репозитория на github,
# куда будет отправлен отчёт баг репорта.
NICK_NAME_AND_NAME_REPOSITORY = 'https://github.com/hodleum/hodl_mobile.git'

directory = os.path.split(os.path.abspath(sys.argv[0]))[0]
sys.path.insert(0, os.path.join(directory, 'libs/applibs'))

try:
    import webbrowser
    try:
        import six.moves.urllib
    except ImportError:
        pass

    import kivy
    kivy.require('1.9.2')

    from kivy.config import Config
    Config.set('kivy', 'keyboard_mode', 'system')
    Config.set('kivy', 'log_enable', 0)

    from kivy import platform
    if platform == 'android':
        from plyer import orientation
        orientation.set_sensor(mode='any')

    from kivymd.theming import ThemeManager
    # Activity баг репорта.
    from bugreporter import BugReporter
except Exception:
    traceback.print_exc(file=open(os.path.join(directory, 'error.log'), 'w'))
    sys.exit(1)


__version__ = '0.05'


def main():
    def create_error_monitor():
        class _App(App):
            theme_cls = ThemeManager()
            theme_cls.primary_palette = 'BlueGrey'

            def build(self):
                box = BoxLayout()
                box.add_widget(report)
                return box
        app = _App()
        app.run()

    app = None

    try:
        from loadplugin import load_plugin # функция загрузки плагинов
        from hodl_mobile import hodl_mobile  # основной класс программы

        # Запуск приложения.
        app = hodl_mobile()
        load_plugin(app, __version__)
        app.run()
    except Exception:
        from kivy.app import App
        from kivy.uix.boxlayout import BoxLayout


        text_error = traceback.format_exc()
        traceback.print_exc(file=open(os.path.join(directory, 'error.log'), 'w'))

        if app:
            try:
                app.stop()
            except AttributeError:
                app = None

        def callback_report(*args):
            '''Функция отправки баг-репорта.'''

            try:
                txt = six.moves.urllib.parse.quote(
                    report.txt_traceback.text.encode('utf-8')
                )
                url = 'https://github.com/{NICK_NAME_AND_NAME_REPOSITORY}/issues/new?body=' + txt
                webbrowser.open(url)
            except Exception:
                sys.exit(1)

        report = BugReporter(
            callback_report=callback_report, txt_report=text_error,
            icon_background=os.path.join('data', 'images', 'icon.png')
        )

        if app:
            try:
                app.screen.clear_widgets()
                app.screen.add_widget(report)
            except AttributeError:
            	create_error_monitor()
        else:
            create_error_monitor()


if __name__ in ('__main__', '__android__'):
    main()
