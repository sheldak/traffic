import pygame

from app.vector import Vector
from app.direction import Direction

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

    def update(self, cars):
        accelerate = True
        for car in cars:
            if car is not self and self.is_near(car):
                accelerate = False

        if accelerate:
            self.speed = min(self.speed + 0.1, MAX_SPEED)
        else:
            self.speed = max(self.speed - 0.2, 0)

        self.position = self.position.add(self.speed, self.direction)

    def is_near(self, car):
        if self.direction == Direction.UP:
            return self.position.y > car.position.y > self.position.y - 60
        elif self.direction == Direction.RIGHT:
            return self.position.x < car.position.x < self.position.x + 60
        elif self.direction == Direction.DOWN:
            return self.position.y < car.position.y < self.position.y + 60
        elif self.direction == Direction.LEFT:
            return self.position.x > car.position.x > self.position.x - 60

    def blit(self):
        self.screen.blit(self.surf, self.position.to_tuple())
