from pynput.keyboard import Listener
from platform.auto import get_active_window_title

from config import Config
from keybind import Keybind

import subprocess
from typing import Optional

MODIFIER_KEYS = [
    'shift',
    'shift_r',
    'shift_l',
    'ctrl',
    'ctrl_r',
    'ctrl_l',
    'alt',
    'alt_r',
    'alt_l',
    'cmd',
    'cmd_r',
    'cmd_l',
]

class AVDTaps:
    config: Config

    _busy_keys = set()

    def __init__(self):
        self.config = Config.from_file('./config.json')

    def _get_actionable_key(self, key) -> Optional[str]:
        active_window = get_active_window_title()

        if not self.config.is_active_window(active_window):
            return None

        try:
            k = key.char
        except AttributeError:
            k = key.name

        if not self.config.is_watched_key(k) and k not in MODIFIER_KEYS:
            return None

        return k

    def _is_modifier_key(self, key) -> bool:
        return key in MODIFIER_KEYS

    def _is_modifier_pressed(self) -> bool:
        return len(self._busy_keys.intersection(MODIFIER_KEYS)) > 0

    def handle_key_press(self, key):
        k = self._get_actionable_key(key)
        if k is None:
            return

        if self._is_modifier_key(k):
            self._busy_keys.add(k)
            return

        keybind = self.config.get_keybind(k)

        if keybind.is_swipe() or keybind.is_swipe_hold():
            self.swipe_keybind(k, keybind)
        else:
            self.tap_keybind(k, keybind)

    def handle_key_release(self, key):
        k = self._get_actionable_key(key)
        if k is None:
            return

        if self._is_modifier_key(k):
            if k in self._busy_keys:
                self._busy_keys.remove(k)
            return

        keybind = self.config.get_keybind(k)

        if keybind.is_swipe_hold():
            x, y = keybind.to_coords()
            subprocess.run(['adb', 'shell', 'input', 'motionevent', 'UP', str(x), str(y)])

        if k in self._busy_keys:
            self._busy_keys.remove(k)

    def tap_keybind(self, k: str, keybind: Keybind):
        if keybind.is_single() and k in self._busy_keys:
            return

        self._busy_keys.add(k)

        if keybind.ignore_modifiers and self._is_modifier_pressed():
            return

        self.debug_print(f'Key {k} pressed, tapping coords ({keybind.x}, {keybind.y})')
        subprocess.run(['adb', 'shell', 'input', 'tap', str(keybind.x), str(keybind.y)])

    def swipe_keybind(self, k: str, keybind: Keybind):
        if k in self._busy_keys:
            return

        self._busy_keys.add(k)

        if keybind.ignore_modifiers and self._is_modifier_pressed():
            return

        from_x, from_y = keybind.from_coords()
        to_x, to_y = keybind.to_coords()

        self.debug_print(f'Key {k} pressed, swiping from coords ({from_x}, {from_y}) to coords ({to_x}, {to_y})')

        subprocess.run(['adb', 'shell', 'input', 'motionevent', 'DOWN', str(from_x), str(from_y)])
        subprocess.run(['adb', 'shell', 'input', 'motionevent', 'MOVE', str(to_x), str(to_y)])

        if keybind.is_swipe():
            subprocess.run(['adb', 'shell', 'input', 'motionevent', 'UP', str(to_x), str(to_y)])

    def run(self):
        with Listener(
            on_press=self.handle_key_press,
            on_release=self.handle_key_release,
        ) as listener:
            print(f'AVD Taps is running. Used preset: {self.config.name()}')
            listener.join()

    def debug_print(self, msg):
        if not self.config.is_debug():
            return

        print(msg)
