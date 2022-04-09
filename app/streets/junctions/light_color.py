from enum import Enum

from app.config import *


class LightColor(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3

    def to_rgb(self):
        if self == LightColor.RED:
            return RED
        elif self == LightColor.YELLOW:
            return YELLOW
        elif self == LightColor.GREEN:
            return GREEN
