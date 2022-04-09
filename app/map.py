from app.entity import Entity

from app.config import *


class Map:
    def __init__(self, width, height, screen, streets, junctions, cars_to_add):
        self.width = width
        self.height = height

        self.screen = screen

        self.streets = streets
        self.junctions = junctions
        self.cars_to_add = cars_to_add

    def update(self, current_time):
        self.screen.fill(BUILDING_COLOR)

        for junction in self.junctions:
            junction.update(current_time)

        for street in self.streets.values():
            street.update()
            street.blit()

        for junction in self.junctions:
            junction.blit()

        for street in self.streets.values():
            street.blit_cars()

        if current_time in self.cars_to_add:
            for car in self.cars_to_add[current_time]:
                car.lane.add_entity(Entity(car))

            del self.cars_to_add[current_time]
