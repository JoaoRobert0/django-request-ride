class CalculateRace():
    def __init__(self):
        self.distance_in_km = 0
        self.price_for_km = 5
    
    def getValue(self):
        return self.distance_in_km * self.price_for_km

class CalculateRaceX(CalculateRace):
    def __init__(self, distance_in_km):
        super().__init__()
        self.distance_in_km = distance_in_km
    
    def getValue(self):
        return super().getValue()
    
class CalculateRaceMotocycle(CalculateRace):
    def __init__(self, distance_in_km):
        super().__init__()
        self.distance_in_km = distance_in_km
    
    def getValue(self):
        return super().getValue() * 0.9
    
class CalculateRaceBlack(CalculateRace):
    def __init__(self, distance_in_km):
        super().__init__()
        self.distance_in_km = distance_in_km
    
    def getValue(self):
        return super().getValue() * 1.1