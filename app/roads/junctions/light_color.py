from enum import Enum

from app.config import *


class LightColor(Enum):
    RED = 1
    GREEN = 2

    def to_rgb(self):
        if self == LightColor.RED:
            return RED
        elif self == LightColor.GREEN:
            return GREEN
