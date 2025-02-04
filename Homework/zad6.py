numbers = list(map(float, input("Въведете числа: ").split()))

absolute_values = list(map(lambda x: abs(x), numbers))

print(absolute_values)