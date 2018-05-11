KivyToast
========

Пакет для работы с сообщениями типа Toast на Android. Предназначен для использования в приложениях, написанных с использованием фреймворка Kivy.

Данный пакет - это улучшенная версия пакета https://github.com/knappador/kivy-toaster в которой по-человечески реализованы тосты, написанные на Kivy.

<img src="https://raw.githubusercontent.com/HeaTTheatR/KivyToast/master/Screenshot.png" 
align="center"/>

Модули пакета написанны с использованием фреймворка для  кроссплатформенной разработки <Kivy>.
Информация о фреймворке <Kivy> доступна по ссылке http://kivy.org

Пример использования (обратите внимание, что при таком импорте будет использована нативная реализация тостов для платформы Android и реализация на Kivy для других:

```python
from toast import toast

…

# И далее в коде тосты доступны 
# посредством вызова функции toast:
toast('Your message')
```

Для принудительного использования Kivy реализации на платформе Android используйте импорт вида:

```python
from toast.kivytoast import toast
```

ЯЗЫК ПРОГРАММИРОВАНИЯ
----------------------
Python 2.7 +

ЗАВИСИМОСТИ
-----------
Фреймворк [Kivy](http://kivy.org/docs/installation/installation.html)

ЛИЦЕНЗИЯ
--------
MIT

