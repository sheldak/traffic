import pygame

from app.direction import Direction
from app.streets.junction import Junction
from app.vector import Vector

from app.config import *


class Car(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, direction, speed, lane):
        super(Car, self).__init__()
        self.surf = pygame.Surface((CAR_WIDTH, CAR_HEIGHT))
        self.surf.fill(CAR_COLOR)
        self.rect = self.surf.get_rect()

        self.screen = screen
        self.position = Vector(x, y)
        self.speed = speed
        self.direction = direction

        self.lane = lane

    def update(self, cars, nearest_junction):
        car_ahead = None
        for car in cars:
            if car is not self and self.is_car_near(car):
                car_ahead = car

        if car_ahead is not None:
            acceleration = self.braking_acceleration(car_ahead)
        elif nearest_junction is not None and self.is_stop_light_near(nearest_junction) \
                and not self.too_late_to_brake(nearest_junction):
            acceleration = self.braking_acceleration(nearest_junction)
        else:
            acceleration = 0.1

        self.speed = max(min(self.speed + acceleration, MAX_SPEED), 0)

        self.position = self.position.add(self.speed, self.direction)

    def is_car_near(self, car):
        if self.direction == car.direction:
            if self.direction == Direction.UP:
                return self.position.y > car.position.y + CAR_HEIGHT > self.position.y - BRAKING_DISTANCE
            elif self.direction == Direction.RIGHT:
                return self.position.x + CAR_WIDTH < car.position.x < self.position.x + CAR_WIDTH + BRAKING_DISTANCE
            elif self.direction == Direction.DOWN:
                return self.position.y + CAR_HEIGHT < car.position.y < self.position.y + CAR_HEIGHT + BRAKING_DISTANCE
            elif self.direction == Direction.LEFT:
                return self.position.x > car.position.x + CAR_WIDTH > self.position.x - BRAKING_DISTANCE

        return False

    def is_stop_light_near(self, junction):
        if junction.has_stop_light(self.direction):
            if self.direction == Direction.UP:
                return self.position.y > junction.start_y + junction.height > self.position.y - BRAKING_DISTANCE
            elif self.direction == Direction.RIGHT:
                return self.position.x + CAR_WIDTH < junction.start_x < self.position.x + CAR_WIDTH + BRAKING_DISTANCE
            elif self.direction == Direction.DOWN:
                return self.position.y + CAR_HEIGHT < junction.start_y < self.position.y + CAR_HEIGHT + BRAKING_DISTANCE
            elif self.direction == Direction.LEFT:
                return self.position.x > junction.start_x + junction.width > self.position.x - BRAKING_DISTANCE

        return False

    def too_late_to_brake(self, junction):
        return self.braking_acceleration(junction) < -MAX_BRAKING

    def braking_acceleration(self, object_ahead):
        if type(object_ahead) == Junction:
            distance = self.distance_to_junction(object_ahead)
        else:
            distance = self.distance_to_car(object_ahead)

        return - (self.speed ** 2) / (2 * distance)

    def distance_to_junction(self, junction):
        if self.direction == Direction.UP:
            return self.position.y - (junction.start_y + junction.height)
        elif self.direction == Direction.RIGHT:
            return junction.start_x - (self.position.x + CAR_WIDTH)
        elif self.direction == Direction.DOWN:
            return junction.start_y - (self.position.y + CAR_HEIGHT)
        elif self.direction == Direction.LEFT:
            return self.position.x - (junction.start_x + junction.width)

    def distance_to_car(self, car):
        if self.direction == Direction.UP:
            return self.position.y - (car.position.y + CAR_HEIGHT)
        elif self.direction == Direction.RIGHT:
            return car.position.x - (self.position.x + CAR_WIDTH)
        elif self.direction == Direction.DOWN:
            return car.position.y - (self.position.y + CAR_HEIGHT)
        elif self.direction == Direction.LEFT:
            return self.position.x - (car.position.x + CAR_WIDTH)

    def blit(self):
        self.screen.blit(self.surf, self.position.to_tuple())
