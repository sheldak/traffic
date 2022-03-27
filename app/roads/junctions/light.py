import pygame

from app.direction import Direction

from app.config import *


class Light:
    def __init__(self, screen, junction, direction, initial_color):
        self.screen = screen

        self.start_x = None
        self.start_y = None
        self.width = None
        self.height = None
        self.set_position(junction, direction)

        self.color = initial_color

    def set_position(self, junction, direction):
        if direction == Direction.UP:
            self.start_x = junction.start_x
            self.start_y = junction.start_y - LIGHT_SIZE
            self.width = junction.width
            self.height = LIGHT_SIZE
        elif direction == Direction.RIGHT:
            self.start_x = junction.start_x + junction.width
            self.start_y = junction.start_y
            self.width = LIGHT_SIZE
            self.height = junction.height
        elif direction == Direction.DOWN:
            self.start_x = junction.start_x
            self.start_y = junction.start_y + junction.height
            self.width = junction.width
            self.height = LIGHT_SIZE
        elif direction == Direction.LEFT:
            self.start_x = junction.start_x - LIGHT_SIZE
            self.start_y = junction.start_y
            self.width = LIGHT_SIZE
            self.height = junction.height

    def blit(self):
        pygame.draw.rect(self.screen, self.color.to_rgb(), (self.start_x, self.start_y, self.width, self.height))
