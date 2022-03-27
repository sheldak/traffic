from app.car import Car

from app.config import *


class Map:
    def __init__(self, width, height, screen, roads, junctions, cars_to_add):
        self.width = width
        self.height = height

        self.screen = screen

        self.roads = roads
        self.junctions = junctions
        self.cars_to_add = cars_to_add

    def update(self, current_time):
        self.screen.fill(BUILDING_COLOR)

        for _, road in self.roads.items():
            road.blit()

        for junction in self.junctions:
            junction.blit()

        for _, road in self.roads.items():
            for _, lane in road.lanes.items():
                for entity in lane.entities:
                    if type(entity) == Car:
                        entity.update(lane.close_entities(entity))
                        entity.blit()

        if current_time in self.cars_to_add:
            for car in self.cars_to_add[current_time]:
                car.lane.add_entity(car)

            del self.cars_to_add[current_time]
