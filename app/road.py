from direction import Direction
from lane import Lane

from app.config import *


class Road:
    def __init__(self, name, x, y, width, height):
        self.name = name
        self.start_x = x
        self.start_y = y
        self.width = width
        self.height = height

        if self.width > self.height:
            self.start_points = {
                Direction("left"): (self.start_x, self.start_y + CAR_HEIGHT + 2 * ROAD_GAP),
                Direction("right"): (self.start_x + width, self.start_y + ROAD_GAP)
            }

            self.lanes = {
                Direction("left"): Lane(Direction("left")),
                Direction("right"): Lane(Direction("right"))
            }
        else:
            self.start_points = {
                Direction("up"): (self.start_x + ROAD_GAP, self.start_y),
                Direction("down"): (self.start_x + CAR_WIDTH + 2 * ROAD_GAP, self.start_y + height - CAR_HEIGHT)
            }

            self.lanes = {
                Direction("up"): Lane(Direction("up")),
                Direction("down"): Lane(Direction("down"))
            }

    def rect(self):
        return self.start_x, self.start_y, self.width, self.height
