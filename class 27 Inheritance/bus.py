# inheritance
class vehicle:
    def __init__(self,name,maxspeed,mileage):
        self.name = name
        self.maxspeed = maxspeed
        self.mileage = mileage
class bus(vehicle):
    pass
bus1 = bus('volvo','100km/h','13km/l')
print("the busname is ",bus1.name)
print("the maxspeed is ",bus1.maxspeed)
print("the mileage is ",bus1.mileage)