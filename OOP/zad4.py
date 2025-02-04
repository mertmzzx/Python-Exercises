import math
class Number:
    def __init__(self, num):
        self.number = num
    def pow2(self):
        return int(math.pow(self.number,2))
    def pow3(self):
        return int(math.pow(self.number, 3))
    def print(self):
        print(self.number)

num = int(input())

MyNumber = Number(num)
MyNumber.print()
stepen2 = MyNumber.pow2()
print(stepen2)
stepen3 = MyNumber.pow3()
print(stepen3)