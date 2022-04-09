import pygame

from app.car import Car
from app.direction import Direction, direction_from_string
from app.entity import Entity
from app.map import Map
from app.streets.junction import Junction
from app.streets.road import Road
from app.streets.street import Street


def load_map(file_path):
    """Loading a map

    `x` and `width` represent horizontal values (from left to right)
    `y` and `height` represent vertical values (from top to bottom)

    ----- Map specification -----

    First line contains size of map in pixels (width, height).

    Next lines specify the objects. They are separated to sections. Each section has one line with section type and next
    lines with listed objects. If line contains section name, it means that new section starts.

    --- Sections ---
    - Streets -
    First line - `streets`
    Next lines - 5 values:
        - street's name
        - x - start horizontally
        - y - start vertically
        - street's width
        - street's height

    - Cars -
    First line - `cars`
    Next lines - 4 values:
        - street's name - the street on which the car should appear
        - initial direction of the car (`left`, `right`, `up` or `down`)
        - spawn time of car (in ticks)
        - initial speed of car in pixels per tick
    """

    with open(file_path) as contents:
        width, height = map(lambda value: int(value), contents.readline().split())
        screen = pygame.display.set_mode([width, height])

        streets = {}
        junctions = []

        future_cars = []

        mode = None
        for line in contents:
            if line == "streets\n":
                mode = "streets"
            elif line == "cars\n":
                junctions = split_streets(screen, streets)
                mode = "cars"
            else:
                if mode == "streets":
                    name, x, y, width, height = line.split()
                    streets[name] = Street(screen, name, int(x), int(y), int(width), int(height))
                elif mode == "cars":
                    street_name, direction_string, spawn_time, speed = line.split()
                    direction = direction_from_string(direction_string)

                    x, y = streets[street_name].start_points[direction]

                    car_direction = direction.opposite()
                    lane = streets[street_name].get_initial_lane_for_car(car_direction)
                    car = Car(screen, x, y, car_direction, int(speed), lane)

                    if int(spawn_time) == 0:
                        lane.add_entity(Entity(car))
                    else:
                        future_cars.append((car, int(spawn_time)))

        spawn_times = set()
        for _, spawn_time in future_cars:
            spawn_times.add(spawn_time)

        spawn_times = sorted(spawn_times)

        cars = dict([(time, []) for time in spawn_times])
        for car, time in future_cars:
            cars[time].append(car)

        return Map(width, height, screen, streets, junctions, cars)


def split_streets(screen, streets):
    horizontal_streets = []
    vertical_streets = []
    for street in streets.values():
        if street.is_horizontal():
            horizontal_streets.append(street)
        else:
            vertical_streets.append(street)

    horizontal_streets.sort(key=lambda s: s.start_y)
    vertical_streets.sort(key=lambda v: v.start_x)

    junctions = []

    start_x = 0
    start_y = 0

    for i, horizontal_street in enumerate(horizontal_streets):
        for j, vertical_street in enumerate(vertical_streets):
            junction = Junction(screen, horizontal_street, vertical_street)

            junction_left = junctions[i * len(vertical_streets) + j - 1] if j > 0 else None
            road_left = Road(
                screen,
                start_x,
                horizontal_street.start_y,
                junction.start_x - start_x,
                horizontal_street.height,
                {
                    Direction.LEFT: junction_left,
                    Direction.RIGHT: junction
                }
            )

            if junction_left is not None:
                junction_left.add_road(Direction.RIGHT, road_left)
            junction.add_road(Direction.LEFT, road_left)

            horizontal_street.add_road(road_left)

            junction_up = junctions[(i - 1) * len(vertical_streets) + j] if i > 0 else None
            road_up = Road(
                screen,
                vertical_street.start_x,
                start_y,
                vertical_street.width,
                junction.start_y - start_y,
                {
                    Direction.UP: junction_up,
                    Direction.DOWN: junction
                }
            )

            if junction_up is not None:
                junction_up.add_road(Direction.DOWN, road_up)
            junction.add_road(Direction.UP, road_up)

            vertical_street.add_road(road_up)

            junctions.append(junction)

            if i == len(horizontal_streets) - 1:
                road_down = Road(
                    screen,
                    vertical_street.start_x,
                    junction.start_y + junction.width,
                    vertical_street.width,
                    vertical_street.height + vertical_street.start_y - (junction.start_y + junction.height),
                    {
                        Direction.UP: junction,
                        Direction.DOWN: None
                    }
                )
                junction.add_road(Direction.DOWN, road_down)

                vertical_street.add_road(road_down)

            if j == len(vertical_streets) - 1:
                road_right = Road(
                    screen,
                    junction.start_x + junction.width,
                    horizontal_street.start_y,
                    horizontal_street.width + horizontal_street.start_x - (junction.start_x + junction.width),
                    horizontal_street.height,
                    {
                        Direction.LEFT: junction,
                        Direction.RIGHT: None
                    }
                )
                junction.add_road(Direction.RIGHT, road_right)

                horizontal_street.add_road(road_right)

    for street in horizontal_streets + vertical_streets:
        street.set_start_roads()

    return junctions
