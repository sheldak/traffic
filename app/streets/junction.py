import pygame

from app.streets.junctions.light import Light
from app.streets.junctions.light_color import LightColor
from app.direction import Direction

from app.config import *


class Junction:
    def __init__(self, screen, horizontal_street, vertical_street):
        self.screen = screen

        self.horizontal_street = horizontal_street
        self.vertical_street = vertical_street

        self.start_x = None
        self.start_y = None
        self.width = None
        self.height = None
        self.calculate_junction_position()

        self.roads = {}

        self.lights = {
            Direction.UP: Light(screen, self, Direction.UP, LightColor.GREEN),
            Direction.RIGHT: Light(screen, self, Direction.RIGHT, LightColor.RED),
            Direction.DOWN: Light(screen, self, Direction.DOWN, LightColor.GREEN),
            Direction.LEFT: Light(screen, self, Direction.LEFT, LightColor.RED)
        }

        self.entities = set()

    def calculate_junction_position(self):
        self.start_x = self.vertical_street.start_x
        self.start_y = self.horizontal_street.start_y
        self.width = self.vertical_street.width
        self.height = self.horizontal_street.height

    def add_road(self, direction, road):
        self.roads[direction] = road

    def has_stop_light(self, coming_direction):
        return self.lights[coming_direction.opposite()].is_stop_light()

    def is_car_on_junction(self, car):
        return self.start_x < car.position.x + CAR_WIDTH < self.start_x + self.width and \
            self.start_y < car.position.y + CAR_HEIGHT < self.start_y + self.height

    def check_being_on_junction(self, entity):
        if self.start_x > entity.entity.position.x + CAR_WIDTH:
            self.roads[Direction.LEFT].lanes[Direction.LEFT].add_entity(entity)
        elif self.start_x + self.width < entity.entity.position.x:
            self.roads[Direction.RIGHT].lanes[Direction.RIGHT].add_entity(entity)
        elif self.start_y > entity.entity.position.y + CAR_HEIGHT:
            self.roads[Direction.UP].lanes[Direction.UP].add_entity(entity)
        elif self.start_y + self.height < entity.entity.position.y:
            self.roads[Direction.DOWN].lanes[Direction.DOWN].add_entity(entity)
        else:
            return

        self.entities.remove(entity)

    def add_entity(self, entity):
        self.entities.add(entity)

    def update(self, current_time):
        for light in self.lights.values():
            light.update(current_time)

        for entity in self.entities.copy():
            entity.update(self.entities, None)
            self.check_being_on_junction(entity)

    def blit(self):
        pygame.draw.rect(self.screen, ROAD_COLOR, (self.start_x, self.start_y, self.width, self.height))

        for light in self.lights.values():
            light.blit()

        for entity in self.entities:
            entity.blit()
