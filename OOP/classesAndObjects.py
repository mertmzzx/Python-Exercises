''''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__w = 10

MyPerson = Person("Ivan", 35)
print(MyPerson.name)
print(MyPerson.age)
'''

'''
class Car:
    car_type = "sports"

    def __init__(self, color):
        self.__color = color

    def print_car(self):
        print(self.__color, "\t", self.car_type)
    def get_color(self):
        return self.__color
    def set_color(self, color):
        self.__color = color

car2 = Car("yellow")
car2.print_car()
car2.color = "black"
car2.print_car()
'''

'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greetings(self):
        print("Hello, my name is " + self.name)


MyPerson = Person("Ivan", 35)
MyPerson.greetings()
'''

class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
    def printname(self):
        print(self.firstName, self.lastName)
    def __str__(self):
        return  f"{self.firstName} {self.lastName}"

'''
class Student(Person):
    pass
'''

'''
class Student(Person):
    def __init__(self, fname, lname, year):
       #Person.__init__(self, fname, lname)
       super().__init__(fname, lname)
       self.graduationyear = year
    def welcome(self):
        print("Welcome,", self.firstName, self.lastName, "to the graduation year of", self.graduationyear)

MyStudent = Student("Petar", "Vasilev", 2019)
MyStudent.printname()
MyStudent.welcome()
'''

