import math

option = input('Въведете вид изчисляване: ')
n1 = int(input('Въведете първото число:'))
n2 = int(input('Въведете второто число:'))

if option == 'Събиране':
    print(f'{n1} + {n2} = {n1 + n2}')
elif option == 'Изваждане':
    print(f'{n1} - {n2} = {n1 - n2}')
elif option == 'Умножение':
    print(f'{n1} * {n2} = {n1 * n2}')
elif option == 'Деление':
    print(f'{n1} / {n2} = {n1 // n2}')
elif option == 'Деление с остатък':
    print(f'{n1} % {n2} = {n1 % n2}')
else:
    print(f'{n1} на степен {n2} = {math.pow(n1, n2)}')


    