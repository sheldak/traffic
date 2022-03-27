import pygame

from app.direction import Direction
from app.roads.lane import Lane

from app.config import *


class Road:
    def __init__(self, screen, name, x, y, width, height):
        self.screen = screen

        self.name = name
        self.start_x = x
        self.start_y = y
        self.width = width
        self.height = height

        self.start_points = None
        self.lanes = None
        self.set_start_points()
        self.set_lanes()

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

    def set_lanes(self):
        if self.width > self.height:
            self.lanes = {
                Direction.LEFT: Lane(Direction.LEFT),
                Direction.RIGHT: Lane(Direction.RIGHT)
            }
        else:
            self.lanes = {
                Direction.UP: Lane(Direction.UP),
                Direction.DOWN: Lane(Direction.DOWN)
            }

    def is_vertical(self):
        return Direction.UP in self.lanes.keys()

    def is_horizontal(self):
        return Direction.LEFT in self.lanes.keys()

    def blit(self):
        pygame.draw.rect(self.screen, ROAD_COLOR, (self.start_x, self.start_y, self.width, self.height))
