from enum import Enum

from app.vector import Vector


class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

    def opposite(self):
        if self == Direction.UP:
            return Direction.DOWN
        elif self == Direction.RIGHT:
            return Direction.LEFT
        elif self == Direction.DOWN:
            return Direction.UP
        elif self == Direction.LEFT:
            return Direction.RIGHT

    def to_vector(self):
        if self == Direction.UP:
            return Vector(0, -1)
        elif self == Direction.RIGHT:
            return Vector(1, 0)
        elif self == Direction.DOWN:
            return Vector(0, 1)
        elif self == Direction.LEFT:
            return Vector(-1, 0)


def direction_from_string(direction):
    if direction == "up":
        return Direction.UP
    elif direction == "right":
        return Direction.RIGHT
    elif direction == "down":
        return Direction.DOWN
    elif direction == "left":
        return Direction.LEFT
