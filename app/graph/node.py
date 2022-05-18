from app.direction import Direction


class Node:
    def __init__(self, junction, streets_names=None):
        self.junction = junction
        self.is_destination = junction is None

        if junction is None:
            self.streets_names = streets_names
        else:
            self.streets_names = {
                Direction.LEFT: junction.horizontal_street.name,
                Direction.RIGHT: junction.horizontal_street.name,
                Direction.UP: junction.vertical_street.name,
                Direction.DOWN: junction.vertical_street.name,
            }

        self.neighbors = {}

    def __setitem__(self, key, value):
        self.neighbors[key] = value

    def __getitem__(self, item):
        return self.neighbors[item]

    def __hash__(self):
        return sum(map(lambda v: v.__hash__(), self.streets_names.values()))

    def __str__(self):
        if Direction.LEFT in self.streets_names:
            h = self.streets_names[Direction.LEFT]
        else:
            h = "."

        if Direction.UP in self.streets_names:
            v = self.streets_names[Direction.UP]
        else:
            v = "."

        return "<{}, {}>".format(h, v)
