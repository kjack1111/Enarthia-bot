import math

class LatLong:
    latitude = 0
    longitude = 0

    def __init__(self, latitude, longitude):
        self.lat = lat
        self.long = long
class City(LatLong):
    def __init__(self, name, population, industry, lat, long):
        super().__init__(self, lat, long)
        this.name = name
        this.population = population
        this.industry = industry
    def getProductivity(self):
        return math.log(self.population + 1)
class Country(LatLong):
    def __init__(self, leader, name, government, population, resources, cities):
        self.leader = str(leader)
        self.name = name
        self.government = government
        self.population = population
        self.resources = resources
        self.cities = cities
        self.__dict__ = {
            "name" : self.name,
            "leader" : self.leader,
            "government" : self.government,
            "population" : self.population,
            "resources" : self.resources,
            "cities" : self.cities
        }
    def __str__(self):
        return f"{self.name} ({self.leader})."
    def getCapital(self):
        return self.cities[0]
    def toJSON(self):
        return self.__dict__
mycountry = Country("kjack1111", "testland", "Social Democracy", 128048, ["Bauxite", "Copper", "Uranium"], ["Dpt 1", "Dpt 2", "Dpt 3"])
print(mycountry)
