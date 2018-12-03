from low_level_root import hodl_mobile
from libs.uix.lists import SingleIconItem
import json


class App(hodl_mobile):
    """
    High-level root
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with open('accounts.json') as f:
            self.accounts = json.loads(f.read())['accounts']
            self.account = json.loads(f.read())['current']
