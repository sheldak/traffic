from app.roads.junctions.light import Light
from app.roads.junctions.light_color import LightColor
from app.direction import Direction


class Junction:
    def __init__(self, screen, roads):
        self.horizontal_road = None
        self.vertical_road = None
        self.position_roads(roads)

        self.start_x = None
        self.start_y = None
        self.width = None
        self.height = None
        self.calculate_junction_position()

        self.lights = {
            Direction.UP: Light(screen, self, Direction.UP, LightColor.GREEN),
            Direction.RIGHT: Light(screen, self, Direction.RIGHT, LightColor.RED),
            Direction.DOWN: Light(screen, self, Direction.DOWN, LightColor.GREEN),
            Direction.LEFT: Light(screen, self, Direction.LEFT, LightColor.RED)
        }

    def position_roads(self, roads):
        road_1, road_2 = roads
        if road_1.is_horizontal():
            self.horizontal_road = road_1
            if not road_2.is_vertical():
                raise "Junction with two horizontal roads!"

            self.vertical_road = road_2
        elif road_1.is_vertical():
            self.vertical_road = road_1
            if not road_2.is_horizontal():
                raise "Junction with two vertical roads!"

            self.horizontal_road = road_2
        else:
            raise "Invalid roads provided to junction"

    def calculate_junction_position(self):
        self.start_x = self.vertical_road.start_x
        self.start_y = self.horizontal_road.start_y
        self.width = self.vertical_road.width
        self.height = self.horizontal_road.height

    def blit(self):
        for _, light in self.lights.items():
            light.blit()
