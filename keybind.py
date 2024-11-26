from typing import Optional
from math import sin, cos, radians

class Keybind:
    KEYBIND_TYPE_SINGLE = 'single'
    KEYBIND_TYPE_HOLD = 'hold'
    KEYBIND_TYPE_SWIPE = 'swipe'
    KEYBIND_TYPE_SWIPE_HOLD = 'swipe_hold'

    x: int
    y: int
    keybind_type: str
    distance: Optional[int] = None
    angle: Optional[int] = None
    ignore_modifiers: bool = True

    def __init__(
        self,
        x: int,
        y: int,
        keybind_type: Optional[str] = KEYBIND_TYPE_SINGLE,
        distance: Optional[int] = None,
        angle: Optional[int] = None,
        ignore_modifiers: bool = True
    ):
        self.x = x
        self.y = y
        self.keybind_type = keybind_type
        self.distance = distance
        self.angle = angle
        self.ignore_modifiers = ignore_modifiers

        if (self.is_swipe() or self.is_swipe_hold()) and (self.distance is None or self.angle is None):
            raise ValueError('distance and angle must be provided for swipe and swipe_hold keybinds')

    def is_single(self):
        return self.keybind_type == self.KEYBIND_TYPE_SINGLE

    def is_hold(self):
        return self.keybind_type == self.KEYBIND_TYPE_HOLD

    def is_swipe(self):
        return self.keybind_type == self.KEYBIND_TYPE_SWIPE

    def is_swipe_hold(self):
        return self.keybind_type == self.KEYBIND_TYPE_SWIPE_HOLD

    def from_coords(self):
        return self.x, self.y

    def to_coords(self):
        x = self.x
        y = self.y

        if self.is_swipe() or self.is_swipe_hold():
            x += self.distance * cos(radians(self.angle))
            y += self.distance * sin(radians(self.angle))

        return x, y

    @staticmethod
    def from_dict(d: dict):
        return Keybind(
            d['x'],
            d['y'],
            d.get('keybind_type', Keybind.KEYBIND_TYPE_SINGLE),
            d.get('distance', None),
            d.get('angle', None),
            d.get('ignore_modifiers', True)
        )
