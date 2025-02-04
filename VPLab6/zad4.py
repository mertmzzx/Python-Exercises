import Calculator

n1 = int(input("Въведете първото цяло число: "))
n2 = int(input("Въведете второто цяло число: "))

print(f"Сборът на двете числа е {Calculator.add(n1,n2)}")
print(f"Разликата на двете числа е {Calculator.substract(n1,n2)}")
print(f"Произведението на числата е {Calculator.multiply(n1,n2)}")
print(f"Деленото на числата е {Calculator.divide(n1,n2)}")