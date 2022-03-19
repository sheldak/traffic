from vector import Vector


class Direction:
    def __init__(self, direction):
        self.direction = direction

    def __hash__(self):
        return self.direction.__hash__()

    def __eq__(self, other):
        return type(other) == Direction and self.direction == other.direction

    def opposite(self):
        if self.direction == "up":
            return Direction("down")
        elif self.direction == "right":
            return Direction("left")
        elif self.direction == "down":
            return Direction("up")
        elif self.direction == "left":
            return Direction("right")

    def to_vector(self):
        if self.direction == "up":
            return Vector(0, -1)
        elif self.direction == "right":
            return Vector(1, 0)
        elif self.direction == "down":
            return Vector(0, 1)
        elif self.direction == "left":
            return Vector(-1, 0)
