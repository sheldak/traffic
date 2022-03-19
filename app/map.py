import pygame

from app.config import *


class Map:
    def __init__(self, width, height, screen, roads, cars_to_add):
        self.width = width
        self.height = height

        self.screen = screen

        self.roads = roads
        self.cars_to_add = cars_to_add

    def update(self, current_time):
        self.screen.fill(BUILDING_COLOR)

        for _, road in self.roads.items():
            pygame.draw.rect(self.screen, ROAD_COLOR, road.rect())

        for _, road in self.roads.items():
            for _, lane in road.lanes.items():
                for car in lane.cars:
                    car.update(lane.cars)
                    car.blit()

        if current_time in self.cars_to_add:
            for car in self.cars_to_add[current_time]:
                car.lane.add_car(car)

            del self.cars_to_add[current_time]
