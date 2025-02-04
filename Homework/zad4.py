class Vehicle:
    def __init__(self, wheels, model, color):
        self.wheels = wheels
        self.model = model
        self.color = color

class LuxCar(Vehicle):
    def __init__(self, wheels, model, color, passengers):
        super().__init__(wheels, model, color)
        self.passengers = passengers

    def show_info(self):
        print(f"Luxuary car model {self.model} in {self.color} with {self.wheels} wheels " +
              f"can have up to {self.passengers} passengers.")

class SportsCar(Vehicle):
    def __init__(self, wheels, model, color, loadlimit):
        super().__init__(wheels, model, color)
        self.loadlimit = loadlimit

    def show_info(self):
        print(f"Sports car model {self.model} in {self.color} with {self.wheels} wheels " +
              f"has {self.loadlimit}kg loadlimit.")

luxcar = LuxCar(4, "Bentley Continental", "black", 7)
luxcar.show_info()

sportscar = SportsCar(2,"Porsche 911", "red", 75)
sportscar.show_info()