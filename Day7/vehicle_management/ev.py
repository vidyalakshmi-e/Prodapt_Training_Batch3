from car import Car
from exception import InvalidBatteryCapacityError
class EV(Car):
    def __init__(self,brand,model,year,battery_capacity,owner=None):
        super().__init__(brand,model,year,owner)
        
        if battery_capacity <=0:
            raise InvalidBatteryCapacityError(battery_capacity)
        self.battery_capacity=battery_capacity

    def start_engine(self):
        print(f"The electric engine of the {self.brand} {self.model} started ")
    
    def charge_battery(self):
        print(f"The battery of the {self.brand} {self.model} is charging. Capcity: {self.battery_capacity}")

