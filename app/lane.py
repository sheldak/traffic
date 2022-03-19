class Lane:
    def __init__(self, direction):
        self.direction = direction
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)
