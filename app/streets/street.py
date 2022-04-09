from app.direction import Direction

from app.config import *


class Street:
    def __init__(self, screen, name, x, y, width, height):
        self.screen = screen

        self.name = name
        self.start_x = x
        self.start_y = y
        self.width = width
        self.height = height

        self.start_points = None
        self.set_start_points()

        self.roads = []
        self.start_roads = None

    def set_start_points(self):
        if self.width > self.height:
            self.start_points = {
                Direction.LEFT: (self.start_x, self.start_y + CAR_HEIGHT + 2 * ROAD_GAP),
                Direction.RIGHT: (self.start_x + self.width, self.start_y + ROAD_GAP)
            }
        else:
            self.start_points = {
                Direction.UP: (self.start_x + ROAD_GAP, self.start_y),
                Direction.DOWN: (self.start_x + CAR_WIDTH + 2 * ROAD_GAP, self.start_y + self.height - CAR_HEIGHT)
            }

    def add_road(self, road):
        self.roads.append(road)

    def set_start_roads(self):
        if self.width > self.height:
            self.start_roads = {
                Direction.LEFT: self.roads[0],
                Direction.RIGHT: self.roads[-1]
            }
        else:
            self.start_roads = {
                Direction.UP: self.roads[0],
                Direction.DOWN: self.roads[-1]
            }

    def get_initial_lane_for_car(self, direction):
        return self.start_roads[direction.opposite()].get_initial_lane_for_car(direction)

    def is_vertical(self):
        return Direction.UP in self.start_points.keys()

    def is_horizontal(self):
        return Direction.LEFT in self.start_points.keys()

    def update(self):
        for road in self.roads:
            road.update()

    def blit(self):
        for road in self.roads:
            road.blit()

    def blit_cars(self):
        for road in self.roads:
            road.blit_cars()
