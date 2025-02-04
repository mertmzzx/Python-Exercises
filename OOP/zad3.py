class Person:
    def __init__(self, name, family, age, nationality):
        self.name = name
        self.family = family
        self.age = age
        self.nationality = nationality
    def print(self):
        print(f"{self.name} {self.family} {self.age} {self.nationality}")


class Student(Person):
    def __init__(self, name, family, age, nationality, university, yearofstudy):
        super().__init__(name, family, age, nationality)
        self.university = university
        self.yearofstudy = yearofstudy
    def print(self):
        print(f"First Name: {self.name}, Last Name: {self.family}, Age: {self.age}, Nationality: {self.nationality}, ")
        print(f"University: {self.university}, Year of Study: {self.yearofstudy}")

MyStudent = Student("Petar", "Vasilev", 19, "Bulgarian", "TU Sofia", "2024")
MyStudent.print()

class Lecturer(Person):
    def __init__(self, name, family, age, nationality, university, experience):
        super().__init__(name, family, age, nationality)
        self.university = university
        self.experience = experience
    def print(self):
        print(f"First Name: {self.name}, Last Name: {self.family}, Age: {self.age}, Nationality: {self.nationality}, ")
        print(f"University: {self.university}, Years of Experience: {self.experience}")

Lecturer = Lecturer("Ivan", "Sapundjiev", 49, "Bulgarian", "TU Sofia", "27")
Lecturer.print()