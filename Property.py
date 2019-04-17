from Address import *
from FloorPlan import *
import json


class Property:
    propertyId: int
    propertyName: str
    description: str
    floorPlans: []
    address: []

    def __init__(self, *_floor_plans):
        self.propertyId = 1
        self.propertyName = "Nashville Place"
        self.description = "Regions and We Work Building"
        self.floorPlans = _floor_plans
        self.address = Address()


floor_plan1 = FloorPlan()
floor_plans = [floor_plan1]
floor_plan2 = FloorPlan()
floor_plan2.description = "Floors with cubes - Old style"
floor_plan2.price = 300000
floor_plan2.planName = "Cubes"
floor_plan2.sqFeet = 100
floor_plans.append(floor_plan2)

p = Property(floor_plans)
s = json.dumps(p, default=lambda x: x.__dict__)
print(s)
