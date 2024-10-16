from car import Car
from truck import Truck

class Garage:
    def __init__(self):
        self.parked_vehicle = None

    def set_vehicle(self, parked):
        self.parked_vehicle =parked

    def __str__(self):
        # Check whether there is any vehicle parked in the garage
        if self.parked_vehicle:
            return f"Description of the parked vehicle:\n{self.parked_vehicle}"
        return "No vehicle parked in the garage."
