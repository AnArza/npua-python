from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        print('Car created')

class Plane(Vehicle):
    def __init__(self):
        super().__init__()
        print('Plane created')

class Boat(Vehicle):
    def __init__(self):
        super().__init__()
        print('Boat created')

class RaceCar(Car):
    def __init__(self):
        super().__init__()
        print('RaceCar created')


vehicle = Vehicle()
car = Car()
plane = Plane()
boat = Boat()
race_car = RaceCar()
