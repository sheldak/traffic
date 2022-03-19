import pygame
from car import Car
from map import Map
from road import Road
from direction import Direction


def load_map(file_path):
    with open(file_path) as contents:
        width, height = map(lambda value: int(value), contents.readline().split())
        screen = pygame.display.set_mode([width, height])

        roads = {}
        future_cars = []

        mode = None
        for line in contents:
            if line == "roads\n":
                mode = "roads"
            elif line == "cars\n":
                mode = "cars"
            else:
                if mode == "roads":
                    name, x, y, width, height = line.split()
                    roads[name] = Road(name, int(x), int(y), int(width), int(height))
                elif mode == "cars":
                    road_name, direction, spawn_time, speed = line.split()
                    x, y = roads[road_name].start_points[Direction(direction)]

                    car_direction = Direction(direction).opposite()
                    lane = roads[road_name].lanes[car_direction]
                    car = Car(screen, x, y, car_direction, int(speed), lane)

                    if int(spawn_time) == 0:
                        roads[road_name].lanes[car.direction].add_car(car)
                    else:
                        future_cars.append((car, int(spawn_time)))

        spawn_times = set()
        for _, spawn_time in future_cars:
            spawn_times.add(spawn_time)

        spawn_times = sorted(spawn_times)

        cars = dict([(time, []) for time in spawn_times])
        for car, time in future_cars:
            cars[time].append(car)

        return Map(width, height, screen, roads, cars)
