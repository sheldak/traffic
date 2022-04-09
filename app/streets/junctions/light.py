import pygame

from app.direction import Direction
from app.streets.junctions.light_color import LightColor

from app.config import *


class Light:
    def __init__(self, screen, junction, direction, initial_color):
        self.screen = screen

        self.start_x = None
        self.start_y = None
        self.width = None
        self.height = None
        self.set_position(junction, direction)

        self.previous_color = LightColor.YELLOW
        self.current_color = initial_color

        if initial_color == LightColor.GREEN:
            self.last_change = 0
        else:
            self.last_change = -(RED_LIGHT_DURATION - GREEN_LIGHT_DURATION - YELLOW_LIGHT_DURATION)

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

    def is_stop_light(self):
        return self.current_color == LightColor.RED or \
               self.current_color == LightColor.YELLOW and self.previous_color == LightColor.GREEN

    def update(self, current_time):
        if self.current_color == LightColor.GREEN and current_time - self.last_change == GREEN_LIGHT_DURATION:
            self.previous_color = self.current_color
            self.current_color = LightColor.YELLOW

            self.last_change = current_time
        elif self.current_color == LightColor.RED and current_time - self.last_change == RED_LIGHT_DURATION:
            self.previous_color = self.current_color
            self.current_color = LightColor.YELLOW

            self.last_change = current_time
        elif self.current_color == LightColor.YELLOW and current_time - self.last_change == YELLOW_LIGHT_DURATION:
            if self.previous_color == LightColor.GREEN:
                self.current_color = LightColor.RED
            elif self.previous_color == LightColor.RED:
                self.current_color = LightColor.GREEN

            self.previous_color = LightColor.YELLOW
        else:
            return

        self.last_change = current_time

    def blit(self):
        pygame.draw.rect(
            self.screen,
            self.current_color.to_rgb(),
            (self.start_x, self.start_y, self.width, self.height)
        )
