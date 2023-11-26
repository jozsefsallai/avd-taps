from pynput.keyboard import Listener
from platform.auto import get_active_window_title

from config import Config

import subprocess

class AVDTaps:
    config: Config

    def __init__(self):
        self.config = Config.from_file('./config.json')

    def handle_key_press(self, key):
        active_window = get_active_window_title()

        if not self.config.is_active_window(active_window):
            return

        try:
            k = key.char
        except AttributeError:
            k = key.name

        if not self.config.is_watched_key(k):
            return

        coords = self.config.get_coords(k)

        self.debug_print(f'Key {k} pressed, tapping coords {coords}')

        self.tap_coords(coords)

    def tap_coords(self, coords):
        x, y = coords
        subprocess.run(['adb', 'shell', 'input', 'tap', str(x), str(y)])

    def run(self):
        with Listener(on_press=self.handle_key_press) as listener:
            print('AVD Taps is running...')
            listener.join()

    def debug_print(self, msg):
        if not self.config.is_debug():
            return

        print(msg)
