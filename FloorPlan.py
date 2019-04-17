from decimal import *


class FloorPlan:
    planName: str
    price: Decimal
    description: str
    sqFeet: str

    def __init__(self):
        self.planName = "Open Floor"
        self.price = 200000
        self.description = "Open Floor We Work Style"
        self.sqFeet = 100
