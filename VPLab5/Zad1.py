figure = input()

def fK():
    a = int(input('a = '))
    S = a * a
    print(f'Лицето на квадрата е равно на {S} cm2')

def fP():
    a = int(input('a = '))
    b = int(input('b = '))
    S = a * b
    print(f'Лицето на правоъгълника е равно на {S} cm2')

def fT():
    a = int(input('a = '))
    b = int(input('b = '))
    S = (a * b) // 2
    print(f'Лицето на прав. триъгълник е равно на {S} cm2')

if figure == 'квадрат':
    fK()
elif figure == 'правоъгълник':
    fP()
elif figure == 'прав. триъгълник':
    fT()
