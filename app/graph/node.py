class Node:
    def __init__(self, is_destination):
        self.is_destination = is_destination
        self.neighbors = {}

    def __setitem__(self, key, value):
        self.neighbors[key] = value
