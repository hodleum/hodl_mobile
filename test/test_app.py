'''
This file is responsible for testing Apps inside the CreatorKivyProject project.
'''

import os
import sys
import unittest

from kivy.clock import Clock


class AppTest(unittest.TestCase):

    def test_creator_app(self):
        sys.path.insert(0, os.path.split(os.path.abspath(sys.argv[0]))[0])
        from testprogram import Testprogram
        test = Testprogram()
        Clock.schedule_once(test.stop, 1)
        test.run()
