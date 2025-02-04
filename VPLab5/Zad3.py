func = input()
a = int(input())
b = int(input())

def subirane(a,b):
    S = a + b
    print(S)

def izvajdane(a, b):
    S = a - b
    print(S)

def umnojenie(a, b):
    S = a * b
    print(S)

def delenie(a, b):
    S = a // b
    print(S)

if  func == 'събиране':
    subirane(a,b)
elif func == 'изваждане':
    izvajdane(a,b)
elif func == 'умножение':
    umnojenie(a,b)
elif func == 'деление':
    delenie(a,b)
