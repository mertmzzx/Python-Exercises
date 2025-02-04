class Arithmetics:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def print(self):
        print(self.num1, self.num2 )
    def sum(self):
        return self.num1 + self.num2
    def razlika(self):
        return self.num1 - self.num2
    def proizvedenie(self):
        return self.num1 * self.num2
    def delenie(self):
        if self.num1 != 0 and self.num2 != 0:
            return self.num1 // self.num2

num1 = int(input())
num2 = int(input())

MyNumbers = Arithmetics(num1, num2)
MyNumbers.print()
print("Сумата на числата е",MyNumbers.sum())
print("Разликата на числата е", MyNumbers.razlika())
print("Произведението на числата е", MyNumbers.proizvedenie())
print(f"Частното на числата е", MyNumbers.delenie())