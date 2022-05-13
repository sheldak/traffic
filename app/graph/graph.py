from app.graph.node import Node


class Graph:
    def __init__(self):
        self.nodes = {}

    def initialize_graph(self, junction):
        queue = []
        index = 0

        node = Node(junction is None)
        queue.append((node, junction))

        while index < len(queue):
            node, junction = queue[index]

            if not node.is_destination and junction not in self.nodes:
                for direction, road in junction.roads.items():
                    next_junction = road.junctions[direction]
                    node[direction] = next_junction

                    next_node = Node(next_junction is None)
                    queue.append((next_node, next_junction))

                self.nodes[junction] = node

            index += 1
