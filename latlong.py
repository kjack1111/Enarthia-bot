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
    def __init__(self, username, name, government, population, resources, cities):
        self.username = username
        self.name = name
        self.government = government
        self.population = population
        self.resources = resources
        self.cities = cities
    def __str__(self):
        return f"{self.name} ({self.username})"
    def getCapital(self):
        return self.cities[0]
mycountry = Country("kjack1111", "testland", "Social Democracy", 128048, ["Bauxite", "Copper", "Uranium"], ["Dpt 1", "Dpt 2", "Dpt 3"])
print(mycountry)
