from StarSurvival.Objects.ship import Ship

class Drone(Ship):
    def __init__(self):
        self.ID = "D"
        Ship.__init__(self)
