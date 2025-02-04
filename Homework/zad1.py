class Building:
    def __init__(self, height, area, address):
        self.height = height
        self.area = area
        self.address = address

    def info(self):
        print(f"Сградата на {self.address} е {self.height}m висока и има площ от {self.area} m2")

class House(Building):
    def __init__(self, height, area, address, floors, owner):
        super().__init__(height, area, address)
        self.floors = floors
        self.owner = owner

    def info(self):
        print(f"Сградата на {self.address} е {self.height}m висока и има площ от {self.area} m2 и " +
              f"{self.floors} етажа. Собственикът е {self.owner} ")

def find_tallest_house(houses):
    tallest = houses[0]
    for house in houses:
        if (house.height / house.floors) > (tallest.height / tallest.floors):
            tallest = house
    return tallest

house1 = House(10, 120, "Ул. акад. Борис Стефанов 2", 2, "Иван Иванов")
house2 = House(15, 200, "Ул. акад. Борис Стефанов 3", 3, "Петър Петров")
house3 = House(8, 80, "Ул. акад. Борис Стефанов 8",1, "Стефан Иванов")

houses = [house1, house2, house3]

tallest = find_tallest_house(houses)
print("Най-просторната къща е: ")
tallest.info()