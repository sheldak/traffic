class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        if type(other) in [int, float]:
            return Vector(self.x * int(other), self.y * int(other))

    def __rmul__(self, other):
        if type(other) in [int, float]:
            return Vector(self.x * int(other), self.y * int(other))

    def add(self, speed, direction):
        return self + speed * direction.to_vector()

    def to_tuple(self):
        return self.x, self.y
