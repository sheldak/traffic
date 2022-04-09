import pygame

from app.direction import Direction
from app.streets.lane import Lane

from app.config import *


class Road:
    def __init__(self, screen, x, y, width, height, junctions):
        self.screen = screen

        self.start_x = x
        self.start_y = y
        self.width = width
        self.height = height

        self.start_points = None
        self.lanes = None

        self.junctions = junctions

        self.set_lanes()

    def set_lanes(self):
        if self.width > self.height:
            self.lanes = {
                Direction.LEFT: Lane(self.junctions[Direction.LEFT], Direction.LEFT),
                Direction.RIGHT: Lane(self.junctions[Direction.RIGHT], Direction.RIGHT)
            }
        else:
            self.lanes = {
                Direction.UP: Lane(self.junctions[Direction.UP], Direction.UP),
                Direction.DOWN: Lane(self.junctions[Direction.DOWN], Direction.DOWN)
            }

    def get_initial_lane_for_car(self, direction):
        return self.lanes[direction]

    def update(self):
        for lane in self.lanes.values():
            lane.update()

    def blit(self):
        pygame.draw.rect(self.screen, ROAD_COLOR, (self.start_x, self.start_y, self.width, self.height))

    def blit_cars(self):
        for lane in self.lanes.values():
            lane.blit()
