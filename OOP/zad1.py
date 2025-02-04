class Person:
    def __init__(self, name, family, age, nationality):
        self.name = name
        self.family = family
        self.age = age
        self.nationality = nationality
    def print(self):
        print(f"{self.name} {self.family} {self.nationality}")

MyPerson = Person("Petar", "Vasilev", 21, "Bulgarian")
MyPerson.print()

