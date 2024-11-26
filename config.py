from typing import Dict, Optional
from keybind import Keybind

import json

class Config:
    __debug: bool
    __active_window_title: str
    __preset_name: Optional[str]
    __keybinds: Dict[str, Keybind]

    swipe_keybinds: Dict[str, Keybind] = {}

    def __init__(self, debug, active_window_title, preset_name, keybinds):
        self.__debug = debug
        self.__active_window_title = active_window_title
        self.__preset_name = preset_name
        self.__keybinds = keybinds

        for k, v in self.__keybinds.items():
            if v.is_swipe() or v.is_swipe_hold():
                self.swipe_keybinds[k] = v

    @staticmethod
    def make_keybinds(d: Dict):
        keybinds = {}

        for k, v in d.items():
            keybinds[k] = Keybind.from_dict(v)

        return keybinds

    @staticmethod
    def from_dict(d: Dict):
        return Config(
            d.get('debug', False),
            d.get('window_title', None),
            d.get('preset_name', None),
            Config.make_keybinds(d.get('keybinds', {}))
        )

    @staticmethod
    def from_json(raw: str):
        return Config.from_dict(json.loads(raw))

    @staticmethod
    def from_file(filepath: str):
        with open(filepath) as f:
            return Config.from_json(f.read())

    def is_active_window(self, title: str):
        return title == self.__active_window_title

    def is_watched_key(self, key: str):
        return key in self.__keybinds

    def get_keybind(self, key: str):
        return self.__keybinds.get(key, None)

    def is_debug(self):
        return self.__debug

    def name(self):
        return self.__preset_name or '(unnamed preset)'
