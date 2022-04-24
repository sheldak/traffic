from enum import Enum

from app.vector import Vector


class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    def opposite(self):
        return Direction((self.value + 2) % 4)

    def turn(self, direction):
        to_add = 1 if direction == Direction.RIGHT else -1
        return Direction((self.value + to_add) % 4)

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
