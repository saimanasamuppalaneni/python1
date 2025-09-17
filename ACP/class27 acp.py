# bus fare
class vehicle:
    def __init__(self,name):
        self.name = name
    def calculate_fare(self,capacity,maintenance):

        self.capacity = capacity
        self.maintenance = maintenance
    
class bus(vehicle):
    def __init__(self):
        super().__init__()
    def bus_fare(self):
        self.capacity * 100 * 0.10
        total_fare = self.capacity + self.maintenance
        print(f"the total fare of the bus ride is ",total_fare)


bus1  = bus ("volvo","50","10%")