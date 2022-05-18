from app.direction import Direction
from app.graph.node import Node

from queue import Queue


class Graph:
    def __init__(self):
        self.nodes = {}

    def initialize(self, junction):
        queue = []
        index = 0

        node = Node(junction)
        queue.append((node, junction))
        self.nodes[junction] = node

        while index < len(queue):
            node, junction = queue[index]

            if not node.is_destination:
                for direction, road in junction.roads.items():
                    next_junction = road.junctions[direction]

                    if next_junction in self.nodes:
                        node[direction] = self.nodes[next_junction]
                        self.nodes[next_junction][direction.opposite()] = node
                    else:
                        if direction in [Direction.LEFT, Direction.RIGHT]:
                            street_name = junction.horizontal_street.name
                        else:
                            street_name = junction.vertical_street.name

                        streets_names = {direction: street_name, direction.opposite(): street_name}

                        next_node = Node(next_junction, streets_names)

                        node[direction] = next_node
                        next_node[direction.opposite()] = node

                        queue.append((next_node, next_junction))

                        if next_junction is not None:
                            self.nodes[next_junction] = next_node

            index += 1

    def find_path_to_destination(self, start_junction, start_direction, destination):
        visited = set()

        queue = Queue()
        queue.put((self.nodes[start_junction], start_direction, []))

        while not queue.empty():
            node, direction, turns = queue.get()

            if node.is_destination:
                if node.streets_names[direction] == destination[0] and direction == destination[1]:
                    return turns
            elif node not in visited:
                for turn_direction in [Direction.LEFT, Direction.UP, Direction.RIGHT]:
                    next_direction = direction.turn(turn_direction)
                    queue.put((node[next_direction], next_direction, turns + [turn_direction]))

            visited.add(node)
