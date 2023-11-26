from typing import Dict
from coords import Coords

import json

class Config:
    __debug: bool
    __active_window_title: str
    __keybinds: Dict[str, Coords]

    def __init__(self, debug, active_window_title, keybinds):
        self.__debug = debug
        self.__active_window_title = active_window_title
        self.__keybinds = keybinds

    @staticmethod
    def from_dict(d: Dict):
        return Config(
            d.get('debug', False),
            d.get('window_title', None),
            d.get('keybinds', {})
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

    def get_coords(self, key: str):
        return self.__keybinds[key]

    def is_debug(self):
        return self.__debug
