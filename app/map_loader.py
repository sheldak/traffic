import pygame

from app.car import Car
from app.direction import direction_from_string
from app.map import Map
from app.roads.junction import Junction
from app.roads.road import Road


def load_map(file_path):
    """Loading a map

    `x` and `width` represent horizontal values (from left to right)
    `y` and `height` represent vertical values (from top to bottom)

    ----- Map specification -----

    First line contains size of map in pixels (width, height).

    Next lines specify the objects. They are separated to sections. Each section has one line with section type and next
    lines with listed objects. If line contains section name, it means that new section starts.

    --- Sections ---
    - Roads -
    First line - `roads`
    Next lines - 5 values:
        - road's name
        - x - start horizontally
        - y - start vertically
        - road's width
        - road's height

    - Cars -
    First line - `cars`
    Next lines - 4 values:
        - road's name - the road on which the car should appear
        - initial direction of the car (`left`, `right`, `up` or `down`)
        - spawn time of car (in ticks)
        - initial speed of car in pixels per tick

    - Junctions -
    First line - `junctions`
    Next lines - 2 values:
        - name of the first of the crossing roads
        - name of the second of the crossing roads
    """

    with open(file_path) as contents:
        width, height = map(lambda value: int(value), contents.readline().split())
        screen = pygame.display.set_mode([width, height])

        roads = {}
        future_cars = []
        junctions = set()

        mode = None
        for line in contents:
            if line == "roads\n":
                mode = "roads"
            elif line == "cars\n":
                mode = "cars"
            elif line == "junctions\n":
                mode = "junctions"
            else:
                if mode == "roads":
                    name, x, y, width, height = line.split()
                    roads[name] = Road(screen, name, int(x), int(y), int(width), int(height))
                elif mode == "cars":
                    road_name, direction_string, spawn_time, speed = line.split()
                    direction = direction_from_string(direction_string)

                    x, y = roads[road_name].start_points[direction]

                    car_direction = direction.opposite()
                    lane = roads[road_name].lanes[car_direction]
                    car = Car(screen, x, y, car_direction, int(speed), lane)

                    if int(spawn_time) == 0:
                        roads[road_name].lanes[car.direction].add_entity(car)
                    else:
                        future_cars.append((car, int(spawn_time)))
                elif mode == "junctions":
                    road_name_1, road_name_2 = line.split()
                    junction = Junction(screen, [roads[road_name_1], roads[road_name_2]])
                    junctions.add(junction)

        spawn_times = set()
        for _, spawn_time in future_cars:
            spawn_times.add(spawn_time)

        spawn_times = sorted(spawn_times)

        cars = dict([(time, []) for time in spawn_times])
        for car, time in future_cars:
            cars[time].append(car)

        return Map(width, height, screen, roads, junctions, cars)
