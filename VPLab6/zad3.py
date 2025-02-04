import geometry

token = input("Въведете фигура: ")

if token == "квадрат":
    a = int(input("a = "))
    S = geometry.square(a)
    print(f"S = {S}")
elif token == "триъгълник":
    a = int(input("a = "))
    b = int(input("b = "))
    S = geometry.triangle(a, b)
    print(f"S = {S}")
elif token == "правоъгълник":
    a = int(input("a = "))
    b = int(input("b = "))
    S = geometry.rectangle(a, b)
    print(f"S = {S}")
elif token == "ромб":
    a = int(input("a = "))
    h = int(input("h = "))
    S = geometry.romb(a, h)
    print(f"S = {S}")
elif token == "трапец":
    a = int(input("a = "))
    b = int(input("b = "))
    h = int(input("h = "))
    S = geometry.trapec(a, h)
    print(f"S = {S}")