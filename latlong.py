import math

class LatLong:
        latitude = 0
        longitude = 0
	
        def __init__(self, latitude, longitude):
                self.lat = lat
                self.long = long
class City:
        def __init__(self, name, population, industry, lat, long):
                super().__init__(self, lat, long)
                this.name = name
                this.population = population
                this.industry = industry
        def getProductivity(self):
                return math.log(self.population + 1)
